import serial as arduino

HAS_SERIAL = True

try:
    # Create serial connection
    serial = arduino.Serial(port='/dev/ttyACM0', baudrate=9600, writeTimeout=0)
except:
    HAS_SERIAL = False
    pass

# Function to format and send command to Wall-E


def send_command(command):
    return serial.write(bytearray(command.encode('utf-8')))

# Wall-E Commands


def init():
    send_command('initX')


def driv(speed, degrees):
    send_command(f'driv{speed}{degrees}X')


def alpo(percent):
    send_command(f'alpo{percent}X')


def arpo(percent):
    send_command(f'arpo{percent}X')


def hrot(percent):
    send_command(f'hrot{percent}X')


def hext(percent):
    send_command(f'hext{percent}X')


def laser(state):
    if state:
        send_command('lase1X')
    else:
        send_command('lase0X')
