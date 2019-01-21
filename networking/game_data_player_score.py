from networking.game_data import GameData


class PlayerScore(GameData):
    __slots__ = (
        'wins',
        'losses',
        'team_kills',
    )
