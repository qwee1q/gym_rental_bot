import aiohttp

url = "http://127.0.0.1:8000/api/telegram/user_vote"

async def poll_post(request_data):
    params = {
        "voting_id": request_data["voting_id"],
        "option_text": request_data["option"],
        "telegram_id": request_data["telegram_id"]
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, params=params) as resp:
            data = await resp.json()
            return data