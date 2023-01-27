from flask import Flask
from flask_socketio import SocketIO, emit
import logging
import commands
import speaker

logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
logger = logging.getLogger("Wall-E")

app = Flask(__name__)
socket = SocketIO(app, cors_allowed_origins="*")

# WebSocket Lifecycle


@socket.on('connect')
def handle_connection():
    if not commands.HAS_SERIAL:
        emit('message', 'No serial connection')
        return
    logger.info('New connection')
    emit('message', 'Connected to Wall-E')


@socket.on('disconnect')
def handle_disconnect():
    logger.info('New disconnect')

# Wall-E Controls


@socket.on('driv')
def driv(json):
    speed = json['speed']
    degrees = json['degrees']
    commands.driv(speed, degrees)
    logging.info(f'driv{speed}{degrees}X')


@socket.on('alpo')
def alpo(json):
    percent = json['value']
    commands.alpo(percent)
    logging.info(f'alpo{percent}X')


@socket.on('arpo')
def arpo(json):
    percent = json['value']
    commands.arpo(percent)
    logging.info(f'arpo{percent}X')


@socket.on('hrot')
def hrot(json):
    percent = json['value']
    commands.hrot(percent)
    logging.info(f'hrot{percent}X')


@socket.on('hext')
def hext(json):
    percent = json['value']
    commands.hext(percent)
    logging.info(f'hext{percent}X')


@socket.on('laser')
def laser(json):
    state = json['value']
    if state:
        commands.laser(True)
        logging.info('lase1X')
        speaker.play('laser')
    else:
        commands.laser(False)
        logging.info('lase0X')

# Speak Controls


@socket.on('speak/welcome')
def speak_welcome():
    logging.info('speak/welcome')
    speaker.play('welcome')


@socket.on('speak/follow')
def speak_follow():
    logging.info('speak/follow')
    speaker.play('follow')


@socket.on('speak/way')
def speak_way():
    logging.info('speak/way')
    speaker.play('way')


@socket.on('speak/bye')
def speak_bye():
    logging.info('speak/bye')
    speaker.play('bye')


@socket.on('speak/thanks')
def speak_thanks():
    logging.info('speak/thanks')
    speaker.play('thanks')


@socket.on('speak/story')
def speak_thanks():
    logging.info('speak/story')
    speaker.play('story')


@socket.on('speak/slogan')
def speak_thanks():
    logging.info('speak/slogan')
    speaker.play('slogan')


if __name__ == "__main__":
    logging.info('Starting Wall-E-Server on port 1606')
    socket.run(app, host='0.0.0.0', port=1606)
