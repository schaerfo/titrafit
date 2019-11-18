#!/usr/bin/python3
# -*- coding: utf-8

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


import numpy as np
from PySide2.QtCore import Signal, Slot
from PySide2.QtWidgets import QDialog, QFileDialog, QWidget

from ui_measuredvalues import Ui_MeasuredValuesForm
from ui_valueinputdialog import Ui_ValueInputDialog
from models import MeasuredValuesModel

class ValueInputDialog(QDialog):
    accepted = Signal(float, float)

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_ValueInputDialog()
        self.ui.setupUi(self)

    def show(self):
        self.ui.volumeInput.setFocus()
        QDialog.show(self)

    def accept(self):
        self.accepted.emit(self.ui.volumeInput.value(), self.ui.pHInput.value())
        QDialog.accept(self)

class MeasuredValuesForm(QWidget):
    valuesChanged = Signal(np.ndarray, np.ndarray)

    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MeasuredValuesForm()
        self.ui.setupUi(self)

        self.valuesModel = MeasuredValuesModel(self)
        self.valuesModel.layoutChanged.connect(lambda: self.valuesChanged.emit(*self.valuesModel.getValuesAsArrays()))
        self.ui.list.setModel(self.valuesModel)
        self.ui.loadButton.clicked.connect(self.loadValues)
        self.ui.saveButton.clicked.connect(self.saveValues)
        self.ui.clearButton.clicked.connect(self.valuesModel.clearValues)

        inputdialog = ValueInputDialog(self)
        self.ui.addButton.clicked.connect(inputdialog.show)
        inputdialog.accepted.connect(self.valuesModel.addValue)

        self.ui.removeButton.clicked.connect(self.removeValue)

    def loadValues(self):
        filename, _ = QFileDialog.getOpenFileName(self)
        self.valuesModel.loadValues(filename if filename != '' else "data.xy")
        self.valuesChanged.emit(*self.valuesModel.getValuesAsArrays())

    def saveValues(self):
        filename, _ = QFileDialog.getSaveFileName(self)
        self.valuesModel.saveValues(filename)

    def removeValue(self):
        m = self.ui.list.selectionModel()
        if m.hasSelection():
            self.valuesModel.removeValue(m.currentIndex().row())
            m.reset()
