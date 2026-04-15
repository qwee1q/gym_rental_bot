from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def keyboard_period(period_id):
    return InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="Monday",
            callback_data=f"monday:{period_id}",
        )],
        [InlineKeyboardButton(
            text="Tuesday",
            callback_data=f"tuesday:{period_id}"
        )],
        [InlineKeyboardButton(
            text="Thursday",
            callback_data=f"thursday:{period_id}"
        )],
        [InlineKeyboardButton(
            text="Friday",
            callback_data=f"friday:{period_id}"
        )]
    ]
)