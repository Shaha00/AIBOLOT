from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
from keyboards.client_kb import start_markup


async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Здравствуйте {message.from_user.first_name}!\nЯ бот клиники Ibolot, чем могу вам помочь?",
                           reply_markup=start_markup)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
