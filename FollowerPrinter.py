import json

import requests
import requests.exceptions


def get_followers(user_id: int, count: int, token: str):
    data = {'user_id': user_id,
            'count': count,
            'fields': 'screen_name',
            'access_token': token}
    try:
        r = requests.post('https://api.vk.com/method/users.getFollowers', data)
    except requests.exceptions.ConnectionError:
        print('Something gone wrong, check your internet connection')
        exit()
    try:
        return json.loads(r.text)['response']['items']
    except KeyError:
        print('Something gone wrong, check the validity of the token')
        exit()


def print_followers(followers):
    for follower in followers:
        print('{:20} {:20} vk.com/{}'.format(follower['first_name'],
                                             follower['last_name'],
                                             follower['uid']))
