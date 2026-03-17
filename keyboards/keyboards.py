from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💊 таблетки"), KeyboardButton(text="📊 статистика")],
        [KeyboardButton(text="🫶 помощь сейчас"), KeyboardButton(text="⚙️ настройки")]
    ],
    resize_keyboard=True
)

mood_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="😊 нормально")],
        [KeyboardButton(text="😐 тяжеловато")],
        [KeyboardButton(text="😔 плохо")],
        [KeyboardButton(text="🫥 нет сил")]
    ],
    resize_keyboard=True
)

meds_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ приняла", callback_data="meds_yes"),
            InlineKeyboardButton(text="⏳ позже", callback_data="meds_later"),
            InlineKeyboardButton(text="❌ пропустила", callback_data="meds_no"),
        ]
    ]
)