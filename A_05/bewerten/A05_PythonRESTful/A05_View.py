# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_A05_GUI(object):
    def setupUi(self, A05_GUI):
        A05_GUI.setObjectName("A05_GUI")
        A05_GUI.resize(703, 634)
        A05_GUI.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(A05_GUI)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setObjectName("title_label")
        self.horizontalLayout_2.addWidget(self.title_label)
        self.selection = QtWidgets.QComboBox(self.centralwidget)
        self.selection.setObjectName("selection")
        self.selection.addItem("")
        self.selection.addItem("")
        self.horizontalLayout_2.addWidget(self.selection)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.start = QtWidgets.QLabel(self.centralwidget)
        self.start.setObjectName("start")
        self.gridLayout_2.addWidget(self.start, 0, 0, 1, 1)
        self.destination = QtWidgets.QLabel(self.centralwidget)
        self.destination.setObjectName("destination")
        self.gridLayout_2.addWidget(self.destination, 1, 0, 1, 1)
        self.input_origin = QtWidgets.QLineEdit(self.centralwidget)
        self.input_origin.setObjectName("input_origin")
        self.gridLayout_2.addWidget(self.input_origin, 0, 1, 1, 1)
        self.input_destination = QtWidgets.QLineEdit(self.centralwidget)
        self.input_destination.setObjectName("input_destination")
        self.gridLayout_2.addWidget(self.input_destination, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.output_display = QtWidgets.QTextEdit(self.centralwidget)
        self.output_display.setEnabled(True)
        self.output_display.setReadOnly(True)
        self.output_display.setObjectName("output_display")
        self.gridLayout.addWidget(self.output_display, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setObjectName("submit")
        self.horizontalLayout.addWidget(self.submit)
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setObjectName("reset")
        self.horizontalLayout.addWidget(self.reset)
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setObjectName("close")
        self.horizontalLayout.addWidget(self.close)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.status, 4, 0, 1, 1)
        A05_GUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(A05_GUI)
        self.close.clicked.connect(A05_GUI.close)
        self.reset.clicked.connect(self.output_display.clear)
        self.reset.clicked.connect(self.input_destination.clear)
        self.reset.clicked.connect(self.input_origin.clear)
        QtCore.QMetaObject.connectSlotsByName(A05_GUI)

    def retranslateUi(self, A05_GUI):
        _translate = QtCore.QCoreApplication.translate
        A05_GUI.setWindowTitle(_translate("A05_GUI", "Python RESTful Service"))
        self.title_label.setText(_translate("A05_GUI", "Google Navigator"))
        self.selection.setItemText(0, _translate("A05_GUI", "JSON"))
        self.selection.setItemText(1, _translate("A05_GUI", "XML"))
        self.start.setText(_translate("A05_GUI", "Start:"))
        self.destination.setText(_translate("A05_GUI", "Ziel:"))
        self.submit.setText(_translate("A05_GUI", "Submit"))
        self.reset.setText(_translate("A05_GUI", "Reset"))
        self.close.setText(_translate("A05_GUI", "Close"))
        self.status.setText(_translate("A05_GUI", "Berechnung nicht ausgeführt"))

