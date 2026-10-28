from weather_data_api.constants.baseurl import OPEN_METEO_GEOCODING
from weather_data_api.ingestion.open_meteo import OpenMeteoBase


class Geocoding(OpenMeteoBase):
    name = "open_meteo_geocoding"
    default_url = OPEN_METEO_GEOCODING
