from Filters.Filter import *


class LowPass(Filter):
    def __init__(self, w0):
        super().__init__()
        self.transferFunc = signal.ZerosPolesGain([], [w0], 1)
