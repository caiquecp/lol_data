# LoL Data

LoL Data is a Python application made to fetch League of Legends data from Riot's API.

## Installation

We use Poetry to manage this project dependencies.

```
poetry install
```

## Configuration

We are using a `.env` file to setup the configuration.

| env | description | required |
|---|---|---|
| api_url_champions | Riot API URL for champions JSON | yes |
| champions_key_selection | List of keys (fields) to consider when fetching champions data | yes |
| champions_data_path | Path to save champions data as JSON | yes |

## Usage

There are a few commands available at this moment.

Format code:

```
make format
```

Type checking with typing and mypy:

```
make check-typing
```

Run and build data (as JSON):

```
make run
```

## Contributing

I'm not accepting pull requests since it's a project made to learn/study some things and maybe build something else.

## License

It's private code (even if this repository is public) and will look for an appropriate license soon.