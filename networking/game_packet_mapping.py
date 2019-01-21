from typing import Dict

from networking.game_packet import GamePacket
from networking.msg_add_player import MsgAddPlayerPacket
from networking.msg_admin_info import MsgAdminInfoPacket
from networking.network_message import NetworkMessage


GamePacketMap: Dict[NetworkMessage, GamePacket] = {
    NetworkMessage.AddPlayer: MsgAddPlayerPacket(),
    NetworkMessage.AdminInfo: MsgAdminInfoPacket(),
}
