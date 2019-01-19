from typing import BinaryIO


class PackableInterface:
    def unpack(self, buf: BinaryIO) -> None:
        raise NotImplementedError()
