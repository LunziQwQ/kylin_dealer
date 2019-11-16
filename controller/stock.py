import datetime
import time

from PyQt5.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QMessageBox, QTableWidget

from controller.add_cargo_type import AddCargoTypeDialog
from controller.edit_cargo import EditCargoDialog
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
        ct_list = self.get_cargo_type_list(self.now_page, self.page_size)
        self.draw_cargo_type_table(ct_list)
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
                self.add_cargo(new_cargo)
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "添加进货失败", "添加进货信息失败", QMessageBox.Yes)
            self.exec(ct_now_row)

    def cargo_type_table_on_click(self, row, column):
        self.cargoTypeListTable.selectRow(row)
        ct_name = self.cargoTypeListTable.item(row, 0).text()
        ct_unit = self.cargoTypeListTable.item(row, 1).text()

        self.draw_cargo_table(self.get_cargo_list(ct_name), ct_unit)

    def next_page_btn_on_click(self):
        ct_list = self.get_cargo_type_list(self.now_page + 1, self.page_size)
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

    def draw_cargo_type_table(self, ct_list):
        self.ct_list = ct_list
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

    def draw_cargo_table(self, cargo_list, unit):
        self.cargo_list = cargo_list
        self.cargoListTable.clearContents()
        self.cargoListTable.setRowCount(0)

        for cargo in cargo_list:
            now_row = self.cargoListTable.rowCount()
            self.cargoListTable.setRowCount(now_row + 1)

            self.cargoListTable.setItem(now_row, 0, QTableWidgetItem(str(cargo.production_date)))
            self.cargoListTable.setItem(now_row, 1, QTableWidgetItem("%d%s" % (cargo.count, unit)))
            self.cargoListTable.setItem(now_row, 2, QTableWidgetItem(cargo.comment))

    def get_cargo_type_list(self, page, page_size):
        results = CargoType.select().order_by(CargoType.name).paginate(int(page), int(page_size))
        if results.count() > 0:
            results = [i for i in results]
            return results
        else:
            return []

    # ----------- Service ---------------

    def get_cargo_list(self, ct_name):
        results = CargoType.get(CargoType.name == ct_name).cargo_list.order_by(Cargo.production_date)
        if results.count() > 0:
            results = [i for i in results]
            return results
        else:
            return []

    def add_cargo(self, cargo):
        cargo_type = cargo.cargo_type
        cargo_type.count += cargo.count
        cargo_type.save()
        for old_cargo in cargo_type.cargo_list:
            if old_cargo.production_date == cargo.production_date:
                old_cargo.count += cargo.count
                old_cargo.save()
                return
        cargo.save()
