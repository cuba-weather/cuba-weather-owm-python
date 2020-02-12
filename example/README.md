# Cuba Weather OWM Examples

```python
from cuba_weather_owm import CubaWeatherOWM

API_KEY = 'YOUR OPENWEATHERMAP KEY'

location = input('Insert municipality:')

api = CubaWeatherOWM(API_KEY)

weather = api.get(location)

print(weather)
```
