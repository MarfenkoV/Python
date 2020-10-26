import pprint
import requests
from dateutil.parser import parse


class YahooWeatherForecast:

    def get(self, city):
        url = f"https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22{city}%22)%20and%20u%3D%27c%27&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
        data = requests.get(url).json()
        forecast_data = data["query"]["results"]["channel"]["item"]["forecast"]
        forecast = []
        for day_data in forecast_data:
            forecast.append({
                "date": parse(day_data["date"]),
                "high_temp": day_data["high"]
            })

class CityInfo:

    def __init__(self, city):
        self.city = city

    def weather_forecast(self):
        pass


def _main():
    city_info = CityInfo("Moscow")
    forecast = city_info.weather_forecast()
    pprint.pprint(forecast)



if __name__=="__main__":
    _main()