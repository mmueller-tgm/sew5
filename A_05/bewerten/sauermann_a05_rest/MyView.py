# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Raphael_\Google Drive\17.18\sew\python\gui_a05\MyView.ui'
#
# Created: Tue Oct 19 20:00:18 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class MyView(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(905, 583)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.startEingabe = QtGui.QLineEdit(Form)
        self.startEingabe.setObjectName("startEingabe")
        self.horizontalLayout_2.addWidget(self.startEingabe)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.zielEingabe = QtGui.QLineEdit(Form)
        self.zielEingabe.setObjectName("zielEingabe")
        self.horizontalLayout_3.addWidget(self.zielEingabe)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.ausgabe = QtGui.QPlainTextEdit(Form)
        self.ausgabe.setEnabled(True)
        self.ausgabe.setReadOnly(True)
        self.ausgabe.setObjectName("ausgabe")
        self.verticalLayout.addWidget(self.ausgabe)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.submitButton = QtGui.QPushButton(Form)
        self.submitButton.setObjectName("submitButton")
        self.horizontalLayout.addWidget(self.submitButton)
        self.resetButton = QtGui.QPushButton(Form)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout.addWidget(self.resetButton)
        self.closeButton = QtGui.QPushButton(Form)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.berechnungStatus = QtGui.QLabel(Form)
        self.berechnungStatus.setObjectName("berechnungStatus")
        self.verticalLayout.addWidget(self.berechnungStatus)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL("clicked()"), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Google Navigation", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Start: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Ziel:   ", None, QtGui.QApplication.UnicodeUTF8))
        self.submitButton.setText(QtGui.QApplication.translate("Form", "submit", None, QtGui.QApplication.UnicodeUTF8))
        self.resetButton.setText(QtGui.QApplication.translate("Form", "reset", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("Form", "close", None, QtGui.QApplication.UnicodeUTF8))
        self.berechnungStatus.setText(QtGui.QApplication.translate("Form", "Berechnung: ", None, QtGui.QApplication.UnicodeUTF8))

