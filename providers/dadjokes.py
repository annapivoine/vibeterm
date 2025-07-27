## Get random dad joke
import urllib.request

url = "https://icanhazdadjoke.com/"
headers = {
    "Accept": "text/plain",
    "User-Agent": "My silly project (https://github.com/annapivoine/vibeterm)"
    }

def get_dad_joke():
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request) as f:
        joke = f.read().decode('utf-8')
        return joke
