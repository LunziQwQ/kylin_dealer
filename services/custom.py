from PyQt5.QtWidgets import QTableWidgetItem

from models.custom import Custom


class CustomService(object):

    @staticmethod
    def get_custom_list(search_text=None):
        custom_list = Custom.select()
        if custom_list.count() > 0:
            if not search_text:
                return list(custom_list)
            else:
                return list(filter(lambda c: search_text in c.name \
                                             or search_text in c.phone \
                                             or search_text in c.addr \
                                             or search_text in c.comment, custom_list))
        else:
            return []

    @staticmethod
    def sale_cargo_for_custom(custom, need_pay, owe):
        custom.owe_money += owe
        custom.trade_money += need_pay
        custom.save()

    @staticmethod
    def draw_custom_list_table(table, custom_list):
        table.clearContents()
        table.setRowCount(0)
        for custom in custom_list:
            now_row = table.rowCount()
            table.setRowCount(now_row + 1)

            table.setItem(now_row, 0, QTableWidgetItem(custom.name))
            table.setItem(now_row, 1, QTableWidgetItem(custom.phone))
            table.setItem(now_row, 2, QTableWidgetItem(custom.addr))
            table.setItem(now_row, 3, QTableWidgetItem("%.2f元" % (float(custom.trade_money) / 100)))
            table.setItem(now_row, 4, QTableWidgetItem("%.2f元" % (float(custom.owe_money) / 100)))
            table.setItem(now_row, 5, QTableWidgetItem(custom.comment))
