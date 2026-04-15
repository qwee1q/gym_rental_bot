from aiogram import Router, types
from aiogram.filters import Command

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from aiogram.fsm.context import FSMContext

from FSM.create_period_FSM import PeriodFSM

import uuid

from keyboard.period_keyboard import keyboard_period

from handlers.storage import Storage

group_id = os.getenv('GROUP_ID')
thread_id = os.getenv('THREAD_ID')

period = Router()

@period.message(Command('period'))
async def period_cmd(message: types.Message, state: FSMContext):
    await message.answer("Enter start date of period")
    await state.set_state(PeriodFSM.start_date)

@period.message(PeriodFSM.start_date)
async def period_start_date(message: types.Message, state: FSMContext):
    await state.update_data(start_date=message.text)
    await message.answer("Enter end date of period")
    await state.set_state(PeriodFSM.end_date)

@period.message(PeriodFSM.end_date)
async def period_end_date(message: types.Message, state: FSMContext):
    await state.update_data(end_date=message.text)
    await message.answer("Enter duration of period")
    await state.set_state(PeriodFSM.duration)

@period.message(PeriodFSM.duration)
async def period_duration(message: types.Message, state: FSMContext):
    await state.update_data(duration=message.text)
    data = await state.get_data()
    await message.answer("Period was created")

    period_id = str(uuid.uuid4())

    sent = await message.bot.send_message(group_id,
                                          f"{data['start_date']} - {data['end_date']}",
                                          message_thread_id=thread_id, reply_markup=keyboard_period(period_id))

    Storage.period[period_id] = {
        "text": data['start_date'] + " - " + data['end_date'],
        "start_date": data['start_date'],
        "end_date": data['end_date'],
        "duration": data['duration'],
        "message_id": sent.message_id,
        "monday": {
            "text": "Monday:",
            "users": [],
        },
        "tuesday": {
            "text": "Tuesday:",
            "users": [],
        },
        "thursday": {
            "text": "Thursday:",
            "users": [],
        },
        "friday": {
            "text": "Friday:",
            "users": [],
        }
    }