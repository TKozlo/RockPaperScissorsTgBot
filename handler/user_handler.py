from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from lexicon.lexicon import LEXICON
from keyboard.keyboard import yes_no_kb, game_kb
from services.servises import get_bot_choice, get_winner


# Этот хэндлер срабатывает на команду /start
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'], reply_markup=yes_no_kb)


# Этот хэндлер срабатывает на команду /help
async def process_help_command(message: Message):
    await message.answer(text=LEXICON['/help'], reply_markup=yes_no_kb)


# Этот хэндлер срабатывает на согласие пользователя играть в игру
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON['yes'], reply_markup=game_kb)


# Этот хэндлер срабатывает на отказ пользователя играть в игру
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON['no'])


# Этот хэндлер срабатывает на любую из игровых кнопок
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON["bot_choice"]} - {LEXICON[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON[winner], reply_markup=yes_no_kb)


# Функция для регистрации хэндлеров в диспетчере. Вызывается в исполняемом файле bot.py
def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands='start')
    dp.register_message_handler(process_help_command, commands='help')
    dp.register_message_handler(process_yes_answer,
                                text=LEXICON['yes_button'])
    dp.register_message_handler(process_no_answer,
                                text=LEXICON['no_button'])
    dp.register_message_handler(process_game_button,
                                Text(equals=[LEXICON['rock'],
                                             LEXICON['paper'],
                                             LEXICON['scissors']]))