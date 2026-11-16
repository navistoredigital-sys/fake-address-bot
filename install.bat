@echo off
chcp 65001 > nul
title Installer - Fake Address ChatGPT Bot (Indonesia dan Vietnam)
color 0B

echo ================================================================
echo    INSTALLER OTOMATIS - BOT FAKE ADDRESS CHATGPT
echo             (Mode Indonesia dan Vietnam)
echo ================================================================
echo.

:: 1. Cek apakah Python terpasang di sistem
echo [1/4] Memeriksa instalasi Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo.
    echo ================================================================
    echo [ERROR] Python tidak terdeteksi di komputer Anda!
    echo ================================================================
    echo 1. Silakan unduh Python dari: https://www.python.org/downloads/
    echo 2. PENTING: Saat instalasi, CENTANG opsi "Add Python to PATH"!
    echo 3. Setelah instalasi Python selesai, buka kembali file install.bat ini.
    echo ================================================================
    echo.
    pause
    exit /b
)

for /f "tokens=*" %%v in ('python --version') do set PYTHON_VERSION=%%v
echo [OK] %PYTHON_VERSION% terdeteksi.
echo.

:: 2. Install library yang dibutuhkan dari requirements.txt
echo [2/4] Menginstall dependensi (python-telegram-bot dan python-dotenv)...
echo Harap tunggu sebentar...
echo.

python -m pip install -r requirements.txt --quiet
if %errorlevel% neq 0 (
    color 0E
    echo [INFO] Mencoba install ulang dengan log detail...
    python -m pip install -r requirements.txt
    if %errorlevel% neq 0 (
        color 0C
        echo.
        echo [ERROR] Gagal menginstall dependensi!
        echo Pastikan komputer Anda terhubung ke internet.
        pause
        exit /b
    )
)

echo [OK] Semua dependensi berhasil terinstall!
echo.

:: 3. Persiapan file .env
echo [3/4] Memeriksa file konfigurasi token (.env)...
if not exist ".env" (
    if exist ".env.example" (
        copy .env.example .env >nul
        echo [OK] File .env berhasil dibuat dari template .env.example!
    ) else (
        echo BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN_HERE > .env
        echo [OK] File .env baru berhasil dibuat!
    )
) else (
    echo [OK] File .env sudah ada.
)
echo.

:: 4. Selesai
echo [4/4] Instalasi Selesai!
echo.
echo ================================================================
echo                   SEMUA BERHASIL DIINSTALL!
echo ================================================================
echo.
echo Langkah selanjutnya:
echo 1. Pastikan Anda sudah mengisi BOT_TOKEN di file '.env'
echo    (Dapatkan token dari @BotFather di Telegram)
echo 2. Untuk menjalankan bot, cukup dobel klik file 'start.bat'
echo ================================================================
echo.

set /p RUN_NOW="Apakah Anda ingin langsung menjalankan bot sekarang? (y/n): "
if /i "%RUN_NOW%"=="y" (
    echo.
    echo Menjalankan bot...
    call start.bat
) else (
    echo.
    echo Anda bisa menjalankan bot kapan saja dengan membuka 'start.bat'.
    echo Selesai.
)
