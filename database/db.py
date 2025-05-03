import json
from pathlib import Path

db_file = Path("user_data.json")

def save_data(username: str, sequence: list):
    data = load_all()
    data[username] = data.get(username, []) + sequence
    with open(db_file, "w") as f:
        json.dump(data, f)

def load_user_data(username: str):
    data = load_all()
    return data.get(username, [])

def load_all():
    if db_file.exists():
        with open(db_file, "r") as f:
            return json.load(f)
    return {}
