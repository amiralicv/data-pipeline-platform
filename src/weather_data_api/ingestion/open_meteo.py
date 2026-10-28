import requests

from weather_data_api.ingestion.base import Source


class OpenMeteoBase(Source):
    default_url: str

    def __init__(self, base_url: str | None = None, **params) -> None:
        self.base_url = base_url or self.default_url
        self.params = params

    def fetch(self) -> dict:
        response = requests.get(self.base_url, params=self.params, timeout=10)
        response.raise_for_status()
        return response.json()
