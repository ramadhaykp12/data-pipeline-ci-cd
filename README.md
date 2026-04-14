# Automated ETL Pipeline with Full CI/CD

Proyek ini adalah implementasi pipeline Data Engineering (ETL) yang dilengkapi dengan siklus otomatisasi penuh menggunakan **Continuous Integration (CI)** dan **Continuous Deployment (CD)**. Sistem ini menjamin bahwa setiap perubahan kode telah melalui proses pengujian otomatis sebelum dideploy ke lingkungan produksi.

## 🚀 Fitur Utama
- **Automated ETL:** Script Python menggunakan Pandas untuk ekstraksi, transformasi, dan pembersihan data.
- **REST API Entry Point:** Menggunakan FastAPI untuk memicu proses ETL melalui protokol HTTP.
- **Continuous Integration (CI):** Automasi testing menggunakan **GitHub Actions** dan **Pytest**.
- **Containerization:** Aplikasi dibungkus menggunakan **Docker** untuk menjamin konsistensi di berbagai lingkungan.
- **Continuous Deployment (CD):** Automasi deployment ke **Railway** setiap kali ada perubahan pada branch `main`.

## 🛠️ Tech Stack
- **Language:** Python 3.9+
- **Data Processing:** Pandas
- **API Framework:** FastAPI & Uvicorn
- **Testing:** Pytest
- **DevOps/CI-CD:** GitHub Actions, Docker, Railway

## 🏗️ Arsitektur CI/CD
1. **Local Development:** Engineer menulis kode dan melakukan `git push`.
2. **GitHub Actions (CI):** - Menjalankan Unit Testing untuk memvalidasi logika transformasi data.
   - Melakukan build Docker Image untuk memastikan konfigurasi kontainer tidak error.
3. **Railway (CD):** - Jika tahap CI lolos (Green Tick), Railway akan otomatis menarik kode terbaru.
   - Melakukan build ulang kontainer dan memperbarui layanan secara otomatis (Seamless Update).

## ⚙️ Cara Menjalankan Secara Lokal

### 1. Clone Repository
```bash
git clone [https://github.com/username/data-pipeline-ci-cd.git](https://github.com/username/data-pipeline-ci-cd.git)
cd data-pipeline-ci-cd
```

### 2. Menggunakan Docker
```bash
docker build -t data-pipeline .
docker run -p 8080:8080 data-pipeline
```

### 3. Tanpa Docker
```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8080
```
### Testing
```bash
pytest test_etl.py
```
