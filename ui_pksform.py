# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pksform.ui',
# licensing of 'pksform.ui' applies.
#
# Created: Thu Nov 28 20:52:50 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_pKsForm(object):
    def setupUi(self, pKsForm):
        pKsForm.setObjectName("pKsForm")
        pKsForm.resize(346, 114)
        self.gridLayout = QtWidgets.QGridLayout(pKsForm)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.addButton = QtWidgets.QPushButton(pKsForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 0, 4, 1, 1)
        self.removeButton = QtWidgets.QPushButton(pKsForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeButton.sizePolicy().hasHeightForWidth())
        self.removeButton.setSizePolicy(sizePolicy)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 1, 4, 1, 1)
        self.clearButton = QtWidgets.QPushButton(pKsForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 2, 4, 1, 1)
        self.list = QtWidgets.QListView(pKsForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list.sizePolicy().hasHeightForWidth())
        self.list.setSizePolicy(sizePolicy)
        self.list.setObjectName("list")
        self.gridLayout.addWidget(self.list, 0, 0, 4, 4)

        self.retranslateUi(pKsForm)
        QtCore.QMetaObject.connectSlotsByName(pKsForm)

    def retranslateUi(self, pKsForm):
        self.addButton.setText(QtWidgets.QApplication.translate("pKsForm", "+", None, -1))
        self.removeButton.setText(QtWidgets.QApplication.translate("pKsForm", "-", None, -1))
        self.clearButton.setText(QtWidgets.QApplication.translate("pKsForm", "Clear", None, -1))

