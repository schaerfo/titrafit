# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'valueinputdialog.ui',
# licensing of 'valueinputdialog.ui' applies.
#
# Created: Thu Nov 28 20:53:01 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ValueInputDialog(object):
    def setupUi(self, ValueInputDialog):
        ValueInputDialog.setObjectName("ValueInputDialog")
        ValueInputDialog.resize(205, 122)
        self.formLayout = QtWidgets.QFormLayout(ValueInputDialog)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.volumeInput = QtWidgets.QDoubleSpinBox(ValueInputDialog)
        self.volumeInput.setObjectName("volumeInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.volumeInput)
        self.volumeLabel = QtWidgets.QLabel(ValueInputDialog)
        self.volumeLabel.setObjectName("volumeLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.volumeLabel)
        self.pHLabel = QtWidgets.QLabel(ValueInputDialog)
        self.pHLabel.setObjectName("pHLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pHLabel)
        self.buttonBox = QtWidgets.QDialogButtonBox(ValueInputDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)
        self.pHInput = QtWidgets.QDoubleSpinBox(ValueInputDialog)
        self.pHInput.setObjectName("pHInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pHInput)

        self.retranslateUi(ValueInputDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ValueInputDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ValueInputDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ValueInputDialog)
        ValueInputDialog.setTabOrder(self.volumeInput, self.pHInput)

    def retranslateUi(self, ValueInputDialog):
        ValueInputDialog.setWindowTitle(QtWidgets.QApplication.translate("ValueInputDialog", "Add value", None, -1))
        self.volumeLabel.setText(QtWidgets.QApplication.translate("ValueInputDialog", "V [ml]:", None, -1))
        self.pHLabel.setText(QtWidgets.QApplication.translate("ValueInputDialog", "pH:", None, -1))

