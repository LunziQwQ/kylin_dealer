from datetime import date

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QDialog
from ui.bug_cargo import Ui_BugCargo


class BuyCargoDialog(QDialog, Ui_BugCargo):
    def __init__(self, parent, ct_name, ct_unit):
        super(BuyCargoDialog, self).__init__(parent)
        self.setupUi(self)

        self.productionDateEdit.setDate(date.today())

        int_val = QIntValidator(self)
        int_val.setBottom(0)
        self.countEdit.setValidator(int_val)

        self.unitLabel.setText(ct_unit)
        self.cargoTypeLabel.setText(ct_name)

    def get_result(self):
        return self.productionDateEdit.date().getDate(), self.countEdit.text(), self.commentEdit.toPlainText()
