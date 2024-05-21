from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from token_1 import TOKEN
from dialoge import Dialoge
from answers.intent import INTENT
import logging


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def button_settings():
    button = [
        KeyboardButton("Список трендов"),
        KeyboardButton("Регистрация"),
    ]
    mark = ReplyKeyboardMarkup(resize_keyboard=True)
    mark.add(*button)
    return mark

# @dp.message_handler()
# async def hello_message(msg: types.Message):
#     send_msg= Dialoge(message_for_user=INTENT)
#     await msg.answer(send_msg.run(msg.text), reply_markup=button_settings())

if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as exc:
        print("Возникла: ", exc)
    
"""
крч надо переписать код для кнопок сделать хендлеры в файле интент
и поменять логику в файле диалог нужно сделать бота таким образом чтобы в файле диалог обрабатывались все функции и кнопки
"""