from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



btnMain = KeyboardButton('↩️ Назад')


#   Main menu
btnRandom = KeyboardButton(text='♾ Рандомное число')
btnOther = KeyboardButton(text='➕ Другое')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRandom, btnOther)


#   Other Menu
btnNews = KeyboardButton(text='🎈 Новости')
btnWeather = KeyboardButton(text='☁ Погода')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnNews, btnWeather).add(btnMain)



btnNewsAll = KeyboardButton(text='Показать все новости')
# btnNewsFive = KeyboardButton(text='Последние 5 новостей')
btnNewsFresh = KeyboardButton(text='Свежие новости')
btnShowNews = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btnNewsAll, btnNewsFresh).add(btnMain)




