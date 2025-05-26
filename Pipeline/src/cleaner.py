import pandas as pd
import json
import numpy as np
from datetime import datetime
from unidecode import unidecode

from utils import delete_missing_data_on_column, parse_date_mixed, Standarization



############## process clinical trials data
def process_clinical_trials_dataframe(df: pd.DataFrame) -> pd.DataFrame:

    # rename column : 
    df = df.rename(columns={"scientific_title": "title"})

    # Fussionner les rows ayant la meme valeur "title" and "date" mais NAN ailleurs
    original_columns = df.columns  # Sauvegarder l'ordre original
    grouped = df.groupby(["title"], dropna=False)
    df = grouped.agg(lambda x: x.dropna().iloc[0] if x.dropna().any() else np.nan).reset_index()
    df = df.reset_index()[original_columns]

    # colonne source pour garder une trace de la provenance de la donnée 
    df['source'] = "clinical_trials"
    
    return df


############## process pubmed data
def process_pubmed_dataframe(pubcsv: pd.DataFrame, pubjson: pd.DataFrame) -> pd.DataFrame:
    df = pd.concat([pubcsv, pubjson], ignore_index=True)
    
    # colonne source pour garder une trace de la provenance de la donnée 
    df['source'] = "pubmed"

    return df

############## process drugs data
def process_drugs(drug: pd.DataFrame) -> pd.DataFrame:
    drug['drug'] = drug['drug'].apply(Standarization)
    return drug


# ########### Global cleaning
def clean(df: pd.DataFrame)-> pd.DataFrame:
    
    # gerer les espaces vides et les remplacer pas NaN
    for column in df.columns:
        df[column] = df[column].replace(r'^\s*$', np.nan, regex=True)

    # Supprimer les "title" null
    df = delete_missing_data_on_column(df, "title")

    # formatage de date
    df['date'] = df['date'].apply(parse_date_mixed)
    
    # formater et uniformiser les titres et journeaux (minuscules, sans accents éventuels)
    df['title'] = df['title'].apply(Standarization)
    df['journal'] = df['journal'].apply(Standarization)

    return df