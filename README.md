---
title: Fake Address ChatGPT Bot
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
---

# 🇮🇩🇻🇳 Telegram Bot - Fake Address ChatGPT (Indonesia & Vietnam)

Bot Telegram pintar untuk menghasilkan **alamat palsu Indonesia & Vietnam** yang akurat dan tervalidasi khusus untuk mengisi **Formulir Pembayaran / Billing ChatGPT (OpenAI / Stripe)**.

Dapat dijalankan secara lokal di komputer (Windows) atau di-deploy **24/7 Gratis di Hugging Face Spaces (Gradio SDK - Tanpa Bayar / Tanpa Kartu Kredit)**.

---

## ✨ Fitur Utama (2 Mode Negara)

### 🇻🇳 1. Mode Vietnam
Format sesuai kolom formulir ChatGPT Vietnam:
- 1️⃣ **Dòng địa chỉ 1:** (Tòa nhà / Căn hộ / Ngõ / Phường)
- 2️⃣ **Thành phố:** (Quận / Distrik)
- 3️⃣ **Tỉnh:** (Provinsi untuk dipilih di dropdown)
- 4️⃣ **Mã bưu chính:** (Kode Pos resmi sesuai distrik)

### 🇮🇩 2. Mode Indonesia
Format sesuai kolom formulir ChatGPT Indonesia:
- 1️⃣ **Baris alamat 1:** (Gedung / Apartemen / Perumahan / RT RW / Kelurahan)
- 2️⃣ **Kota:** (Kecamatan / Kota, misal: Jakarta Selatan, Surabaya, Bandung)
- 3️⃣ **Provinsi:** (DKI Jakarta, Jawa Timur, Jawa Barat, Bali, dll.)
- 4️⃣ **Kode Pos:** (Kode pos 5 digit resmi sesuai kelurahan)

---

## ☁️ Panduan Deploy 24/7 Gratis di Hugging Face Spaces

### Langkah 1: Buat Space Baru
1. Buka [huggingface.co/new-space](https://huggingface.co/new-space).
2. Isi form pembuatan Space:
   - **Space name**: misalnya `fake-address-bot`
   - **License**: `mit`
   - **Select the Space SDK**: Pilih **Gradio** (100% Gratis untuk semua akun)
   - **Space hardware**: Pilih **CPU Basic (2 vCPU · 16GB · Free)**
   - **Visibility**: Pilih **Public**
3. Klik tombol **Create Space**.

---

### Langkah 2: Masukkan BOT_TOKEN ke Secrets Hugging Face (Wajib & Aman)
1. Di halaman Space yang baru dibuat, klik tab **⚙️ Settings** (di bagian atas sebelah 'Files').
2. Gulir ke bawah ke bagian **Variables and secrets**.
3. Di bagian **Secrets**, klik tombol **New secret**.
4. Masukkan:
   - **Name**: `BOT_TOKEN`
   - **Value**: Masukkan API Token bot Anda dari `@BotFather`
5. Klik **Save**.

---

### Langkah 3: Upload File ke Hugging Face (Metode Web - Paling Mudah)
1. Di halaman Space Anda, klik tab **Files and versions**.
2. Klik tombol **Add file** > pilih **Upload files**.
3. Upload file dan folder berikut:
   - `Dockerfile`
   - `app.py`
   - `bot.py`
   - `generator.py`
   - `requirements.txt`
   - `README.md`
   - `.dockerignore`
   - Folder `data/` (beserta isinya: `vietnam_data.py`, `indonesia_data.py`, `__init__.py`)
   *(Catatan: File `.env` **JANGAN** di-upload karena token sudah aman di menu Secrets).*
4. Masukkan pesan commit (misal: `Initial deploy`), lalu klik **Commit changes to main**.

---

### Langkah 4: Selesai & Bot Aktif!
- Hugging Face akan otomatis melakukan proses **Building Container** (sekitar 1-2 menit).
- Setelah selesai, status Space akan berubah menjadi **🟢 Running**.
- Buka web Space Anda: akan tampil dashboard status web bot di port 7860.
- Buka bot Anda di Telegram dan ketik `/start` atau `ha noi` / `jakarta`. Bot siap digunakan 24/7!

> 💡 **Tips Agar Tidak Tidur (Always ON 24/7):**  
> Gunakan layanan gratis seperti [UptimeRobot.com](https://uptimerobot.com/) atau [cron-job.org](https://cron-job.org/).  
> Masukkan URL Space Anda (misalnya `https://username-fake-address-bot.hf.space`) untuk di-ping setiap 10-15 menit agar Space tidak masuk mode sleep.

---

## 💻 Cara Menjalankan Secara Lokal di Komputer (Windows)

1. **Instalasi Cepat:** Dobel-klik file `install.bat` (menginstall library otomatis).
2. **Konfigurasi Token:** Masukkan bot token di file `.env`.
3. **Jalankan Bot:** Dobel-klik file `start.bat`.

---

## 📁 Struktur File Proyek

```
FAKE ADDRESS VIETNAM/
├── Dockerfile                # Konfigurasi container Docker untuk Hugging Face
├── app.py                    # Entrypoint Hugging Face (Web Dashboard & Bot Runner)
├── .dockerignore             # Mencegah file sensitif ter-upload ke Docker
├── bot.py                    # Script bot Telegram utama (Mode ID & VN)
├── generator.py              # Generator alamat presisi format ChatGPT
├── data/
│   ├── indonesia_data.py     # Dataset kota & kode pos akurat Indonesia
│   ├── vietnam_data.py       # Dataset kota & kode pos distrik Vietnam
│   └── __init__.py
├── requirements.txt          # Library Python yang dibutuhkan
├── install.bat               # Installer otomatis 1-klik untuk Windows
├── start.bat                 # Menjalankan bot di Windows (hemat RAM & CPU)
├── .env                      # File konfigurasi token (Lokal saja)
└── README.md                 # Dokumentasi panduan lengkap
```

---

## 📱 Bot Telegram Aktif
- **Username Bot:** [@fakevietnam_bot](https://t.me/fakevietnam_bot)
