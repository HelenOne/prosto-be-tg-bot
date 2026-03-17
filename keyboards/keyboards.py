from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💊 таблетки"), KeyboardButton(text="📊 статистика")],
        [KeyboardButton(text="🫶 помощь сейчас")]
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