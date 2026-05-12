from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Router,types,F

from request.user_request import post_participant

private = Router()

@private.message(Command('register'))
async def start(message: types.Message):
    await message.answer("Send your phone number",reply_markup=ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Send phone number", request_contact=True)],
    ],resize_keyboard=True))

@private.message(F.contact)
async def contact(message: types.Message):
    phone_number = message.contact.phone_number
    user_id = message.contact.user_id
    username = message.from_user.username
    name = message.contact.first_name

    response = await post_participant(phone_number, user_id, username,name)

    await message.answer(f"ID: {response['data']['id']}\n"
                         f"Name: {response['data']['name']}\n"
                         f"Phone Number: {response['data']['phone']}\n")
    print(response)

