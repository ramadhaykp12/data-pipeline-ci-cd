# Gunakan image Python yang ringan
FROM python:3.9-slim

# Tentukan folder kerja di dalam kontainer
WORKDIR /app

# Salin requirements dan install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua kode ke dalam kontainer
COPY . .

# Perintah yang dijalankan saat kontainer dimulai
# Kita asumsikan script ETL dijalankan sebagai perintah utama
CMD ["python", "etl_process.py"]