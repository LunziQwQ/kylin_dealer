from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QDialog
from ui.edit_office_exp import Ui_EditOfficeExp


class EditOfficeExpDialog(QDialog, Ui_EditOfficeExp):
    def __init__(self, parent, exp=None):
        super(EditOfficeExpDialog, self).__init__(parent)
        self.setupUi(self)

        double_val = QDoubleValidator(self)
        double_val.setBottom(0)
        double_val.setDecimals(2)
        self.moneyEdit.setValidator(double_val)

        if exp:
            self.setWindowTitle("修改记录信息")
            self.nameEdit.setText(exp.name)
            self.moneyEdit.setText("%.2f" % (float(exp.money) / 100))
            self.commentEdit.setText(exp.comment)
        else:
            self.setWindowTitle("添加记录")

    def get_result(self):
        return self.nameEdit.text(), self.moneyEdit.text(), self.commentEdit.toPlainText()
