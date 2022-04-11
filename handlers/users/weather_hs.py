from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp
from config import open_weather_token
import datetime
import requests
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

#☁ Погода

class FSMAdmin(StatesGroup):
    name = State()


@dp.message_handler(commands=["weather"], state=None)
@dp.message_handler(Text(equals=['☁ Погода']),state=None)
async def weather_command(message : types.Message):
    await FSMAdmin.name.set()
    await message.reply("Напиши мне название города и я пришлю сводку погоды", reply_markup=types.ReplyKeyboardRemove())



@dp.message_handler(state=FSMAdmin.name)
async def load_name(message : types.Message, state: FSMContext):
    code_to_smile = { 
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Морось \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001f328",
        "Mist": "Туман \U0001f328"
    }
    
    
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        
        weather_description =data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city}\n{wd}\nТемпература: {cur_weather}°С\n"
            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\n{wind} м/с\n"
            f"Восход солнца: {sunrise_timestamp}\n"
            f"Закат солнца: {sunset_timestamp}\n"
            f"Продолжительность дня: {length_of_the_day}\n"
            F"***Хорошего дня:)***"
        )
        await state.finish()

    except:
        await message.reply("Проверьте название города и попробуйте еще раз \U00002757")