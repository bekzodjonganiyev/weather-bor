import datetime
from pprint import pprint
import requests
from config import api_key


def get_weather(city, api_key):

    icons_codes = {
        "Clear": "Ajoyib \U00002600",
        "Clouds": "Bulutli \U00002601",
        "Rain": "Yomg'ir \U00002614",
        "Drizzle": "Kuchli yomg'ir \U00002614",
        "Thunderstorm": "Momaqaldiroq \U000026A1",
        "Snow": "Qor \U0001F328",
        "Mist": "Tuman \U0001f32B",
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data["name"]

        weather_discription = data["weather"][0]["main"]
        if weather_discription in icons_codes:
            wd = icons_codes[weather_discription]
        else:
            wd = "Nimadir xato ketti"

        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d- %H:%M')}***\n"
              f"Shahar: {city}\n"
              f"Xarorat: {cur_weather}C° {wd}\n"
              f"Namlik: {humidity}%\n"
              f"Bosim: {pressure}\n"
              f"Shamol: {wind} m/s\n"
              f"Quyosh chiqishi: {sunrise_timestamp}\n"
              f"Quyosh botishi: {sunset_timestamp}\n"
              f"Kun davomiyigi: {length_of_the_day}\n"
              f"Xayrli kun"
             )
    except Exception as ex:
        print(ex)
        print("Shahar nomini xato kiritdingiz")


def main():
    city = input("Shahar nomini kiriting: ")
    get_weather(city, api_key)


if __name__ == "__main__":
    main()