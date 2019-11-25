# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inputform.ui',
# licensing of 'inputform.ui' applies.
#
# Created: Thu Nov 28 20:52:25 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_inputForm(object):
    def setupUi(self, inputForm):
        inputForm.setObjectName("inputForm")
        inputForm.resize(244, 182)
        self.formLayout = QtWidgets.QFormLayout(inputForm)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.vLabel = QtWidgets.QLabel(inputForm)
        self.vLabel.setObjectName("vLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.vLabel)
        self.v0Input = QtWidgets.QDoubleSpinBox(inputForm)
        self.v0Input.setMaximum(9999999999.0)
        self.v0Input.setObjectName("v0Input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.v0Input)
        self.cBLabel = QtWidgets.QLabel(inputForm)
        self.cBLabel.setObjectName("cBLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.cBLabel)
        self.cBInput = QtWidgets.QDoubleSpinBox(inputForm)
        self.cBInput.setObjectName("cBInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cBInput)
        self.pKsLabel = QtWidgets.QLabel(inputForm)
        self.pKsLabel.setObjectName("pKsLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pKsLabel)
        self.valueLabel = QtWidgets.QLabel(inputForm)
        self.valueLabel.setObjectName("valueLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.valueLabel)
        self.fitButton = QtWidgets.QPushButton(inputForm)
        self.fitButton.setObjectName("fitButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.fitButton)
        self.pKsForm = PKsForm(inputForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pKsForm.sizePolicy().hasHeightForWidth())
        self.pKsForm.setSizePolicy(sizePolicy)
        self.pKsForm.setObjectName("pKsForm")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pKsForm)
        self.measuredValuesForm = MeasuredValuesForm(inputForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measuredValuesForm.sizePolicy().hasHeightForWidth())
        self.measuredValuesForm.setSizePolicy(sizePolicy)
        self.measuredValuesForm.setObjectName("measuredValuesForm")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.measuredValuesForm)
        self.resultLabel = QtWidgets.QLabel(inputForm)
        self.resultLabel.setText("")
        self.resultLabel.setObjectName("resultLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.resultLabel)

        self.retranslateUi(inputForm)
        QtCore.QMetaObject.connectSlotsByName(inputForm)

    def retranslateUi(self, inputForm):
        self.vLabel.setText(QtWidgets.QApplication.translate("inputForm", "<html><head/><body><p>V<span style=\" vertical-align:sub;\">0</span> [ml]:</p></body></html>", None, -1))
        self.cBLabel.setText(QtWidgets.QApplication.translate("inputForm", "c(NaOH) [mol/l]:", None, -1))
        self.pKsLabel.setText(QtWidgets.QApplication.translate("inputForm", "<html><head/><body><p>pK<span style=\" vertical-align:sub;\">a</span>:</p></body></html>", None, -1))
        self.valueLabel.setText(QtWidgets.QApplication.translate("inputForm", "Measured Values:", None, -1))
        self.fitButton.setText(QtWidgets.QApplication.translate("inputForm", "Fit", None, -1))

from pksform import PKsForm
from measuredvaluesform import MeasuredValuesForm
