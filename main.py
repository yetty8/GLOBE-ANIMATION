from flask import Flask, render_template
from flask_socketio import SocketIO
import os
import requests

app = Flask(__name__)
socketio = SocketIO(app)

# Create templates and static directories if they don't exist
if not os.path.exists('templates'):
    os.makedirs('templates')
if not os.path.exists('static'):
    os.makedirs('static')

# Create HTML template


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001)
