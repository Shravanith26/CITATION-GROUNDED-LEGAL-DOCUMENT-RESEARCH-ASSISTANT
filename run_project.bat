@echo off
REM ==============================================================================
REM Citation-Grounded Legal Document Research Assistant - Windows Startup Script
REM ==============================================================================

echo ====================================================================
echo Starting Citation-Grounded Legal Document Research Assistant...
echo ====================================================================

REM 1. Check Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH. Please install Python 3.10+.
    pause
    exit /b 1
)

REM 2. Create virtual environment if not exists
if not exist "venv" (
    echo [INFO] Creating Python virtual environment...
    python -m venv venv
)

REM 3. Activate venv
call venv\Scripts\activate

REM 4. Install backend dependencies
echo [INFO] Installing Python requirements...
pip install -r backend\requirements.txt

REM 5. Seed legal corpus and build index
echo [INFO] Indexing legal document corpus...
python scripts\build_index.py

REM 6. Start the backend API server
echo [INFO] Launching FastAPI backend server on http://127.0.0.1:8000 ...
cd backend
python run.py

pause
