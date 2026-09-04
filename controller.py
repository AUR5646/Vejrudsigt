from datetime import datetime
 
 

class WeatherController:

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def getWeather(self):
        response = self.model.request()
        self.processingData(response)

    def processingData(self, response):
        data = response.json()
        print(data)

      
        city = data.get("name")
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        temp_min = data["main"]["temp_min"]
        temp_max = data["main"]["temp_max"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        icon = data["weather"][0]["icon"]
        wind_speed = data["wind"]["speed"]

       
        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M")
        sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M")
        measured_at = datetime.fromtimestamp(data["dt"]).strftime("%H:%M")

   
        processed = {
            "city": city,
            "temp": f"{round(temp)}°C",
            "feels_like": f"{round(feels_like)}°C",
            "temp_min": f"{round(temp_min)}°C",
            "temp_max": f"{round(temp_max)}°C",
            "humidity": f"{humidity}%",
            "description": description.capitalize(),
            "icon": icon,
            "wind_speed": f"{wind_speed} m/s",
            "sunrise": sunrise,
            "sunset": sunset,
            "measured_at": measured_at,
        }

        self.view.display(processed)