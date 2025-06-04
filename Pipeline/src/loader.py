import pandas as pd
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # <- on remonte à project_root
DATA_DIR = os.path.join(BASE_DIR, 'data')

def load_clinical_trials():
    path = os.path.join(DATA_DIR, 'clinical_trials.csv')
    return pd.read_csv(path)


def load_drugs():
    path = os.path.join(DATA_DIR, 'drugs.csv')
    return pd.read_csv(path)

def load_pubmed():
    path = os.path.join(DATA_DIR, 'pubmed.csv')
    return pd.read_csv(path)

def load_pubmed_json():
    path = os.path.join(DATA_DIR, 'pubmed.json')
        
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return pd.json_normalize(data)  