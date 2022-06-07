from scipy import signal



'''
RLC circuit calculator.

Circuit:       Vin-----/\/\/-----uuuuu-----| |-----GND
Measure point:      1         2         3       4


'''
class RLC():
    R: float
    L: float
    C: float
    measure_point: int
    reference: int
    transfer_function: signal.TransferFunction
    
    def __init__(self, R=1, L=1, C=1, measure_point=1, reference=2) -> None:
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
                self.transfer_function.__init__([self.C * self.R, 0], denom)
                pass
            case 2, 1:
                self.transfer_function.__init__([-1 * self.C * self.R, 0], denom)
                pass
            case 2, 3:
                self.transfer_function.__init__([self.C * self.L, 0, 0], denom)
                pass
            case 3, 2:
                self.transfer_function.__init__([-1 * self.C * self.L, 0, 0], denom)
                pass
            case 3, 4:
                self.transfer_function.__init__([1], denom)
                pass
            case 4, 3:
                self.transfer_function.__init__([-1], denom)
                pass
            case 1, 3:
                self.transfer_function.__init__([self.L * self.C, self.C * self.R, 0], denom)
                pass
            case 3, 1:
                self.transfer_function.__init__([-1 * self.L * self.C, -1 * self.C * self.R, 0], denom)
                pass
            case 2, 4:
                self.transfer_function.__init__([self.C * self.L, 0, 1], denom)
                pass
            case 4, 2:
                self.transfer_function.__init__([-1 * self.C * self.L, 0, -1], denom)
                pass
            case 1, 4:
                self.transfer_function.__init__([1], [1])
                pass
            case 4, 1:
                self.transfer_function.__init__([-1], [1])
                pass
            
            