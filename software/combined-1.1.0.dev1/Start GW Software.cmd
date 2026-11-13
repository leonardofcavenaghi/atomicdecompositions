@echo off
cd /d "%~dp0"
python -m gwapp
if errorlevel 1 pause
