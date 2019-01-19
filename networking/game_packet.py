from networking.packet import Packet


class GamePacket:
    __slots__ = (
        'type'
    )

    def from_packet(self, packet: Packet):
        raise NotImplementedError
