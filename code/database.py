import json
from json.decoder import JSONDecodeError

class JManager:

    def __init__(self, fn):
        self.filename = fn

    def record(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f)

    def read(self):
        try:
            with open(self.filename) as json_file:
                data = json.load(json_file)
                return data
        except JSONDecodeError:
            pass