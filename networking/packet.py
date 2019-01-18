from typing import BinaryIO


class Packet:
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
