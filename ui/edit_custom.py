# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/lunzi/Projects/Python/Kylin_Dealer/ui/edit_custom.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditCustom(object):
    def setupUi(self, EditCustom):
        EditCustom.setObjectName("EditCustom")
        EditCustom.resize(272, 305)
        self.buttonBox = QtWidgets.QDialogButtonBox(EditCustom)
        self.buttonBox.setGeometry(QtCore.QRect(30, 260, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(EditCustom)
        self.label.setGeometry(QtCore.QRect(20, 50, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(EditCustom)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(EditCustom)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 60, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(EditCustom)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 71, 21))
        self.label_5.setObjectName("label_5")
        self.cargoTypeLabel = QtWidgets.QLabel(EditCustom)
        self.cargoTypeLabel.setGeometry(QtCore.QRect(100, 20, 141, 21))
        self.cargoTypeLabel.setText("")
        self.cargoTypeLabel.setObjectName("cargoTypeLabel")
        self.commentEdit = QtWidgets.QTextEdit(EditCustom)
        self.commentEdit.setGeometry(QtCore.QRect(20, 180, 231, 71))
        self.commentEdit.setObjectName("commentEdit")
        self.phoneEdit = QtWidgets.QLineEdit(EditCustom)
        self.phoneEdit.setGeometry(QtCore.QRect(90, 50, 151, 21))
        self.phoneEdit.setObjectName("phoneEdit")
        self.nameEdit = QtWidgets.QLineEdit(EditCustom)
        self.nameEdit.setGeometry(QtCore.QRect(90, 20, 151, 21))
        self.nameEdit.setObjectName("nameEdit")
        self.addrEdit = QtWidgets.QTextEdit(EditCustom)
        self.addrEdit.setGeometry(QtCore.QRect(20, 100, 231, 51))
        self.addrEdit.setObjectName("addrEdit")

        self.retranslateUi(EditCustom)
        self.buttonBox.rejected.connect(EditCustom.reject)
        self.buttonBox.accepted.connect(EditCustom.accept)
        QtCore.QMetaObject.connectSlotsByName(EditCustom)

    def retranslateUi(self, EditCustom):
        _translate = QtCore.QCoreApplication.translate
        EditCustom.setWindowTitle(_translate("EditCustom", "添加客户"))
        self.label.setText(_translate("EditCustom", "电话："))
        self.label_2.setText(_translate("EditCustom", "地址:"))
        self.label_4.setText(_translate("EditCustom", "备注："))
        self.label_5.setText(_translate("EditCustom", "客户姓名："))


