from PySide.QtGui import QMainWindow

from src.MyModel import MyModel
from src.output import Ui_MainWindow


class controller(QMainWindow):
    def __init__(self):
        super(controller, self).__init__()
        self.view = Ui_MainWindow()
        self.view.setupUi(self)

        self.view.sendData.clicked.connect(self.buttonClick)

    def buttonClick(self):
        self.model = MyModel(self.view.startEingabe.text(),self.view.EndEingabe.text())

        self.view.output.setText(self.model.jsonToText(self.model.getJson()))