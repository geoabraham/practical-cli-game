import requests
from . import __version__

API_URL = "https://{locale}.wikipedia.org/api/rest_v1/page/random/summary"


def main(locale_code: str = None) -> tuple:
    locale_code = locale_code or locale.getdefaultlocale()[0]

    try:
        response = requests.get(API_URL.format(locale=locale_code))

        if not response.ok:
            raise Exception(f"Failed to retrieve random page: {response.status_code}")

        data = response.json()
        return data["title"], data["extract"]

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None, None
