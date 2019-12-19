from PyQt5.QtWidgets import QTableWidgetItem

from models.cargo_type import CargoType


class CargoTypeService(object):
    @staticmethod
    def get_cargo_type_list_by_page(page, page_size):
        return list(CargoType.select().order_by(CargoType.name).paginate(int(page), int(page_size)))

    @staticmethod
    def get_cargo_type_list_by_search(search_text=None):
        if search_text:
            return list(CargoType.select().where(CargoType.name.contains(search_text)).order_by(CargoType.name))
        else:
            return list(CargoType.select().order_by(CargoType.name))

    @staticmethod
    def draw_cargo_type_table(table, ct_list):
        table.clearContents()
        table.setRowCount(0)
        for ct in ct_list:
            now_row = table.rowCount()
            table.setRowCount(now_row + 1)

            table.setItem(now_row, 0, QTableWidgetItem(ct.name))
            table.setItem(now_row, 1, QTableWidgetItem(ct.unit))
            table.setItem(now_row, 2, QTableWidgetItem("%d" % ct.count))
            table.setItem(now_row, 3, QTableWidgetItem("%d天" % ct.life))
            table.setItem(now_row, 4, QTableWidgetItem("%.2f元" % (float(ct.price) / 100)))
