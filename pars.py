import requests

def take_posts(domain):
    token = 'acces_token'
    version = 5.103
    count = 10
    offset = 0
    all_posts = []

    while offset < 10000:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                    'offset': offset
                                }
                                )

        data = response.json()['response']['items']
        all_posts.extend(data)
        offset += 500
    return all_posts
