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

    # merge the rows that has the value "title" or "date" with those with NAN 
    original_columns = df.columns  # Sauvegarder l'ordre original
    grouped = df.groupby(["title"], dropna=False)
    df = grouped.agg(lambda x: x.dropna().iloc[0] if x.dropna().any() else np.nan).reset_index()
    df = df.reset_index()[original_columns]

    #  source to know whiche source it came from 
    df['source'] = "clinical_trials"
    
    return df


############## process pubmed data
def process_pubmed_dataframe(pubcsv: pd.DataFrame, pubjson: pd.DataFrame) -> pd.DataFrame:
    df = pd.concat([pubcsv, pubjson], ignore_index=True)
    
    #  column source to know which source it came from
    df['source'] = "pubmed"

    return df

############## process drugs data
def process_drugs(drug: pd.DataFrame) -> pd.DataFrame:
    drug['drug'] = drug['drug'].apply(Standarization)
    return drug


# ########### Global cleaning
def clean(df: pd.DataFrame)-> pd.DataFrame:
    
    # manage spaces and replace them with NaN values
    for column in df.columns:
        df[column] = df[column].replace(r'^\s*$', np.nan, regex=True)

    # delete NaN titles
    df = delete_missing_data_on_column(df, "title")

    # date processing
    df['date'] = df['date'].apply(parse_date_mixed)
    
    # standarization (lower, accents, spaces, commas, ...)
    df['title'] = df['title'].apply(Standarization)
    df['journal'] = df['journal'].apply(Standarization)

    return df