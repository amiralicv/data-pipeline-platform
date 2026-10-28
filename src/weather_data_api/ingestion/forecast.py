from weather_data_api.constants.baseurl import OPEN_METEO_FORECAST
from weather_data_api.ingestion.open_meteo import OpenMeteoBase


class Forecast(OpenMeteoBase):
    name = "open_meteo_forecast"
    default_url = OPEN_METEO_FORECAST
