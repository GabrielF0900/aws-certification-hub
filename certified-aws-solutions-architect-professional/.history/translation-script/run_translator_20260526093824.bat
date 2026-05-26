@echo off
REM Translation Script Launcher for Windows
REM Inicializa o script de tradução

echo.
echo ============================================================
echo  AWS Solutions Architect Professional - Portuguese Translator
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://www.python.org
    pause
    exit /b 1
)

echo [1/3] Checking Python installation...
python --version
echo.

echo [2/3] Installing/Updating dependencies...
pip install -q -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo Dependencies installed successfully!
echo.

echo [3/3] Starting translation process...
echo.
python translate_all.py

echo.
echo ============================================================
echo Translation process completed!
echo Check translation_log.json for details.
echo ============================================================
echo.

pause
