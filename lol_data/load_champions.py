import json
import requests

from lol_data import settings


def load_champions() -> None:
    response = requests.get(settings.champions_api_url)
    response_json = response.json()

    # We create a new dictionary based on API response selecting some keys and using the champion's name as the key
    champions = {
        k: {dk: dv for dk, dv in v.items() if dk in settings.champions_key_selection}
        for k, v in response_json["data"].items()
    }

    champions_json = json.dumps(champions)

    # Then we save the data as JSON in a file (always overriding it)
    with open(settings.champions_data_path, mode="w", encoding="utf-8") as file:
        file.write(champions_json)
