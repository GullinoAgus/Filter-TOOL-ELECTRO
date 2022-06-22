from typing import Tuple

import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

'''
RLC circuit calculator.

Circuit:       Vin-----/\/\/-----uuuuu-----| |-----GND
Measure point:      1         2         3       4
'''


class RLC:
    def __init__(self, R=1, L=1, C=1, measure_point=1, reference=2) -> None:
        self.transfer_function = None
        if measure_point == reference:
            raise ValueError("Measure point and reference cannot be the same")

        if R <= 0 or L <= 0 or C <= 0:
            raise ValueError("R, L, and C must be positive")

        self.R = R
        self.L = L
        self.C = C
        self.measure_point = measure_point
        self.reference = reference
        self.generate_transfer_function()

    def generate_transfer_function(self) -> None:
        '''
        Generate the transfer function of the circuit according to its measure points
        '''

        denom = [self.L * self.C, self.C * self.R, 1]

        match self.measure_point, self.reference:

            case 1, 2:
                self.transfer_function = signal.TransferFunction([self.C * self.R, 0], denom)
                pass
            case 2, 1:
                self.transfer_function = signal.TransferFunction([-1 * self.C * self.R, 0], denom)
                pass
            case 2, 3:
                self.transfer_function = signal.TransferFunction([self.C * self.L, 0, 0], denom)
                pass
            case 3, 2:
                self.transfer_function = signal.TransferFunction([-1 * self.C * self.L, 0, 0], denom)
                pass
            case 3, 4:
                self.transfer_function = signal.TransferFunction([1], denom)
                pass
            case 4, 3:
                self.transfer_function = signal.TransferFunction([-1], denom)
                pass
            case 1, 3:
                self.transfer_function = signal.TransferFunction([self.L * self.C, self.C * self.R, 0], denom)
                pass
            case 3, 1:
                self.transfer_function = signal.TransferFunction([-1 * self.L * self.C, -1 * self.C * self.R, 0], denom)
                pass
            case 2, 4:
                self.transfer_function = signal.TransferFunction([self.C * self.L, 0, 1], denom)
                pass
            case 4, 2:
                self.transfer_function = signal.TransferFunction([-1 * self.C * self.L, 0, -1], denom)
                pass
            case 1, 4:
                self.transfer_function = signal.TransferFunction([1], [1])
                pass
            case 4, 1:
                self.transfer_function = signal.TransferFunction([-1], [1])
                pass

    def get_bode(self) -> tuple[int, int, int]:
        return signal.bode(self.transfer_function, n=5000)

    def get_output_from_input(self, inputtime=None, inputvalue=None, impulse=False):
        if impulse:
            tout, yout = signal.impulse(self.transfer_function)
        elif inputvalue is not None and inputtime is not None:
            tout, yout, xout = signal.lsim(self.transfer_function, U=inputvalue, T=inputtime)
        else:
            return [], []
        return tout, yout

    def get_resonant_freq(self) -> float:
        return 1 / np.sqrt(self.L * self.C)

    def get_Q(self) -> float:
        return np.sqrt(self.L / self.C) / self.R


if __name__ == '__main__':
    for i in range(1, 5):
        for j in range(1, 5):
            if i == j:
                continue
            rlc = RLC(measure_point=i, reference=j)
            w, gain, phase = rlc.get_bode()
            eje1 = plt.subplot(211)
            eje2 = plt.subplot(212)
            eje1.semilogx(w, gain)
            eje2.semilogx(w, phase)
            plt.show()
