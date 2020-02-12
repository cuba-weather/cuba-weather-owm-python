__version__ = '0.0.8'

from cuba_weather_municipality import CubaWeatherMunicipality
from .models import WeatherModel
from .repositories import SourceRepository, WeatherRepository

class CubaWeatherOWM:
  def __init__(self, api_key):
    self._cubaWeatherMunicipality = CubaWeatherMunicipality()
    self._sourceRepository = SourceRepository()
    self._weatherRepository = WeatherRepository(api_key)

  def get(self, input: str) -> WeatherModel:
    '''
      Method that given a municipality searches the cuban municipalities to find the best match and returns the weather information.
    '''
    municipality = self._cubaWeatherMunicipality.get(input, suggestion=True)
    source = self._sourceRepository.getSource(municipality)
    weather = self._weatherRepository.getWeather(source)
    weather.cityName = municipality.name
    return weather