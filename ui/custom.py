# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/lunzi/Projects/Python/Kylin_Dealer/ui/custom.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CustomWindow(object):
    def setupUi(self, CustomWindow):
        CustomWindow.setObjectName("CustomWindow")
        CustomWindow.resize(879, 554)
        self.centralwidget = QtWidgets.QWidget(CustomWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.customListTable = QtWidgets.QTableWidget(self.centralwidget)
        self.customListTable.setGeometry(QtCore.QRect(10, 70, 861, 471))
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
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(10, 10, 91, 61))
        self.addBtn.setObjectName("addBtn")
        self.editBtn = QtWidgets.QPushButton(self.centralwidget)
        self.editBtn.setGeometry(QtCore.QRect(100, 10, 91, 61))
        self.editBtn.setObjectName("editBtn")
        self.delBtn = QtWidgets.QPushButton(self.centralwidget)
        self.delBtn.setGeometry(QtCore.QRect(190, 10, 51, 61))
        self.delBtn.setObjectName("delBtn")
        self.searchEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.searchEdit.setGeometry(QtCore.QRect(700, 20, 171, 31))
        self.searchEdit.setObjectName("searchEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(660, 20, 41, 31))
        self.label.setObjectName("label")
        CustomWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CustomWindow)
        QtCore.QMetaObject.connectSlotsByName(CustomWindow)

    def retranslateUi(self, CustomWindow):
        _translate = QtCore.QCoreApplication.translate
        CustomWindow.setWindowTitle(_translate("CustomWindow", "客户管理"))
        item = self.customListTable.horizontalHeaderItem(0)
        item.setText(_translate("CustomWindow", "姓名"))
        item = self.customListTable.horizontalHeaderItem(1)
        item.setText(_translate("CustomWindow", "电话"))
        item = self.customListTable.horizontalHeaderItem(2)
        item.setText(_translate("CustomWindow", "地址"))
        item = self.customListTable.horizontalHeaderItem(3)
        item.setText(_translate("CustomWindow", "总交易额"))
        item = self.customListTable.horizontalHeaderItem(4)
        item.setText(_translate("CustomWindow", "总欠款"))
        item = self.customListTable.horizontalHeaderItem(5)
        item.setText(_translate("CustomWindow", "备注"))
        self.addBtn.setText(_translate("CustomWindow", "添加客户"))
        self.editBtn.setText(_translate("CustomWindow", "修改信息"))
        self.delBtn.setText(_translate("CustomWindow", "删除"))
        self.label.setText(_translate("CustomWindow", "搜索："))


