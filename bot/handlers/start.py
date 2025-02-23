from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from config.settings import settings

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: types.Message, state: FSMContext):
    await message.answer('Привет!')
    url = f'{settings.app_host}:{settings.app_port}'
    button = types.InlineKeyboardButton(text="Приложение", web_app=types.WebAppInfo(url=url))
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
    from bot.bot import bot
    await bot.send_message(498283860, 'В start')
    await message.answer(
         "Для тестирования введите артикул:",
      )
    await message.answer(
         "211695539",
      )
    await message.answer(
         "Для управления товарами перейди в приложение",
         reply_markup=keyboard
      )
