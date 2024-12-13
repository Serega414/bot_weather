import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, Router, types
from aiogram.types import Message
from aiogram.utils import executor
import asyncio

# Создание бота и диспетчера
bot = Bot(token=tg_bot_token)
router = Router()

# Обработчик команды /start


@router.message(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("Hello motherfucker! Who is you sity? Получишь погоду")


# Функция main для запуска
async def main():
    from aiogram import Dispatcher
    dp = Dispatcher()
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
