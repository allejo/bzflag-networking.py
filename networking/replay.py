from typing import BinaryIO, List

from networking.game_packet import GamePacket
from networking.game_packet_mapping import GamePacketMap
from networking.network_message import NetworkMessage, chars_from_code
from networking.packet import Packet
from networking.replay_header import ReplayHeader


class Replay:
    __slots__ = [
        'header',
        'packets',
        'errors',
    ]

    def __init__(self, buf: BinaryIO):
        self.header: ReplayHeader = ReplayHeader()
        self.packets: List[GamePacket] = []
        self.errors: List[str] = []

        self.header.unpack(buf)
        self._load_packets(buf)

    def _load_packets(self, buf: BinaryIO):
        # We've loaded the replay header already, so let's save the current
        # starting position for the packets
        packets_start = buf.tell()

        # Get the full file size and save it
        buf.seek(0, 2)
        file_size = buf.tell()

        # Go back to the start of the packets so we can read them in
        buf.seek(packets_start)

        while True:
            packet = Packet()

            try:
                packet.unpack(buf)

                msg_code = NetworkMessage(packet.code)
                game_packet = GamePacketMap[msg_code]
                game_packet.packet = packet
                game_packet.build()

                self.packets.append(game_packet)
            except KeyError:
                game_code: str = chars_from_code(packet.code)
                self.errors.append(f'Unsupported game packet code: {game_code}')

            # We've reached the end of the replay
            if buf.tell() == file_size:
                break
