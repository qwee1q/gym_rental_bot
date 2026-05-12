import os, asyncio

from aiogram import Bot, Dispatcher

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from handlers.admin.admin_cmd import admin_cmd
from handlers.admin.poll_handler import poll
from handlers.admin.period_handler import period
from handlers.private.private_handler import private
from handlers.group.group_handler import group

bot = Bot(token=os.getenv("BOT_TOKEN"))

dp = Dispatcher()

dp.include_routers(admin_cmd,period,private,group,poll)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())