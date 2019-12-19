from PyQt5.QtWidgets import QTableWidgetItem

from models.cargo_type import CargoType
from models.cargo import Cargo


class CargoService(object):
    @staticmethod
    def get_cargo_list_by_ct_name(ct_name):
        return list(CargoType.get(CargoType.name == ct_name).cargo_list.order_by(Cargo.production_date.desc()))

    @staticmethod
    def add_cargo(cargo):
        cargo_type = cargo.cargo_type
        cargo_type.count += cargo.count
        cargo_type.save()
        for old_cargo in cargo_type.cargo_list:
            if old_cargo.production_date == cargo.production_date:
                old_cargo.count += cargo.count
                old_cargo.save()
                return
        cargo.save()

    @staticmethod
    def sale_cargoes(cargo_dict):
        for cargo, count in cargo_dict.items():
            cargo.count -= count
            cargo.save()

            cargo_type = CargoType.get_by_id(cargo.cargo_type.id)
            cargo_type.count -= count
            cargo_type.save()

    @staticmethod
    def draw_cargo_table(table, cargo_list):
        table.clearContents()
        table.setRowCount(0)

        for cargo in cargo_list:
            now_row = table.rowCount()
            table.setRowCount(now_row + 1)

            table.setItem(now_row, 0, QTableWidgetItem(str(cargo.production_date)))
            table.setItem(now_row, 1, QTableWidgetItem("%d%s" % (cargo.count, cargo.cargo_type.unit)))
            table.setItem(now_row, 2, QTableWidgetItem(cargo.comment))
