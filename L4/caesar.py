import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import logging
import config

logger = logging.getLogger(__name__)
bot = Bot(config.getToken())
dp = Dispatcher(bot)

@dp.message_handler() #commands=['start']
async def start(message: types.Message):
    ans = ''
    for i in range(len(message.text)):
        ans += chr(ord(str(message.text)[i]) + 1)
    await message.answer(ans)


if __name__ == '__main__':
    # Launch bot
    executor.start_polling(dp)
