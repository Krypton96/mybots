import logging
from loader import dp
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from keyboards.inline.choise_buttons import choice, pear_keyboard, apple_keyboard
from keyboards.inline.calbakk_kb import buy_callback

@dp.callback_query_handler(text='cancel')
async def cancel_buying(call : CallbackQuery):
    await call.answer('Вы отменили покупку', show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()

@dp.message_handler(Command('items'))
async def show_items(message : Message):
    await message.answer(text='На продаже у нас есть 2 товара: 5 яблок и 2 груши. \nЕсли вам ничего не нужно - жмите отмену', reply_markup=choice)


@dp.callback_query_handler(buy_callback.filter(item_name='apple'))
async def buying_apple(call : CallbackQuery, callback_data : dict):
    await call.answer(cache_time=50)
    logging.info(f"cal = {callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"вы выбрали яблоко, яблок всего {quantity}. Спасибо", reply_markup=apple_keyboard)


@dp.callback_query_handler(text_contains='pear')
async def buying_pear(call : CallbackQuery):
    await call.answer(cache_time=50)
    callback_data = call.data
    logging.info(f"cal = {callback_data}")
    await call.message.answer('Вы выбрали грушу, груши всего две, спасибо.', reply_markup=pear_keyboard) 






