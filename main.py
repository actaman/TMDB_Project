

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
from GUI import *

import sqlite3


if __name__ == "__main__":
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    def page_sign():
        ui.stackedWidget.setCurrentIndex(0)
    ui.to_login.clicked.connect(page_sign)

    def page_log():
        ui.stackedWidget.setCurrentIndex(1)

    ui.to_register.clicked.connect(page_log)









    sys.exit(app.exec_())