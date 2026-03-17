import asyncio
from datetime import datetime

from aiogram import Bot
from keyboards.keyboards import meds_kb

SCHEDULE = [
    ("10:00", "💊 утро\nЛамиктал + Феназепам\nс едой: Омега + D3"),
    ("14:00", "💊 день\nс едой: Омега + Хром"),
    ("22:00", "💊 вечер\nЛамиктал\nперед сном: Феназепам + Кветиапин"),
]


async def reminder_loop(bot: Bot):
    sent_today = set()

    while True:
        now = datetime.now().strftime("%H:%M")
        today = datetime.now().date()

        for time, text in SCHEDULE:
            key = f"{today}_{time}"

            if now == time and key not in sent_today:
                # 👉 сюда можно потом добавить несколько пользователей
                # сейчас отправляем одному
                for user_id in get_users():
                    await bot.send_message(user_id, text, reply_markup=meds_kb)

                sent_today.add(key)

        await asyncio.sleep(60)


def get_users():
    # пока просто список
    # позже можно из data.json
    return ["YOUR_USER_ID"]

async def remind_later(bot, user_id, text, delay=1200):
    await asyncio.sleep(delay)

    from keyboards.keyboards import meds_kb

    await bot.send_message(
        user_id,
        f"напоминаю 💛\n\n{text}",
        reply_markup=meds_kb
    )