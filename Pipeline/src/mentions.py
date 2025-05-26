import pandas as pd
import json
import numpy as np
from datetime import datetime
from unidecode import unidecode


def check_mentions_and_create_dict(drugs:pd.DataFrame, publications:pd.DataFrame):

    result = {}

    drug_names = drugs['drug']
    
    for drug in drug_names:
        mention = []

        # recherche des publications ou le titre contient le nom du médicament
        # le regex=True indique qu’on utilise une expression régulière
        # le na=False évite une erreur quand la colonne contient des nulles
        # le /b indique qu'on cherche le mot exact et limité a ce mot la 
        # le rf au debut du contains pour inserer une varibale ( le f ) et conserver les '/' dans la regex
        matched = publications[publications['title'].str.contains(rf"\b{drug}\b",  na=False, regex=True)]

        for _, row in matched.iterrows():
            mention.append({
                'title': row['title'],
                'journal': row['journal'],
                'date': row['date'],
                'source': row['source']
            })

        result[drug] = mention
    
    return result