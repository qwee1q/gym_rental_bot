from aiogram import Router, types
from aiogram.filters import Command

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

group_id = os.getenv('GROUP_ID')
thread_id = os.getenv('THREAD_ID')

admin_cmd = Router()

@admin_cmd.message(Command('help'))
async def help_cmd(message: types.Message):
    await message.answer("/period - create period\n"
                         "/poll - create poll\n")


