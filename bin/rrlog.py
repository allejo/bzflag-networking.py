import argparse
import json

from bzflag.utilities.json_encoder import RRLogEncoder
from bzflag.replay import Replay


parser = argparse.ArgumentParser()
parser.add_argument(
    'replay_file',
    help='a replay file to convert into JSON',
    type=str,
)
parser.add_argument(
    '--blacklist',
    help='a comma separated list of packet types to exclude from the output',
    default='',
    type=str,
)
parser.add_argument(
    '--whitelist',
    help='a comma separated list of packet types that will only be included; this option overrides `--blacklist`',
    default='',
    type=str,
)

args = parser.parse_args()

RRLogEncoder.black_list = args.blacklist.split(',') if args.blacklist else []
RRLogEncoder.white_list = args.whitelist.split(',') if args.whitelist else []

replay = Replay(args.replay_file)

with open(f'{args.replay_file}.json', 'w') as json_file:
    json_file.write(json.dumps(replay, cls=RRLogEncoder, indent=2))
