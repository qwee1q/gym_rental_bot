import aiohttp

url = "http://127.0.0.1:8000/api/telegram/participant"

async def post_participant(phone_number,user_id,username,name):
    params = {
        'name': name,
        'phone': phone_number,
        'telegram_id': user_id,
        'telegram_username': username
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, params=params) as resp:
            data = await resp.json()
            return data