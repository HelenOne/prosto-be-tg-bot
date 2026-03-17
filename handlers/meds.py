import asyncio

from aiogram import Router
from aiogram.types import Message, CallbackQuery
from datetime import datetime

from keyboards.keyboards import meds_kb, main_kb
from services.storage import load_data, save_data

from aiogram import Bot
from services.reminders import remind_later

router = Router()

@router.message(lambda m: m.text == "💊 таблетки")
async def meds(message: Message):
    await message.answer(
        "💊 пора таблетки\n\nты уже приняла?",
        reply_markup=meds_kb
    )

@router.callback_query(lambda c: c.data.startswith("meds_"))
async def meds_callback(callback: CallbackQuery):
    action = callback.data

    data = load_data()
    today = str(datetime.now().date())
    user_id = str(callback.from_user.id)

    if user_id not in data:
        data[user_id] = {}

    if today not in data[user_id]:
        data[user_id][today] = {}

    if action == "meds_yes":
        data[user_id][today]["meds"] = True
        text = "супер 💛"

    elif action == "meds_later":
        text = "окей, напомню через 20 минут 💛"

        bot = callback.bot
        user_id = callback.from_user.id

        original_text = callback.message.text

        asyncio.create_task(
            remind_later(bot, user_id, original_text)
        )

    else:
        data[user_id][today]["meds"] = False
        text = "ничего страшного"

    save_data(data)

    await callback.message.answer(text, reply_markup=main_kb)
    await callback.answer()