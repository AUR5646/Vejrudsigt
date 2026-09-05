from tkinter import *


class WeatherView:

    def __init__(self):
        self.root = Tk()
        self.root.title("Vejrudsigt")
        self.root.geometry("400x400")

        # Overskrift til byens navn
        self.city_label = Label(self.root, text="Henter data...",
                                 font=("Helvetica", 20, "bold"), bg="#eaf2f8")
        self.city_label.pack(pady=(20, 5))

        # En kort beskrivelse fx "Klar himmel"
        self.description_label = Label(self.root, text="",
                                        font=("Helvetica", 14), bg="#eaf2f8")
        self.description_label.pack(pady=5)

        # Stor temperatur visning
        self.temp_label = Label(self.root, text="",
                                 font=("Helvetica", 40, "bold"), bg="#eaf2f8")
        self.temp_label.pack(pady=10)

    def display(self, data):
        self.city_label.config(text=data["city"])
        self.description_label.config(text=data["description"])
        self.temp_label.config(text=data["temp"])