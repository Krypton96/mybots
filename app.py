import asyncio
from aiogram import executor, Bot
from handlers.users.news_hs import news_every_minute
from loader import dp, bot
import middlewares, handlers

from utils.set_bot_commands import set_default_commands
from utils.notify_admins import on_startup_notify
from config import admin_id
from sql import create_db



async def set_all_default_commands(bot : Bot):
    await set_default_commands(bot)


async def on_shutdown(dp):
    await bot.close()



async def on_startup(dispatcher):
    await set_all_default_commands(bot)
    await asyncio.sleep(10)
    await create_db()
    await bot.send_message(admin_id, 'Я запущен!!!')
    
    # sqlite_db.sql_start()
    await on_startup_notify(dispatcher)



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(news_every_minute())
    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)

