from typing import BinaryIO

from networking.json_serializable import JsonSerializable
from networking.unpackable import Unpackable
from networking.network_protocol import NetworkProtocol
from networking.packet import Packet
from networking.replay_duration import ReplayDuration


class ReplayHeader(JsonSerializable, Unpackable):
    __slots__ = (
        'magic_number',
        'version',
        'offset',
        'file_time',
        'player',
        'flags_size',
        'world_size',
        'callsign',
        'motto',
        'server_version',
        'app_version',
        'real_hash',
        'length',
    )

    def __init__(self):
        self.magic_number = -1
        self.version = -1
        self.offset = 0
        self.file_time = 0
        self.player = -1
        self.flags_size = 0
        self.world_size = 0
        self.callsign = ''
        self.motto = ''
        self.server_version = ''
        self.app_version = ''
        self.real_hash = ''
        self.length = None

    def unpack(self, buf: BinaryIO) -> None:
        self.magic_number = Packet.unpack_uint32(buf)
        self.version = Packet.unpack_uint32(buf)
        self.offset = Packet.unpack_uint32(buf)
        self.file_time = Packet.unpack_int64(buf)
        self.player = Packet.unpack_uint32(buf)
        self.flags_size = Packet.unpack_uint32(buf)
        self.world_size = Packet.unpack_uint32(buf)
        self.callsign = Packet.unpack_string(buf, NetworkProtocol.CALLSIGN_LEN)
        self.motto = Packet.unpack_string(buf, NetworkProtocol.MOTTO_LEN)
        self.server_version = Packet.unpack_string(buf, NetworkProtocol.SERVER_LEN)
        self.app_version = Packet.unpack_string(buf, NetworkProtocol.MESSAGE_LEN)
        self.real_hash = Packet.unpack_string(buf, NetworkProtocol.HASH_LEN)

        self.length = ReplayDuration(self.file_time)

        # Skip the appropriate number of bytes since we're not making use of this
        # data yet

        buf.read(4 + NetworkProtocol.WORLD_SETTING_SIZE)

        if self.flags_size > 0:
            buf.read(self.flags_size)

        buf.read(self.world_size)
