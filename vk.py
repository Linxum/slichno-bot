import requests
text = ''
photo = ''
token = '7515c8507515c8507515c850eb7562f8fe775157515c8501572d86bb2671fe02886fb16'
ver = 5.126
domain = 'clishkomlichnoe'
count = 1
offset = 1

def send_text(self):
    response = requests.get('https://api.vk.com/method/wall.get',
                            params={
                                'access_token': token,
                                'v': ver,
                                'domain': domain,
                                'offset': offset,
                                'count': count
                            }
                            )
    text = response.json()['response']['items'][0]['text']
    print(text)
    return text

def send_photo(photo):
    response = requests.get('https://api.vk.com/method/wall.get',
                            params={
                                'access_token': token,
                                'v': ver,
                                'domain': domain,
                                'offset': offset,
                                'count': count
                            }
                            )
    try:
        photo = response.json()['response']['items'][0]['attachments'][0]['photo']['sizes'][-1]['url']
        print(photo)
        return photo
    except:
        pass