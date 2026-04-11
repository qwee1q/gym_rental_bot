from aiogram.filters import CommandObject, CommandStart
from aiogram.types import Message
from aiogram import Router,types

private = Router()

@private.message(CommandStart(deep_link=True))
async def start(message: types.Message, command: CommandObject):
    args = command.args

    group_id, message_id = args.split('_')

    group_id = int(group_id)
    message_id = int(message_id)

    chat_id = message.chat.id
    await message.answer(f"Your payload is {args}, chat_id is {chat_id}")
    await message.bot.edit_message_text(chat_id=group_id, message_id=message_id,text=f'Connected: {chat_id}')

