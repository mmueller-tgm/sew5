from PyQt5.QtWidgets import QMainWindow
from model import Model
from view import Ui_MainWindow


class Controller(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.model = Model()
        self.view = Ui_MainWindow()

