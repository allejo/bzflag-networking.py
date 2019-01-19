from typing import BinaryIO

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
        self.mode = Packet.unpack_uint16(buf)
        self.code = Packet.unpack_uint16(buf)
        self.length = Packet.unpack_uint32(buf)
        self.next_file_pos = Packet.unpack_uint32(buf)
        self.prev_file_pos = Packet.unpack_uint32(buf)
        self.timestamp = Packet.unpack_int64(buf)

        if self.length > 0:
            self.data = buf.read()
        else:
            self.data = None

    @staticmethod
    def unpack_int8(buf: BinaryIO) -> int:
        return int.from_bytes(buf.read(1), byteorder='big', signed=False)

    @staticmethod
    def unpack_uint8(buf: BinaryIO) -> int:
        return int.from_bytes(buf.read(1), byteorder='big', signed=True)

    @staticmethod
    def unpack_int16(buf: BinaryIO) -> int:
        return int.from_bytes(buf.read(2), byteorder='big', signed=False)

    @staticmethod
    def unpack_uint16(buf: BinaryIO) -> int:
        return int.from_bytes(buf.read(2), byteorder='big', signed=True)

    @staticmethod
    def unpack_int32(buf: BinaryIO) -> int:
        return int.from_bytes(buf.read(4), byteorder='big', signed=True)

    @staticmethod
    def unpack_uint32(buf: BinaryIO) -> int:
        return int.from_bytes(buf.read(4), byteorder='big', signed=False)

    @staticmethod
    def unpack_int64(buf: BinaryIO) -> int:
        return int.from_bytes(buf.read(8), byteorder='big', signed=True)

    @staticmethod
    def unpack_uint64(buf: BinaryIO) -> int:
        return int.from_bytes(buf.read(8), byteorder='big', signed=False)

    @staticmethod
    def unpack_string(buf: BinaryIO, length: int) -> str:
        raw = buf.read(length)

        return raw.strip(b'\x00').decode('utf-8')
