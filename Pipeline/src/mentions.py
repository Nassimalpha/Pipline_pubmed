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

        # search for publications or titles that contains the drug name 
        # regex=True for regular expressions
        # na=False to avoid the error in NaN cases
        # le /b indique to get the exct word inside
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