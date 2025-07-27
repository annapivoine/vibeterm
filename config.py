import os
import json

CONFIG_PATH = os.path.expanduser("~/.vibeterm/config.json")
DEFAULT_CONFIG = {
    "preferences": {
        "include": ["dadjokes", "quotes", "fortune", "lifehacks", "facts"],
        "exclude": []
    }
}


def read_config():
    try:
        with open(CONFIG_PATH, "rb") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return DEFAULT_CONFIG.copy()

def write_config(input):
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        json.dump(input, f, indent=2)
