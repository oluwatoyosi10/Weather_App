# Import required modules
import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap


# Function to get weather information from OpenWeatherMap API
def get_weather(city):
    API_key = "30d1cf22246548cc78b54c5d020f6ba4"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None

     # Parse the response JSON to get weather information
        weather = res.json()
        icon_id = weather['weather'][0]['icon']
        temperature = weather['main']['temp'] - 273.15
        description = weather['weather'][0]['description']
        city = weather['name']
        country = weather['sys']['country']

        # Get the icon URL and return all the weather information
        icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
        return (icon_url, temperature, description, city, country)


    # Function to seatch weather for a city
    def search():
        city = city_entry.get()
        result = get_weather(city)
        if result is None:
            return
