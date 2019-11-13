from PyQt5.QtWidgets import QMainWindow, QApplication

from controller.setting import SettingController
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
        self.setting_window = None

        self.stockBtn.clicked.connect(self.stock_btn_on_click)
        self.orderBtn.clicked.connect(self.order_btn_on_click)
        self.customBtn.clicked.connect(self.custom_btn_on_click)
        self.settingBtn.clicked.connect(self.setting_btn_on_click)

    def stock_btn_on_click(self):
        self.stock_window = StockController()
        self.stock_window.show()
        QApplication.processEvents()
        self.stock_window.exec()

    def order_btn_on_click(self):
        # self.order_window = OrderController()
        # self.order_window.show()
        # QApplication.processEvents()
        # self.order_window.exec()
        pass


    def custom_btn_on_click(self):
        # self.custom_window = CustomController()
        # self.custom_window.show()
        # QApplication.processEvents()
        # self.custom_window.exec()
        pass


    def setting_btn_on_click(self):
        # self.setting_window = SettingController()
        # self.setting_window.show()
        # QApplication.processEvents()
        # self.setting_window.exec()
        pass
