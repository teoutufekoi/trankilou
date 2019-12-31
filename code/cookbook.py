import json

class Ingredient:

    def __init__(self, jdata: object, gid: object):
        if jdata is not None:
            self.__dict__ = json.loads(jdata)
        else:
            self.gid = gid
            self.domain = "no domain"
            self.unit = "no unit"
            self.season = "no season"
            self.language = "french"