from flask import Flask, send_from_directory
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return send_from_directory('.', 'app.html')

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    print("Server: http://localhost:8000")
    print("Dashboard: http://localhost:8000/dashboard.html")
    app.run(host='0.0.0.0', port=8000, debug=True)