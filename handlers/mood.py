from aiogram import Router
from aiogram.types import Message
from datetime import datetime

from keyboards.keyboards import main_kb, mood_kb
from services.storage import load_data, save_data

router = Router()

@router.message(lambda m: m.text == "📊 статистика")
async def ask_mood(message: Message):
    await message.answer("как ты сейчас?", reply_markup=mood_kb)

@router.message(lambda m: m.text in ["😊 нормально", "😐 тяжеловато", "😔 плохо", "🫥 нет сил"])
async def mood_handler(message: Message):
    data = load_data()
    today = str(datetime.now().date())

    if today not in data:
        data[today] = {}

    data[today]["mood"] = message.text
    save_data(data)

    await message.answer("приняла", reply_markup=main_kb)