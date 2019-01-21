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

    def _unpack(self):
        self.player_index = Packet.unpack_uint8(self.buffer)
        self.player_type = Packet.unpack_uint16(self.buffer)
        self.team_value = Packet.unpack_uint16(self.buffer)
        self.score.wins = Packet.unpack_uint16(self.buffer)
        self.score.losses = Packet.unpack_uint16(self.buffer)
        self.score.team_kills = Packet.unpack_uint16(self.buffer)

        self.callsign = Packet.unpack_string(self.buffer, NetworkProtocol.CALLSIGN_LEN)
        self.motto = Packet.unpack_string(self.buffer, NetworkProtocol.MOTTO_LEN)