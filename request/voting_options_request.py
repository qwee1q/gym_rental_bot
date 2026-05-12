import aiohttp

url = 'http://127.0.0.1:8000/api/telegram/voting_option'

async def voting_options_post(request_data):
    response = {}
    for i in request_data['options']:
        params = {
            'voting_id': request_data['voting_id'],
            'option_text': i,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url, params=params) as resp:
                response_data = await resp.json()
                response[f'{response_data["data"]["id"]}'] = response_data
    return response