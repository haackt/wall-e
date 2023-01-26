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


@socket.on('speak/welcome')
def speak_welcome():
    logging.info('speak/welcome')
    speaker.play_welcome()


if __name__ == "__main__":
    logging.info('Starting Wall-E-Server on port 1606')
    socket.run(app, host='0.0.0.0', port=1606)
