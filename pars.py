import requests
import time

def take_posts(domain):
    token = 'access_token'
    version = 5.103
    count = 100
    offset = 0
    all_posts = []

    while True:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                    'offset': offset
                                }
                                )
        data = response.json()
        if 'error' in data or data['response']['items'] == []:
            print(data, domain)
            break
        all_posts.extend(data['response']['items'])
        if domain == 'jumoreski':
            offset += 5000
        else:
            offset += count
        time.sleep(1)
    return all_posts
