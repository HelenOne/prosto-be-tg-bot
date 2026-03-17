from aiogram import Router
from aiogram.types import Message
from datetime import datetime

from keyboards.keyboards import main_kb
from services.storage import load_data, save_data

router = Router()

@router.message(lambda m: m.text == "💊 таблетки")
async def meds(message: Message):
    await message.answer("ты приняла таблетки? напиши 'приняла'")

@router.message(lambda m: "приняла" in m.text.lower())
async def meds_done(message: Message):
    data = load_data()
    today = str(datetime.now().date())

    if today not in data:
        data[today] = {}

    data[today]["meds"] = True
    save_data(data)

    await message.answer("отлично", reply_markup=main_kb)