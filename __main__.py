import ssl, certifi
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

from cli import parse_args
from config import read_config
from config import write_config
from runner import run_provider
import pprint

args, parser = parse_args()

all_sources = {"dadjokes", "quotes", "fortune", "lifehacks", "facts"}
active_sources = set()

if args.view_config:
    pprint.pprint(read_config())

if args.update_config and not any([args.include, args.exclude]):
    parser._print_message("You need to use one of the flags: --include or --exclude")

if args.update_config and any([args.include, args.exclude]):
    config = read_config()
    preferences = config.setdefault("preferences", {})

    if args.include:
        if "all" in args.include:
            preferences["include"] = list(all_sources)
            preferences["exclude"] = []
        else:
            new_include = set(args.include)
            new_exclude = all_sources - new_include
            preferences["include"] = list(new_include)
            preferences["exclude"] = list(new_exclude)
    elif args.exclude:
        current_include = set(preferences.get("include", all_sources))
        new_exclude = set(args.exclude)
        current_include -= new_exclude
        new_include = current_include
        new_exclude = all_sources - new_include
        preferences["include"] = list(new_include)
        preferences["exclude"] = list(new_exclude)

    write_config(config)
    print("Configuration updated.")
    print("Current configuration:")
    pprint.pprint(read_config())
    exit(0)

if not args.include and not args.exclude:
    config = read_config()
    preferences = config.get("preferences", {})
    include = preferences.get("include", [])
    exclude = preferences.get("exclude", [])

    if include:
        active_sources = set(include)
    else:
        active_sources = all_sources.copy()

    if exclude:
        active_sources -= set(exclude)

if args.include and args.exclude:
    print("Warning: --include and --exclude used together; --include will take precedence.")

if args.include:
    if "all" in args.include:
        active_sources = all_sources.copy()
    else:
        invalid_sources = set(args.include) - all_sources
        if invalid_sources:
            print(f"Invalid sources: {', '.join(invalid_sources)}, please use one of: {', '.join(all_sources)} or all.")
            exit(1)
        active_sources = set(args.include)
    print(f"You are going to receive one of the following: {', '.join(active_sources)}")

elif args.exclude:
    invalid_sources = set(args.exclude) - all_sources
    if invalid_sources:
        print(f"Invalid sources: {', '.join(invalid_sources)}, please use one of: {', '.join(all_sources)}.")
        exit(1)
    active_sources = all_sources - set(args.exclude)
    print(f"You are going to receive one of the following: {', '.join(active_sources)}.")

else:
    config = read_config()
    preferences = config.get("preferences", {})
    include = preferences.get("include", [])
    exclude = preferences.get("exclude", [])

    active_sources = set(include) if include else all_sources.copy()
    if exclude:
        active_sources -= set(exclude)

if not (active_sources or args.view_config or args.update_config):
    print("No active sources found from args or config.")
    exit(1)

if not (args.view_config or args.update_config):
    run_provider(active_sources)
