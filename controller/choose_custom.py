from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QTableWidget, QHeaderView

from services.custom import CustomService
from ui.choose_custom import Ui_ChooseCustom


class ChooseCustomDialog(QDialog, Ui_ChooseCustom):
    def __init__(self, parent):
        super(ChooseCustomDialog, self).__init__(parent)
        self.setupUi(self)

        self.customListTable.setEditTriggers(QTableWidget.NoEditTriggers)

        self.searchEdit.textChanged.connect(self.search_edit_changed)
        self.customListTable.cellClicked.connect(self.customListTable.selectRow)

        self.customListTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.customListTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.customListTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.customListTable.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.customListTable.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.customListTable.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)

        self.custom_list = []
        self.exec()

    def exec(self, search_text=None):
        self.custom_list = CustomService.get_custom_list(search_text)
        CustomService.draw_custom_list_table(self.customListTable, self.custom_list)
        if len(self.custom_list) > 0:
            self.customListTable.selectRow(0)

    def search_edit_changed(self):
        search_text = self.searchEdit.text()
        self.exec(search_text=search_text)

    def get_result(self):
        now_row = self.customListTable.currentRow()
        if self.custom_list and now_row < len(self.custom_list):
            return self.custom_list[now_row]
        else:
            return None
