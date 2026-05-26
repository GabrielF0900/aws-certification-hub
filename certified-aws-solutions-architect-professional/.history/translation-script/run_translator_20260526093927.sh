#!/bin/bash

# Translation Script Launcher for Linux/Mac
# Inicializa o script de tradução

echo ""
echo "============================================================"
echo "  AWS Solutions Architect Professional - Portuguese Translator"
echo "============================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.7+ from https://www.python.org"
    exit 1
fi

echo "[1/3] Checking Python installation..."
python3 --version
echo ""

echo "[2/3] Installing/Updating dependencies..."
pip3 install -q -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi
echo "Dependencies installed successfully!"
echo ""

echo "[3/3] Starting translation process..."
echo ""
python3 translate_all.py

echo ""
echo "============================================================"
echo "Translation process completed!"
echo "Check translation_log.json for details."
echo "============================================================"
echo ""
