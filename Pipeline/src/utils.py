import pandas as pd
import json
import numpy as np
from datetime import datetime
import unicodedata
from unidecode import unidecode
import re

def delete_missing_data_on_column(df: pd.DataFrame, subset: str):
    no_nan = df.dropna(subset=[subset])
    return no_nan


def parse_date_mixed(date_str):
    from datetime import datetime
    # 1. test parsing with format %d/%m/%Y (format slash)
    try:
        return datetime.strptime(date_str, '%d/%m/%Y')
    except:
        pass
    
    # 2. test parsing with format%d %B %Y (format text month)
    try:
        return datetime.strptime(date_str, '%d %B %Y')
    except:
        pass
    
    # 3. fallback avec pandas to_datetime
    try:
        return pd.to_datetime(date_str, dayfirst=True)
    except:
        return pd.NaT
    

def Standarization(texte):
    if pd.isnull(texte):
        return ''

    # replace the '-' with spaces to no lose the word due to concatenation
    texte = texte.replace('-', ' ')
    # delete  accents
    texte = unicodedata.normalize('NFD', texte).encode('ascii', 'ignore').decode('utf-8')
    # delete la ponctuation
    texte = re.sub(r'[^\w\s]', '', texte)
    # to lower
    texte = texte.lower()
    return texte


    