import json
from pathlib import Path

# Get the project directory
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "inventory.json"


def load_data():
    """
    Load inventory data from the JSON file.
    Returns an empty list if the file does not exist or is invalid.
    """
    DATA_DIR.mkdir(exist_ok=True)

    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data

            return []

    except (json.JSONDecodeError, OSError):
        return []


def save_data(products):
    """
    Save inventory data to the JSON file.
    """
    DATA_DIR.mkdir(exist_ok=True)

    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(products, file, indent=4, ensure_ascii=False)

        return True

    except OSError:
        return False
