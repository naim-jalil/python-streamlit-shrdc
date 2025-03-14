@echo off
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error while installing requirements.
) else (
    echo Requirements installed successfully.
)
