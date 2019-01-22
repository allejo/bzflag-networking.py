from typing import Dict

from networking.msg_add_player import MsgAddPlayerPacket
from networking.msg_admin_info import MsgAdminInfoPacket
from networking.msg_alive import MsgAlivePacket
from networking.msg_capture_flag import MsgCaptureFlagPacket
from networking.msg_drop_flag import MsgDropFlagPacket
from networking.msg_flag_grab import MsgGrabFlagPacket
from networking.msg_flag_update import MsgFlagUpdatePacket
from networking.msg_game_time import MsgGameTimePacket
from networking.msg_gm_update import MsgGMUpdatePacket
from networking.msg_killed import MsgKilledPacket
from networking.msg_message import MsgMessagePacket
from networking.msg_new_rabbit import MsgNewRabbitPacket
from networking.msg_null import MsgNullPacket
from networking.msg_pause import MsgPausePacket
from networking.msg_player_info import MsgPlayerInfoPacket
from networking.msg_player_update import MsgPlayerUpdatePacket
from networking.msg_remove_player import MsgRemovePlayerPacket
from networking.msg_score import MsgScorePacket
from networking.msg_score_over import MsgScoreOverPacket
from networking.msg_set_var import MsgSetVarPacket
from networking.msg_shot_begin import MsgShotBeginPacket
from networking.msg_shot_end import MsgShotEndPacket
from networking.msg_team_update import MsgTeamUpdatePacket
from networking.msg_teleport import MsgTeleportPacket
from networking.msg_time_update import MsgTimeUpdatePacket
from networking.msg_transfer_flag import MsgTransferFlagPacket
from networking.network_message import NetworkMessage


GamePacketMap: Dict[NetworkMessage, callable] = {
    NetworkMessage.Null: MsgNullPacket.factory,
    NetworkMessage.AddPlayer: MsgAddPlayerPacket.factory,
    NetworkMessage.AdminInfo: MsgAdminInfoPacket.factory,
    NetworkMessage.Alive: MsgAlivePacket.factory,
    NetworkMessage.CaptureFlag: MsgCaptureFlagPacket.factory,
    NetworkMessage.DropFlag: MsgDropFlagPacket.factory,
    NetworkMessage.GrabFlag: MsgGrabFlagPacket.factory,
    NetworkMessage.FlagUpdate: MsgFlagUpdatePacket.factory,
    NetworkMessage.GameTime: MsgGameTimePacket.factory,
    NetworkMessage.GMUpdate: MsgGMUpdatePacket.factory,
    NetworkMessage.Killed: MsgKilledPacket.factory,
    NetworkMessage.Message: MsgMessagePacket.factory,
    NetworkMessage.NewRabbit: MsgNewRabbitPacket.factory,
    NetworkMessage.Pause: MsgPausePacket.factory,
    NetworkMessage.PlayerInfo: MsgPlayerInfoPacket.factory,
    NetworkMessage.PlayerUpdate: MsgPlayerUpdatePacket.factory,
    NetworkMessage.PlayerUpdateSmall: MsgPlayerUpdatePacket.factory,
    NetworkMessage.RemovePlayer: MsgRemovePlayerPacket.factory,
    NetworkMessage.Score: MsgScorePacket.factory,
    NetworkMessage.ScoreOver: MsgScoreOverPacket.factory,
    NetworkMessage.SetVar: MsgSetVarPacket.factory,
    NetworkMessage.ShotBegin: MsgShotBeginPacket.factory,
    NetworkMessage.ShotEnd: MsgShotEndPacket.factory,
    NetworkMessage.TeamUpdate: MsgTeamUpdatePacket.factory,
    NetworkMessage.Teleport: MsgTeleportPacket.factory,
    NetworkMessage.TimeUpdate: MsgTimeUpdatePacket.factory,
    NetworkMessage.TransferFlag: MsgTransferFlagPacket.factory,
}
