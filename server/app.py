from flask import Flask
from flask_socketio import SocketIO, emit
import logging
import commands
import speaker

# Logging Setup
logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
logger = logging.getLogger("Wall-E")

# Flask Setup
app = Flask(__name__)
socket = SocketIO(app, cors_allowed_origins="*")

# WebSocket Lifecycle


@socket.on('connect')
def handle_connection():
    if not commands.HAS_SERIAL:  # Check if serial connection is available
        # If not, send message to client
        emit('message', 'No serial connection')
        return
    logger.info('New connection')
    emit('message', 'Connected to Wall-E')  # If yes, send message to client


@socket.on('disconnect')
def handle_disconnect():
    logger.info('New disconnect')  # Log disconnect

# Wall-E Controls


@socket.on('driv')
def driv(json):
    # Get speed and degrees from json
    speed = json['speed']
    degrees = json['degrees']
    commands.driv(speed, degrees)  # Send command to Wall-E
    logging.info(f'driv{speed}{degrees}X')  # Log command


@socket.on('alpo')
def alpo(json):
    # Get percent from json
    percent = json['value']
    commands.alpo(percent)  # Send command to Wall-E
    logging.info(f'alpo{percent}X')  # Log command


@socket.on('arpo')
def arpo(json):
    # Get percent from json
    percent = json['value']
    commands.arpo(percent)  # Send command to Wall-E
    logging.info(f'arpo{percent}X')  # Log command


@socket.on('hrot')
def hrot(json):
    # Get percent from json
    percent = json['value']
    commands.hrot(percent)  # Send command to Wall-E
    logging.info(f'hrot{percent}X')  # Log command


@socket.on('hext')
def hext(json):
    # Get percent from json
    percent = json['value']
    commands.hext(percent)  # Send command to Wall-E
    logging.info(f'hext{percent}X')  # Log command


@socket.on('laser')
def laser(json):
    # Get state from json
    state = json['value']
    if state:  # If state is true
        commands.laser(True)  # Send command to Wall-E
        logging.info('lase1X')  # Log command
        speaker.play('laser')  # Play laser sound
    else:  # If state is false
        commands.laser(False)  # Send command to Wall-E
        logging.info('lase0X')  # Log command

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


@socket.on('speak/language')
def speak_thanks():
    logging.info('speak/language')
    speaker.play('language')


# If this file is run directly, start the server
if __name__ == "__main__":
    logging.info('Starting Wall-E-Server on port 1606')
    socket.run(app, host='0.0.0.0', port=1606)
