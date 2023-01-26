import serial as arduino

HAS_SERIAL = True

try:
    serial = arduino.Serial(port='/dev/ttyACM0', baudrate=9600)
except:
    HAS_SERIAL = False
    pass


def send_command(command):
    return serial.write(bytearray(command.encode('utf-8')))


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
