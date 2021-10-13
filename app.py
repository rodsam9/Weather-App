import requests
import configparser
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def weather_app():
    return render_template("weather.html")


@app.route("/weather-results", methods=["POST"])
def results():
    city = request.form['city_name']

    api_key = get_api_key()
    weather_data = get_weather(city, api_key)
    
    temperature = (weather_data["main"]["temp"])
    feels_like_temperature = (weather_data["main"]["feels_like"])
    city_name = weather_data["name"]
    country = weather_data["sys"]["country"]

    return render_template("results.html", temperature=temperature, feels_like_temperature=feels_like_temperature, city_name=city_name, country=country)

if __name__ == '__main__':
    app.run()

def get_api_key():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["openweatherapp"]["api"]


def get_weather(city, api_key):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}".format(
        city, api_key)
    r = requests.get(api_url)
    return r.json()


