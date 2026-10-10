from data_pipeline_platform.constants.baseurl import OPEN_METEO_CUSTOMER
from data_pipeline_platform.ingestion.open_meteo import OpenMeteoBase


class Customer(OpenMeteoBase):
    name = "open_meteo_customer"
    default_url = OPEN_METEO_CUSTOMER
