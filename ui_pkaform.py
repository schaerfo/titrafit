# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pkaform.ui',
# licensing of 'pkaform.ui' applies.
#
# Created: Mon Nov 25 21:06:15 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_pKaForm(object):
    def setupUi(self, pKaForm):
        pKaForm.setObjectName("pKaForm")
        pKaForm.resize(346, 114)
        self.gridLayout = QtWidgets.QGridLayout(pKaForm)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.addButton = QtWidgets.QPushButton(pKaForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 0, 4, 1, 1)
        self.removeButton = QtWidgets.QPushButton(pKaForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeButton.sizePolicy().hasHeightForWidth())
        self.removeButton.setSizePolicy(sizePolicy)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 1, 4, 1, 1)
        self.clearButton = QtWidgets.QPushButton(pKaForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 2, 4, 1, 1)
        self.list = QtWidgets.QListView(pKaForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list.sizePolicy().hasHeightForWidth())
        self.list.setSizePolicy(sizePolicy)
        self.list.setObjectName("list")
        self.gridLayout.addWidget(self.list, 0, 0, 4, 4)

        self.retranslateUi(pKaForm)
        QtCore.QMetaObject.connectSlotsByName(pKaForm)

    def retranslateUi(self, pKaForm):
        self.addButton.setText(QtWidgets.QApplication.translate("pKaForm", "+", None, -1))
        self.removeButton.setText(QtWidgets.QApplication.translate("pKaForm", "-", None, -1))
        self.clearButton.setText(QtWidgets.QApplication.translate("pKaForm", "Clear", None, -1))

