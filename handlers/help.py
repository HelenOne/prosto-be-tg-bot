from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message(lambda m: m.text == "🫶 помощь сейчас")
async def help_now(message: Message):
    await message.answer(
        "выбери:\n\n"
        "1 — дыхание\n"
        "2 — grounding\n"
        "3 — пережить момент"
    )

@router.message(lambda m: m.text == "1")
async def breathing(message: Message):
    await message.answer("вдох 4 сек → выдох 6 сек × 5 раз")

@router.message(lambda m: m.text == "2")
async def grounding(message: Message):
    await message.answer(
        "5 вещей которые видишь\n"
        "4 которые чувствуешь\n"
        "3 которые слышишь"
    )

@router.message(lambda m: m.text == "3")
async def survive(message: Message):
    await message.answer("достаточно просто дожить этот момент")