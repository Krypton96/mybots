from aiogram.dispatcher.filters import Command, Text
from loader import dp, bot
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
import random


@dp.message_handler(Command("menu"))
async def show_menu(message : Message):
    await message.reply("Выберите: \n", reply_markup=menu.mainMenu)


@dp.message_handler(Text(equals=['♾ Рандомное число']))
async def random_int(message : Message):
    await message.reply( 'Ваше число: ' + str(random.randint(1, 100)))


@dp.message_handler(Text(equals=['➕ Другое']))
async def other(message : Message):
    await message.reply( 'Другое: ', reply_markup=menu.otherMenu)


@dp.message_handler(Text(equals=['↩️ Назад']))
async def back_to_menu(message : Message):
    await message.reply('↩️↩️↩️↩️↩️', reply_markup=menu.mainMenu)



