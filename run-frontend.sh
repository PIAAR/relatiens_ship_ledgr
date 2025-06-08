#!/bin/bash

# run-frontend.sh — Starts the Vite frontend dev server for Relationship Ledger

FRONTEND_DIR="frontend"
REQUIRED_NODE_MAJOR=20

echo "🌐 Starting Relationship Ledger Frontend..."

# Ensure bash shell
if [ -z "$BASH_VERSION" ]; then
    echo "❌ Please run this script using bash: bash ./run-frontend.sh"
    exit 1
fi

# Try to load NVM
if [ -s "$HOME/.nvm/nvm.sh" ]; then
    source "$HOME/.nvm/nvm.sh"
    echo "🧠 NVM loaded."
else
    echo "⚠️ NVM not found. Please install it from https://github.com/nvm-sh/nvm"
    exit 1
fi

# Use Node 20 (or prompt if not installed)
nvm use 20 >/dev/null 2>&1 || {
    echo "📦 Installing Node.js v20..."
    nvm install 20
    nvm use 20
}

# Check active version
NODE_VERSION=$(node -v | cut -d. -f1 | tr -dc '0-9')
if [ "$NODE_VERSION" -ne "$REQUIRED_NODE_MAJOR" ]; then
    echo "❌ Node.js v$REQUIRED_NODE_MAJOR.x is required. Current version: $(node -v)"
    exit 1
fi

echo "🧪 Node version OK: $(node -v)"

# Navigate and start frontend
cd "$FRONTEND_DIR" || { echo "❌ Cannot find frontend directory"; exit 1; }

if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install
fi

echo "🚀 Launching Vite server at http://localhost:5173"
npm run dev
