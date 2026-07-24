from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
from dotenv import load_dotenv, find_dotenv

from handlers.storage import Storage

load_dotenv(find_dotenv())


group_id = os.environ.get("GROUP_ID")

def polls_keyboard():
    buttons = [
        InlineKeyboardButton(
            text=poll['text'],
            callback_data=f"poll:{poll_id}"
        )
        for poll_id, poll in Storage.polls.items()
    ]

    if not buttons:
        return None

    rows = [buttons[i:i+2] for i in range(0, len(buttons), 2)]

    return InlineKeyboardMarkup(inline_keyboard=rows)

def period_keyboard():
    buttons = [
        InlineKeyboardButton(
            text=period['text'],
            callback_data=f"period:{period_id}"
        )
        for period_id, period in Storage.period.items()
    ]

    if not buttons:
        return None

    rows = [buttons[i:i+2] for i in range(0, len(buttons), 2)]

    return InlineKeyboardMarkup(inline_keyboard=rows)