@echo off
chcp 65001 > nul
title Telegram Bot - Fake Address Vietnam
color 0A

echo ======================================================
echo    TELEGRAM BOT - FAKE ADDRESS VIETNAM GENERATOR
echo ======================================================
echo.

:: Cek apakah Python terinstall
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python tidak terdeteksi di komputer Anda!
    echo Silakan install Python terlebih dahulu dari https://www.python.org/
    pause
    exit /b
)

:: Optimasi performa Python
set PYTHONOPTIMIZE=2
set PYTHONUNBUFFERED=1

:: Jalankan bot
python bot.py

if %errorlevel% neq 0 (
    echo.
    echo [INFO] Bot berhenti atau terjadi error.
    pause
)
