from io import BytesIO

from networking.game_packet import GamePacket
from networking.network_protocol import NetworkProtocol
from networking.packet import Packet


class PlayerScore:
    __slots__ = (
        'wins',
        'losses',
        'team_kills',
    )


class MsgAddPlayerPacket(GamePacket):
    __slots__ = (
        'player_index',
        'player_type',
        'team_value',
        'callsign',
        'motto',
        'score',
    )

    def __init__(self):
        super().__init__()

        self.type: str = 'MsgAddPlayer'

        self.player_index: int = -1
        self.player_type: int = -1
        self.team_value: int = -1

        self.score = PlayerScore
        self.score.wins: int = 0
        self.score.losses: int = 0
        self.score.team_kills: int = 0

        self.callsign: str = ''
        self.motto: str = ''

    def from_packet(self, packet: Packet):
        data = BytesIO(packet.data)

        self.player_index = Packet.unpack_uint8(data)
        self.player_type = Packet.unpack_uint16(data)
        self.team_value = Packet.unpack_uint16(data)
        self.score.wins = Packet.unpack_uint16(data)
        self.score.losses = Packet.unpack_uint16(data)
        self.score.team_kills = Packet.unpack_uint16(data)

        self.callsign = Packet.unpack_string(data, NetworkProtocol.CALLSIGN_LEN)
        self.motto = Packet.unpack_string(data, NetworkProtocol.MOTTO_LEN)
