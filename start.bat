@echo off
chcp 65001 > nul
title Bot Telegram - Fake Address ChatGPT (Indonesia & Vietnam)
color 0B

echo ================================================================
echo    TELEGRAM BOT - FAKE ADDRESS CHATGPT (INDONESIA & VIETNAM)
echo ================================================================
echo.

:: 1. Cek apakah Python terpasang di sistem
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python tidak terdeteksi di komputer Anda!
    echo Silakan unduh dan install Python dari https://www.python.org/
    echo Pastikan centang "Add Python to PATH" saat menginstall.
    echo.
    pause
    exit /b
)

:: 2. Cek apakah file .env ada
if not exist ".env" (
    echo [PERINGATAN] File .env tidak ditemukan!
    if exist ".env.example" (
        copy .env.example .env >nul
        echo File .env berhasil dibuat dari template .env.example.
    )
)

echo [STATUS] Menjalankan Bot Telegram (Mode Hemat CPU & RAM Super Gacor)...
echo [INFO] Buka Telegram Anda dan cari bot: @fakevietnam_bot
echo [INFO] Tekan tombol Ctrl + C di jendela ini untuk mematikan bot.
echo.
echo ================================================================
echo.

:: 3. Optimasi performa Python: PYTHONOPTIMIZE=2 untuk memangkas ukuran bytecode memori
set PYTHONOPTIMIZE=2
set PYTHONUNBUFFERED=1

:: Jalankan bot utama
python bot.py

:: 4. Jika bot berhenti atau crash, tahan jendela agar pesan error terbaca
if %errorlevel% neq 0 (
    echo.
    echo ================================================================
    echo [INFO] Bot berhenti atau terjadi error.
    echo ================================================================
    pause
)
