from Filters.VirtualFilter import *

class LowPass(VirtualFilter):
    def __init__(self, w0):
        super().__init__()
        self.transferFunc = signal.ZerosPolesGain([], [-w0], w0)  #Zeros Polos Ganancia

