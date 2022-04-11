import asyncio
from aiogram.dispatcher.filters import Command, Text
import json
from loader import dp, bot
from aiogram import types
import datetime
from keyboards.default import menu
from main import check_news_update
from config import admin_id



@dp.message_handler(commands=["news"])
@dp.message_handler(Text(equals=['🎈 Новости']))
async def news(message : types.Message):
    await message.answer('Сколько новостей вывести?', reply_markup=menu.btnShowNews)


@dp.message_handler(Text(equals=['Показать все новости']))
async def get_all_news(message : types.Message):
    with open("news_dict.json", encoding='utf-8') as file:
        news_dict = json.load(file)
    
    for k, v in sorted(news_dict.items()):
        news = f"<b>{datetime.datetime.fromtimestamp(v['article_date_timestamp'])}</b>\n" \
            f"<b>{v['article_title']}</b>\n" \
            f"<u>{v['article_url']}</u>"

        await message.answer(news)



@dp.message_handler(commands="fresh_news")
@dp.message_handler(Text(equals=['Свежие новости']))
async def fresh_news(message : types.Message):
    fresh_news = check_news_update()

    if len(fresh_news) >= 1:
        for k, v in sorted(fresh_news.items()):
            news = f"<b>{datetime.datetime.fromtimestamp(v['article_date_timestamp'])}</b>\n" \
            f"<b>{v['article_title']}</b>\n" \
            f"<u>{v['article_url']}</u>"

            await message.answer(news)
    else:
        await message.answer('Пока цхьа новость яц керл')



async def news_every_minute():
    while True:
        fresh_news = check_news_update()

        if len(fresh_news) >= 1:
                for k, v in sorted(fresh_news.items()):
                    news = f"<b>{datetime.datetime.fromtimestamp(v['article_date_timestamp'])}</b>\n" \
                    f"<b>{v['article_title']}</b>\n" \
                    f"<u>{v['article_url']}</u>"
                
                    await bot.send_message(admin_id, news, disable_notification=True)
        await asyncio.sleep(150)         





# @dp.message_handler(Text(equals=['Последние 5 новостей']))
# async def get_five_news(message : types.Message):
#     with open("news_dict.json", encoding='utf-8') as file:
#         news_dict = json.load(file)
    
#     for k, v in sorted(news_dict.items())[-5:]:
#         news = f"<b>{datetime.datetime.fromtimestamp(v['article_date_timestamp'])}</b>\n" \
#             f"<b>{v['article_title']}</b>\n" \
#             f"<u>{v['article_url']}</u>"

#         await message.answer(news)