import numpy as np
from Filters.VirtualFilter import VirtualFilter
from scipy import signal


class LowPass(VirtualFilter):
    def __init__(self, w0, xi, k=1):
        super().__init__()
        self.transferFunc = signal.TransferFunction([0, 0, k], [1 / w0 ** 2, 2 * xi / w0, 1])


class HighPass(VirtualFilter):
    def __init__(self, w0, xi, k=1):
        super().__init__()
        self.transferFunc = signal.TransferFunction([k / w0 ** 2, 0, 0], [1 / w0 ** 2, 2 * xi / w0, 1])


class AllPass(VirtualFilter):
    def __init__(self, w0, xi, k=1):
        super().__init__()
        self.transferFunc = signal.TransferFunction([k / w0 ** 2, -k * 2 * xi / w0, k], [1 / w0 ** 2, 2 * xi / w0, 1])


class BandPass(VirtualFilter):
    def __init__(self, w0, xi, k=1):
        super().__init__()
        self.transferFunc = signal.TransferFunction([0, k * 2 * xi / w0, 0], [1 / w0 ** 2, 2 * xi / w0, 1])


class NotchPass(VirtualFilter):
    def __init__(self, w0, xi, k=1):
        super().__init__()
        self.transferFunc = signal.TransferFunction([k / w0 ** 2, 0, k], [1 / w0 ** 2, 2 * xi / w0, 1])


class ArbitraryFilter(VirtualFilter):
    def __init__(self, w0=np.inf, xi=0, num=None, k=1, maxGain=False):
        super().__init__()
        if num is None:
            num = np.array([1])
        else:
            num = np.array(num)
        if maxGain:
            self.transferFunc = signal.TransferFunction(num, [1 / w0 ** 2, 2 * xi / w0, 1])
            w, gain, phase = signal.bode(self.transferFunc, n=5000)
            index = signal.argrelmax(gain)
            if len(index[0]) > 1:
                index = index[0][0]
            maxgainvalue = 10**(gain[index]/20)
            if maxgainvalue > k:

                self.transferFunc = signal.TransferFunction(num * k/maxgainvalue, [1 / w0 ** 2, 2 * xi / w0, 1])
            else:
                self.transferFunc = signal.TransferFunction(num, [1 / w0 ** 2, 2 * xi / w0, 1])
        else:
            self.transferFunc = signal.TransferFunction(num * k, [1 / w0 ** 2, 2 * xi / w0, 1])

    @classmethod
    def secondordnum(cls, w0=np.inf, xi=0, w02=0, xi2=0, k=1, maxGain=False):
        return cls(w0, xi, [1 / w02 ** 2, 2 * xi2 / w02, 1], k, maxGain)

