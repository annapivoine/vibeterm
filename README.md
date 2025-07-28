# Vibeterm

Vibeterm is a CLI tool that shows a random dad joke, inspirational quote, fortune cookie message, lifehack, or useless fact whenever you run it.

## Features

- Random content each run: dad jokes, quotes, fortunes, lifehacks, facts.
- Configurable: choose which categories you want.
- Persistent preferences saved to a config file.

## Installation

```sh
git clone https://github.com/annapivoine/vibeterm.git
cd vibeterm
make build
```

This creates a vibeterm binary in the project directory.

Optional cleanup:

```sh
make clean
```

(removes intermediate build files but keeps the compiled binary.)

## Usage

### Run Vibeterm:

`./vibeterm`

### Options

- `-i`, `--include`: Specify which content types to include (e.g., `dadjokes quotes`, you can also include `all`).
- `-e`, `--exclude`: Specify which content types to exclude (e.g., `facts lifehacks`).
- `--update-config`: Update your configuration preferences.
- `--view-config`: View your current configuration.

### Example:

```sh
./vibeterm --include quotes fortune --update-config
./vibeterm --view-config
```

## Configuration

Stored in:
`~/.vibeterm/config.json`

Default:

```json
{
  "preferences": {
    "include": ["dadjokes", "quotes", "fortune", "lifehacks", "facts"],
    "exclude": []
  }
}
```

## Providers

- Dad Jokes: [icanhazdadjoke.com](https://icanhazdadjoke.com/)
- Quotes, Lifehacks, Fortune Cookies, Facts: [viewbits.com](https://viewbits.com/)

## Project Structure

- `__main__.py`: Entry point for the CLI.
- `cli.py`: Argument parsing.
- `config.py`: Configuration management.
- `runner.py`: Main logic for selecting and displaying content.
- `providers/`: Individual content providers.

## Important note

This project was made for the [Boot.dev](https://www.boot.dev/) Hackathon. The binary runs a bit slow because Python isn’t really meant to be compiled. I went with a binary anyway just to make it easier for people to try out. I could use another language to make it faster, but that’s not where I’m at yet.

## License

MIT License.

---

Enjoy some good vibes in your terminal!
