from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from handlers.utils.admins import ADMINS
from handlers.utils.record_history_by_user_id import record_history_by_user_id



router = Router()


@router.message(CommandStart())
async def command_start_handler(message: types.Message, state: FSMContext):

    if message.from_user.id in ADMINS:
        pass
    else:
        if ' ' in message.text:
            pass
        else:
            pass
