from data_pipeline_platform.constants.baseurl import OPEN_METEO_MARINE
from data_pipeline_platform.ingestion.open_meteo import OpenMeteoBase


class Marine(OpenMeteoBase):
    name = "open_meteo_marine"
    default_url = OPEN_METEO_MARINE
