from io import BytesIO
from typing import List

from networking.game_packet import GamePacket
from networking.packet import Packet


class PlayerInfo:
    player_index: int = -1
    ip_address: str = ''


class MsgAdminInfoPacket(GamePacket):
    __slots__ = (
        'players',
    )

    def __init__(self):
        super().__init__()

        self.type: str = 'MsgAdminInfo'
        self.players: List[PlayerInfo] = []

    def _unpack(self):
        count: int = Packet.unpack_uint8(self.buffer)

        for i in range(0, count):
            Packet.unpack_uint8(self.buffer)

            p_info: PlayerInfo = PlayerInfo()
            p_info.player_index = Packet.unpack_uint8(self.buffer)
            p_info.ip_address = Packet.unpack_ip_address(self.buffer)

            self.players.append(p_info)
