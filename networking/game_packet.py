from io import BytesIO
from typing import Optional, List

from networking.json_serializable import JsonSerializable
from networking.packet import Packet


class GamePacket(JsonSerializable):
    __slots__ = (
        'packet',
        'buffer',
        'type',
    )

    def __init__(self):
        self.packet: Optional[Packet] = None
        self.buffer: Optional[BytesIO] = None
        self.json_ignored: List[str] = ['buffer', 'packet']

    def _unpack(self):
        raise NotImplementedError

    def build(self):
        self.buffer = BytesIO(self.packet.data)
        self._unpack()
        self.buffer.close()
