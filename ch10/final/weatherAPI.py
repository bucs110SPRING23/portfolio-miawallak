import requests
import json

class WeatherAPI:

    def __init__(self):
        self.url = "http://dataservice.accuweather.com/forecasts/v1/daily/10day/"
       
       
    def get_daily_forecasts(self, location_key):
        url = f"{self.base_url}/forecasts/v1/daily/10day/{location_key}"
        r = requests.get(url, params={"apikey": self.api_key})
        return r.json() 
