from typing import BinaryIO, List

from networking.packet import Packet
from networking.replay_header import ReplayHeader


class Replay:
    __slots__ = [
        'header',
        'packets',
    ]

    def __init__(self, buf: BinaryIO):
        self.header: ReplayHeader = ReplayHeader()
        self.packets: List[Packet] = []

        self.header.unpack(buf)
