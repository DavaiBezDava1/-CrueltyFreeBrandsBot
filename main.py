import aiogram
import asyncio
from aiogram import Bot, Dispatcher, executor
BOT_TOKEN = "5260259993:AAH9A8grMYehT71ouGlr1f-O5zQ7uwdIv_I"


loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)
if __name__ == "__main__":
    from handlers22 import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)