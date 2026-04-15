from aiogram import Router, types
from aiogram.filters import Command

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from aiogram.fsm.context import FSMContext

from FSM.create_poll_FSM import PollFSM

from keyboard.poll_keyboard import keyboard

from handlers.storage import Storage

import uuid

group_id = os.getenv('GROUP_ID')
thread_id = os.getenv('THREAD_ID')

poll = Router()

@poll.message(Command("poll"))
async def poll_cmd(message: types.Message, state: FSMContext):
    await message.answer("Enter date of poll")
    await state.set_state(PollFSM.date)

@poll.message(Command("poll_close"))
async def poll_close_cmd(message: types.Message):
    await message.answer("Closing poll")
    # ще не зробив

@poll.message(PollFSM.date)
async def poll_day(message: types.Message, state: FSMContext):
    await state.update_data(date=message.text)
    await message.answer("Enter date of poll")
    await state.set_state(PollFSM.day)

@poll.message(PollFSM.day)
async def poll_type(message: types.Message, state: FSMContext):
    await state.update_data(day=message.text)
    await message.answer("Enter type of poll")
    await state.set_state(PollFSM.type)

@poll.message(PollFSM.type)
async def poll_send(message: types.Message, state: FSMContext):
    await state.update_data(type=message.text)
    data = await state.get_data()
    await state.clear()

    poll_id = str(uuid.uuid4())

    await message.answer("Poll was sent")

    sent = await message.bot.send_message(group_id,
                                   f"{data['date']} {data['day']} {data['type']}\n\nConnected: ",
                                   message_thread_id=thread_id,reply_markup=keyboard(poll_id))

    key = f'{data["date"]} {data["day"]} {data["type"]}'

    Storage.polls[poll_id] = {
        "message_id": sent.message_id,
        "chat_id": message.chat.id,
        "users": [],
        "text": key,
        "status": "open"
    }

