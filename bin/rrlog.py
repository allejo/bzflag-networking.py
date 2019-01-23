import json

from bzflag.utilities.json_encoder import RRLogEncoder
from bzflag.replay import Replay


replay = Replay('20170701-1926-fun.rec')

with open('20170701-1926-fun.json', 'w') as json_file:
    json_file.write(json.dumps(replay, cls=RRLogEncoder, indent=2))

print('Done!')
