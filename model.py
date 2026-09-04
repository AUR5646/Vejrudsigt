import requests



class WeatherModel:
    
    def __init__(self):
        self.apiKey = "7016957b15f8e6b9c1a1fd757ef8a94d"          
        self.city = "Copenhagen"
        self.countryCode = "DK"
        self.basePoint = "https://api.openweathermap.org/data/2.5/"
        self.endPoint = "weather"

    def request(self):
        params = {
            "q": f"{self.city},{self.countryCode}",
            "appid": self.apiKey,
            "units": "metric",   # Giver temperatur i celsius
            "lang": "da"         # Vejrbeskrivelser på dansk
        }
        url = self.basePoint + self.endPoint
        return requests.get(url, params=params)