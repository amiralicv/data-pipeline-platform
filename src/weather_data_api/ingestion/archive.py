from weather_data_api.constants.baseurl import OPEN_METEO_ARCHIVE
from weather_data_api.ingestion.open_meteo import OpenMeteoBase


class Archive(OpenMeteoBase):
    name = "open_meteo_archive"
    default_url = OPEN_METEO_ARCHIVE
