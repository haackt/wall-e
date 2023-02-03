// COPY OF https://github.com/kiramanaka/GlaDOS/blob/controller/ArduinoMain.cpp

#include <Adafruit_PWMServoDriver.h>
#include <Wire.h>

// TODO Check if we can re-enable the Servo OE pin for quieter operation
// TODO Implement a NEBO Offset whenever the Laser is enabled
// called this way, it uses the default address 0x40
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x40);
/*
    can also be called it with a different address:
    Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x41);
    can also be called with a different address and I2C interface:
    Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x40, Wire);
*/

const int SERVO_FREQUENCY = 200;
const int SERVO_OUTPUT_ENABLE = 10;  // servo PWM controller Output enable pin
int SERVO_TIMEOUT = 5001;            // timeout for servo movement
int SERVO_TIMEOUT_COUNTER = 0;       // counter for servo movement timeout
int LASER_OFFSET = 0;                // offset for laser movement

const int A_MOTOR_DIRECTION = 12;
const int A_MOTOR_VALUE = 3;
const int A_MOTOR_BRAKE = 9;
const int A_MOTOR_SENS = A0;
const int B_MOTOR_DIRECTION = 13;
const int B_MOTOR_VALUE = 11;
const int B_MOTOR_BRAKE = 8;
const int B_MOTOR_SENS = A1;
const int LASER_PIN = 11;

const int NECK_BOTTOM_SERVO = 0;
const int NECK_TOP_SERVO = 1;
const int HEAD_ROTATION_SERVO = 2;
const int RIGHT_EYE_SERVO = 3;
const int LEFT_EYE_SERVO = 4;
const int RIGHT_ARM_SERVO = 5;
const int LEFT_ARM_SERVO = 6;

const int EYE_L_RANGE_MIN = 1000;
const int EYE_L_RANGE_MAX = 1300;
const int EYE_R_RANGE_MIN = 100;
const int EYE_R_RANGE_MAX = 1500;
const int NECK_BOTTOM_RANGE_MIN = 1000;
const int NECK_BOTTOM_RANGE_MAX = 1800;
const int NECK_TOP_RANGE_MIN = 800;
const int NECK_TOP_RANGE_MAX = 1800;
const int HEAD_ROTATION_MIN = 900;
const int HEAD_ROTATION_MAX = 1700;
const int LEFT_ARM_POSITION_MIN = 100;
const int LEFT_ARM_POSITION_MAX = 2200;
const int RIGHT_ARM_POSITION_MIN = 1550;
const int RIGHT_ARM_POSITION_MAX = 2000;

String command;
int controlled_servo;
String input;
// Use an object to store the command parameters
struct CommandParams {
    int parameter;
    int steer;
};
CommandParams params = {0, 0};

