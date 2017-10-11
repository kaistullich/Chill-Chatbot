# FIXME: ValueError: attempted relative import beyond top-level package
from ..get_weather import GetWeather

sf = 'san francisco, sf'
fra = 'frankfurt, ger'
wai = 'waikiki, hi'

sf_weather = GetWeather()
fra_weather = GetWeather()
wai_weather = GetWeather()

# get woeid for each city
sf_weather.get_woeid(sf)
fra_weather.get_woeid(fra)
wai_weather.get_woeid(wai)

# get full weather for each city
sf_weather.get_weather()
fra_weather.get_weather()
wai_weather.get_weather()

# get 5 day forecast
sf_weather.get_5day_forecast()
fra_weather.get_5day_forecast()
wai_weather.get_5day_forecast()
