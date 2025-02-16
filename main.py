from main_ui import Ui_MainWindow
from PySide6 import QtWidgets

app = QtWidgets.QApplication()
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

app.exec()