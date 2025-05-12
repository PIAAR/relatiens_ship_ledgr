#!/bin/bash

# setup.sh — Environment bootstrap and system check for Relationship Ledger

ENV_NAME="rl-env"

echo "🔧 Starting setup for Relationship Ledger..."

# Check if conda is available
if ! command -v conda &> /dev/null; then
    echo "❌ Conda is not installed. Please install Miniconda or Anaconda first."
    exit 1
fi

# Create environment if it doesn't exist
if ! conda info --envs | grep -q "$ENV_NAME"; then
    echo "📦 Creating conda environment '$ENV_NAME'..."
    conda env create -f environment.yml
else
    echo "✅ Conda environment '$ENV_NAME' already exists."
fi

# Activate the environment
echo "🔁 Activating conda environment '$ENV_NAME'..."
eval "$(conda shell.bash hook)"  # needed to allow conda activation inside scripts
conda activate "$ENV_NAME"

# Install Python dependencies via Makefile
echo "📦 Installing Python packages..."
make install

# Check database connections
echo "🔍 Checking MongoDB connection..."
python -c "import sys; sys.path.append('backend'); from db import mongo_db; print('✅ MongoDB OK' if mongo_db else '⚠️ MongoDB NOT CONNECTED')"

echo "🔍 Checking Redis connection..."
python -c "import sys; sys.path.append('backend'); from db import redis_client; print('✅ Redis OK' if redis_client.ping() else '⚠️ Redis NOT CONNECTED')"

# Run unit tests
echo "🧪 Running unit tests..."
make unit

echo "✅ Setup complete. Environment '$ENV_NAME' is ready."
