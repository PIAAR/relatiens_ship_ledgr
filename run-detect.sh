#!/bin/bash

# Smart run.sh — Detects OS and launches backend + frontend properly

ENV_NAME="rl-env"
APP_MODULE="main:app"
APP_DIR="backend"
FRONTEND_DIR="frontend"
HOST="127.0.0.1"
PORT="8000"

echo "🚀 Launching Relationship Ledger Fullstack App..."

# Ensure bash shell
if [ -z "$BASH_VERSION" ]; then
    echo "❌ Please run this script using bash: bash ./run.sh"
    exit 1
fi

# Activate backend environment
eval "$(conda shell.bash hook)"
conda activate "$ENV_NAME"
export PYTHONPATH=$(pwd)/$APP_DIR

# Launch backend
echo "⚙️ Starting Backend API on http://$HOST:$PORT ..."
cd "$APP_DIR"
uvicorn "$APP_MODULE" --reload --host "$HOST" --port "$PORT" &
BACKEND_PID=$!
cd ..

# Determine OS and terminal
OS=$(uname)
FRONTEND_PATH=$(pwd)/$FRONTEND_DIR

launch_frontend() {
    echo "🌐 Starting Frontend (Vite)..."
    cd "$FRONTEND_DIR"
    npm install > /dev/null 2>&1
    npm run dev
}

if [[ "$OS" == "Darwin" ]]; then
    # macOS — Use AppleScript
    echo "🧠 macOS detected: Opening new Terminal window..."
    osascript <<EOF
tell application "Terminal"
    activate
    do script "cd \"$FRONTEND_PATH\" && [ -d node_modules ] || npm install && npm run dev"
end tell
EOF

elif [[ "$OS" == "Linux" ]]; then
    # Linux — Try gnome-terminal or x-terminal-emulator
    if command -v gnome-terminal &> /dev/null; then
        echo "🧠 Linux + GNOME Terminal detected"
        gnome-terminal -- bash -c "cd \"$FRONTEND_PATH\" && [ -d node_modules ] || npm install && npm run dev; exec bash"
    elif command -v x-terminal-emulator &> /dev/null; then
        echo "🧠 Linux + x-terminal-emulator detected"
        x-terminal-emulator -e "bash -c 'cd \"$FRONTEND_PATH\" && [ -d node_modules ] || npm install && npm run dev; exec bash'"
    else
        echo "⚠️ No supported Linux terminal found. Running frontend in same window..."
        launch_frontend &
    fi

elif [[ "$OS" == "MINGW"* || "$OS" == "CYGWIN"* || "$OS" == "WSL"* ]]; then
    echo "🧠 Windows or WSL detected. Opening new terminal is limited."
    echo "⚠️ Please open a separate terminal and run: cd \"$FRONTEND_PATH\" && npm run dev"
else
    echo "❓ Unknown OS. Running frontend in same terminal..."
    launch_frontend &
fi

echo "🟢 Backend PID: $BACKEND_PID"
wait $BACKEND_PID
