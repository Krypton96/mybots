from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.calbakk_kb import buy_callback
from config import url_pear, url_apples

# choise = InlineKeyboardMarkup(
#     inline_keyboard= [ 
#         [ 
#             InlineKeyboardButton(text='Купить грушу', callback_data=buy_callback.new(item_name='pear', quantity=2)),
#             InlineKeyboardButton(text='Купить яблоко', callback_data='buy:apple:5'),
#         ],
#         [ 
#             InlineKeyboardButton(text='Отмена', callback_data='cancel')
#         ]
#     ]
# )


choice = InlineKeyboardMarkup(row_width=2)
buy_pear = InlineKeyboardButton(text='Купить грушу', callback_data=buy_callback.new(item_name='pear', quantity=2))
choice.insert(buy_pear)

buy_apple = InlineKeyboardButton(text='Купить яблоко', callback_data='buy:apple:5')
choice.insert(buy_apple)

cancel_button = InlineKeyboardButton(text='Отмена', callback_data='cancel')
choice.insert(cancel_button)

pear_keyboard = InlineKeyboardMarkup(
    inline_keyboard= [ 
        [ 
            InlineKeyboardButton(text='Купи тут', url=url_pear)
        ]
    ]
)

apple_keyboard = InlineKeyboardMarkup(
    inline_keyboard= [ 
        [ 
            InlineKeyboardButton(text='Купи тут', url=url_apples)
        ]
    ]
)