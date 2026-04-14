# 1. Gunakan image Python yang ringan
FROM python:3.9-slim

# 2. Atur environment variable agar Python tidak menghasilkan file .pyc 
# dan output log bisa langsung terlihat di dashboard Railway
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Tentukan folder kerja di dalam kontainer
WORKDIR /app

# 4. Salin requirements dan install
# Kita salin ini duluan agar jika kode berubah tapi library tetap, 
# Docker bisa menggunakan 'cache' dan build jadi lebih cepat
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Salin semua kode ke dalam kontainer
COPY . .

# 6. Perintah untuk menjalankan FastAPI
# Railway akan memberikan port secara dinamis melalui env variable PORT.
# Kita gunakan 8080 sebagai default jika variabel PORT tidak ditemukan.
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}"]
