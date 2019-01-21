from typing import List

from networking.game_packet import GamePacket
from networking.packet import Packet


class ScoreData:
    __slots__ = (
        'player_id',
        'wins',
        'losses',
        'team_kills',
    )


class MsgScorePacket(GamePacket):
    __slots__ = (
        'scores',
    )

    def __init__(self):
        super().__init__()

        self.type: str = 'MsgScore'
        self.scores: List[ScoreData] = []

    def _unpack(self):
        count: int = Packet.unpack_uint8(self.buffer)

        for i in range(0, count):
            data: ScoreData = ScoreData()
            data.player_id = Packet.unpack_uint8(self.buffer)
            data.wins = Packet.unpack_uint16(self.buffer)
            data.losses = Packet.unpack_uint16(self.buffer)
            data.team_kills = Packet.unpack_uint16(self.buffer)

            self.scores.append(data)
