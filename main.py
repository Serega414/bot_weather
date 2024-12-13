import requests
import datetime
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):

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
                city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_emodji:
            wd = code_to_emodji[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за ху@#я твориться."
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(
            data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(
            data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        print(f"***{datetime.datetime.now().strftime('%H:%M %d-%m-%Y')}***\n"
              f"Погода тута: {city}\nТемпература: {cur_weather}C° {wd}\n"
              f"Важность: {humidity}%\nГубатый: {wind}м/с\n"
              f"Восход лампы: {sunrise_timestamp}\n"
              f"Заход лампы: {sunset_timestamp}\n"
              f"Продолжительность дня: {length_of_the_day}\n"
              f"Хорошего дня сука!"
              )
    except Exception as ex:
        print(ex)
        print("Nope again Now!")


def main():
    print("start bot")
    city = input("Who is city motherfucker: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
