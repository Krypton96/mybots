
import logging

from aiogram import Dispatcher

from config import admin_id


async def on_startup_notify(dp: Dispatcher):
    for admin in admin_id:
        try:
            await dp.bot.send_message(admin, "Бот Запущен!!!!!!")

        except Exception as err:
            logging.exception(err)
