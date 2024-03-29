from aiogram import Dispatcher
from aiogram.types import Message

from lexicon.lexicon import LEXICON

# Хэндлер для текстовых сообщений, которые не попали в другие хэндлеры
async def send_answer(message: Message):
    await message.answer(text=LEXICON['other_answer'])


# Функция для регистрации хэндлера. Вызывается в исполняемом файле bot.py
def register_other_handlers(dp: Dispatcher):
    dp.register_message_handler(send_answer)