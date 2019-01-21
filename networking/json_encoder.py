import json

from networking.json_serializable import JsonSerializable


class RRLogEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, JsonSerializable):
            return {}

        return obj.to_dict()
