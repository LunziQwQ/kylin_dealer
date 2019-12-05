# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/lunzi/Projects/Python/Kylin_Dealer/ui/edit_order.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditOrder(object):
    def setupUi(self, EditOrder):
        EditOrder.setObjectName("EditOrder")
        EditOrder.resize(272, 212)
        self.buttonBox = QtWidgets.QDialogButtonBox(EditOrder)
        self.buttonBox.setGeometry(QtCore.QRect(50, 170, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(EditOrder)
        self.label.setGeometry(QtCore.QRect(20, 60, 71, 21))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(EditOrder)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 71, 21))
        self.label_5.setObjectName("label_5")
        self.totalMoneyEdit = QtWidgets.QLineEdit(EditOrder)
        self.totalMoneyEdit.setGeometry(QtCore.QRect(90, 60, 131, 21))
        self.totalMoneyEdit.setObjectName("totalMoneyEdit")
        self.customNameLabel = QtWidgets.QLabel(EditOrder)
        self.customNameLabel.setGeometry(QtCore.QRect(100, 20, 121, 21))
        self.customNameLabel.setText("")
        self.customNameLabel.setObjectName("customNameLabel")
        self.label_2 = QtWidgets.QLabel(EditOrder)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 71, 21))
        self.label_2.setObjectName("label_2")
        self.payMoneyEdit = QtWidgets.QLineEdit(EditOrder)
        self.payMoneyEdit.setGeometry(QtCore.QRect(90, 100, 131, 21))
        self.payMoneyEdit.setObjectName("payMoneyEdit")
        self.oweMoneyEdit = QtWidgets.QLineEdit(EditOrder)
        self.oweMoneyEdit.setGeometry(QtCore.QRect(90, 140, 131, 21))
        self.oweMoneyEdit.setText("")
        self.oweMoneyEdit.setObjectName("oweMoneyEdit")
        self.label_3 = QtWidgets.QLabel(EditOrder)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(EditOrder)
        self.label_4.setGeometry(QtCore.QRect(230, 60, 21, 21))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(EditOrder)
        self.label_6.setGeometry(QtCore.QRect(230, 100, 21, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(EditOrder)
        self.label_7.setGeometry(QtCore.QRect(230, 140, 21, 21))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(EditOrder)
        self.buttonBox.rejected.connect(EditOrder.reject)
        self.buttonBox.accepted.connect(EditOrder.accept)
        QtCore.QMetaObject.connectSlotsByName(EditOrder)

    def retranslateUi(self, EditOrder):
        _translate = QtCore.QCoreApplication.translate
        EditOrder.setWindowTitle(_translate("EditOrder", "修改订单"))
        self.label.setText(_translate("EditOrder", "总金额："))
        self.label_5.setText(_translate("EditOrder", "客户名称："))
        self.label_2.setText(_translate("EditOrder", "已付金额："))
        self.label_3.setText(_translate("EditOrder", "欠款金额："))
        self.label_4.setText(_translate("EditOrder", "元"))
        self.label_6.setText(_translate("EditOrder", "元"))
        self.label_7.setText(_translate("EditOrder", "元"))


