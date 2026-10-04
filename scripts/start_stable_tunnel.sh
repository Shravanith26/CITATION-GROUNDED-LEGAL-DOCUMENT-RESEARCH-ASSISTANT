#!/bin/bash
# ==============================================================================
# Persistent Auto-Reconnecting Tunnel Supervisor for Streamlit
# ==============================================================================
# Uses HTTP/2 over TCP (avoiding QUIC/UDP route drops on Mac/Wi-Fi)
# Automatically restarts if the tunnel is interrupted by a network blip.
# ==============================================================================

PORT=${1:-8501}
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
CLOUDFLARED_BIN="$PROJECT_ROOT/bin/cloudflared"

if [ ! -f "$CLOUDFLARED_BIN" ]; then
    echo "cloudflared binary not found at $CLOUDFLARED_BIN. Attempting system cloudflared..."
    CLOUDFLARED_BIN=$(which cloudflared)
    if [ -z "$CLOUDFLARED_BIN" ]; then
        echo "Error: cloudflared is not installed."
        exit 1
    fi
fi

echo "=========================================================="
echo " Starting Persistent Tunnel on port $PORT"
echo " Protocol: HTTP/2 (Resilient TCP)"
echo "=========================================================="

while true; do
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting tunnel process..."
    "$CLOUDFLARED_BIN" tunnel --protocol http2 --url "http://localhost:$PORT"
    EXIT_CODE=$?
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Tunnel process exited with code $EXIT_CODE. Reconnecting in 3 seconds..."
    sleep 3
done
