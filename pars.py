import requests
import time

def take_posts(domain):
    token = '78f912a078f912a078f912a0b17888d609778f978f912a0264c99734c52809618421fe4'
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
        offset += count
        time.sleep(1)
    return all_posts
