# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(614, 372)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_submit = QtWidgets.QPushButton(self.centralwidget)
        self.button_submit.setObjectName("button_submit")
        self.gridLayout_2.addWidget(self.button_submit, 0, 0, 1, 1)
        self.button_reset = QtWidgets.QPushButton(self.centralwidget)
        self.button_reset.setObjectName("button_reset")
        self.gridLayout_2.addWidget(self.button_reset, 0, 1, 1, 1)
        self.button_close = QtWidgets.QPushButton(self.centralwidget)
        self.button_close.setObjectName("button_close")
        self.gridLayout_2.addWidget(self.button_close, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_start = QtWidgets.QLabel(self.centralwidget)
        self.label_start.setObjectName("label_start")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_start)
        self.label_dest = QtWidgets.QLabel(self.centralwidget)
        self.label_dest.setObjectName("label_dest")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_dest)
        self.line_start = QtWidgets.QLineEdit(self.centralwidget)
        self.line_start.setObjectName("line_start")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_start)
        self.line_dest = QtWidgets.QLineEdit(self.centralwidget)
        self.line_dest.setObjectName("line_dest")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_dest)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        self.textedit_output = QtWidgets.QTextEdit(self.centralwidget)
        self.textedit_output.setReadOnly(True)
        self.textedit_output.setObjectName("textedit_output")
        self.gridLayout.addWidget(self.textedit_output, 2, 0, 1, 1)
        self.label_Status = QtWidgets.QLabel(self.centralwidget)
        self.label_Status.setObjectName("label_Status")
        self.gridLayout.addWidget(self.label_Status, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.button_close.pressed.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Google Navigation"))
        self.button_submit.setText(_translate("MainWindow", "Submit"))
        self.button_reset.setText(_translate("MainWindow", "Reset"))
        self.button_close.setText(_translate("MainWindow", "Close"))
        self.label_start.setText(_translate("MainWindow", "Start:"))
        self.label_dest.setText(_translate("MainWindow", "Ziel:"))
        self.label_Status.setText(_translate("MainWindow", "TextLabel"))

