from model import WeatherModel
from view import WeatherView
from controller import WeatherController


def main():
    model = WeatherModel()
    view = WeatherView()
    controller = WeatherController(view, model)

    controller.getWeather() 
    view.root.mainloop()     


if __name__ == "__main__":
    main()