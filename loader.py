import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import *
from pycoingecko import CoinGeckoAPI
from sql import create_pool


loop = asyncio.get_event_loop()

storage = MemoryStorage()
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

db = loop.run_until_complete(create_pool())

