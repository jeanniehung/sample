import requests
import json


class Request(object):

    def get_api(self):
        api = 'https://api.github.com/events'
        req = requests.get(url=api)
        re = req.json()
        return re[0].get('id')





