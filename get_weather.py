import requests
import json

from urllib.parse import urlencode


class Weather:
    def __init__(self):
        self.baseurl = "https://query.yahooapis.com/v1/public/yql?"
        self.format = "&format=json"
        self.yql_query = ''
        self.yql_url = ''
        self.woeID = ''

    def get_woeid(self, loc):
        self.yql_query = f'select woeid from geo.places where text="{loc}"'
        self.yql_url = self.baseurl + urlencode({'q': self.yql_query}) + self.format
        result = requests.get(self.yql_url).text
        data = json.loads(result)
        try:
            self.woeID = data['query']['results']['place']['woeid']
        except TypeError:
            self.woeID = data['query']['results']['place'][0]['woeid']

    def get_weather(self):
        self.yql_query = f'select * from weather.forecast where woeid={self.woeID}'
        self.yql_url = self.baseurl + urlencode({'q': self.yql_query}) + self.format
        result = requests.get(self.yql_url).text
        weather_data = json.loads(result)

        return weather_data

    def get_5day_forecast(self):
        weather_data = self.get_weather()
        five_day_forecast = weather_data['query']['results']['channel']['item']['forecast']

        return five_day_forecast
