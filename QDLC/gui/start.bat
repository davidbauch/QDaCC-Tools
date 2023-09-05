@echo off
setlocal EnableDelayedExpansion

set "arg=%~1"
set "dir=%~dp0"

if "%~1" == "" (
    python3 "%dir%/gui.py"
) else (
    python3 "%dir%/gui.py" "%arg%"
)

pause