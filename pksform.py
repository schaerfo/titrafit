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


from PySide2.QtWidgets import QInputDialog, QWidget

from models import PKsModel
from ui_pksform import Ui_pKsForm


class PKsForm(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_pKsForm()
        self.ui.setupUi(self)

        self.pKsModel = PKsModel(self)
        self.ui.list.setModel(self.pKsModel)
        self.ui.addButton.clicked.connect(self.addPKs)
        self.ui.removeButton.clicked.connect(self.removePKs)
        self.ui.clearButton.clicked.connect(self.pKsModel.clear)

    def addPKs(self):
        pKs, ok = QInputDialog.getDouble(self, "Add pKa value", "pK<sub>a</sub> value:", decimals=2)
        if ok:
            self.pKsModel.addValue(pKs)

    def removePKs(self):
        model = self.ui.list.selectionModel()
        if model.hasSelection():
            self.pKsModel.removeValue(model.currentIndex().row())
            model.reset()
