from PyQt5.QtWidgets import QDialog
from ui.edit_custom import Ui_EditCustom


class EditCustomDialog(QDialog, Ui_EditCustom):
    def __init__(self, parent, custom=None):
        super(EditCustomDialog, self).__init__(parent)
        self.setupUi(self)

        if custom:
            self.setWindowTitle("修改客户信息")
            self.nameEdit.setText(custom.name)
            self.phoneEdit.setText(custom.phone)
            self.addrEdit.setText(custom.addr)
            self.commentEdit.setText(custom.comment)
        else:
            self.setWindowTitle("添加客户")

    def get_result(self):
        return self.nameEdit.text(), self.phoneEdit.text(), self.addrEdit.toPlainText(), self.commentEdit.toPlainText()
