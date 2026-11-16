# Gunakan Python 3.11 versi slim yang sangat ringan dan stabil
FROM python:3.11-slim

# Optimasi environment Python
ENV PYTHONUNBUFFERED=1 \
    PYTHONOPTIMIZE=2 \
    PORT=7860

# Set direktori kerja
WORKDIR /app

# Salin requirements dan install library
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh kode aplikasi
COPY . .

# Port yang dipantau oleh Hugging Face Spaces
EXPOSE 7860

# Jalankan app.py (Web health check + Bot Telegram)
CMD ["python", "app.py"]
