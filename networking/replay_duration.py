class ReplayDuration:
    __slots__ = [
        'days',
        'hours',
        'minutes',
        'seconds',
        'milliseconds',
    ]

    def __init__(self, timestamp: int):
        secs = timestamp / 1000000

        day_len = 24 * 60 * 60
        self.days = int(secs / day_len)
        secs = secs % day_len

        hour_len = 60 * 60
        self.hours = int(secs / hour_len)
        secs = secs % hour_len

        min_len = 60
        self.minutes = int(secs / min_len)
        secs = secs % min_len

        self.seconds = int(secs)
        self.milliseconds = int(timestamp % 1000000)
