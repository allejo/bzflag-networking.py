from typing import Dict, Union


class JsonSerializable:
    __slots__ = (
        'json_ignored',
    )

    def is_json_ignored(self, slot: str) -> bool:
        if slot == 'json_ignored':
            return True

        if hasattr(slot, 'json_ignored') and slot in self.json_ignored:
            return True

        return False

    def to_dict(self):
        result: Dict[str, Union[list, str]] = {}

        for slot in self.__slots__:
            if self.is_json_ignored(slot):
                continue

            result[JsonSerializable.jsonify_name(slot)] = getattr(self, slot)

        return result

    @staticmethod
    def jsonify_name(string: str) -> str:
        raw = string.strip('_').title().replace('_', '')

        return raw[:1].lower() + raw[1:]
