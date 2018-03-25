# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.text_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_input.setObjectName("text_input")
        self.gridLayout.addWidget(self.text_input, 2, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.text_output = QtWidgets.QTextEdit(self.centralwidget)
        self.text_output.setReadOnly(True)
        self.text_output.setObjectName("text_output")
        self.gridLayout.addWidget(self.text_output, 4, 0, 1, 3)
        self.button_submit = QtWidgets.QPushButton(self.centralwidget)
        self.button_submit.setObjectName("button_submit")
        self.gridLayout.addWidget(self.button_submit, 5, 0, 1, 1)
        self.button_reset = QtWidgets.QPushButton(self.centralwidget)
        self.button_reset.setObjectName("button_reset")
        self.gridLayout.addWidget(self.button_reset, 5, 1, 1, 1)
        self.button_close = QtWidgets.QPushButton(self.centralwidget)
        self.button_close.setObjectName("button_close")
        self.gridLayout.addWidget(self.button_close, 5, 2, 1, 1)
        self.line_addr = QtWidgets.QLineEdit(self.centralwidget)
        self.line_addr.setObjectName("line_addr")
        self.gridLayout.addWidget(self.line_addr, 0, 0, 1, 1)
        self.line_port = QtWidgets.QLineEdit(self.centralwidget)
        self.line_port.setObjectName("line_port")
        self.gridLayout.addWidget(self.line_port, 0, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.button_close.released.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Pleas provide your text here:"))
        self.label_2.setText(_translate("MainWindow", "Here is your result:"))
        self.button_submit.setText(_translate("MainWindow", "check"))
        self.button_reset.setText(_translate("MainWindow", "reset"))
        self.button_close.setText(_translate("MainWindow", "close"))
        self.line_addr.setText(_translate("MainWindow", "localhost"))
        self.line_port.setText(_translate("MainWindow", "8080"))

