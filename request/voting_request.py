import aiohttp

url = 'http://127.0.0.1:8000/api/telegram/voting'

async def voting_post(data):
    params = {
        'question': data['question'],
        'start_date': data['start_date'],
        'end_date': data['end_date'],
        'is_active': data['is_active'],
        'voting_type': data['voting_type'],
        'related_class': data['related_class'],
        'status': data['status'],
    }
    if data['voting_type'] == 'multiple_choice':
        response = {}
        params_game_period = {
            'start_date': data['start_date'],
            'end_date': data['end_date'],
            'duration_weeks': data['duration'],
        }
        url_game_period = 'http://127.0.0.1:8000/api/telegram/game_period'
        async with aiohttp.ClientSession() as session:
            async with session.post(url, params=params) as resp:
                response['voting'] = await resp.json()
        async with aiohttp.ClientSession() as session:
            async with session.post(url_game_period, params=params_game_period) as resp:
                response['game_period'] = await resp.json()

        return response

    else:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, params=params) as resp:
                response_data = await resp.json()
                return response_data