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
      day = w[0].get_reference_time('date')
      tmax = w[0].get_temperature(unit='celsius')['temp_max']
      tmin = w[0].get_temperature(unit='celsius')['temp_min']
      description = w[0].get_detailed_status()
      for d in w:
        tmx = d.get_temperature(unit='celsius')['temp_max']
        tmn = d.get_temperature(unit='celsius')['temp_min']

        if tmx > tmax:
          tmax = tmx

        if tmn < tmin:
          tmin = tmn
        
      self.days.append(WeatherDayModel(day, tmax, tmin, description))

      self.today = self.days[0]

  def __str__(self):
    result: str = ''
    result += 'City Name: {}\n'.format(self.cityName)
    result += 'Datetime Update: {}\n'.format(self.datetime)
    result += 'Maximum Temperature: {}°C\n'.format(self.today.tmax)
    result += 'Minimum Temperature: {}°C\n'.format(self.today.tmin)
    result += 'Description: {}'.format(self.today.description)


    for i in range(1, len(self.days)):
      result += '{}\n'.format(self.days[i])

    return result

class WeatherDayModel:
  '''
    Model class for mapping part of the json returned by the https://www.insmet.cu weather API
  '''

  def __init__(self, day, tmax, tmin, description):
    self.day = day
    self.tmax = tmax
    self.tmin = tmin
    self.description = description

  def __str__(self):
    return '''
    \nDay: {}\n 
    Maximum Temperature: {}°C\n
    Minimum Temperature: {}°C\n 
    Description: {}\n
    '''.format(self.day, self.tmax, self.tmin, self.description)