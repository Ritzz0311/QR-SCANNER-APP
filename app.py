import cv2
import numpy as np
from pyzbar.pyzbar import decode
import webbrowser
from flask import Flask, render_template, Response
import time

app = Flask(__name__)

# Use a global set to keep track of opened URLs across different requests
opened_urls = set()
last_open_time = 0
url_open_delay = 5  # seconds

def generate_frames():
    """Generator function to yield video frames."""
    global last_open_time
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        return

    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            decoded_objects = decode(frame)
            for obj in decoded_objects:
                points = obj.polygon
                if len(points) == 4:
                    # Draw a bounding box around the QR code
                    pts = np.array([point for point in points], np.int32)
                    pts = pts.reshape((-1, 1, 2))
                    cv2.polylines(frame, [pts], isClosed=True, color=(0, 255, 0), thickness=2)

                    qr_data = obj.data.decode('utf-8')
                    # Put the QR data text above the bounding box
                    cv2.putText(frame, qr_data, (pts[0][0][0], pts[0][0][1] - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                    # Check if the QR code is a URL and if it should be opened
                    current_time = time.time()
                    if qr_data.startswith("http") and qr_data not in opened_urls and (current_time - last_open_time > url_open_delay):
                        print("Opening URL:", qr_data)
                        webbrowser.open(qr_data)
                        opened_urls.add(qr_data)
                        last_open_time = current_time

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            # Yield the frame in the format required for a multipart response
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the 'src' of an img tag."""
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)