from dotenv import load_dotenv
import os
import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, Router, types, Dispatcher, F
from aiogram.types import Message
import asyncio

load_dotenv()
tg_bot_token = os.getenv("TG_BOT_TOKEN")
open_weather_token = os.getenv("OPEN_WEATHER_TOKEN")
# Создание бота и диспетчера
bot = Bot(token=tg_bot_token)
router = Router()

# Обработчик команды /start


@router.message(F.text == "/start")
async def start_command(message: Message):
    await message.answer("Hello motherfucker! Вот сити are you from? Получишь погоду")


@router.message()
async def get_weather(message: Message):
    code_to_emodji = {
        "Clear": "все Ясно с вами ☀️",
        "Clouds": "как то заОблачно 🌥️",
        "Rain": "Дождь курва 🌧️",
        "Snow": "Снеговит седня 🌨️",
        "Mist": "заТуманило 🌫️"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={
                message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_emodji:
            wd = code_to_emodji[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что на сервере за ху@#я твориться."
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(
            data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(
            data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        await message.answer(f"***{datetime.datetime.now().strftime('%H:%M %d-%m-%Y')}***\n"
                             f"Погода тута: {city}\nТемпература: {
            cur_weather}C° {wd}\n"
            f"Важность: {humidity}%\nГубатый: {wind}м/с\n"
            # f"Восход лампы: {sunrise_timestamp}\n"
            # f"Заход лампы: {sunset_timestamp}\n"
            f"Продолжительность дня: {length_of_the_day}\n"
            f"Хорошего дня курва!"
        )

    except:
        await message.reply("no way Gangsta, start over!")


# Функция main для запуска
async def main():
    print('bot start...')
    dp = Dispatcher()
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
