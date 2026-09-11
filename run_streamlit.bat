@echo off
REM ==============================================================================
REM Launch Streamlit Legal Research Dashboard (Windows)
REM ==============================================================================

echo ============================================================
echo  Launching Streamlit Legal Research Assistant Dashboard...
echo ============================================================

if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

streamlit run app_streamlit.py --server.port 8501
pause
