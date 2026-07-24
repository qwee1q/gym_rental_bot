from aiogram import Router, types
from aiogram.filters import Command

import os

from aiogram import types, F
from dotenv import load_dotenv, find_dotenv

from handlers.storage import Storage

load_dotenv(find_dotenv())

from keyboard.close_keyboard import polls_keyboard, period_keyboard

group_id = os.getenv('GROUP_ID')
thread_id = os.getenv('THREAD_ID')

admin_cmd = Router()

@admin_cmd.message(Command('help'))
async def help_cmd(message: types.Message):
    await message.answer("/period - create period\n"
                         "/poll - create poll\n")

@admin_cmd.message(Command('close'))
async def close_cmd(message: types.Message):
    await message.answer("Chose poll/period to close")
    await message.answer("Polls:", reply_markup=polls_keyboard())
    await message.answer("Period:", reply_markup=period_keyboard())
    print(Storage.polls)


@admin_cmd.callback_query(F.data.startswith("poll:"))
async def poll_close(query: types.CallbackQuery):
    poll_id = query.data.split(":")[1]
    poll = Storage.polls.get(poll_id)
    people = poll["users"]
    await query.answer(f"Info:\n{people}")