import yaml
import json
import csv
import pandas as pd
from pathlib import Path

def load_deck(file_path: str, deck_name: str = None) -> dict:
    """
    Loads an input deck containing key: value pairs from a file.
    Supported file formats are YAML, JSON, and CSV. Each file should
    contain
    """
    path = Path(file_path)
    if not deck_name:
        deck_name = path.stem.replace("_", " ").title()
    if path.suffix == ".yaml":
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    elif path.suffix == ".json":
        with open(path, 'r') as f:
            return {deck_name: json.load(f)}
    elif path.suffix == ".csv":
        with open(path, "r") as f:
            df = pd.read_csv(f)
            return {deck_name: dict(zip(df.iloc[:, 0], df.iloc[:, 1]))}
    else:
        raise ValueError(f"Unsupported file format:\t{path.suffix}")
    
if __name__ == "__main__":
    import os
    print(os.getcwd())
    file_path = Path("examples/example_data/german_nouns.yaml")
    deck = load_deck(file_path, "German Nouns")
    print(deck)