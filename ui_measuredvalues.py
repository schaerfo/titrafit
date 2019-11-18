# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'measuredvaluesform.ui',
# licensing of 'measuredvaluesform.ui' applies.
#
# Created: Thu Nov  7 16:00:46 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MeasuredValuesForm(object):
    def setupUi(self, MeasuredValuesForm):
        MeasuredValuesForm.setObjectName("MeasuredValuesForm")
        MeasuredValuesForm.resize(346, 280)
        self.gridLayout = QtWidgets.QGridLayout(MeasuredValuesForm)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.addButton = QtWidgets.QPushButton(MeasuredValuesForm)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 1, 4, 1, 1)
        self.loadButton = QtWidgets.QPushButton(MeasuredValuesForm)
        self.loadButton.setObjectName("loadButton")
        self.gridLayout.addWidget(self.loadButton, 9, 3, 1, 2)
        self.saveButton = QtWidgets.QPushButton(MeasuredValuesForm)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 8, 3, 1, 2)
        self.removeButton = QtWidgets.QPushButton(MeasuredValuesForm)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 2, 4, 1, 1)
        self.clearButton = QtWidgets.QPushButton(MeasuredValuesForm)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 3, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 4, 1, 1)
        self.list = QtWidgets.QTableView(MeasuredValuesForm)
        self.list.setMinimumSize(QtCore.QSize(250, 200))
        self.list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.list.setObjectName("list")
        self.list.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.list, 1, 3, 4, 1)

        self.retranslateUi(MeasuredValuesForm)
        QtCore.QMetaObject.connectSlotsByName(MeasuredValuesForm)

    def retranslateUi(self, MeasuredValuesForm):
        self.addButton.setText(QtWidgets.QApplication.translate("MeasuredValuesForm", "+", None, -1))
        self.loadButton.setText(QtWidgets.QApplication.translate("MeasuredValuesForm", "Aus Datei laden...", None, -1))
        self.saveButton.setText(QtWidgets.QApplication.translate("MeasuredValuesForm", "In Datei speichern...", None, -1))
        self.removeButton.setText(QtWidgets.QApplication.translate("MeasuredValuesForm", "-", None, -1))
        self.clearButton.setText(QtWidgets.QApplication.translate("MeasuredValuesForm", "Löschen", None, -1))

