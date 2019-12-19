import json

from PyQt5.QtWidgets import QTableWidgetItem

from models.order import Order


class OrderService(object):
    @staticmethod
    def get_order_list(order_method, search_text):
        order_method_map = {
            "订单日期": Order.date.desc(),
            "欠款": Order.owe_money.desc(),
            "总金额": Order.need_pay.desc(),
            "客户名称": Order.custom.name
        }
        results = Order.select().order_by(order_method_map[order_method])
        if not search_text:
            return list(results)
        else:
            return list(filter(lambda o: search_text in o.custom.name \
                                  or search_text in o.comment \
                                  or search_text in o.custom.addr \
                                  or search_text in o.custom.comment \
                                  or search_text in o.custom.phone, results))

    @staticmethod
    def count_by_custom(custom):
        return Order.select().where(Order.custom == custom).count()

    @staticmethod
    def delete_by_custom(custom):
        Order.delete().where(Order.custom == custom).execute()

    @staticmethod
    def draw_order_list_table(table, order_list):
        table.clearContents()
        table.setRowCount(0)
        for order in order_list:
            now_row = table.rowCount()
            table.setRowCount(now_row + 1)

            table.setItem(now_row, 0, QTableWidgetItem(order.custom.name))
            table.setItem(now_row, 1, QTableWidgetItem("%.2f元" % (float(order.need_pay) / 100)))
            table.setItem(now_row, 2, QTableWidgetItem("%.2f元" % (float(order.now_pay) / 100)))
            table.setItem(now_row, 3, QTableWidgetItem("%.2f元" % (float(order.owe_money) / 100)))
            table.setItem(now_row, 4, QTableWidgetItem(str(order.date)))

    @staticmethod
    def draw_order_sale_item_table(table, order):
        sale_list = json.loads(order.sale_list)

        table.clearContents()
        table.setRowCount(0)
        for item in sale_list:
            now_row = table.rowCount()
            table.setRowCount(now_row + 1)

            table.setItem(now_row, 0, QTableWidgetItem(item["cargo_type"]))
            table.setItem(now_row, 1, QTableWidgetItem(str(item["count"])))
            table.setItem(now_row, 2, QTableWidgetItem(item["unit"]))
            table.setItem(now_row, 3, QTableWidgetItem("%.2f元" % (float(item["price"]) / 100)))
            table.setItem(now_row, 4, QTableWidgetItem("%d天" % item["life"]))
            table.setItem(now_row, 5, QTableWidgetItem(str(item["production_date"])))

    @staticmethod
    def get_total_money():
        total_money = 0
        total_owe = 0
        order_list = Order.select()
        for order in order_list:
            total_money += order.need_pay
            total_owe += order.owe_money

        return total_money, total_owe
