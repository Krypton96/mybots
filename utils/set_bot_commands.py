from aiogram import Bot, types
from aiogram.types import  BotCommand
from aiogram.types.bot_command_scope import BotCommandScopeChat, BotCommandScopeDefault




async def set_default_commands(bot : Bot):
    return await bot.set_my_commands(
        commands=[ 
            BotCommand('start', 'Начать заново'),
            BotCommand('menu', 'Меню'),
            BotCommand('news', 'Новости'),
            BotCommand('help', 'Помощь')
        ],
        scope=BotCommandScopeDefault()
    )




# async def set_default_commands(bot : Bot):
#     STARTING_COMMANDS = { 
#         'ru': [
#             BotCommand('start', 'Начать заново'),
#             BotCommand('menu', 'Меню'),
#             BotCommand('news', 'Новости'),
#             BotCommand('help', 'Помощь'),
#         ],

#         'en': [ 
#             BotCommand('start', 'Restart bot'),
#             BotCommand('menu', 'Menu'),
#             BotCommand('news', 'News'),
#             BotCommand('help', 'Help'),
#         ],
#     }

#     for language_code, commands in STARTING_COMMANDS.items():
#         await bot.set_my_commands(
#             commands=commands,
#             # scope=BotCommandScopeChat(chat_id),
#             language_code=language_code
#         )








