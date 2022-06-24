import matplotlib.axes
import numpy as np
from matplotlib.widgets import Cursor
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qt import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import mplcursors


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot()
        self.fig.set_tight_layout(True)
        super().__init__(self.fig)
        self.navToolBar = NavigationToolbar(self, parent=parent)


class BodePlot(MplCanvas):
    def __init__(self, parent=None):
        if parent is not None:
            super().__init__(parent)
            self.phaseaxes = None
            self.gainline = None
            self.gainlinedataCursor = None
            self.phaseline = None
            self.phaselinedataCursor = None
            self.cursor = None

    def plot(self, t=None, y=None, z=None):
        if t is None or y is None or z is None:
            self.axes.set_xscale("linear")
            self.axes.cla()
            self.phaseaxes.cla()
            return

        self.getphaseaxes()
        self.axes.set_xscale("linear")
        self.axes.cla()
        self.phaseaxes.cla()
        self.axes.set_xlabel('$\\omega \\left[ \\frac{rad}{s} \\right]$')
        self.axes.set_ylabel('$Gain [dB]$')
        self.phaseaxes.set_ylabel('$Phase [°]$')

        self.gainline = self.axes.semilogx(t, y, 'C0', label='Gain')
        self.phaseline = self.phaseaxes.semilogx(t, z, 'C1', label='Phase')
        self.gainlinedataCursor = mplcursors.cursor(self.gainline)
        self.phaselinedataCursor = mplcursors.cursor(self.phaseline)
        self.cursor = Cursor(self.phaseaxes, useblit=True, color='gray', linestyle='--', linewidth=0.8)
        self.phaseaxes.format_coord = make_format(self.phaseaxes, self.axes)
        self.axes.grid(visible=True, which='both')
        self.phaseaxes.grid(visible=True, which='both')
        self.axes.set_yticks(calculate_ticks(self.axes, 10, round_to=1, center=True))
        self.phaseaxes.set_yticks(calculate_ticks(self.phaseaxes, 10, round_to=1, center=True))
        self.axes.axhline(0, color='black', linewidth=0.75)
        lines = self.gainline + self.phaseline
        labs = [line.get_label() for line in lines]
        self.axes.legend(lines, labs, loc=0)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def getphaseaxes(self):
        if self.phaseaxes is None:
            self.phaseaxes = self.axes.twinx()

        return self.phaseaxes


class InOutPlot(MplCanvas):
    def __init__(self, parent=None):
        if parent is not None:
            super().__init__(parent)
            self.inputline = None
            self.inputdataCursor = None
            self.outputline = None
            self.outputdataCursor = None
            self.cursor = None

    def plot(self, inputtime=None, inputamp=None, outputamp=None):
        if inputamp is None or inputtime is None or outputamp is None:
            self.axes.cla()
            return

        self.axes.cla()
        self.axes.set_xlabel('$Time [s]$')
        self.axes.set_ylabel('$Amplitude [UA]$')

        if len(inputamp) == 1:
            self.inputline, stemline, baseline = self.axes.stem([0], inputamp, linefmt='C1', markerfmt='C1^',
                                                                label='Input')
        else:
            self.inputline = self.axes.plot(inputtime, inputamp, 'C1', label='Input')

        self.outputline = self.axes.plot(inputtime, outputamp, 'C0', label='Output')
        self.cursor = Cursor(self.axes, useblit=True, color='gray', linestyle='--', linewidth=0.8)
        self.inputdataCursor = mplcursors.cursor(self.inputline)
        self.outputdataCursor = mplcursors.cursor(self.outputline)
        self.axes.grid(visible=True)
        self.axes.set_yticks(calculate_ticks(self.axes, 10, round_to=0.001))
        self.axes.legend(loc=0)
        self.axes.axhline(0, color='black', linewidth=0.75)
        self.axes.axvline(0, color='black', linewidth=0.75)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()


class PolesZerosPlot(MplCanvas):
    def __init__(self, parent=None):
        if parent is not None:
            super().__init__(parent)
            self.polesline = None
            self.polesdataCursor = None
            self.zerosline = None
            self.zerosdataCursor = None
            self.cursor = None

    def plot(self, poles=None, zeros=None):
        self.axes.cla()
        self.axes.set_xlabel('$\\Re$')
        self.axes.set_ylabel('$\\Im$')
        self.axes.format_coord = format_coord_complex
        if len(poles) != 0:
            self.polesline = self.axes.scatter(np.real(poles), np.imag(poles), c='Red', marker='x')
            self.polesdataCursor = mplcursors.cursor(self.polesline)
        if len(zeros) != 0:
            self.zerosline = self.axes.scatter(np.real(zeros), np.imag(zeros), c='Blue', marker='o')
            self.zerosdataCursor = mplcursors.cursor(self.zerosline)

        self.cursor = Cursor(self.axes, useblit=True, color='gray', linestyle='--', linewidth=0.8)
        self.axes.grid(visible=True)
        self.axes.set_yticks(calculate_ticks(self.axes, 10, round_to=0.01))
        self.axes.axhline(0, color='black', linewidth=0.75)
        self.axes.axvline(0, color='black', linewidth=0.75)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()


def make_format(current, other):
    # current and other are axes
    def format_coord(x, y):
        # x, y are data coordinates
        # convert to display coords
        display_coord = current.transData.transform((x, y))
        inv = other.transData.inverted()
        # convert back to data coords with respect to ax
        ax_coord = inv.transform(display_coord)
        coords = [ax_coord, (x, y)]
        return ('Left: {:<}   Right: {:}'
                .format(*['({:.3E}, {:.3E})'.format(x, y) for x, y in coords]))

    return format_coord


def format_coord_complex(x, y):
    return "{:.2E} + j*({:.2E})".format(x, y)


def calculate_ticks(ax, ticks, round_to=0.1, center=False):
    upperbound = np.ceil(ax.get_ybound()[1] / round_to)
    lowerbound = np.floor(ax.get_ybound()[0] / round_to)
    dy = upperbound - lowerbound
    fit = np.floor(dy / (ticks - 1)) + 1
    dy_new = (ticks - 1) * fit
    if center:
        offset = np.floor((dy_new - dy) / 2)
        lowerbound = lowerbound - offset
    values = np.linspace(lowerbound, lowerbound + dy_new, ticks)
    return values * round_to
