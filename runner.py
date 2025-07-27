import random
from providers import dadjokes, quotes, fortune, lifehacks, facts

call_providers = {
    "dadjokes": dadjokes.get_dad_joke,
    "quotes": quotes.get_quote,
    "fortune": fortune.get_fortune,
    "lifehacks": lifehacks.get_lifehack,
    "facts": facts.get_fact,
}

def print_framed(text):
    lines = text.split("\n")
    width = max(len(line) for line in lines)
    border = "+" + "-" * (width + 2) + "+"
    print(border)
    for line in lines:
        print(f"| {line.ljust(width)} |")
    print(border)

def pick_provider(active_sources):
    return random.choice(list(active_sources))

def run_provider(active_sources):
    provider_name = pick_provider(active_sources)
    fetch = call_providers.get(provider_name)
    content = fetch()

    if provider_name == "dadjokes":
        text = f"Dadjoke:\n{content}"
        print_framed(text)
    if provider_name == "quotes":
        quote, author = content
        text = f"Quote:\n{quote}\n     -- {author}"
        print_framed(text)
    if provider_name == "fortune":
        text = f"Your fortune cookie reading:\n{content}"
        print_framed(text)
    if provider_name == "lifehacks":
        text = f"Lifehack:\n{content}"
        print_framed(text)
    if provider_name == "facts":
        text = f"Useless fact:\n{content}"
        print_framed(text)
