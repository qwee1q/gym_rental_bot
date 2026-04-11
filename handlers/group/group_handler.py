from aiogram import Router, types, F

from handlers.storage import Storage

from keyboard.poll_keyboard import keyboard

group = Router()

@group.callback_query(F.data.startswith("connect:"))
async def connect_query(query: types.CallbackQuery):
    poll_id = query.data.split(":")[1]
    poll = Storage.polls.get(poll_id)

    if not poll:
        return await query.answer("Poll not found", show_alert=True)

    user = query.from_user
    name = "@"+user.username or user.first_name

    if name not in poll["users"]:
        poll["users"].append(name)

        users_text = "\n".join([f"{i+1}. {u}" for i, u in enumerate(poll["users"])])
        text = f"{poll['text']}\n{users_text}"

        await query.message.edit_text(text, reply_markup=keyboard(poll_id))
        await query.answer("Connected")
    else:
        await query.answer("You are already connected")

@group.callback_query(F.data.startswith("disconnect:"))
async def disconnect_query(query: types.CallbackQuery):
    poll_id = query.data.split(":")[1]
    poll = Storage.polls.get(poll_id)

    if not poll:
        return await query.answer("Poll not found", show_alert=True)

    user = query.from_user
    name = user.username or user.first_name

    if name in poll["users"]:
        poll["users"].remove(name)

        users_text = "\n".join([f"{i+1}. {u}" for i, u in enumerate(poll["users"])])
        text = f"{poll['text']}\n{users_text}"

        await query.message.edit_text(text, reply_markup=keyboard(poll_id))
        await query.answer("Disconnected")
    else:
        await query.answer("You are not connected")