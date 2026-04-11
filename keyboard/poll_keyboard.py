from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

group_id = os.environ.get("GROUP_ID")

def keyboard(poll_id):
    return InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Connect!",
                callback_data=f"connect:{poll_id}",
                #url=f"https://t.me/qwee1_bot?start={group_id}_{message_id}" #замінити qwee1_bot на свій телеграм бот
            ),
            InlineKeyboardButton(
                text="Disconnect!",
                callback_data=f"disconnect:{poll_id}"
            )
        ]
    ]
)