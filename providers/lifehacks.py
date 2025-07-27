## Get random lifehack
import urllib.request
import json

url = "https://api.viewbits.com/v1/lifehacks?mode=random"
headers = {
    "User-Agent": "My silly project (https://github.com/annapivoine/vibeterm)"
    }

def get_lifehack():
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request) as f:
        response = json.load(f)
        lifehack = response["text"]
        return lifehack
