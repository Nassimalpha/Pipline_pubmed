import pandas as pd
import json
import numpy as np
from datetime import datetime


from loader import *
from cleaner import *
from mentions import check_mentions_and_create_dict
from writer import mentions_to_json


# loading and preprocessing: 
drugs = process_drugs(load_drugs())
clinilical_trials = process_clinical_trials_dataframe(load_clinical_trials())
pubmed = process_pubmed_dataframe(load_pubmed(), load_pubmed_json())

# concat ( or merge) sources : 
publications = pd.concat([clinilical_trials, pubmed], ignore_index=True)

#  drugs graph  :
mentions_dict = check_mentions_and_create_dict(drugs, publications)

# export in json:
mentions_to_json(mentions_dict, "output/graph.json")