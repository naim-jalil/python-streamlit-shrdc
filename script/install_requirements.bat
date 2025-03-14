@echo off

:: Set virtual environment directory
set VENV_DIR=.venv

:: Check if virtual environment exists
if not exist %VENV_DIR% (
    echo Creating virtual environment...
    python -m venv %VENV_DIR%
)

:: Activate virtual environment
call %VENV_DIR%\Scripts\activate.bat

:: Install requirements
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error while installing requirements.
) else (
    echo Requirements installed successfully.
)
