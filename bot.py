import datetime
import requests

from config import bot_token, api_key
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Assalomu alaykum. Men sizga kiritgan shaharingizni ob-havosini aniqlab beraman")

@dp.message_handler()
async def get_weather(message: types.Message):
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
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={api_key}&units=metric"
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

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d- %H:%M')}***\n"
              f"Shahar: {city}\n"
              f"Xarorat: {cur_weather}C° {wd}\n"
              f"Namlik: {humidity}%\n"
              f"Bosim: {pressure} \n"
              f"Shamol: {wind} m/s\n"
              f"Quyosh chiqishi: {sunrise_timestamp}\n"
              f"Quyosh botishi: {sunset_timestamp}\n"
              f"Kun davomiyigi: {length_of_the_day}\n"
              f"Xayrli kun"
             )
    except:
        await message.reply("\U00002620 Shahar nomini xato kiritdingiz \U00002620")


if __name__ == '__main__':
    executor.start_polling(dp)