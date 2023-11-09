import json
class Communicate: 
    @staticmethod
    def strToJson(jsonStr):
        return json.loads(jsonStr)

    @staticmethod
    def jsonToStr(jsonDict):
        return json.dumps(jsonDict)
