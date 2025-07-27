## Get random useless fact
import urllib.request
import json

url = "https://api.viewbits.com/v1/uselessfacts?mode=random"
headers = {
    "User-Agent": "My silly project (https://github.com/annapivoine/vibeterm)"
    }

def get_fact():
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request) as f:
        response = json.load(f)
        fact = response["text"]
        return fact
