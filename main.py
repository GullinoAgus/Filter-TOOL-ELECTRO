# noinspection PyUnresolvedReferences
from scipy import signal
import sys
from Filters import LowPass
import numpy as np
from UI import *
from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.widgets import Cursor
from matplotlib.backends.backend_qtagg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

import mplcursors


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


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot()
        self.axesCursor = None
        self.twinxaxes = None
        self.twinxaxesCursor = None
        self.fig.set_tight_layout(True)
        self.lineaxes = None
        self.linetwinxaxes = None
        self.axesdataCursor = None
        self.twinxaxesdataCursor = None
        super(MplCanvas, self).__init__(self.fig)

    def getTwinAxes(self):
        if self.twinxaxes is None:
            self.twinxaxes = self.axes.twinx()

        return self.twinxaxes

    def plot(self, t=None, y=None, z=None):
        if t is None or y is None:
            return

        if z is None:
            self.axes.clear()
            self.axes.plot(t, y)
            self.axesCursor = Cursor(self.axes, useblit=True, color='gray', linestyle='--', linewidth=0.8)
        else:
            self.getTwinAxes()
            self.axes.set_xscale("linear")
            self.axes.cla()
            self.twinxaxes.cla()
            self.lineaxes = self.axes.semilogx(t, y)
            self.linetwinxaxes = self.twinxaxes.semilogx(t, z)
            self.axesdataCursor = mplcursors.cursor(self.lineaxes)
            self.twinxaxesdataCursor = mplcursors.cursor(self.linetwinxaxes)
            self.twinxaxesCursor = Cursor(self.twinxaxes, useblit=True, color='gray', linestyle='--', linewidth=0.8)
            self.twinxaxes.format_coord = make_format(self.twinxaxes, self.axes)

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Bodeplot = MplCanvas(parent=self.BodePlotBox, width=2, height=2, dpi=100)
        self.InOutplot = MplCanvas(parent=self.InputAndOutputBox, width=2, height=2, dpi=100)
        self.PolesZerosplot = MplCanvas(parent=self.PolesAndZerosBox, width=2, height=2, dpi=100)
        self.BodePlotBox.layout().addWidget(NavigationToolbar(self.Bodeplot, self.BodePlotBox))
        self.BodePlotBox.layout().addWidget(self.Bodeplot)
        self.PolesAndZerosBox.layout().addWidget(NavigationToolbar(self.PolesZerosplot, self.PolesAndZerosBox))
        self.PolesAndZerosBox.layout().addWidget(self.PolesZerosplot)
        self.InputAndOutputBox.layout().addWidget(NavigationToolbar(self.InOutplot, self.InputAndOutputBox))
        self.InputAndOutputBox.layout().addWidget(self.InOutplot)

    def plotbode(self, w, mag, phase):
        self.Bodeplot.plot(w, mag, phase)

    def ClickBoton(self):
        filtrito = LowPass.LowPass(float(self.omegaZero.text()))
        w, a, p = filtrito.getbode()
        self.plotbode(w, a, p)


def main():
    aplicacion = QtWidgets.QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(aplicacion.exec())


if __name__ == "__main__":
    main()
