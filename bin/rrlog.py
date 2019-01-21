import json

from networking.json_encoder import RRLogEncoder
from networking.replay import Replay

with open('20170701-1926-fun.rec', 'rb') as replay_file:
    replay = Replay(replay_file)

    with open('20170701-1926-fun.json', 'w') as json_file:
        json_file.write(json.dumps(replay, cls=RRLogEncoder))

    print('Done!')
