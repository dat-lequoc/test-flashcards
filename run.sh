#!/bin/bash

# Install frontend dependencies
# echo "Installing frontend dependencies..."
# npm install

# Install backend dependencies
# echo "Installing backend dependencies..."
# pip install flask flask-cors

# Start the backend server
echo "Starting backend server..."
python app.py &

# Start the frontend development server
echo "Starting frontend development server..."
npm run dev
