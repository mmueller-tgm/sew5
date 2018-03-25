"""
@author: 
@date: 18-10-2017
@use: Controller that connects the class that handles the requests with the view
"""
import sys
from PyQt5 import QtGui, QWidgets
import A05_View
import A05_RequestHandler


class A05Controller(QtGui.QMainWindow):
    """
    Controller of the application
    """

    def __init__(self):
        """
        The constructor that just sets up the GUI and initializes the request handler.
        """
        super(A05Controller, self).__init__()

        self.__myForm = A05_View.Ui_A05_GUI()
        self.__myForm.setupUi(self)
        self.__myRequestHandler = A05_RequestHandler.A05RequestHandler()

        self.__myForm.submit.clicked.connect(self.generate_request)

    def generate_request(self):
        """
        This method is called when the 'submit' button is clicked.
        It take the input texts and the request method.
        Then it calls the requestHandler and puts the returned value in the display screen.

        :return: None
        """
        selection = str(self.__myForm.selection.currentText())
        origin = str(self.__myForm.input_origin.text())
        destination = str(self.__myForm.input_destination.text())

        if selection == "JSON":
            output = self.__myRequestHandler.handle_request(origin, destination, True)
        else:
            output = self.__myRequestHandler.handle_request(origin, destination, False)

        self.__myForm.output_display.clear()
        self.__myForm.output_display.setText(output[0])
        self.__myForm.status.setText("Status " + output[1])

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    c = A05Controller()
    c.show()
    sys.exit(app.exec_())
