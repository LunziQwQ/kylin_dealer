from PyQt5.QtGui import QDoubleValidator, QIntValidator
from PyQt5.QtWidgets import QDialog

from ui.add_cargo_type import Ui_AddCargoType


class AddCargoTypeDialog(QDialog, Ui_AddCargoType):
    def __init__(self, parent):
        super(AddCargoTypeDialog, self).__init__(parent)
        self.setupUi(self)

        double_val = QDoubleValidator(self)
        double_val.setBottom(0)
        double_val.setDecimals(2)
        self.price.setValidator(double_val)

        int_val = QIntValidator(self)
        int_val.setBottom(0)
        self.life.setValidator(int_val)

    def get_result(self):
        return self.name.text(), self.unit.text(), self.life.text(), self.price.text()
