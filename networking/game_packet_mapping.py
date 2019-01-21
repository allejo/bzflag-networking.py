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
from networking.msg_message import MsgMessagePacket
from networking.msg_new_rabbit import MsgNewRabbitPacket
from networking.msg_pause import MsgPausePacket
from networking.msg_player_info import MsgPlayerInfoPacket
from networking.msg_player_update import MsgPlayerUpdatePacket
from networking.msg_remove_player import MsgRemovePlayerPacket
from networking.msg_score import MsgScorePacket
from networking.msg_score_over import MsgScoreOverPacket
from networking.msg_set_var import MsgSetVarPacket
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
    NetworkMessage.Message: MsgMessagePacket(),
    NetworkMessage.NewRabbit: MsgNewRabbitPacket(),
    NetworkMessage.Pause: MsgPausePacket(),
    NetworkMessage.PlayerInfo: MsgPlayerInfoPacket(),
    NetworkMessage.PlayerUpdate: MsgPlayerUpdatePacket(),
    NetworkMessage.PlayerUpdateSmall: MsgPlayerUpdatePacket(),
    NetworkMessage.RemovePlayer: MsgRemovePlayerPacket(),
    NetworkMessage.Score: MsgScorePacket(),
    NetworkMessage.ScoreOver: MsgScoreOverPacket(),
    NetworkMessage.SetVar: MsgSetVarPacket(),
}
