from scipy import signal


class VirtualFilter:
    def __init__(self):
        self.transferFunc = signal.ZerosPolesGain([], [], 1)

    def getbode(self):
        w, mag, phase = signal.bode(self.transferFunc, n=5000)
        return w, mag, phase

    def getpolesandzeros(self):
        return self.transferFunc.poles, self.transferFunc.zeros

    def getoutputfrominput(self, inputtime=None, inputvalue=None, impulse=False):
        if impulse:
            tout, yout = signal.impulse(self.transferFunc, N=5000)
        elif inputvalue is not None and inputtime is not None:
            tout, yout, xout = signal.lsim(self.transferFunc, U=inputvalue, T=inputtime)
        else:
            return [], []
        return tout, yout

