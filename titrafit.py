#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Copyright (C) 2019  Christian Schärf

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


from sys import argv

import numpy as np
import scipy.optimize
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QGridLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from ui_inputform import Ui_inputForm

try:
    from tfast import TitrationVolume
except ImportError:
    print("tfast module not found, using Python implementation of fit function")
    from titration import TitrationVolume


class TWrapper(TitrationVolume):
    def __init__(self, *args):
        super().__init__(*args)

    def __call__(self, c0_b, *args):
        return [TitrationVolume.__call__(self, i, *args) for i in c0_b]


class Titrafit(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.form = QWidget(self)
        self.ui = Ui_inputForm()
        self.ui.setupUi(self.form)

        self.ui.measuredValuesForm.valuesChanged.connect(self.updatePlot)
        self.ui.fitButton.clicked.connect(self.fit)

        figure = Figure()
        self.axes = figure.add_subplot()
        self.axes.set_xlabel("V(NaOH) [ml]")
        self.axes.set_ylabel("pH")
        self.canvas = FigureCanvas(figure)
        navbar = NavigationToolbar(self.canvas, self)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.form, 0, 0, 2, 1)
        self.layout.addWidget(navbar, 0, 1, 1, 1)
        self.layout.addWidget(self.canvas, 1, 1, 1, 1)
        self.layout.setColumnStretch(0, 0)
        self.layout.setColumnStretch(1, 1)
        self.setLayout(self.layout)

        self.setWindowTitle("Titrafit")

    @Slot(np.ndarray, np.ndarray)
    def updatePlot(self, x, y):
        self.axes.clear()
        self.axes.scatter(x * 1000, y, marker='+')
        self.axes.set_xlabel("V(NaOH) [ml]")
        self.axes.set_ylabel("pH")
        self.canvas.draw()

    def fit(self):
        v0 = self.ui.v0Input.value()
        cB = self.ui.cBInput.value()
        t = TWrapper(v0, cB, self.ui.pKsForm.pKsModel.pKs)
        x, y = self.ui.measuredValuesForm.valuesModel.getValuesAsArrays()
        popt, _ = scipy.optimize.curve_fit(t, x, y, p0=(0.2,), bounds=(0, np.inf))
        xFit = np.linspace(x[0], x[-1], 500)
        self.axes.plot(xFit * 1000, t(xFit, *popt))
        self.canvas.draw()
        self.ui.resultLabel.setText(f"c<sub>0</sub> = {popt[0]} mol/l")


def main():
    a = QApplication(argv)
    w = Titrafit()
    w.show()
    a.exec_()


if __name__ == "__main__":
    main()
