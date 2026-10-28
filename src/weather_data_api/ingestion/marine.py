from weather_data_api.constants.baseurl import OPEN_METEO_MARINE
from weather_data_api.ingestion.open_meteo import OpenMeteoBase


class Marine(OpenMeteoBase):
    name = "open_meteo_marine"
    default_url = OPEN_METEO_MARINE
