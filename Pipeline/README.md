# Drug Mention Graph Builder

This project builds a graph linking **drugs** to their mentions in:
- **Scientific publications** (PubMed)
- **Clinical trials** (Clinical Trials)

Each connection is annotated with:
- the **publication date**
- the **journal name**

##  Objective

> Identify drug mentions through the titles of publications and trials, and generate a structured JSON graph representing the relationships between drugs, journals, and dates.


## Project Directory

Make sure to navigate into the `Pipeline` directory before running any commands:

```bash
cd Pipeline
```
because outside of `Pipeline` we find the find the folders `Questions` and `SQL` that mainly for the other theorical parts of the project   
## Project Structure

```
project_root/
├── data/
│   ├── drugs.csv
│   ├── pubmed.csv
│   ├── pubmed.json
│   └── clinical_trials.csv
├── output/
│   └── graph.json
├── src/
│   ├── loader.py          # Load data from CSV/JSON
│   ├── cleaner.py         # Clean and normalize data
│   ├── mentions.py        # Match drugs in publication titles
│   ├── writer.py          # Build the final graph
│   ├── utils.py           # functions to use 
│   └── main.py            # Orchestrate the pipeline
│── test/
│   └── test.py            # tester la fonction clean avec un simple exemple
│
├── requirements.txt
└── README.md
```

##  Business Rules

- A **drug** is considered mentioned if its name appears in the **title** of a publication or clinical trial.
- A **journal** is linked to a drug if it published a **mentioning article**.

##  How to Run



1. Create the virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the environment:
  ```bash
  .\venv\Scripts\activate
   ```
> You’ll know the environment is activated when you see `(venv)` in your terminal prompt.


3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the main pipeline script:
   ```bash
   python src/main.py
   ```

5. The output is saved as:
   ```
   output/graph.json
   ```

6. Deactivate when you're done working:
```bash
deactivate
```

## Input Data

- `drugs.csv` – list of drugs
- `pubmed.csv` & `pubmed.json` – scientific publications
- `clinical_trials.csv` – clinical trial metadata

##  Cleaning Process

- Dates are normalized to `YYYY-MM-DD`
- Duplicate entries (`title + journal + date`) are removed
- Missing data is flagged or kept based on configuration

## Output Format

A JSON file representing the graph:

```json
[
  {
    "drug": "aspirin",
    "mentions": [
      {
        "source": "pubmed",
        "journal": "the lancet",
        "date": "2020-05-03",
        "title": "aspirin reduces heart attack"
      },
      {
        "source": "clinical_trials",
        "journal": "nejm",
        "date": "2019-11-10",
        "title": "clinical effect of aspirin in stroke"
      }
    ]
  }
]
```


