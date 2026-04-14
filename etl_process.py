import pandas as pd
import os

def clean_data(df):
    # Simulasi pembersihan data: hapus baris dengan nilai kosong
    return df.dropna()

def transform_data(df):
    # Simulasi transformasi: hitung total per kategori
    return df.groupby('category')['amount'].sum().reset_index()

def run_pipeline(input_path, output_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"File {input_path} tidak ditemukan!")
    
    df = pd.read_csv(input_path)
    clean_df = clean_data(df)
    result = transform_data(clean_df)
    result.to_csv(output_path, index=False)
    return True