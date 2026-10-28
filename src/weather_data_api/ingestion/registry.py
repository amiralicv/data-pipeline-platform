from weather_data_api.ingestion.airquality import AirQuality
from weather_data_api.ingestion.archive import Archive
from weather_data_api.ingestion.customer import Customer
from weather_data_api.ingestion.forecast import Forecast
from weather_data_api.ingestion.geocoding import Geocoding
from weather_data_api.ingestion.marine import Marine

SOURCES = {
    cls.name: cls
    for cls in (Forecast, Archive, Geocoding, AirQuality, Marine, Customer)
}
