from PyQt5.QtWidgets import QMainWindow, QApplication

from controller.office_exp import OfficeExpController
from controller.custom import CustomController
from controller.order import OrderController
from controller.stock import StockController
from ui.main import Ui_MainWindow


class MainController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.stock_window = None
        self.order_window = None
        self.custom_window = None
        self.office_ext_window = None

        self.stockBtn.clicked.connect(self.stock_btn_on_click)
        self.orderBtn.clicked.connect(self.order_btn_on_click)
        self.customBtn.clicked.connect(self.custom_btn_on_click)
        self.officeExpBtn.clicked.connect(self.office_exp_btn_on_click)

    def stock_btn_on_click(self):
        self.stock_window = StockController()
        self.stock_window.show()
        QApplication.processEvents()
        self.stock_window.exec()

    def order_btn_on_click(self):
        self.order_window = OrderController()
        self.order_window.show()
        QApplication.processEvents()
        self.order_window.exec()

    def custom_btn_on_click(self):
        self.custom_window = CustomController()
        self.custom_window.show()
        QApplication.processEvents()
        self.custom_window.exec()

    def office_exp_btn_on_click(self):
        self.office_ext_window = OfficeExpController()
        self.office_ext_window.show()
        QApplication.processEvents()
        self.office_ext_window.exec()
