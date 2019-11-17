from PyQt5 import QtCore
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QDialog, QTableWidget, QMessageBox

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
        self.cargoListTable.setEditTriggers(QTableWidget.NoEditTriggers)

        self.dateEdit.setDate(datetime.date.today())

        self.needPayEdit.textChanged.connect(self.cal_owe)
        self.payEdit.textChanged.connect(self.cal_owe)
        self.chooseCustomBtn.clicked.connect(self.choose_custom_btn_on_click)
        self.addCargoBtn.clicked.connect(self.add_cargo_btn_on_click)

        self.custom = None

    def get_result(self):
        return self.nameEdit.text(), self.phoneEdit.text(), self.addrEdit.toPlainText(), self.commentEdit.toPlainText()

    def cal_owe(self):
        need_pay = self.needPayEdit.text()
        pay = self.payEdit.text()
        owe = int(need_pay if need_pay else 0) - int(pay if pay else 0)
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
        pass
