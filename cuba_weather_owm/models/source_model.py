from math import sqrt

class SourceModel:
  def __init__(self, name: str, lat: float, lon: float):
    self.name = name
    self.lat = lat
    self.lon = lon

  def distance(self, lat: float, lon: float) -> float:
    '''
      Method that return the distance between source and input lat and lon
    '''
    return sqrt(pow(self.lat - lat, 2) + pow(self.lon - lon, 2))