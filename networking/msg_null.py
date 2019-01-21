from networking.game_packet import GamePacket


class MsgNullPacket(GamePacket):
    def __init__(self):
        super().__init__()

        self.type = 'MsgNull'

    def _unpack(self):
        pass
