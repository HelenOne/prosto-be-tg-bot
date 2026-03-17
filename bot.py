import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import start, mood, meds, help

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# регистрируем роутеры
dp.include_router(start.router)
dp.include_router(mood.router)
dp.include_router(meds.router)
dp.include_router(help.router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())