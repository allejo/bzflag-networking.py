from networking.replay import Replay

with open('20170701-1926-fun.rec', 'rb') as replay_file:
    replay = Replay()
    replay.load_header(replay_file)

    print('t')
