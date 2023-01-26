FROM python:3.9

ADD app.py .
ADD commands.py .

RUN pip install pyserial flask flask-socketio eventlet

CMD [ "python", "app.py" ]

EXPOSE 1606