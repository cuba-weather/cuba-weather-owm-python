from cuba_weather_redcuba import CubaWeatherRedCuba

location = input('Insert municipality:')

api = CubaWeatherRedCuba()

weather = api.get(location)

print(weather)