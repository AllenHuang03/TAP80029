# Sprint 1: Project Setup & Basic Web Framework

# 1. Install dependencies (Flask, Gunicorn, GitHub Actions for CI/CD)
# Run this in terminal:
# pip install flask gunicorn requests

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Cosmic Lighthouse Map</h1><p>Serving up real-time radio astronomy data.</p>"

# Health check route for deployment monitoring
@app.route('/health')
def health_check():
    return jsonify(status="ok"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
