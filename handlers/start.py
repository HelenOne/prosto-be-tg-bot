from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards.keyboards import main_kb

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "можно просто быть\n\nчто хочешь сейчас?",
        reply_markup=main_kb
    )