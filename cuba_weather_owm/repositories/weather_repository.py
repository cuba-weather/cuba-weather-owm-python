from ..data_providers import WeatherApiClient
from ..models import SourceModel, WeatherModel

class WeatherRepository:
  '''
    Class to provide the functionality of obtaining weather data
  '''
  def __init__(self):
    self.weatherApiClient = WeatherApiClient()

  def getWeather(self, source: SourceModel) -> WeatherModel:
    return self.weatherApiClient.fetchWeather(source.pattern)