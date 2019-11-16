from datetime import date

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QDialog
from ui.edit_cargo import Ui_EditCargo


class EditCargoDialog(QDialog, Ui_EditCargo):
    def __init__(self, parent, cargo_type, edit_cargo=None):
        super(EditCargoDialog, self).__init__(parent)
        self.setupUi(self)

        if edit_cargo:
            self.setWindowTitle("修改货物信息")
            self.countEdit.setText(str(edit_cargo.count))
            self.productionDateEdit.setDate(edit_cargo.production_date)
            self.commentEdit.setText(edit_cargo.comment)
        else:
            self.setWindowTitle("进货")
            self.productionDateEdit.setDate(date.today())
            self.countEdit.setText("0")

        int_val = QIntValidator(self)
        int_val.setBottom(0)
        self.countEdit.setValidator(int_val)

        self.unitLabel.setText(cargo_type.unit)
        self.cargoTypeLabel.setText(cargo_type.name)

    def get_result(self):
        return self.productionDateEdit.date().getDate(), self.countEdit.text(), self.commentEdit.toPlainText()
