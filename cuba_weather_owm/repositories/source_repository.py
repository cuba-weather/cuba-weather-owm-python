from cuba_weather_municipality import MunicipalityModel
from ..data_providers import sources
from ..models import SourceModel

class SourceRepository:
  '''
    Class to provide the functionality of searching for a source
  '''

  def getSource(self, municipality: MunicipalityModel) -> SourceModel:
    '''
      Method that returns the source closest to the given municipality.
    '''
    queryLat = municipality.lat
    queryLon = municipality.lon
    bestSource = sources[0]
    bestDistance = bestSource.distance(queryLat, queryLon)

    for i in range(1, len(sources)):
      tempSource = sources[i]
      tempDistance = tempSource.distance(queryLat, queryLon)

      if tempDistance < bestDistance:
        bestSource = tempSource
        bestDistance = tempDistance

    return bestSource
