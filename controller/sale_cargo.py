from PyQt5 import QtCore
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QDialog, QTableWidget, QMessageBox, QTableWidgetItem

from controller.choose_cargo import ChooseCargoDialog
from controller.choose_custom import ChooseCustomDialog
from ui.sale_cargo import Ui_SaleDialog

import datetime


class SaleCargoDialog(QDialog, Ui_SaleDialog):
    def __init__(self, parent):
        super(SaleCargoDialog, self).__init__(parent)
        self.setupUi(self)

        double_val = QDoubleValidator(self)
        double_val.setBottom(0)
        double_val.setDecimals(2)
        self.needPayEdit.setValidator(double_val)
        self.payEdit.setValidator(double_val)

        self.oweEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.saleListTable.setEditTriggers(QTableWidget.NoEditTriggers)

        self.dateEdit.setDate(datetime.date.today())

        self.needPayEdit.textChanged.connect(self.cal_owe)
        self.payEdit.textChanged.connect(self.cal_owe)
        self.chooseCustomBtn.clicked.connect(self.choose_custom_btn_on_click)
        self.addCargoBtn.clicked.connect(self.add_cargo_btn_on_click)

        self.custom = None
        self.sale_dict = {}

    def get_result(self):
        return self.custom, self.sale_dict, \
               int(float(self.needPayEdit.text()) * 100), \
               int(float(self.payEdit.text()) * 100), \
               int(float(self.oweEdit.text()) * 100), \
               self.dateEdit.date().getDate(), \
               self.commentEdit.text()

    def cal_owe(self):
        need_pay = self.needPayEdit.text()
        pay = self.payEdit.text()
        owe = float(need_pay if need_pay else 0) - float(pay if pay else 0)
        self.oweEdit.setText(str(owe))

    def choose_custom_btn_on_click(self):
        choose_custom_dialog = ChooseCustomDialog(self)
        if choose_custom_dialog.exec_():
            custom = choose_custom_dialog.get_result()
            if custom:
                self.customNameLabel.setText(custom.name)
                self.custom = custom
            else:
                QMessageBox.warning(self, "参数错误", "参数错误：未选中有效客户", QMessageBox.Yes)
                self.customNameLabel.setText("未选择")

    def add_cargo_btn_on_click(self):
        choose_cargo_dialog = ChooseCargoDialog(self)
        if choose_cargo_dialog.exec_():
            cargo, count = choose_cargo_dialog.get_result()
            if cargo is None or count == 0:
                return

            if cargo in self.sale_dict:
                total = self.sale_dict[cargo] + count
                if total > cargo.count:
                    QMessageBox.warning(self, "添加失败", "添加失败：超过最大库存 %d" % cargo.count, QMessageBox.Yes)
                else:
                    self.sale_dict[cargo] += count
            else:
                self.sale_dict[cargo] = count

            self.draw_sale_list_table()

    def draw_sale_list_table(self):
        self.saleListTable.clearContents()
        self.saleListTable.setRowCount(0)

        need_pay = 0
        for cargo, count in self.sale_dict.items():
            now_row = self.saleListTable.rowCount()
            ct = cargo.cargo_type
            self.saleListTable.setRowCount(now_row + 1)

            self.saleListTable.setItem(now_row, 0, QTableWidgetItem(ct.name))
            self.saleListTable.setItem(now_row, 1, QTableWidgetItem(ct.unit))
            self.saleListTable.setItem(now_row, 2, QTableWidgetItem("%d" % count))
            self.saleListTable.setItem(now_row, 3, QTableWidgetItem(str(cargo.production_date)))
            self.saleListTable.setItem(now_row, 4, QTableWidgetItem("%d天" % ct.life))
            self.saleListTable.setItem(now_row, 5, QTableWidgetItem("%.2f元" % (float(ct.price) / 100)))

            need_pay += count * ct.price
        self.needPayEdit.setText("%.2f" % (float(need_pay) / 100))
