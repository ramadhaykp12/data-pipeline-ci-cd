import pandas as pd
import pytest
from etl_process import clean_data, transform_data

def test_clean_data():
    raw_data = pd.DataFrame({
        'category': ['A', 'B', None],
        'amount': [100, 200, 300]
    })
    cleaned = clean_data(raw_data)
    # Memastikan baris dengan None dihapus
    assert len(cleaned) == 2

def test_transform_data():
    data = pd.DataFrame({
        'category': ['A', 'A', 'B'],
        'amount': [100, 150, 200]
    })
    transformed = transform_data(data)
    # Memastikan total kategori A adalah 250
    val_a = transformed[transformed['category'] == 'A']['amount'].values[0]
    assert val_a == 250