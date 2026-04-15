from aiogram import Router, types, F

from handlers.storage import Storage

from keyboard.poll_keyboard import keyboard
from keyboard.period_keyboard import keyboard_period

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
        return await query.answer("Connected")
    else:
        return await query.answer("You are already connected")

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
        return await query.answer("Disconnected")
    else:
        return await query.answer("You are not connected")

@group.callback_query(F.data.startswith("monday:"))
async def monday_query(query: types.CallbackQuery):
    period_id = query.data.split(":")[1]
    period = Storage.period.get(period_id)

    if not period:
        return await query.answer("Period not found", show_alert=True)

    user = query.from_user
    name = "@"+user.username or user.first_name

    if name not in period["monday"]["users"]:
        period["monday"]["users"].append(name)

        monday_users = "\n".join([f"{i + 1}. {u}" for i, u in enumerate(period["monday"]["users"])])
        tuesday_users = "\n".join([f"{i + 1}. {u}" for i, u in enumerate(period["tuesday"]["users"])])
        thursday_users = "\n".join([f"{i + 1}. {u}" for i, u in enumerate(period["thursday"]["users"])])
        friday_users = "\n".join([f"{i + 1}. {u}" for i, u in enumerate(period["friday"]["users"])])

        period["text"] = (
            f"{period['start_date']} - {period['end_date']}\n\n"
            f"{period['monday']['text']} {monday_users}\n\n"
            f"{period['tuesday']['text']} {tuesday_users}\n\n"
            f"{period['thursday']['text']} {thursday_users}\n\n"
            f"{period['friday']['text']} {friday_users}")

        await query.message.edit_text(period["text"], reply_markup=keyboard_period(period_id))

        return await query.answer("Monday")

    else:
        return await query.answer("You are already voice") #переробити на те щоб забрати голос

@group.callback_query(F.data.startswith("tuesday:"))
async def tuesday_query(query: types.CallbackQuery):
    period_id = query.data.split(":")[1]
    period = Storage.period.get(period_id)

    if not period:
        return await query.answer("Period not found", show_alert=True)

    user = query.from_user
    name = "@"+user.username or user.first_name

    if name not in period["tuesday"]["users"]:
        period["tuesday"]["users"].append(name)

        monday_users = "\n".join([f"{i + 1}. {u}" for i, u in enumerate(period["monday"]["users"])])
        tuesday_users = "\n".join([f"{i + 1}. {u}" for i, u in enumerate(period["tuesday"]["users"])])
        thursday_users = "\n".join([f"{i + 1}. {u}" for i, u in enumerate(period["thursday"]["users"])])
        friday_users = "\n".join([f"{i + 1}. {u}" for i, u in enumerate(period["friday"]["users"])])

        period["text"] = (
            f"{period['start_date']} - {period['end_date']}\n\n"
            f"{period['monday']['text']} {monday_users}\n\n"
            f"{period['tuesday']['text']} {tuesday_users}\n\n"
            f"{period['thursday']['text']} {thursday_users}\n\n"
            f"{period['friday']['text']} {friday_users}")

        await query.message.edit_text(period["text"], reply_markup=keyboard_period(period_id))

        return await query.answer("Tuesday")

    else:
        return await query.answer("You are already voice") #переробити на те щоб забрати голос

@group.callback_query(F.data.startswith("thursday:"))
async def thursday_query(query: types.CallbackQuery):
    period_id = query.data.split(":")[1]
    period = Storage.period.get(period_id)

    if not period:
        return await query.answer("Period not found", show_alert=True)

    user = query.from_user
    name = "@"+user.username or user.first_name

    if name not in period["thursday"]["users"]:
        period["thursday"]["users"].append(name)

        monday_users = "\n".join([f"{i + 1}. {u}" for i, u in enumerate(period["monday"]["users"])])
        tuesday_users = "\n".join([f"{i + 1}. {u}" for i, u in enumerate(period["tuesday"]["users"])])
        thursday_users = "\n".join([f"{i + 1}. {u}" for i, u in enumerate(period["thursday"]["users"])])
        friday_users = "\n".join([f"{i + 1}. {u}" for i, u in enumerate(period["friday"]["users"])])

        period["text"] = (
            f"{period['start_date']} - {period['end_date']}\n\n"
            f"{period['monday']['text']} {monday_users}\n\n"
            f"{period['tuesday']['text']} {tuesday_users}\n\n"
            f"{period['thursday']['text']} {thursday_users}\n\n"
            f"{period['friday']['text']} {friday_users}")

        await query.message.edit_text(period["text"], reply_markup=keyboard_period(period_id))

        return await query.answer("Thursday")

    else:
        return await query.answer("You are already voice") #переробити на те щоб забрати голос

@group.callback_query(F.data.startswith("friday:"))
async def friday_query(query: types.CallbackQuery):
    period_id = query.data.split(":")[1]
    period = Storage.period.get(period_id)

    if not period:
        return await query.answer("Period not found", show_alert=True)

    user = query.from_user
    name = "@"+user.username or user.first_name

    if name not in period["friday"]["users"]:
        period["friday"]["users"].append(name)

        monday_users = "\n".join([f"{i + 1}. {u}" for i, u in enumerate(period["monday"]["users"])])
        tuesday_users = "\n".join([f"{i + 1}. {u}" for i, u in enumerate(period["tuesday"]["users"])])
        thursday_users = "\n".join([f"{i + 1}. {u}" for i, u in enumerate(period["thursday"]["users"])])
        friday_users = "\n".join([f"{i + 1}. {u}" for i, u in enumerate(period["friday"]["users"])])

        period["text"] = (
            f"{period['start_date']} - {period['end_date']}\n\n"
            f"{period['monday']['text']} {monday_users}\n\n"
            f"{period['tuesday']['text']} {tuesday_users}\n\n"
            f"{period['thursday']['text']} {thursday_users}\n\n"
            f"{period['friday']['text']} {friday_users}")

        await query.message.edit_text(period["text"], reply_markup=keyboard_period(period_id))

        return await query.answer("Friday")

    else:
        return await query.answer("You are already voice") #переробити на те щоб забрати голос