## Get random quote
import urllib.request
import json

url = "https://api.viewbits.com/v1/zenquotes?mode=random"
headers = {
    "User-Agent": "My silly project (https://github.com/annapivoine/vibeterm)"
    }

def get_quote():
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request) as f:
        response = json.load(f)
        content = response[0]
        quote = content["q"]
        author = content["a"]
        return quote, author
