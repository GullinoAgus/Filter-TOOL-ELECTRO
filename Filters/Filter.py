from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


class Filter:
    def __init__(self):
        self.transferFunc = signal.ZerosPolesGain([], [], 1)

    def plotgain(self):
        w, mag, phase = signal.bode(self.transferFunc)
        plt.figure()
        plt.semilogx(w, mag)  # Bode magnitude plot
        plt.figure()
        plt.semilogx(w, phase)  # Bode phase plot
        plt.show()

    def plotphase(self):
        print('NotImplemented')

    def plotpolesandperos(self):
        print('NotImplemented')

    def plotoutput(self, inputtime, inputvalue):
        tout, yout, xout = signal.lsim(self.transferFunc, U=inputvalue, T=inputtime)
        plt.plot(inputtime, inputvalue, 'r', alpha=0.5, linewidth=1, label='input')
        plt.plot(tout, yout, linewidth=1.5, label='output')
        plt.legend(loc='best', shadow=True, framealpha=1)
        plt.title("Respuesta")
        plt.xlabel('t (sec)')
        plt.show()
