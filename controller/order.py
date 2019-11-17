from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QHeaderView

from services.order import OrderService
from ui.order import Ui_OrderWindow


class OrderController(QMainWindow, Ui_OrderWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_OrderWindow.__init__(self)
        self.setupUi(self)

        int_val = QIntValidator(self)
        int_val.setBottom(1)
        self.pageSizeEdit.setValidator(int_val)

        self.orderListTable.setEditTriggers(QTableWidget.NoEditTriggers)
        self.saleItemListTable.setEditTriggers(QTableWidget.NoEditTriggers)

        self.nextPageBtn.clicked.connect(self.next_page_btn_on_click)
        self.lastPageBtn.clicked.connect(self.last_page_btn_on_click)
        self.orderListTable.cellClicked.connect(self.order_list_table_on_click)
        self.saleItemListTable.cellClicked.connect(self.saleItemListTable.selectRow)
        self.sortComboBox.currentIndexChanged.connect(self.sort_combo_box_change)
        self.pageSizeEdit.textChanged.connect(self.page_size_edit_text_change)

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

        self.page_size = 15
        self.now_page = 1
        self.order_list = []

    def exec(self, selected_row=0):
        self.pageLabel.setText(str(self.now_page))
        self.order_list = OrderService.get_order_list(self.now_page, self.page_size, self.sortComboBox.currentText())
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

    def page_size_edit_text_change(self):
        try:
            new_page_size = int(self.pageSizeEdit.text())
            self.page_size = new_page_size
            self.exec()
        except Exception:
            self.pageSizeEdit.setText(str(self.page_size))

    def next_page_btn_on_click(self):
        order_list = OrderService.get_order_list(self.now_page + 1, self.page_size, self.sortComboBox.currentText())
        if order_list:
            self.now_page += 1
            self.exec()

    def last_page_btn_on_click(self):
        if self.now_page > 1:
            self.now_page -= 1
            self.exec()

    def sort_combo_box_change(self):
        self.exec()
