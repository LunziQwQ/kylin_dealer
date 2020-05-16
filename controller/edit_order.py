from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QDialog
from ui.edit_order import Ui_EditOrder


class EditOrderDialog(QDialog, Ui_EditOrder):
    def __init__(self, parent, order):
        super(EditOrderDialog, self).__init__(parent)
        self.setupUi(self)

        double_val = QDoubleValidator(self)
        double_val.setBottom(0)
        double_val.setDecimals(2)
        self.totalMoneyEdit.setValidator(double_val)
        self.payMoneyEdit.setValidator(double_val)
        self.oweMoneyEdit.setValidator(double_val)

        self.setWindowTitle("修改订单信息")
        self.customNameLabel.setText(order.custom.name)
        self.totalMoneyEdit.setText("%.2f" % (float(order.need_pay) / 100))
        self.payMoneyEdit.setText("%.2f" % (float(order.now_pay) / 100))
        self.oweMoneyEdit.setText("%.2f" % (float(order.owe_money) / 100))

        self.totalMoneyEdit.textChanged.connect(self.edit_total_money)
        self.payMoneyEdit.textChanged.connect(self.edit_pay_money)
        self.oweMoneyEdit.textChanged.connect(self.edit_owe_money)

    def get_result(self):
        return self.totalMoneyEdit.text(), self.payMoneyEdit.text(), self.oweMoneyEdit.text()

    def edit_total_money(self):
        cur_index = self.totalMoneyEdit.cursorPosition()
        self.cal_owe()
        self.totalMoneyEdit.setCursorPosition(cur_index)

    def edit_pay_money(self):
        cur_index = self.payMoneyEdit.cursorPosition()
        self.cal_owe()
        self.payMoneyEdit.setCursorPosition(cur_index)

    def edit_owe_money(self):
        cur_index = self.oweMoneyEdit.cursorPosition()
        self.cal_pay()
        self.oweMoneyEdit.setCursorPosition(cur_index)

    # 更新欠款金额
    def cal_owe(self):
        need_pay = int(float(self.totalMoneyEdit.text()) * 100) if self.totalMoneyEdit.text() else 0
        pay = int(float(self.payMoneyEdit.text()) * 100) if self.payMoneyEdit.text() else 0
        owe = need_pay - pay
        self.oweMoneyEdit.setText(str(float(owe) / 100))

    # 更新已付金额
    def cal_pay(self):
        need_pay = int(float(self.totalMoneyEdit.text()) * 100) if self.totalMoneyEdit.text() else 0
        owe = int(float(self.oweMoneyEdit.text()) * 100) if self.oweMoneyEdit.text() else 0
        pay = need_pay - owe
        self.payMoneyEdit.setText(str(float(pay) / 100))
