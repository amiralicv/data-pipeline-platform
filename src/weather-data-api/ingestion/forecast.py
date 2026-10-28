from data_pipeline_platform.constants.baseurl import OPEN_METEO_FORECAST
from data_pipeline_platform.ingestion.open_meteo import OpenMeteoBase


class Forecast(OpenMeteoBase):
    name = "open_meteo_forecast"
    default_url = OPEN_METEO_FORECAST
