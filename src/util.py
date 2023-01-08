from src.parameters import fps


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class FramesCounter:
    frame = 0  # [0, fps-1]

    @staticmethod
    def count_frames():
        FramesCounter.frame += 1
        if FramesCounter.frame >= fps:
            FramesCounter.frame = 0
