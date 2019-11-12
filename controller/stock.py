from PyQt5.QtWidgets import QMainWindow, QHeaderView, QApplication, QTableWidgetItem, QMessageBox

from controller.add_cargo_type import AddCargoTypeDialog
from ui.add_cargo_type import Ui_AddCargoType
from ui.stock import Ui_StockWindow
from models.cargo_type import CargoType


class StockController(QMainWindow, Ui_StockWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_StockWindow.__init__(self)
        self.setupUi(self)

        self.saleBtn.clicked.connect(self.sale_btn_on_click)
        self.buyBtn.clicked.connect(self.buy_btn_on_click)
        self.nextPageBtn.clicked.connect(self.next_page_btn_on_click)
        self.lastPageBtn.clicked.connect(self.last_page_btn_on_click)
        self.addCargoTypeBtn.clicked.connect(self.add_cargo_type_btn_on_click)

        self.pageSizeEdit.textChanged.connect(self.page_size_edit_text_change)

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

        self.pageSizeEdit.setText(str(self.page_size))

    def exec(self):
        ct_list = self.get_cargo_type_list(self.now_page)
        if ct_list is not None:
            self.draw_cargo_type_table(ct_list)

    def add_cargo_type_btn_on_click(self):
        add_dialog = AddCargoTypeDialog(self)
        if add_dialog.exec_():
            name, unit, life, price = add_dialog.get_result()
            if not name:
                reply = QMessageBox.warning(self, "参数错误", "参数错误：添加的货物种类必须填写名字", QMessageBox.Yes)
            else:
                new_cargo_type = CargoType.create(name, unit, life, price)
                try:
                    new_cargo_type.save()
                except Exception:
                    reply = QMessageBox.warning(self, "添加失败", "添加失败：可能是您的货物种类名称重复", QMessageBox.Yes)
                self.exec()

    def sale_btn_on_click(self):
        pass

    def buy_btn_on_click(self):
        pass

    def next_page_btn_on_click(self):
        ct_list = self.get_cargo_type_list(self.now_page + 1)
        if ct_list is not None:
            self.draw_cargo_type_table(ct_list)
            self.pageLabel.setText(str(self.now_page))

    def last_page_btn_on_click(self):
        if self.now_page > 1:
            ct_list = self.get_cargo_type_list(self.now_page - 1)
            self.draw_cargo_type_table(ct_list)
            self.pageLabel.setText(str(self.now_page))

    def page_size_edit_text_change(self):
        try:
            new_page_size = int(self.pageSizeEdit.text())
            self.page_size = new_page_size
            self.exec()
        except Exception:
            self.pageSizeEdit.setText(str(self.page_size))

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
        self.cargoTypeListTable.setRowCount(0)
        for ct in ct_list:
            now_row = self.cargoTypeListTable.rowCount()
            self.cargoTypeListTable.setRowCount(now_row + 1)

            self.cargoTypeListTable.setItem(now_row, 0, QTableWidgetItem(ct.name))
            self.cargoTypeListTable.setItem(now_row, 1, QTableWidgetItem(ct.unit))
            self.cargoTypeListTable.setItem(now_row, 2, QTableWidgetItem("%d" % ct.count))
            self.cargoTypeListTable.setItem(now_row, 3, QTableWidgetItem("%d天" % ct.life))
            self.cargoTypeListTable.setItem(now_row, 4, QTableWidgetItem("%.2f元" % (float(ct.price) / 100)))
