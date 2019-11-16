from PyQt5.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QMessageBox, QTableWidget

from controller.edit_custom import EditCustomDialog
from models.cargo_type import CargoType
from models.custom import Custom
from ui.custom import Ui_CustomWindow


class CustomController(QMainWindow, Ui_CustomWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_CustomWindow.__init__(self)
        self.setupUi(self)

        self.customListTable.setEditTriggers(QTableWidget.NoEditTriggers)

        self.customListTable.cellClicked.connect(self.customListTable.selectRow)

        self.addBtn.clicked.connect(self.add_custom_btn_on_click)
        self.editBtn.clicked.connect(self.edit_custom_btn_on_click)
        self.delBtn.clicked.connect(self.del_custom_btn_on_click)

        self.searchEdit.textChanged.connect(self.serach_edit_changed)

        self.customListTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.customListTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.customListTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.customListTable.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.customListTable.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.customListTable.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)

        self.custom_list = []

    def exec(self, selected_row=0, search_text=None):
        self.get_custom_list(search_text)
        self.draw_custom_list_table()
        if len(self.custom_list) > 0:
            self.customListTable.selectRow(selected_row)
            self.customListTable.selectRow(selected_row)
        else:
            self.customListTable.clearContents()
            self.customListTable.setRowCount(0)

    def get_custom_list(self, search_text=None):
        custom_list = Custom.select()
        if custom_list.count() > 0:
            if not search_text:
                self.custom_list = [i for i in custom_list]
            else:
                self.custom_list = list(filter(lambda c: search_text in c.name \
                                                         or search_text in c.phone \
                                                         or search_text in c.addr \
                                                         or search_text in c.comment, custom_list))

    def add_custom_btn_on_click(self):
        add_dialog = EditCustomDialog(self)
        if add_dialog.exec_():
            name, phone, addr, comment = add_dialog.get_result()
            if not name:
                QMessageBox.warning(self, "参数错误", "参数错误：添加的客户信息必须填写名字", QMessageBox.Yes)
            else:
                new_custom = Custom.build(name, phone, addr, comment)
                try:
                    new_custom.save()
                except Exception:
                    QMessageBox.warning(self, "添加失败", "添加失败：可能是您的客户名称重复", QMessageBox.Yes)
                self.exec()

    def edit_custom_btn_on_click(self):
        if self.customListTable.rowCount() == 0:
            QMessageBox.warning(self, "编辑客户失败", "选中一条客户才可修改", QMessageBox.Yes)
            return
        now_row = self.customListTable.currentRow()
        custom = self.custom_list[now_row]
        edit_dialog = EditCustomDialog(self, custom)

        if edit_dialog.exec_():
            name, phone, addr, comment = edit_dialog.get_result()
            if not name:
                QMessageBox.warning(self, "参数错误", "参数错误：客户信息必须填写名字", QMessageBox.Yes)
            else:
                custom.name = name
                custom.phone = phone
                custom.addr = addr
                custom.comment = comment
                custom.save()
                self.exec(now_row)

    def serach_edit_changed(self):
        search_text = self.searchEdit.text()
        self.exec(search_text=search_text)

    def del_custom_btn_on_click(self):
        if self.customListTable.rowCount() == 0:
            QMessageBox.warning(self, "删除失败", "选中一个客户才可删除", QMessageBox.Yes)
            return

        now_row = self.customListTable.currentRow()
        custom = self.custom_list[now_row]
        reply = QMessageBox.warning(self, "删除客户", "您确定要删除%s吗" % custom.name, QMessageBox.Yes | QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            custom.delete_instance()
            self.custom_list.remove(custom)
            self.exec()

    def draw_custom_list_table(self):
        self.customListTable.clearContents()
        self.customListTable.setRowCount(0)
        for custom in self.custom_list:
            now_row = self.customListTable.rowCount()
            self.customListTable.setRowCount(now_row + 1)

            self.customListTable.setItem(now_row, 0, QTableWidgetItem(custom.name))
            self.customListTable.setItem(now_row, 1, QTableWidgetItem(custom.phone))
            self.customListTable.setItem(now_row, 2, QTableWidgetItem(custom.addr))
            self.customListTable.setItem(now_row, 3, QTableWidgetItem("%.2f元" % (float(custom.trade_money) / 100)))
            self.customListTable.setItem(now_row, 4, QTableWidgetItem("%.2f元" % (float(custom.owe_money) / 100)))
            self.customListTable.setItem(now_row, 5, QTableWidgetItem(custom.comment))
