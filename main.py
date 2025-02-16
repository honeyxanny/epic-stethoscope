from PySide6.QtWidgets import QApplication
from window import MainWindow

app = QApplication()
window = MainWindow()
window.run()
app.exec()