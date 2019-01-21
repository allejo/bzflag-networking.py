from typing import Dict

from networking.game_packet import GamePacket
from networking.msg_add_player import MsgAddPlayerPacket
from networking.msg_admin_info import MsgAdminInfoPacket
from networking.msg_alive import MsgAlivePacket
from networking.msg_capture_flag import MsgCaptureFlagPacket
from networking.msg_drop_flag import MsgDropFlagPacket
from networking.msg_flag_grab import MsgGrabFlagPacket
from networking.msg_flag_update import MsgFlagUpdatePacket
from networking.msg_gm_update import MsgGMUpdatePacket
from networking.msg_killed import MsgKilledPacket
from networking.network_message import NetworkMessage


GamePacketMap: Dict[NetworkMessage, GamePacket] = {
    NetworkMessage.AddPlayer: MsgAddPlayerPacket(),
    NetworkMessage.AdminInfo: MsgAdminInfoPacket(),
    NetworkMessage.Alive: MsgAlivePacket(),
    NetworkMessage.CaptureFlag: MsgCaptureFlagPacket(),
    NetworkMessage.DropFlag: MsgDropFlagPacket(),
    NetworkMessage.GrabFlag: MsgGrabFlagPacket(),
    NetworkMessage.FlagUpdate: MsgFlagUpdatePacket(),
    NetworkMessage.GMUpdate: MsgGMUpdatePacket(),
    NetworkMessage.Killed: MsgKilledPacket(),
}
