#!/bin/bash
echo "Pulling latest updates..."
git pull origin main

echo "Updating dependencies..."
pip install -r requirements.txt

echo "Restarting Flask app..."
pkill -f "flask run"
flask run --host=0.0.0.0 --port=5000 &
echo "Deployment complete!"
