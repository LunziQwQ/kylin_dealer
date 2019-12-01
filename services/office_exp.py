from PyQt5.QtWidgets import QTableWidgetItem

from models.office_exp import OfficeExp


class OfficeExpService(object):

    @staticmethod
    def get_exp_list(search_text=None):
        exp_list = OfficeExp.select()
        if exp_list.count() > 0:
            if not search_text:
                return list(exp_list)
            else:
                return list(filter(lambda c: search_text in c.name \
                                             or search_text in c.comment, exp_list))
        else:
            return []

    @staticmethod
    def draw_exp_list_table(table, exp_list):
        table.clearContents()
        table.setRowCount(0)
        for exp in exp_list:
            now_row = table.rowCount()
            table.setRowCount(now_row + 1)

            table.setItem(now_row, 0, QTableWidgetItem(exp.name))
            table.setItem(now_row, 1, QTableWidgetItem("%.2f元" % (float(exp.money) / 100)))
            table.setItem(now_row, 2, QTableWidgetItem(exp.comment))

    @staticmethod
    def get_total_money():
        exp_list = OfficeExp.select()
        total = 0
        for exp in exp_list:
            total += exp.money
        return "%.2f元" % (float(total) / 100)
