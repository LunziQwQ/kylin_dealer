from PyQt5.QtWidgets import QTableWidgetItem

from models.custom import Custom


class CustomService(object):

    @staticmethod
    def get_custom_list(search_text=None):
        if not search_text:
            return list(Custom.select().order_by(Custom.name))
        else:
            return list(Custom.select().where(
                Custom.name.contains(search_text) | Custom.phone.contains(search_text) | Custom.addr.contains(
                    search_text) | Custom.comment.contains(search_text)).order_by(Custom.name))

    @staticmethod
    def delete_custom(custom):
        custom.delete_instance()

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
