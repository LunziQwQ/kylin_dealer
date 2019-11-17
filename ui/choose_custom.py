# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/lunzi/Projects/Python/Kylin_Dealer/ui/choose_custom.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChooseCustom(object):
    def setupUi(self, ChooseCustom):
        ChooseCustom.setObjectName("ChooseCustom")
        ChooseCustom.resize(654, 307)
        self.buttonBox = QtWidgets.QDialogButtonBox(ChooseCustom)
        self.buttonBox.setGeometry(QtCore.QRect(420, 270, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.searchEdit = QtWidgets.QLineEdit(ChooseCustom)
        self.searchEdit.setGeometry(QtCore.QRect(60, 10, 191, 31))
        self.searchEdit.setObjectName("searchEdit")
        self.label = QtWidgets.QLabel(ChooseCustom)
        self.label.setGeometry(QtCore.QRect(20, 10, 41, 31))
        self.label.setObjectName("label")
        self.customListTable = QtWidgets.QTableWidget(ChooseCustom)
        self.customListTable.setGeometry(QtCore.QRect(10, 50, 631, 221))
        self.customListTable.setObjectName("customListTable")
        self.customListTable.setColumnCount(6)
        self.customListTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.customListTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.customListTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.customListTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.customListTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.customListTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.customListTable.setHorizontalHeaderItem(5, item)

        self.retranslateUi(ChooseCustom)
        self.buttonBox.accepted.connect(ChooseCustom.accept)
        self.buttonBox.rejected.connect(ChooseCustom.reject)
        QtCore.QMetaObject.connectSlotsByName(ChooseCustom)

    def retranslateUi(self, ChooseCustom):
        _translate = QtCore.QCoreApplication.translate
        ChooseCustom.setWindowTitle(_translate("ChooseCustom", "选择客户"))
        self.label.setText(_translate("ChooseCustom", "搜索："))
        item = self.customListTable.horizontalHeaderItem(0)
        item.setText(_translate("ChooseCustom", "姓名"))
        item = self.customListTable.horizontalHeaderItem(1)
        item.setText(_translate("ChooseCustom", "电话"))
        item = self.customListTable.horizontalHeaderItem(2)
        item.setText(_translate("ChooseCustom", "地址"))
        item = self.customListTable.horizontalHeaderItem(3)
        item.setText(_translate("ChooseCustom", "总交易额"))
        item = self.customListTable.horizontalHeaderItem(4)
        item.setText(_translate("ChooseCustom", "总欠款"))
        item = self.customListTable.horizontalHeaderItem(5)
        item.setText(_translate("ChooseCustom", "备注"))


