import requests
from main import response

class function:
    def __init__(self, api, path, link):
        self.api = api
        self.path = path
        self.link = link

    def Link(link, api):
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            data={
                'image_url': link,
                'size': 'auto'
            },
            headers={'X-Api-Key': api},
        )

    def path(api, path):
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(path, 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': api},
        )
