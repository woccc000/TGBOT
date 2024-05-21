from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from token_1 import TOKEN
from dialoge import Dialoge
from answers.intent import INTENT
import logging
from bot import dp, button_settings

@dp.message_handler()
async def hello_message(msg: types.Message):
    send_msg= Dialoge(message_for_user=INTENT)
    await msg.answer(send_msg.run(msg.text), reply_markup=button_settings())