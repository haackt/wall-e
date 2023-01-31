import io
import picamera
import logging
import socketserver
from threading import Condition
from http import server

# Create a streaming output object that holds image data in memory


class StreamingOutput(object):
    # Initialize the object
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    # Write the image data to the buffer
    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

# Create a streaming handler that sends the image data to the client


class StreamingHandler(server.BaseHTTPRequestHandler):
    # Handle a GET request
    def do_GET(self):
        self.send_response(200)
        self.send_header('Age', 0)
        self.send_header('Cache-Control', 'no-cache, private')
        self.send_header('Pragma', 'no-cache')
        self.send_header(
            'Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
        self.end_headers()
        try:
            # Loop until the client disconnects
            while True:
                with output.condition:
                    output.condition.wait()
                    frame = output.frame
                # Write the image data to the client
                self.wfile.write(b'--FRAME\r\n')
                self.send_header('Content-Type', 'image/jpeg')
                self.send_header('Content-Length', len(frame))
                self.end_headers()
                self.wfile.write(frame)
                self.wfile.write(b'\r\n')
        except Exception as e:
            logging.warning(
                'Removed streaming client %s: %s',
                self.client_address, str(e))


# Create a streaming server that listens on port 1507
class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


# Start the streaming server
with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
    output = StreamingOutput()
    camera.rotation = 270  # Rotate the camera 270 degrees since the camera is not straight
    camera.start_recording(output, format='mjpeg')
    try:
        address = ('', 1507)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        camera.stop_recording()
