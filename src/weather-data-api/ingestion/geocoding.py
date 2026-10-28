from data_pipeline_platform.constants.baseurl import OPEN_METEO_GEOCODING
from data_pipeline_platform.ingestion.open_meteo import OpenMeteoBase


class Geocoding(OpenMeteoBase):
    name = "open_meteo_geocoding"
    default_url = OPEN_METEO_GEOCODING
