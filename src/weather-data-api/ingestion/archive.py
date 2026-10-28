from data_pipeline_platform.constants.baseurl import OPEN_METEO_ARCHIVE
from data_pipeline_platform.ingestion.open_meteo import OpenMeteoBase


class Archive(OpenMeteoBase):
    name = "open_meteo_archive"
    default_url = OPEN_METEO_ARCHIVE
