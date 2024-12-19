import requests
import locale

from . import __version__

API_URL = "https://<locale>.wikipedia.org/api/rest_v1/page/random/summary"


def main(locale_code: str = None) -> tuple:
    localed_url = (
        API_URL.replace("<locale>", locale_code)
        if locale_code
        else API_URL.replace("<locale>", str(locale.getlocale()[0][0:2]))
    )

    with requests.get(localed_url) as response:
        response.raise_for_status()
        data = response.json()

    return data["title"], data["extract"]
