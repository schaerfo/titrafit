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
from time import monotonic

import numpy as np
import scipy.optimize
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QGridLayout, QMessageBox, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from ui_inputform import Ui_inputForm

try:
    from tfast import Titration
except ImportError as e:
    print("tfast module not found, using Python implementation of fit function")
    print(e)
    from titration import Titration


class TWrapper(Titration):
    def __init__(self, *args):
        super().__init__(*args)

    def __call__(self, c0_b, c0_s):
        return [Titration.__call__(self, c0_b_i, c0_s_i) for (c0_b_i, c0_s_i) in zip(c0_b, c0_s)]


class TitrationVolume(TWrapper):
    def __init__(self, V0, c0_b, pKa):
        self.c0_b = c0_b
        self.V0 = V0
        super().__init__(pKa)

    def __call__(self, V_b, n0_s):
        V = self.V0 + V_b
        c_s = n0_s / V
        c_b = self.c0_b * V_b / V
        return super().__call__(c_b, c_s)

    def percentage(self, percentage, n0_s):
        x = self.__call__(percentage * n0_s / self.c0_b, n0_s)
        return x


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
        # Volume input is in ml, therefore divide by 1000 to obtain l
        v0 = self.ui.v0Input.value() / 1000
        if v0 == 0.0:
            QMessageBox.information(self, "Information", "V<sub>0</sub> must not be 0.")
            return

        cB = self.ui.cBInput.value()
        if cB == 0.0:
            QMessageBox.information(self, "Information", "c(NaOH) must not be 0.")
            return

        pKa = self.ui.pKaForm.pKaModel.pKa
        if not len(pKa):
            QMessageBox.information(self, "Information", "At least one pK<sub>a</sub> value must be specified.")
            return

        x, y = self.ui.measuredValuesForm.valuesModel.getValuesAsArrays()
        assert len(x) == len(y)
        if not len(x):
            QMessageBox.information(self, "Information", "At least one measured value must be specified.")
            return

        t = TitrationVolume(v0, cB, pKa)

        start = monotonic()
        popt, _ = scipy.optimize.curve_fit(t, x, y, p0=(0.2,), bounds=(0, np.inf))
        xFit = np.linspace(x[0], x[-1], 500)
        yFit = t(xFit, *popt)
        duration = monotonic() - start

        self.updatePlot(x, y)
        self.axes.plot(xFit * 1000, yFit)
        self.canvas.draw()
        self.ui.resultLabel.setText(f"c<sub>0</sub> = {popt[0]} mol/l; Duration: {duration} s")


def main():
    a = QApplication(argv)
    w = Titrafit()
    w.show()
    a.exec_()


if __name__ == "__main__":
    main()
