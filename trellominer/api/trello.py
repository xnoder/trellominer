import os

import requests

from trellominer.config import yaml


class HTTP(object):

    def __init__(self):
        self.config = yaml.read(os.getenv("TRELLO_CONFIG", default=os.path.join(os.path.expanduser('~'), ".trellominer.yaml")))
        self.api_url = os.getenv("TRELLO_URL", default=self.config['api']['url'])
        self.api_key = os.getenv("TRELLO_API_KEY", default=self.config['api']['key'])
        self.api_token = os.getenv("TRELLO_API_TOKEN", default=self.config['api']['token'])
        self.organization = os.getenv("TRELLO_ORGANIZATION", default=self.config['api']['organization'])
        self.output_file = os.getenv("TRELLO_OUTPUT_FILE", default=self.config['api']['output_file_name'])

class Trello(HTTP):

    def __init__(self):
        super().__init__()

    def boards(self):
        url = "{0}/organizations/{1}/boards?key={2}&token={3}".format(
                self.api_url, self.organization, self.api_key, self.api_token)
        req = requests.get(url, params=None)
        return req.json()

    def cards(self, board_id):
        url = "{0}/boards/{1}/cards?fields=name,desc,idList,due,dueComplete,closed,idMembers&members=true&member_fields=fullName&key={2}&token={3}".format(
                self.api_url, board_id, self.api_key, self.api_token)
        req = requests.get(url, params=None)
        return req.json()

    def lists(self, list_id):
        url = "{0}/lists/{1}?key={2}&token={3}".format(self.api_url, list_id, self.api_key, self.api_token)
        req = requests.get(url, params=None)
        return req.json()
