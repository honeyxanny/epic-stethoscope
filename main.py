from PySide6.QtWidgets import QApplication
from window import MainWindow
from audio import AudioProcessor

app = QApplication()
window = MainWindow(AudioProcessor())
window.run()
app.exec()