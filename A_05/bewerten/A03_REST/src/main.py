import sys
from PySide.QtGui import QApplication

from src.MyCont import controller
from src.MyModel import MyModel

if __name__ == '__main__':

    app = QApplication(sys.argv)

    win = controller()
    win.show()


    app.exec_()
