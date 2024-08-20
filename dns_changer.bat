@echo off
setlocal

:: Determine the directory of this batch file
set "BAT_DIR=%~dp0"

:: Set the path to the Python script relative to the batch file location
set "PYTHON_SCRIPT=%BAT_DIR%main.py"

:: Run the Python script
python "%PYTHON_SCRIPT%" %*

