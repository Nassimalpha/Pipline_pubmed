import json
import os

def mentions_to_json(drug_mentions: dict, output_path: str = "Pipeline/output/medicaments.json"):

    # creer le dossier output si il n'existe pas    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # fichier en ecriture avec l'encoding pour les caracteres spécieaux 
    with open(output_path, "w", encoding="utf-8") as f:
        # le contenu du dictionnaire dans le fichier JSON 
        json.dump(drug_mentions, f, indent=2, ensure_ascii=False)

    