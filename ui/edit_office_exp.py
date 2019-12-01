# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/lunzi/Projects/Python/Kylin_Dealer/ui/edit_office_exp.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditOfficeExp(object):
    def setupUi(self, EditOfficeExp):
        EditOfficeExp.setObjectName("EditOfficeExp")
        EditOfficeExp.resize(272, 220)
        self.buttonBox = QtWidgets.QDialogButtonBox(EditOfficeExp)
        self.buttonBox.setGeometry(QtCore.QRect(30, 180, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(EditOfficeExp)
        self.label.setGeometry(QtCore.QRect(20, 50, 71, 21))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(EditOfficeExp)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 60, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(EditOfficeExp)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 71, 21))
        self.label_5.setObjectName("label_5")
        self.commentEdit = QtWidgets.QTextEdit(EditOfficeExp)
        self.commentEdit.setGeometry(QtCore.QRect(20, 100, 231, 71))
        self.commentEdit.setObjectName("commentEdit")
        self.moneyEdit = QtWidgets.QLineEdit(EditOfficeExp)
        self.moneyEdit.setGeometry(QtCore.QRect(90, 50, 151, 21))
        self.moneyEdit.setObjectName("moneyEdit")
        self.nameEdit = QtWidgets.QLineEdit(EditOfficeExp)
        self.nameEdit.setGeometry(QtCore.QRect(90, 20, 151, 21))
        self.nameEdit.setObjectName("nameEdit")

        self.retranslateUi(EditOfficeExp)
        self.buttonBox.rejected.connect(EditOfficeExp.reject)
        self.buttonBox.accepted.connect(EditOfficeExp.accept)
        QtCore.QMetaObject.connectSlotsByName(EditOfficeExp)

    def retranslateUi(self, EditOfficeExp):
        _translate = QtCore.QCoreApplication.translate
        EditOfficeExp.setWindowTitle(_translate("EditOfficeExp", "添加办公支出记录"))
        self.label.setText(_translate("EditOfficeExp", "金额："))
        self.label_4.setText(_translate("EditOfficeExp", "备注："))
        self.label_5.setText(_translate("EditOfficeExp", "支出名称："))


