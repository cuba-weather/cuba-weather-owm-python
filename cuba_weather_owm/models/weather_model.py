from datetime import datetime

class WeatherModel:
  '''
    Model class for mapping the json returned by the https://www.insmet.cu weather API
  '''

  def __init__(self, location, date, daysForecast):
    self.cityName: str = location
    self.datetime = date

    self.days = []

    for w in daysForecast:
      self.days.append(WeatherDayModel(w))

  def __str__(self):
    result: str = ''
    result += 'City Name: {}\n'.format(self.cityName)
    result += 'Datetime Update: {}\n'.format(self.datetime)

    for w in self.days:
      result += '{}\n'.format(w)

    return result

class WeatherDayModel:
  '''
    Model class for mapping part of the json returned by the https://www.insmet.cu weather API
  '''

  def __init__(self, owm):
    self.day = owm.get_reference_time('date')
    self.tmax = owm.get_temperature(unit='celsius')['temp_max']
    self.tmin = owm.get_temperature(unit='celsius')['temp_min']
    self.description = owm.get_detailed_status()

  def __str__(self):
    return '''
    \nDay: {}\n 
    Maximum Temperature: {}°C\n
    Minimum Temperature: {}°C\n 
    Description: {}\n
    '''.format(self.day, self.tmax, self.tmin, self.description)