from PyQt5.QtWidgets import QMainWindow, QTableWidget, QHeaderView, QMessageBox

from controller.edit_exp import EditOfficeExpDialog
from models.office_exp import OfficeExp
from services.office_exp import OfficeExpService
from ui.office_exp import Ui_OfficeExpWindow


class OfficeExpController(QMainWindow, Ui_OfficeExpWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_OfficeExpWindow.__init__(self)
        self.setupUi(self)

        self.expListTable.setEditTriggers(QTableWidget.NoEditTriggers)

        self.expListTable.cellClicked.connect(self.expListTable.selectRow)

        self.addBtn.clicked.connect(self.add_exp_btn_on_click)
        self.editBtn.clicked.connect(self.edit_custom_btn_on_click)
        self.delBtn.clicked.connect(self.del_custom_btn_on_click)

        self.searchEdit.textChanged.connect(self.search_edit_changed)

        self.expListTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.expListTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.expListTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

        self.exp_list = []

    def exec(self, selected_row=0, search_text=None):
        self.exp_list = OfficeExpService.get_exp_list(search_text)
        OfficeExpService.draw_exp_list_table(self.expListTable, self.exp_list)
        if len(self.exp_list) > 0:
            self.expListTable.selectRow(selected_row)
        else:
            self.expListTable.clearContents()
            self.expListTable.setRowCount(0)

        self.total_money_label.setText(OfficeExpService.get_total_money())

    def add_exp_btn_on_click(self):
        add_dialog = EditOfficeExpDialog(self)
        if add_dialog.exec_():
            name, money, comment = add_dialog.get_result()
            if not name:
                QMessageBox.warning(self, "参数错误", "参数错误：添加的支出记录必须填写名称", QMessageBox.Yes)
            else:
                new_exp = OfficeExp.build(name, money, comment)
                try:
                    new_exp.save()
                except Exception:
                    QMessageBox.warning(self, "添加失败", "添加失败：未知错误", QMessageBox.Yes)
                self.exec()

    def edit_custom_btn_on_click(self):
        if self.expListTable.rowCount() == 0:
            QMessageBox.warning(self, "编辑失败", "选中一条记录才可修改", QMessageBox.Yes)
            return
        now_row = self.expListTable.currentRow()
        exp = self.exp_list[now_row]
        edit_dialog = EditOfficeExpDialog(self, exp)

        if edit_dialog.exec_():
            name, money, comment = edit_dialog.get_result()
            if not name:
                QMessageBox.warning(self, "参数错误", "参数错误：客户信息必须填写名字", QMessageBox.Yes)
            else:
                exp.name = name
                exp.money = int(float(money) * 100)
                exp.comment = comment
                exp.save()
                self.exec(now_row)

    def search_edit_changed(self):
        search_text = self.searchEdit.text()
        self.exec(search_text=search_text)

    def del_custom_btn_on_click(self):
        if self.expListTable.rowCount() == 0:
            QMessageBox.warning(self, "删除失败", "选中一条记录才可删除", QMessageBox.Yes)
            return

        now_row = self.expListTable.currentRow()
        exp = self.exp_list[now_row]
        reply = QMessageBox.warning(self, "删除记录", "您确定要删除%s吗" % exp.name, QMessageBox.Yes | QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            exp.delete_instance()
            self.exp_list.remove(exp)
            self.exec()
