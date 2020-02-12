import xml.etree.ElementTree as ET
from urllib.request import urlopen

from ..models import WeatherModel
from ..utils import BadRequestException, ParseException, InvalidSourceException

from pyowm import OWM
import os

class WeatherApiClient:
  '''
    Class to provide the functionality of making API requests
  '''
  def __init__(self, api_key):
    self.api = OWM(api_key, language='es')
  
  def fetchWeather(self, location: str) -> WeatherModel:
    '''
      Method to make the request GET to API
    '''
    
    res = self.api.three_hours_forecast(location)

    f = res.get_forecast()

    date = f.get_reception_time('date')

    days_forecasts = []

    for i in range(0, len(f), 8):
      one_day = []
      for j in range(i, i+8):
        one_day.append(f.get(j))
      
      days_forecasts.append(one_day)

    return WeatherModel(location=location, date=date, daysForecast=days_forecasts)