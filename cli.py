import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Vibeterm is a CLI tool that delivers random dad jokes, inspirational quotes, fortune cookie readings, lifehacks and useless facts every time you open your terminal.\nAvailable options are: dadjokes, quotes, fortune, lifehacks, facts.",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("-i", "--include", nargs='+', help="Content types to include (e.g., dadjokes quotes) separated by space.")
    parser.add_argument("-e", "--exclude", nargs='+', help="Content types to exclude (e.g., facts lifehacks) separated by space.")
    parser.add_argument("--update-config", action="store_true", help="Update configuration.")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--view-config", action="store_true", help="View the current configuration.")

    return parser.parse_args(), parser
