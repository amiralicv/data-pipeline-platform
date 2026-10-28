from weather_data_api.constants.baseurl import OPEN_METEO_CUSTOMER
from weather_data_api.ingestion.open_meteo import OpenMeteoBase


class Customer(OpenMeteoBase):
    name = "open_meteo_customer"
    default_url = OPEN_METEO_CUSTOMER
