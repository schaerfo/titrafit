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
from PySide2.QtCore import Qt, QAbstractListModel, QAbstractTableModel, Slot


class PKaModel(QAbstractListModel):
    def __init__(self, parent=None):
        QAbstractListModel.__init__(self, parent)
        self.pKa = []

    def rowCount(self, _):
        return len(self.pKa)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.pKa[index.row()]
        else:
            return None

    def addValue(self, pKa):
        self.pKa.append(pKa)
        self.pKa.sort()
        self.layoutChanged.emit()

    def removeValue(self, index):
        if index < len(self.pKa):
            del self.pKa[index]
            self.layoutChanged.emit()

    @Slot()
    def clear(self):
        self.pKa.clear()
        self.layoutChanged.emit()


class MeasuredValuesModel(QAbstractTableModel):
    def __init__(self, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self.values = []

    def rowCount(self, _):
        return len(self.values)

    def columnCount(self, _):
        return 2

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.values[index.row()][index.column()]
        else:
            return None
        
    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if section == 0:
                return "V [ml]"
            elif section == 1:
                return "pH"
            else:
                return None
        else:
            return None

    def sortValues(self):
        self.values.sort(key=lambda x: x[0])
        self.layoutChanged.emit()

    @Slot(float, float)
    def addValue(self, v, pH):
        self.values.append((v, pH))
        self.sortValues()

    def removeValue(self, index):
        del self.values[index]
        self.layoutChanged.emit()

    def clearValues(self):
        self.values.clear()
        self.layoutChanged.emit()

    def loadValues(self, filename):
        f = open(filename, "r")
        for l in f:
            if not l.startswith("#"):
                s = l.split(" ")
                self.values.append((float(s[0]), float(s[1])))

        f.close()
        self.sortValues()

    def saveValues(self, filename):
        f = open(filename, 'w')
        for v, pH in self.values:
            f.write(f"{v} {pH}\n")
        f.close()

    def getValuesAsArrays(self):
        x = np.array([i[0] for i in self.values])
        y = np.array([i[1] for i in self.values])
        return x*0.001, y