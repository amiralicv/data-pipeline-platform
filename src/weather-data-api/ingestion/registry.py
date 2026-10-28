from data_pipeline_platform.ingestion.airquality import AirQuality
from data_pipeline_platform.ingestion.archive import Archive
from data_pipeline_platform.ingestion.customer import Customer
from data_pipeline_platform.ingestion.forecast import Forecast
from data_pipeline_platform.ingestion.geocoding import Geocoding
from data_pipeline_platform.ingestion.marine import Marine

SOURCES = {
    cls.name: cls
    for cls in (Forecast, Archive, Geocoding, AirQuality, Marine, Customer)
}
