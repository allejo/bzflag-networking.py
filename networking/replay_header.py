from typing import BinaryIO

from networking.packet import Packet


class ReplayHeader:
    __slots__ = [
        'magic_number',
        'version',
        'offset',
        'file_time',
        'player',
        'flags_size',
        'world_size',
        'callsign',
    ]

    def __init__(self):
        self.magic_number = -1
        self.version = -1
        self.offset = 0
        self.file_time = 0
        self.player = -1
        self.flags_size = 0
        self.world_size = 0
        self.callsign = ''

    def load(self, buf: BinaryIO) -> None:
        self.magic_number = Packet.unpack_uint32(buf)
        self.version = Packet.unpack_uint32(buf)
        self.offset = Packet.unpack_uint32(buf)
        self.file_time = Packet.unpack_int64(buf)
        self.player = Packet.unpack_uint32(buf)
        self.flags_size = Packet.unpack_uint32(buf)
        self.world_size = Packet.unpack_uint32(buf)
        self.callsign = Packet.unpack_string(buf, 32)
