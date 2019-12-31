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