from io import BytesIO, BufferedIOBase
from typing import BinaryIO, Union

from networking.packable_interface import PackableInterface


class Packet(PackableInterface):
    __slots__ = [
        'mode',
        'code',
        'length',
        'next_file_pos',
        'prev_file_pos',
        'timestamp',
        'data',
    ]

    def __init__(self):
        self.mode = -1
        self.code = -1
        self.length = -1
        self.next_file_pos = -1
        self.prev_file_pos = -1
        self.timestamp = -1
        self.data = None

    def unpack(self, buf: BinaryIO) -> None:
        chunk = BytesIO(buf.read(32))

        self.mode = Packet.unpack_uint16(chunk)
        self.code = Packet.unpack_uint16(chunk)
        self.length = Packet.unpack_uint32(chunk)
        self.next_file_pos = Packet.unpack_uint32(chunk)
        self.prev_file_pos = Packet.unpack_uint32(chunk)
        self.timestamp = Packet.unpack_int64(chunk)

        if self.length > 0:
            self.data = buf.read(self.length)
        else:
            self.data = None

    @staticmethod
    def unpack_int8(buf: BinaryIO) -> int:
        return Packet._unpack_int(buf, 1)

    @staticmethod
    def unpack_uint8(buf: BinaryIO) -> int:
        return Packet._unpack_int(buf, 1, False)

    @staticmethod
    def unpack_int16(buf: BinaryIO) -> int:
        return Packet._unpack_int(buf, 2)

    @staticmethod
    def unpack_uint16(buf: BinaryIO) -> int:
        return Packet._unpack_int(buf, 2, False)

    @staticmethod
    def unpack_int32(buf: BinaryIO) -> int:
        return Packet._unpack_int(buf, 4)

    @staticmethod
    def unpack_uint32(buf: BinaryIO) -> int:
        return Packet._unpack_int(buf, 4, False)

    @staticmethod
    def unpack_int64(buf: BinaryIO) -> int:
        return Packet._unpack_int(buf, 8)

    @staticmethod
    def unpack_uint64(buf: BinaryIO) -> int:
        return Packet._unpack_int(buf, 8, False)

    @staticmethod
    def unpack_string(buf: BinaryIO, length: int) -> str:
        raw = buf.read(length)
        return raw.strip(b'\x00').decode('utf-8')

    @staticmethod
    def _unpack_int(buf: Union[BinaryIO, BufferedIOBase], size: int, signed: bool = True) -> int:
        return int.from_bytes(buf.read(size), byteorder='big', signed=signed)
