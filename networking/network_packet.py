from typing import BinaryIO


class NetworkPacket:
    def unpack(self, buf: BinaryIO) -> None:
        raise NotImplementedError()
