from PyQt5.QtWidgets import QMainWindow
from ui.main import Ui_MainWindow


class OrderController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    def exec(self):
        pass
