#!/bin/python3.5
# -*- coding: utf-8 -*-
"""
Autor: Maximilian Müller
Aufgabe: A05
Datei: GoogleNavController.py
Bescheibung:
Der Controller stellt dem View die Daten bereit, die das Model zurückliefert.
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from GoogleNavView import Ui_MainWindow
from GoogleNavModel import GoogleNavModel


class GoogleNavController(QMainWindow):
    def __init__(self):
        """
        initializes the UI and connects to the Model
        """
        QMainWindow.__init__(self)
        # initialisieren der UI
        self.view = Ui_MainWindow()
        self.model = GoogleNavModel()
        self.view.setupUi(self)
        self.view.label_Status.setText("OK")

        # connecting buttons to core functions
        self.view.button_submit.clicked.connect(self.submit)
        self.view.button_submit.pressed.connect(self.calc)
        self.view.button_reset.pressed.connect(self.reset)

    def reset(self):
        """
        resets all fields
        :return:
        """
        self.view.line_dest.setText("")
        self.view.line_start.setText("")
        self.view.textedit_output.setText("")
        self.view.label_Status.setText("OK")

    def calc(self):
        """
        Sets Status Text to "Calculating"
        :return:
        """
        self.view.label_Status.setText("Calculating")

    def submit(self):
        """
        Requests the route from the model and displays it to the view.
        :return:
        """
        self.model.set_source(self.view.line_start.text())
        self.model.set_destination(self.view.line_dest.text())
        status, answer = self.model.get_directions()
        self.view.textedit_output.setText(answer)
        self.view.label_Status.setText(status)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = GoogleNavController()
    main_window.show()
    sys.exit(app.exec_())
