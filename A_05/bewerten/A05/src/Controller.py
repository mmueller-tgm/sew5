import View
import Model
import sys

from PySide.QtGui import *


class Controller:
    """
        The controller handels the input and the click event of the buttons
    """

    def __init__(self):
        """
            The controller handels the input and the click event of the buttons
            :var view: MainWindow for the gui
            :var model: Model object for calling the google api
        """
        self.app = QApplication(sys.argv)
        self.window = MainWindow()
        self.view = View.Ui_MainWindow()
        self.view.setupUi(self.window)

        self.model = Model.Model()

        self.view.submitButton.clicked.connect(lambda: self.submit())
        self.view.resetButton.clicked.connect(lambda: self.reset())
        self.view.jsonButton.clicked.connect(lambda: self.model.setformat("json"))
        self.view.xmlButton.clicked.connect(lambda: self.model.setformat("xml"))

        self.view.start.setText("Mistelbach, Niederösterreich")
        self.view.ziel.setText("Wexstraße, Wien")
        self.view.statusbar.setText("Warten auf Eingaben")

        sys.exit(self.app.exec_())

    def submit(self):
        """
        submit is called, when the submit button is pressed, takes the input from origin and destination and gives these
        parameter the model class to call the api
        :return: None
        """
        start = self.view.start.text()
        ziel = self.view.ziel.text()

        if self.model.format == "json":
            text = self.model.requestJson(start, ziel)
        else:
            text = self.model.requestXml(start, ziel)

        if text == "Fehler aufgetreten":
            self.view.statusbar.setText(text)
            self.view.textBrowser.setText("")
        else:
            if len(text) == 0:
                self.view.textBrowser.setText("Keinen Weg gefunden")
                self.view.statusbar.setText("Berechnung ok")
            else:
                self.view.textBrowser.setText(text)
                self.view.statusbar.setText("Berechnung ok")

    def reset(self):
        """
        reset is called, when the reset button is pressed, clears the input fields
        :return: None
        """
        self.view.start.setText("")
        self.view.ziel.setText("")
        self.view.textBrowser.setText("")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
       super(MainWindow, self).__init__(parent)
       self.show()

if __name__ == "__main__":
    Controller()
