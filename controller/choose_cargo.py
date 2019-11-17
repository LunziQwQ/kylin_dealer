from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QTableWidget, QInputDialog, QHeaderView

from services.cargo import CargoService
from services.cargo_type import CargoTypeService
from services.custom import CustomService
from ui.choose_cargo import Ui_ChooseCargo


class ChooseCargoDialog(QDialog, Ui_ChooseCargo):
    def __init__(self, parent):
        super(ChooseCargoDialog, self).__init__(parent)
        self.setupUi(self)

        self.cargoListTable.setEditTriggers(QTableWidget.NoEditTriggers)
        self.cargoTypeListTable.setEditTriggers(QTableWidget.NoEditTriggers)

        self.searchEdit.textChanged.connect(self.search_edit_changed)
        self.cargoTypeListTable.cellClicked.connect(self.cargo_type_list_table_on_click)
        self.cargoListTable.cellClicked.connect(self.cargo_list_table_on_click)

        self.cargoTypeListTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.cargoTypeListTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.cargoTypeListTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.cargoTypeListTable.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.cargoTypeListTable.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)

        self.cargoListTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.cargoListTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.cargoListTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

        self.ct_list = []
        self.cargo_list = []
        self.cargo_type = None
        self.cargo = None
        self.count = 0
        self.exec()

    def exec(self, search_text=None, ct_row=0):
        self.ct_list = CargoTypeService.get_cargo_type_list_by_search(search_text)
        CargoTypeService.draw_cargo_type_table(self.cargoTypeListTable, self.ct_list)

        if len(self.ct_list) > 0:
            self.cargo_type_list_table_on_click(ct_row, 0)
        else:
            self.cargoListTable.clearContents()
            self.cargoListTable.setRowCount(0)

    def search_edit_changed(self):
        search_text = self.searchEdit.text()
        self.exec(search_text=search_text)

    def cargo_type_list_table_on_click(self, row, column):
        self.cargoTypeListTable.selectRow(row)

        self.cargo_type = self.ct_list[row]
        self.cargoTypeNameLabel.setText(self.cargo_type.name)
        self.cargo_list = CargoService.get_cargo_list_by_ct_name(self.cargo_type.name)
        CargoService.draw_cargo_table(self.cargoListTable, self.cargo_list)

    def cargo_list_table_on_click(self, row, column):
        self.cargoListTable.selectRow(row)

        self.cargo = self.cargo_list[row]
        self.dateLabel.setText(str(self.cargo.production_date))
        number, ok = QInputDialog.getInt(self, "输入货物数量", "请输入出货数量，目前库存%s" % str(self.cargo.count))
        if ok:
            if number > self.cargo.count:
                number = self.cargo.count
            self.count = number
            self.countLabel.setText(str(self.count))

    def get_result(self):
        return self.cargo, self.count
