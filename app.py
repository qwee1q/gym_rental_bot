import os, asyncio

from aiogram import Bot, Dispatcher

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


from handlers.admin.poll_handler import poll
from handlers.group.group_handler import group
from handlers.admin.period_handler import period

bot = Bot(token=os.getenv("BOT_TOKEN"))

dp = Dispatcher()

dp.include_routers(poll,period,group)

async def main():
    await dp.start_polling(bot)

asyncio.run(main())