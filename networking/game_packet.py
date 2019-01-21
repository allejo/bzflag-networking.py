from io import BytesIO
from typing import Optional

from networking.packet import Packet


class GamePacket:
    __slots__ = (
        'packet',
        'buffer',
        'type',
    )

    def __init__(self):
        self.packet: Optional[Packet] = None
        self.buffer: Optional[BytesIO] = None

    def _unpack(self):
        raise NotImplementedError

    def build(self):
        self.buffer = BytesIO(self.packet.data)
        self._unpack()
        self.buffer.close()
