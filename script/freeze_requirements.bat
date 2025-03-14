@echo off
pip freeze > requirements.txt
if %errorlevel% neq 0 (
    echo Error while freezing requirements.
) else (
    echo Requirements saved to requirements.txt
)