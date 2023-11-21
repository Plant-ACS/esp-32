import json
class Communicate: 
    @staticmethod
    def str_to_json(json_str):
        return json.loads(json_str)

    @staticmethod
    def json_to_str(json_dict: dict):
        return json.dumps(json_dict)
