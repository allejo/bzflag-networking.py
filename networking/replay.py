from typing import BinaryIO, List

from networking.game_packet import GamePacket
from networking.game_packet_mapping import GamePacketMap
from networking.network_message import NetworkMessage
from networking.packet import Packet
from networking.replay_header import ReplayHeader


class Replay:
    __slots__ = [
        'header',
        'packets',
    ]

    def __init__(self, buf: BinaryIO):
        self.header: ReplayHeader = ReplayHeader()
        self.packets: List[GamePacket] = []

        self.header.unpack(buf)
        self._load_packets(buf)

    def _load_packets(self, buf: BinaryIO):
        while True:
            packet = Packet()
            packet.unpack(buf)

            try:
                msg_code = NetworkMessage(packet.code)
                game_packet = GamePacketMap[msg_code]
                game_packet.from_packet(packet)

                self.packets.append(game_packet)
            except KeyError:
                pass

            if packet.mode == -1:
                break
