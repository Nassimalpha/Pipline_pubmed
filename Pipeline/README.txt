Ce projet construit une pipeline de traitement de données permettant d'identifier 
les mentions de médicaments dans les publications scientifiques et essais cliniques, 
et de générer un graphe de liaison entre médicaments, journaux et dates de mention.


Les données sources sont stockées dans le dossier `data/` :

- `drugs.csv` : liste des médicaments à détecter
- `clinical_trials.csv` : données sur les essais cliniques
- `pubmed.csv` / `pubmed.json` : publications scientifiques 



1. **Chargement des données** (`loader.py`)
2. **Nettoyage et normalisation** (`cleaner.py`)
3. **Matching** (`mentions.py`)
4. **Export JSON** (`writer.py`)
4. **Main** (`main.py`)


Le résultat final est généré dans :
Pipeline/output/drug_mentions.json