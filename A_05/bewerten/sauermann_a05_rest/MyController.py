import ctypes
import sys
from MyView import MyView
from MyModel import MyModel
from PySide.QtGui import *
# Quellen:
# http://stackoverflow.com/questions/2963263/how-can-i-create-a-simple-message-box-in-python
# http://stackoverflow.com/questions/5714404/how-to-make-a-qpushbutton-disabled
# http://eli.thegreenplace.net/2011/04/25/passing-extra-arguments-to-pyqt-slot
# http://stackoverflow.com/questions/15080731/call-a-function-when-a-button-is-pressed-pyqt

class MyController(QWidget):
    """ MVC pattern: Creates a controller - mvc pattern.
    """

    def __init__(self, parent=None):
        """ Create a new controller with a object MyView and a object MyModel
        using the mvc pattern.
        :param parent:
        """

        super().__init__(parent)
        self.myForm = MyView()
        self.myForm.setupUi(self)
        self.myModel = MyModel()

        # connect the buttons with the clicked signal
        self.connectButtons()

    def connectButtons(self):
        """
        Connectet alle Buttons mit der Methode die fuer sie bestimmt ist

        :return:
        """
        # Spiele Buttons
        # Siehe Quellen (ganz oben)
        self.myForm.resetButton.clicked.connect(self.resetPressd)
        self.myForm.submitButton.clicked.connect(self.submitPressed)


    def submitPressed(self):
        """
        Wird aufgerufen wenn der Benutzer fuer seine Angaben die passende Route bekommen will
        Ruft alle notwendigen Methoden im Model auf und gibt Entsprechend die Ergebnise auf der GUI aus

        :return:
        """
        self.myForm.ausgabe.setPlainText("")
        startAdresse = self.myForm.startEingabe.text()
        zielAdresse = self.myForm.zielEingabe.text()
        routenPlanung = self.myModel.findWay(startAdresse,zielAdresse)
        berechnungStatus = self.myModel.getStatus()
        if berechnungStatus == "OK":
            self.myForm.berechnungStatus.setText("Berechnung: OK")
            weg = self.myModel.getWay()
            self.myForm.ausgabe.appendHtml(weg)
        else:
            self.myForm.berechnungStatus.setText("Berechnung: ein Fehler ist Aufgetreten")

    def resetPressd(self):
        """
        Leert alle Textfelder welche Informationen enthalten koennten

        :return:
        """
        self.myForm.startEingabe.setText("")
        self.myForm.zielEingabe.setText("")
        self.myForm.ausgabe.setPlainText("")
        self.myForm.berechnungStatus.setText("Berechnung:")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = MyController()
    c.show()
    sys.exit(app.exec_())
