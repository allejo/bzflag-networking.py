import socket
import struct

from io import BytesIO, BufferedIOBase
from typing import BinaryIO, Union

from networking.game_data_flag import FlagData
from networking.network_packet import NetworkPacket
from networking.network_protocol import Vector3F


class Packet(NetworkPacket):
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
    def unpack_ip_address(buf: BinaryIO) -> str:
        # This byte was reserved for differentiating between IPv4 and IPv6 addresses
        # However, since BZFlag only supports IPv4, this byte is skipped
        buf.read(1)

        # IP addresses are stored in network byte order (aka Little Endian)
        ip_as_int = int.from_bytes(buf.read(4), byteorder='little', signed=False)

        # Output the IP address as little-endian unsigned long
        #   https://docs.python.org/3/library/struct.html#format-strings
        return socket.inet_ntoa(struct.pack('<L', ip_as_int))

    @staticmethod
    def unpack_float(buf: BinaryIO) -> float:
        return struct.unpack('>f', buf.read(4))[0]

    @staticmethod
    def unpack_vector(buf: BinaryIO) -> Vector3F:
        return (
            Packet.unpack_float(buf),
            Packet.unpack_float(buf),
            Packet.unpack_float(buf),
        )

    @staticmethod
    def unpack_flag(buf: BinaryIO) -> FlagData:
        flag = FlagData()

        flag.index = Packet.unpack_uint16(buf)
        flag.abbv = Packet.unpack_string(buf, 2)
        flag.status = Packet.unpack_uint16(buf)
        flag.endurance = Packet.unpack_uint16(buf)
        flag.owner = Packet.unpack_uint8(buf)
        flag.position = Packet.unpack_vector(buf)
        flag.launch_pos = Packet.unpack_vector(buf)
        flag.landing_pos = Packet.unpack_vector(buf)
        flag.flight_time = Packet.unpack_float(buf)
        flag.flight_end = Packet.unpack_float(buf)
        flag.initial_velocity = Packet.unpack_float(buf)

        return flag

    @staticmethod
    def _unpack_int(buf: Union[BinaryIO, BufferedIOBase], size: int, signed: bool = True) -> int:
        return int.from_bytes(buf.read(size), byteorder='big', signed=signed)
