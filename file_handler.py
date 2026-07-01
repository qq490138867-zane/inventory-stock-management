import json
import os


DATA_FILE = "data/inventory.json"


def load_data():
    """Load product data from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_data(products):
    """Save product data to JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(products, file, indent=4)
