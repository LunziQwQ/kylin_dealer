from PyQt5.QtWidgets import QMainWindow, QTableWidget, QHeaderView, QMessageBox

from controller.edit_order import EditOrderDialog
from services.order import OrderService
from ui.order import Ui_OrderWindow


class OrderController(QMainWindow, Ui_OrderWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_OrderWindow.__init__(self)
        self.setupUi(self)

        self.orderListTable.setEditTriggers(QTableWidget.NoEditTriggers)
        self.saleItemListTable.setEditTriggers(QTableWidget.NoEditTriggers)

        self.editBtn.clicked.connect(self.edit_btn_on_click)
        self.orderListTable.cellClicked.connect(self.order_list_table_on_click)
        self.saleItemListTable.cellClicked.connect(self.saleItemListTable.selectRow)
        self.sortComboBox.currentIndexChanged.connect(self.sort_combo_box_change)

        # unused str params
        self.searchBtn.clicked.connect(self.exec)
        self.searchEdit.textChanged.connect(self.search_edit_change)

        self.orderListTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.orderListTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.orderListTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.orderListTable.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.orderListTable.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)

        self.saleItemListTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.saleItemListTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.saleItemListTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.saleItemListTable.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.saleItemListTable.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.saleItemListTable.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)

        self.order_list = []
        self.total_money, self.total_owe = OrderService.get_total_money()

    def exec(self,  selected_row=0):
        self.totalMoneyLabel.setText("%.2f元" % (float(self.total_money) / 100))
        self.totalOweLabel.setText("%.2f元" % (float(self.total_owe) / 100))

        self.order_list = OrderService.get_order_list(self.sortComboBox.currentText(), self.searchEdit.text())
        OrderService.draw_order_list_table(self.orderListTable, self.order_list)
        if len(self.order_list) > 0:
            self.orderListTable.selectRow(selected_row)
            self.order_list_table_on_click(row=selected_row, column=0)
        else:
            self.saleItemListTable.clearContents()
            self.saleItemListTable.setRowCount(0)

    def order_list_table_on_click(self, row, column):
        self.orderListTable.selectRow(row)
        order = self.order_list[row]

        OrderService.draw_order_sale_item_table(self.saleItemListTable, order)

    def search_edit_change(self, text):
        if len(text) == 0:
            self.exec()

    def edit_btn_on_click(self):
        if self.orderListTable.rowCount() == 0:
            QMessageBox.warning(self, "编辑订单失败", "选中一条订单才可修改", QMessageBox.Yes)
            return
        now_row = self.orderListTable.currentRow()
        order = self.order_list[now_row]
        edit_dialog = EditOrderDialog(self, order)

        if edit_dialog.exec_():
            total, pay, owe = edit_dialog.get_result()

            total_change = int(float(total) * 100) - order.need_pay
            owe_change = int(float(owe) * 100) - order.owe_money
            self.total_money += total_change
            self.total_owe += owe_change
            order.need_pay = int(float(total) * 100)
            order.now_pay = int(float(pay) * 100)
            order.owe_money = int(float(owe) * 100)
            order.save()

            custom = order.custom
            custom.trade_money += total_change
            custom.owe_money += owe_change
            custom.save()
            self.exec(selected_row=now_row)

    def sort_combo_box_change(self):
        self.exec()
