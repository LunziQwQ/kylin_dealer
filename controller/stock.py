import datetime
import time

from PyQt5.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QMessageBox, QTableWidget

from controller.add_cargo_type import AddCargoTypeDialog
from controller.edit_cargo import EditCargoDialog
from controller.sale_cargo import SaleCargoDialog
from models.order import Order
from services.cargo import CargoService
from services.cargo_type import CargoTypeService
from services.custom import CustomService
from ui.stock import Ui_StockWindow

from models.cargo_type import CargoType
from models.cargo import Cargo


class StockController(QMainWindow, Ui_StockWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_StockWindow.__init__(self)
        self.setupUi(self)

        self.cargoTypeListTable.setEditTriggers(QTableWidget.NoEditTriggers)
        self.cargoListTable.setEditTriggers(QTableWidget.NoEditTriggers)

        self.cargoTypeListTable.cellClicked.connect(self.cargo_type_table_on_click)
        self.cargoListTable.cellClicked.connect(self.cargoListTable.selectRow)

        self.editBtn.clicked.connect(self.edit_btn_on_click)
        self.buyBtn.clicked.connect(self.buy_btn_on_click)
        self.saleBtn.clicked.connect(self.sale_btn_on_click)
        self.nextPageBtn.clicked.connect(self.next_page_btn_on_click)
        self.lastPageBtn.clicked.connect(self.last_page_btn_on_click)
        self.addCargoTypeBtn.clicked.connect(self.add_cargo_type_btn_on_click)
        self.delCargoTypeBtn.clicked.connect(self.del_cargo_type_btn_on_click)

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

        self.ct_list = []
        self.cargo_list = []

    def exec(self, selected_row=0):
        self.ct_list = CargoTypeService.get_cargo_type_list_by_page(self.now_page, self.page_size)
        CargoTypeService.draw_cargo_type_table(self.cargoTypeListTable, self.ct_list)
        if len(self.ct_list) > 0:
            self.cargoTypeListTable.selectRow(selected_row)
            self.cargo_type_table_on_click(row=selected_row, column=0)
        else:
            self.cargoListTable.clearContents()
            self.cargoListTable.setRowCount(0)

    def add_cargo_type_btn_on_click(self):
        add_dialog = AddCargoTypeDialog(self)
        if add_dialog.exec_():
            name, unit, life, price = add_dialog.get_result()
            if not name:
                QMessageBox.warning(self, "参数错误", "参数错误：添加的货物种类必须填写名字", QMessageBox.Yes)
            else:
                new_cargo_type = CargoType.build(name, unit, life, price)
                try:
                    new_cargo_type.save()
                except Exception:
                    QMessageBox.warning(self, "添加失败", "添加失败：可能是您的货物种类名称重复", QMessageBox.Yes)
                self.exec()

    def del_cargo_type_btn_on_click(self):
        if self.cargoTypeListTable.rowCount() == 0:
            QMessageBox.warning(self, "删除失败", "选中一条货物种类才可删除", QMessageBox.Yes)
            return

        ct_now_row = self.cargoTypeListTable.currentRow()
        cargo_type = self.ct_list[ct_now_row]
        reply = QMessageBox.warning(self, "删除货物种类", "您确定要删除%s吗" % cargo_type.name, QMessageBox.Yes | QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            cargo_type.delete_instance()
            self.ct_list.remove(cargo_type)
            self.exec()

    def edit_btn_on_click(self):
        ct_now_row = self.cargoTypeListTable.currentRow()
        cargo_type = self.ct_list[ct_now_row]

        if self.cargoListTable.rowCount() == 0:
            QMessageBox.warning(self, "编辑货物失败", "选中一条货物才可修改", QMessageBox.Yes)
            return

        cargo_now_row = self.cargoListTable.currentRow()
        cargo = self.cargo_list[cargo_now_row]
        old_count = cargo.count
        edit_dialog = EditCargoDialog(self, cargo_type, cargo)
        if edit_dialog.exec_():
            production_date, count, comment = edit_dialog.get_result()
            count_change = int(count) - old_count
            if int(count) == 0:
                ex = cargo.delete_instance()
            else:
                cargo.comment = comment
                cargo.production_date = datetime.date(*production_date)
                cargo.count = int(count)
                cargo.save()

            cargo_type.count += count_change
            cargo_type.save()
            self.exec(ct_now_row)

    def buy_btn_on_click(self):
        ct_now_row = self.cargoTypeListTable.currentRow()
        cargo_type = self.ct_list[ct_now_row]

        buy_dialog = EditCargoDialog(self, cargo_type)
        if buy_dialog.exec_():
            production_date, count, comment = buy_dialog.get_result()
            new_cargo = Cargo.build(cargo_type, production_date, count,
                                    comment)
            try:
                CargoService.add_cargo(new_cargo)
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "添加进货失败", "添加进货信息失败", QMessageBox.Yes)
            self.exec(ct_now_row)

    def sale_btn_on_click(self):
        sale_dialog = SaleCargoDialog(self)
        if sale_dialog.exec_():
            custom, sale_dict, need_pay, now_pay, owe, date, comment = sale_dialog.get_result()
            if not custom:
                QMessageBox.warning(self, "出货失败", "必须选择一个客户", QMessageBox.Yes)
                return
            order = Order.build(custom, sale_dict, need_pay, now_pay, owe, date, comment)
            order.save()
            CargoService.sale_cargoes(sale_dict)
            CustomService.sale_cargo_for_custom(custom, need_pay, owe)
            QMessageBox.information(self, "出货成功", "出货成功：可在订单管理中查询", QMessageBox.Yes)

    def cargo_type_table_on_click(self, row, column):
        self.cargoTypeListTable.selectRow(row)
        ct_name = self.cargoTypeListTable.item(row, 0).text()

        self.cargo_list = CargoService.get_cargo_list_by_ct_name(ct_name)
        CargoService.draw_cargo_table(self.cargoListTable, self.cargo_list)

    def next_page_btn_on_click(self):
        ct_list = CargoTypeService.get_cargo_type_list_by_page(self.now_page + 1, self.page_size)
        if ct_list is not None:
            self.now_page += 1
            self.exec()

    def last_page_btn_on_click(self):
        if self.now_page > 1:
            self.now_page -= 1
            self.exec()

    def page_size_edit_text_change(self):
        try:
            new_page_size = int(self.pageSizeEdit.text())
            self.page_size = new_page_size
            self.exec()
        except Exception:
            self.pageSizeEdit.setText(str(self.page_size))
