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
    def __init__(self, w0=np.inf, xi=0, num=[1], k=1):
        super().__init__()
        self.transferFunc = signal.TransferFunction(num * k, [1 / w0 ** 2, 2 * xi / w0, 1])
