#!/usr/bin/env bash
# ==============================================================================
# Launch Streamlit Legal Research Dashboard (macOS / Linux)
# ==============================================================================

set -e
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_ROOT"

if [ -d "venv" ]; then
    source venv/bin/activate
fi

echo "============================================================"
echo " Launching Streamlit Legal Research Assistant Dashboard..."
echo "============================================================"
streamlit run app_streamlit.py --server.port 8501
