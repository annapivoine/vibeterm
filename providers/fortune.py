## Get random fortune cookie reading
import urllib.request
import json

url = "https://api.viewbits.com/v1/fortunecookie?mode=random"
headers = {
    "User-Agent": "My silly project (https://github.com/annapivoine/vibeterm)"
    }

def get_fortune():
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request) as f:
        response = json.load(f)
        fortune = response["text"]
        return fortune
