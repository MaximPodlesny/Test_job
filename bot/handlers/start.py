from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: types.Message, state: FSMContext):
    await message.answer('Привет!')
    url = f"https://127.0.0.1:8000"  # Передаем telegram_id в URL
    button = types.InlineKeyboardButton(text="Приложение", web_app=types.WebAppInfo(url=url))
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
    await message.answer(
         "Для управления товарами перейди в приложение",
         reply_markup=keyboard
      )
