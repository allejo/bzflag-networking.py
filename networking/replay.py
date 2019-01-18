from typing import BinaryIO

from networking.replay_header import ReplayHeader


class Replay:
    __slots__ = ['header']

    def __init__(self):
        self.header = ReplayHeader()

    def load_header(self, buf: BinaryIO) -> None:
        self.header.load(buf)
