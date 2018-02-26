import json

import requests


def get_followers(user_id: int, count: int, token: str):
    data = {'user_id': user_id,
            'count': count,
            'fields': 'screen_name',
            'access_token': token}
    r = requests.post('https://api.vk.com/method/users.getFollowers', data)
    try:
        return json.loads(r.text)['response']['items']
    except KeyError:
        print('Something gone wrong, check the validity of the token')
        exit()


def print_followers(followers):
    for follower in followers:
        print('{:20} {:20} vk.com/{}'.format(follower['first_name'], follower['last_name'], follower['uid']))
