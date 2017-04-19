import os

import requests

from tellominer.config import yaml


class HTTP(object):

    def __init__(self):
        self.config = yaml.read(os.getenv("TRELLO_CONFIG", default=os.path.join(os.path.expanduser('~'), "trellominer.yaml")))
        self.api_url = os.getenv("TRELLO_URL", default=config['api']['url'])
        self.api_key = os.getenv("TRELLO_API_KEY", default=config['api']['key'])
        self.api_token = os.getenv("TRELLO_API_TOKEN", default=config['api']['token'])
        self.organization = os.getenv("TRELLO_ORGANIZATION", default=config['api']['organization'])

class Trello(HTTP):

    def __init__(self):
        super().__init__()

    def boards(self):
        url = "{0}/organizations/{1}/boards?key={2}&token={3}".format(
                self.api_url, self.organization, self.api_key, self.api_token)
        req = requests.get(url, params=None)
        return req.json()
