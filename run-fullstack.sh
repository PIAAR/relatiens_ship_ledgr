#!/bin/bash

# run.sh — Starts both the Relationship Ledger backend and frontend

# Backend settings
ENV_NAME="rl-env"
APP_MODULE="main:app"
APP_DIR="backend"
HOST="127.0.0.1"
PORT="8000"

# Frontend settings
FRONTEND_DIR="frontend"

echo "🚀 Launching Relationship Ledger Fullstack App..."

# Ensure this script is run in bash
if [ -z "$BASH_VERSION" ]; then
    echo "❌ Please run this script using bash: bash ./run.sh"
    exit 1
fi

# Activate Conda environment for backend
eval "$(conda shell.bash hook)"
conda activate "$ENV_NAME"
export PYTHONPATH=$(pwd)/$APP_DIR

# Start backend in current terminal
echo "⚙️ Starting Backend API on http://$HOST:$PORT ..."
cd "$APP_DIR"
uvicorn "$APP_MODULE" --reload --host "$HOST" --port "$PORT" &
BACKEND_PID=$!
cd ..

# Launch frontend in new terminal (macOS)
FRONTEND_PATH=$(pwd)/$FRONTEND_DIR
osascript <<EOF
tell application "Terminal"
    activate
    do script "cd \"$FRONTEND_PATH\" && npm run dev"
end tell
EOF

# Feedback and wait
echo "🟢 Backend PID: $BACKEND_PID"
echo "🌐 Frontend is launching in a new Terminal window..."
wait $BACKEND_PID
