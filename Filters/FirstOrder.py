from Filters.VirtualFilter import VirtualFilter
from scipy import signal


class LowPass(VirtualFilter):
    def __init__(self, w0, k=1):
        super(LowPass, self).__init__()
        self.transferFunc = signal.ZerosPolesGain([], [-w0], w0*k)  # Zeros Polos Ganancia


class HighPass(VirtualFilter):
    def __init__(self, w0, k=1):
        super(HighPass, self).__init__()
        self.transferFunc = signal.ZerosPolesGain([0], [-w0], k)


class AllPass(VirtualFilter):
    def __init__(self, w0, k=1):
        super(AllPass, self).__init__()
        self.transferFunc = signal.ZerosPolesGain([w0], [-w0], k)


class ArbitraryFO(VirtualFilter):
    def __init__(self, w0pole=None, w0zero=None, k=1):
        super(ArbitraryFO, self).__init__()
        self.transferFunc = signal.ZerosPolesGain([-w0zero], [-w0pole], k * w0pole / w0zero)
