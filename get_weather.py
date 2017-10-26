import json
from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup


class Weather:
    """The Weather() class is used to get all pertinent information related to Yahoo YQL"""

    def __init__(self):
        self.baseurl = "https://query.yahooapis.com/v1/public/yql?"
        self.format = "&format=json"
        self.yql_query = ''
        self.yql_url = ''
        self.woeID = ''

    def get_woeid(self, loc):
        """
        This method is used to get the `woeid` from YQL. Every city, state, country etc.
        has its own unique woeid. With the woeid it is eaiser and more accurate to get
        any information.

        :param loc: the location entered by the user on the front end. This will be a city,
                     or country.
        :return: woeid
        """
        self.yql_query = f'select woeid from geo.places where text="{loc}"'
        self.yql_url = self.baseurl + urlencode({'q': self.yql_query}) + self.format
        result = requests.get(self.yql_url).text
        data = json.loads(result)
        try:
            self.woeID = data['query']['results']['place']['woeid']
        except TypeError:
            self.woeID = data['query']['results']['place'][0]['woeid']

    def get_weather(self):
        """
        This method will take the woeid received from the get_woeid() method and it
        will send off the request to fetch the JSON weather information for that woeid

        :return: JSON weather data
        """
        self.yql_query = f'select * from weather.forecast where woeid={self.woeID}'
        self.yql_url = self.baseurl + urlencode({'q': self.yql_query}) + self.format
        result = requests.get(self.yql_url).text
        weather_data = json.loads(result)

        return weather_data

    def get_5day_forecast(self):
        """
        This method will take the returned JSON data from get_weather() and get
        the 5-day forecast.

        :return: JSON 5-day forecast
        """
        weather_data = self.get_weather()
        five_day_forecast = weather_data['query']['results']['channel']['item']['forecast']

        return five_day_forecast

    @staticmethod
    def weather_codes():
        """
        This method scrapes the Yahoo YQL documentation for all the weather status codes. There
        are 48 weather codes. Each code matches a description (i.e. 32 --> "sunny") and each
        description will be mapped to the description of the WeatherIcon.js description provided
        for each icon.

        :return: dictionary of codes
        """
        url = 'https://developer.yahoo.com/weather/documentation.html'
        r = requests.get(url)

        if r.status_code == 200:
            html = r.text
            soup = BeautifulSoup(html, 'lxml')
            table = soup.find('table', {'id': 'codetable'})
            rows = table.find_all('tr')

            codes = {}
            for row in rows[1::]:
                cols = row.find_all('td')
                code = cols[0].text
                desc = cols[1].text
                codes[code] = desc
            return codes
        else:
            raise ConnectionError(f'Could not connect to the URL "{url}"')
