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
    # 1. tenter parsing avec format %d/%m/%Y (format slash)
    try:
        return datetime.strptime(date_str, '%d/%m/%Y')
    except:
        pass
    
    # 2. tenter parsing avec format %d %B %Y (format texte mois)
    try:
        return datetime.strptime(date_str, '%d %B %Y')
    except:
        pass
    
    # 3. fallback avec pandas to_datetime (qui est plus permissif)
    try:
        return pd.to_datetime(date_str, dayfirst=True)
    except:
        return pd.NaT
    

def Standarization(texte):
    if pd.isnull(texte):
        return ''

    # Remplacer les '-' par des espace pour ne pas perdre le mot a cause de la concatenation qui viens ensuire
    texte = texte.replace('-', ' ')
    # Supprimer les accents
    texte = unicodedata.normalize('NFD', texte).encode('ascii', 'ignore').decode('utf-8')
    # Supprimer la ponctuation
    texte = re.sub(r'[^\w\s]', '', texte)
    # Mettre en minuscules
    texte = texte.lower()
    return texte


    