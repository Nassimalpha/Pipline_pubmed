import pandas as pd
import json

def load_clinical_trials():
    return pd.read_csv("Pipeline/data/clinical_trials.csv")

def load_drugs():
    return pd.read_csv("Pipeline/data/drugs.csv")

def load_pubmed():
    return pd.read_csv("Pipeline/data/pubmed.csv")

def load_pubmed_json():
        with open("Pipeline/data/pubmed.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
            return pd.json_normalize(data)  