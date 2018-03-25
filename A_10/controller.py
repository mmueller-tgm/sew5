from model import RESTModel
from view import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import json


class LanguageDetectorController(QMainWindow):
    """
        The Controller combining the GUI and the model.
    """

    def __init__(self):
        """
            Initialization of the UI and the REST Client
        """
        super().__init__()
        self.view = Ui_MainWindow()
        self.model = RESTModel()
        self.view.setupUi(self)
        self.view.button_submit.released.connect(self.submit)
        self.view.button_reset.released.connect(self.clear)

    def clear(self):
        """
            Clears input and output fields
        """
        self.view.text_input.clear()
        self.view.text_output.clear()

    def submit(self):
        """
            Sets the address and port for the REST Client form the
            input fields, makes an request according to the input data
            and sets the output field.
        """
        self.model.set_addr(self.view.line_addr.text())
        self.model.set_port(self.view.line_port.text())
        resp = json.loads(self.model.get(self.view.text_input.toPlainText()))

        text = "reliable: <b>%s</b> <br> " \
               "language: <b>%s</b> <br> " \
               "probability: <b>%s</b>" % (resp['reliable'],
                                           resp['language'], resp['prob'])

        self.view.text_output.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = LanguageDetectorController()
    main_window.show()
    sys.exit(app.exec_())
