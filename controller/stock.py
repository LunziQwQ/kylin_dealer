from PyQt5.QtWidgets import QMainWindow, QHeaderView, QApplication, QTableWidgetItem
from ui.stock import Ui_StockWindow
from models.cargo_type import CargoType


class StockController(QMainWindow, Ui_StockWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_StockWindow.__init__(self)
        self.setupUi(self)

        self.saleBtn.clicked.connect(self.sale_btn_on_click)
        self.buyBtn.clicked.connect(self.buy_btn_on_click)

        self.cargoTypeListTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.cargoTypeListTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.cargoTypeListTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.cargoTypeListTable.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.cargoTypeListTable.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)

        self.cargoListTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.cargoListTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.cargoListTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

        self.page_size = 10
        self.now_page = 1

    def exec(self):
        ct_list = self.get_cargo_type_list(self.now_page)
        if ct_list is not None:
            self.draw_cargo_type_table(ct_list)

    def sale_btn_on_click(self):
        pass

    def buy_btn_on_click(self):
        pass

    def get_cargo_type_list(self, page):
        results = CargoType.select().order_by(CargoType.name).paginate(int(page), int(self.page_size))
        if results.count() > 0:
            self.now_page = page
            results = [i for i in results]
            return results
        else:
            return None

    def draw_cargo_type_table(self, ct_list):
        self.cargoTypeListTable.clearContents()
        for ct in ct_list:
            now_row = self.cargoTypeListTable.rowCount()
            self.cargoTypeListTable.setRowCount(now_row + 1)

            self.cargoTypeListTable.setItem(now_row, 0, QTableWidgetItem(ct.name))
            self.cargoTypeListTable.setItem(now_row, 1, QTableWidgetItem(ct.unit))
            self.cargoTypeListTable.setItem(now_row, 2, QTableWidgetItem("%d" % ct.count))
            self.cargoTypeListTable.setItem(now_row, 3, QTableWidgetItem("%d天" % ct.life))
            self.cargoTypeListTable.setItem(now_row, 4, QTableWidgetItem("%.2f元" % (float(ct.price) / 100)))

        QApplication.processEvents()
