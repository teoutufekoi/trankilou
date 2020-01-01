import json
from json.decoder import JSONDecodeError


class JManager:

    def __init__(self, fn):
        self.filename = fn

    def record(self, data):
        with open(self.filename, 'w') as f:
            f.write(data)

    def read(self):
        try:
            with open(self.filename) as f:
                data = f.read()
                return data
        except JSONDecodeError:
            pass

    def record_list(self, data_list):
        data = json.dumps(data_list, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        with open(self.filename, 'w') as f:
            f.write(data)

    def read_list(self, func):
        try:
            with open(self.filename) as f:
                data = f.read()
                data_json = json.loads(data)
                decoded_list = list(map(func, data_json))
                return decoded_list
        except JSONDecodeError:
            pass
