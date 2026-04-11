import os, asyncio

from aiogram import Bot, Dispatcher

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from handlers.private.private_handler import private
from handlers.admin.poll_handler import poll
from handlers.group.group_handler import group

bot = Bot(token=os.getenv("BOT_TOKEN"))

dp = Dispatcher()

dp.include_routers(private,poll,group)

async def main():
    await dp.start_polling(bot)

asyncio.run(main())