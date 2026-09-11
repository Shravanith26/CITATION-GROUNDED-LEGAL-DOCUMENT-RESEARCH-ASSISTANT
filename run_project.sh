#!/usr/bin/env bash
# ==============================================================================
# Citation-Grounded Legal Document Research Assistant - Unix/macOS Startup Script
# ==============================================================================

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_ROOT"

echo "===================================================================="
echo " Starting Citation-Grounded Legal Document Research Assistant"
echo "===================================================================="

# Determine Python 3 binary
if command -v python3 &>/dev/null; then
    PYTHON=python3
elif command -v python &>/dev/null; then
    PYTHON=python
else
    echo "[ERROR] Python 3 not found. Please install Python 3.10+."
    exit 1
fi

echo "[INFO] Using Python: $($PYTHON --version)"

# Check or create virtual environment
if [ ! -d "venv" ]; then
    echo "[INFO] Creating virtual environment 'venv'..."
    $PYTHON -m venv venv
fi

# Activate venv
source venv/bin/activate

echo "[INFO] Installing dependencies..."
pip install -q -r backend/requirements.txt || true

echo "[INFO] Ingesting documents and building search index..."
python scripts/build_index.py

echo "[INFO] Launching FastAPI backend server on http://127.0.0.1:8000 ..."
echo "[INFO] Open http://127.0.0.1:8000/docs for Swagger API documentation"
echo "[INFO] Open http://127.0.0.1:8000 for the Web Interface"

cd backend
python run.py
