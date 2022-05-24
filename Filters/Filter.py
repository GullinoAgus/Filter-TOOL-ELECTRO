from scipy import signal

import numpy as np
from matplotlib.widgets import Cursor


class Filter:
    def __init__(self):
        self.transferFunc = signal.ZerosPolesGain([], [], 1)

    def getbode(self):
        w, mag, phase = signal.bode(self.transferFunc)
        return w, mag, phase

    def getpolesandzeros(self):
        return self.transferFunc.poles, self.transferFunc.zeros

    def getoutputfrominput(self, inputtime, inputvalue):
        tout, yout, xout = signal.lsim(self.transferFunc, U=inputvalue, T=inputtime)
        return tout, yout

