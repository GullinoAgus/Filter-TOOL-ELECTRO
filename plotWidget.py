import numpy as np
from matplotlib.widgets import Cursor
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qt import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
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
        self.gainline = self.axes.semilogx(t, y)
        self.phaseline = self.phaseaxes.semilogx(t, z)
        self.gainlinedataCursor = mplcursors.cursor(self.gainline)
        self.phaselinedataCursor = mplcursors.cursor(self.phaseline)
        self.cursor = Cursor(self.phaseaxes, useblit=True, color='gray', linestyle='--', linewidth=0.8)
        self.phaseaxes.format_coord = make_format(self.phaseaxes, self.axes)

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
        self.inputline = self.axes.plot(inputtime, inputamp)
        self.outputline = self.axes.plot(inputtime, outputamp)
        self.cursor = Cursor(self.axes, useblit=True, color='gray', linestyle='--', linewidth=0.8)
        self.inputdataCursor = mplcursors.cursor(self.inputline)
        self.outputdataCursor = mplcursors.cursor(self.outputline)

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
        self.axes.format_coord = format_coord_complex
        if len(poles) != 0:
            self.polesline = self.axes.scatter(np.real(poles), np.imag(poles), c='Red', marker='x')
            self.polesdataCursor = mplcursors.cursor(self.polesline)
        if len(zeros) != 0:
            self.zerosline = self.axes.scatter(np.real(zeros), np.imag(zeros), c='Blue', marker='o')
            self.zerosdataCursor = mplcursors.cursor(self.zerosline)

        self.cursor = Cursor(self.axes, useblit=True, color='gray', linestyle='--', linewidth=0.8)

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
