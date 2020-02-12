# Cuba Weather Red Cuba Python Examples

Example of application programming interface of the Cuba Weather project for [www.redcuba.cu](https://www.redcuba.cu) implemented in Python.

```python
from cuba_weather_redcuba import CubaWeatherRedCuba

location = input('Insert municipality:')

api = CubaWeatherRedCuba()

weather = api.get(location)

print(weather)
```
