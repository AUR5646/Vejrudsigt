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

        # Beskrivelse fx "Klar himmel"
        self.description_label = Label(self.root, text="",
                                        font=("Helvetica", 14), bg="#eaf2f8")
        self.description_label.pack(pady=5)

        # Stor temperatur visning
        self.temp_label = Label(self.root, text="",
                                 font=("Helvetica", 40, "bold"), bg="#eaf2f8")
        self.temp_label.pack(pady=10)

        # Ramme til detaljer, så de kan stå pænt i to kolonner
        self.details_frame = Frame(self.root, bg="#eaf2f8")
        self.details_frame.pack(pady=10)

        self.feels_like_label = self._make_detail_row(0, "Føles som:")
        self.min_max_label = self._make_detail_row(1, "Min / Max:")
        self.humidity_label = self._make_detail_row(2, "Luftfugtighed:")
        self.wind_label = self._make_detail_row(3, "Vind:")
        self.sunrise_label = self._make_detail_row(4, "Solopgang:")
        self.sunset_label = self._make_detail_row(5, "Solnedgang:")

        # Opdaterings knap
        self.refresh_button = Button(self.root, text="↪️ Opdater",
                                      font=("Arial", 12), command=self.refresh)
        self.refresh_button.pack(pady=20)

    def _make_detail_row(self, row, label_text):
        Label(self.details_frame, text=label_text, font=("Helvetica", 11, "bold"),
              bg="#eaf2f8", anchor="w", width=15).grid(row=row, column=0, sticky="w", pady=2)
        value_label = Label(self.details_frame, text="", font=("Helvetica", 11),
                             bg="#eaf2f8", anchor="w", width=15)
        value_label.grid(row=row, column=1, sticky="w", pady=2)
        return value_label

    def display(self, data):
        self.city_label.config(text=data["city"])
        self.description_label.config(text=data["description"])
        self.temp_label.config(text=data["temp"])
        self.feels_like_label.config(text=data["feels_like"])
        self.min_max_label.config(text=f"{data['temp_min']} / {data['temp_max']}")
        self.humidity_label.config(text=data["humidity"])
        self.wind_label.config(text=data["wind_speed"])
        self.sunrise_label.config(text=data["sunrise"])
        self.sunset_label.config(text=data["sunset"])

    def refresh(self):
        print("Refresh button pressed")