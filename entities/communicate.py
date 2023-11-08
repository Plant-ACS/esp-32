import json
class Communicate: 
    @staticmethod
    def strToJson(self, jsonStr):
        return json.loads(jsonStr)

    @staticmethod
    def jsonToStr(self, jsonDict):
        return json.dumps(jsonDict)
