from fastapi import FastAPI
from etl_process import run_pipeline

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Data Pipeline API is Running Successfully!"}

@app.get("/run-etl")
def trigger_etl():
    try:
        # Jalankan fungsi ETL yang sudah kita buat sebelumnya
        run_pipeline('data_mentah.csv', 'hasil_output.csv')
        return {"status": "success", "message": "ETL Process Completed"}
    except Exception as e:
        return {"status": "error", "message": str(e)}