#!/bin/bash

# run.sh — Starts the Relationship Ledger backend server

ENV_NAME="rl-env"
APP_MODULE="main:app"
APP_DIR="backend"
HOST="127.0.0.1"
PORT="8000"

echo "🚀 Launching Relationship Ledger API..."

# Ensure this script is run in bash
if [ -z "$BASH_VERSION" ]; then
    echo "❌ Please run this script using bash: bash ./run.sh"
    exit 1
fi

# Activate Conda environment
eval "$(conda shell.bash hook)"
conda activate "$ENV_NAME"

# Set Python path so imports work
export PYTHONPATH=$(pwd)/backend

# Navigate to backend if needed
cd "$APP_DIR"

# Start the FastAPI server with Uvicorn
uvicorn "$APP_MODULE" --reload --host "$HOST" --port "$PORT"
