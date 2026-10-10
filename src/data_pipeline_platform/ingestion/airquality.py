from data_pipeline_platform.constants.baseurl import OPEN_METEO_AIR_QUALITY
from data_pipeline_platform.ingestion.open_meteo import OpenMeteoBase


class AirQuality(OpenMeteoBase):
    name = "open_meteo_air_quality"
    default_url = OPEN_METEO_AIR_QUALITY