void setup() {
    pwm.begin();
    pwm.setOscillatorFrequency(27000000);
    pwm.setPWMFreq(SERVO_FREQUENCY);
    delay(20);  // delay to give pwm time to finish setup

    // setup for Arduino outputs
    pinMode(A_MOTOR_DIRECTION, OUTPUT);
    pinMode(A_MOTOR_VALUE, OUTPUT);
    pinMode(A_MOTOR_BRAKE, OUTPUT);
    pinMode(B_MOTOR_DIRECTION, OUTPUT);
    pinMode(B_MOTOR_VALUE, OUTPUT);
    pinMode(B_MOTOR_BRAKE, OUTPUT);
    pinMode(LASER_PIN, OUTPUT);
    pinMode(SERVO_OUTPUT_ENABLE, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    Serial.setTimeout(100);
    if (Serial.available()) {
        input = Serial.readStringUntil('X');
        if (!input.startsWith("d") && !input.startsWith("i") && !input.startsWith("h") && !input.startsWith("a") && !input.startsWith("l")) return;
        command = input.substring(0, 4);
        SERVO_TIMEOUT_COUNTER = 0;
        // Use a switch statement to handle different commands
        if (command.equals("driv")) {
            // Find the indices of the relevant characters in the input string
            int parameterIndex = input.indexOf("driv") + 4;
            int steerIndex = parameterIndex + 3;

            // Extract the command parameters using the indices
            params.parameter = input.substring(parameterIndex, steerIndex).toInt();
            params.steer = input.substring(steerIndex).toInt();

        } else {
            // Find the index of the relevant character in the input string
            params.parameter = input.substring(4).toInt();
        }
    }
    if (command == "driv") {
        Drive(params.parameter, params.steer);
    } else if (command == "init") {
        InitializeMovements();
    } else if (command == "hext") {
        HeadMovement(params.parameter);
    } else if (command == "hrot") {
        HeadRotation(params.parameter);
    } else if (command == "arpo") {
        RightArmPosition(params.parameter);
    } else if (command == "alpo") {
        LeftArmPosition(params.parameter);
    } else if (command == "lase") {
        SetLaser(params.parameter);
    }
    // Determines a random value to trigger the random eye movements
    // I know this is dirty, but it triggers too often otherwise
    // Deal with it
    if (random(0, 10000000) == 80085) {
        if (random(0, 10000000) == 80085) {
            RandomEyeMovements();
        }
    }
    command = "null";
    SERVO_TIMEOUT_COUNTER++;
    if (SERVO_TIMEOUT_COUNTER > SERVO_TIMEOUT) {
        digitalWrite(SERVO_OUTPUT_ENABLE, HIGH);
    }
}

void Drive(int speed, int steer) {
    // Set the direction of the motors based on the value of speed
    // If speed is positive, set the direction of both motors to forward
    // If speed is negative, set the direction of both motors to reverse
    if (speed != 0) {
        digitalWrite(A_MOTOR_DIRECTION, (speed > 0) ? HIGH : LOW);
        digitalWrite(B_MOTOR_DIRECTION, (speed > 0) ? HIGH : LOW);
        digitalWrite(A_MOTOR_BRAKE, LOW);
        digitalWrite(B_MOTOR_BRAKE, LOW);
    }
    // Set the speed of the motors based on the sign of steer
    // If steer is negative, adjust the speed of the motors such that one motor runs faster than the other, causing the vehicle to turn
    // If steer is positive, adjust the speed of the motors in the opposite way, causing the vehicle to turn in the opposite direction
    // If steer is zero, set the speed of the motors to the value of speed, causing the vehicle to move forward or backward at a constant speed
    // Set the speed of the motors based on the value of steer
    if (steer < 0) {
        analogWrite(A_MOTOR_VALUE, AlwaysPositive(speed) + AlwaysPositive(steer));
        analogWrite(B_MOTOR_VALUE, (AlwaysPositive(speed) + AlwaysPositive(steer)) / 2);
    } else if (steer > 0) {
        analogWrite(A_MOTOR_VALUE, (AlwaysPositive(speed) + AlwaysPositive(steer)) / 2);
        analogWrite(B_MOTOR_VALUE, AlwaysPositive(speed) + AlwaysPositive(steer));
    } else {
        // Set the speed of the motors to the value of speed if steer is zero
        analogWrite(A_MOTOR_VALUE, AlwaysPositive(speed));
        analogWrite(B_MOTOR_VALUE, AlwaysPositive(speed));
    }
    // If both speed and steer are zero, set the brakes on the motors to stop the vehicle
    if (speed && steer == 0) {
        digitalWrite(A_MOTOR_BRAKE, HIGH);
        digitalWrite(B_MOTOR_BRAKE, HIGH);
    }
}

void RandomEyeMovements() {
    int eye_position_l = GetValueFromRange(EYE_L_RANGE_MIN, EYE_L_RANGE_MAX, random(0, 100));
    int eye_position_r = GetValueFromRange(EYE_R_RANGE_MIN, EYE_R_RANGE_MAX, random(0, 100));
    // Actuate Servos based on created values (hopefully)
    pwm.setPWM(LEFT_EYE_SERVO, 0, eye_position_l);
    pwm.setPWM(RIGHT_EYE_SERVO, 0, eye_position_r);
}

void HeadMovement(int param) {
    digitalWrite(SERVO_OUTPUT_ENABLE, LOW);
    int neck_bottom_value = GetValueFromRange(NECK_BOTTOM_RANGE_MIN, NECK_BOTTOM_RANGE_MAX, param);
    int neck_top_value = GetValueFromRange(NECK_TOP_RANGE_MIN, NECK_TOP_RANGE_MAX, param);
    pwm.setPWM(NECK_TOP_SERVO, 0, neck_top_value);
    pwm.setPWM(NECK_BOTTOM_SERVO, 0, neck_bottom_value);
}

void HeadRotation(int param) {
    digitalWrite(SERVO_OUTPUT_ENABLE, LOW);
    param = GetValueFromRange(HEAD_ROTATION_MIN, HEAD_ROTATION_MAX, param);
    pwm.setPWM(HEAD_ROTATION_SERVO, 0, param);
}

void LeftArmPosition(int param) {
    digitalWrite(SERVO_OUTPUT_ENABLE, LOW);
    param = GetValueFromRange(LEFT_ARM_POSITION_MIN, LEFT_ARM_POSITION_MAX, param);
    pwm.setPWM(LEFT_ARM_SERVO, 0, param);
}

void RightArmPosition(int param) {
    digitalWrite(SERVO_OUTPUT_ENABLE, LOW);
    param = GetValueFromRange(RIGHT_ARM_POSITION_MIN, RIGHT_ARM_POSITION_MAX, param);
    pwm.setPWM(RIGHT_ARM_SERVO, 0, param);
}

void SetLaser(int param) {
    if (param == 1) {
        digitalWrite(LASER_PIN, HIGH);
        LASER_OFFSET = 10;

    } else {
        digitalWrite(LASER_PIN, LOW);
        LASER_OFFSET = 0;
    }
}

void InitializeMovements() {
    digitalWrite(SERVO_OUTPUT_ENABLE, LOW);
    for (int servo_id = 0; servo_id <= 4; servo_id++) {
        int range_maximums[5] = {NECK_BOTTOM_RANGE_MAX, NECK_TOP_RANGE_MAX, HEAD_ROTATION_MAX,
                                 RIGHT_ARM_POSITION_MAX, LEFT_ARM_POSITION_MAX};
        int range_minimums[5] = {NECK_BOTTOM_RANGE_MIN, NECK_TOP_RANGE_MIN, HEAD_ROTATION_MIN,
                                 RIGHT_ARM_POSITION_MIN, LEFT_ARM_POSITION_MIN};
        int param = GetValueFromRange(range_minimums[servo_id], range_maximums[servo_id], 50);
        pwm.setPWM(servo_id, 0, param);
    }
}

int GetValueFromRange(int min, int max, int percent) {
    float perc = float(percent);
    float value = min + (max - min) * (perc / 100);
    return int(value);
}

int AlwaysPositive(int value) {
    if (value < 0) {
        return value * -1;
    } else {
        return value;
    }
}