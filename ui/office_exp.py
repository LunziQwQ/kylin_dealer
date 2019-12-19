# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/lunzi/Projects/Python/Kylin_Dealer/ui/office_exp.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OfficeExpWindow(object):
    def setupUi(self, OfficeExpWindow):
        OfficeExpWindow.setObjectName("OfficeExpWindow")
        OfficeExpWindow.resize(536, 582)
        self.centralwidget = QtWidgets.QWidget(OfficeExpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.expListTable = QtWidgets.QTableWidget(self.centralwidget)
        self.expListTable.setGeometry(QtCore.QRect(10, 70, 521, 471))
        self.expListTable.setObjectName("expListTable")
        self.expListTable.setColumnCount(3)
        self.expListTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.expListTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.expListTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.expListTable.setHorizontalHeaderItem(2, item)
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(10, 10, 61, 61))
        self.addBtn.setObjectName("addBtn")
        self.editBtn = QtWidgets.QPushButton(self.centralwidget)
        self.editBtn.setGeometry(QtCore.QRect(70, 10, 61, 61))
        self.editBtn.setObjectName("editBtn")
        self.delBtn = QtWidgets.QPushButton(self.centralwidget)
        self.delBtn.setGeometry(QtCore.QRect(130, 10, 51, 61))
        self.delBtn.setObjectName("delBtn")
        self.searchEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.searchEdit.setGeometry(QtCore.QRect(360, 20, 171, 31))
        self.searchEdit.setObjectName("searchEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 20, 41, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 550, 41, 16))
        self.label_2.setObjectName("label_2")
        self.total_money_label = QtWidgets.QLabel(self.centralwidget)
        self.total_money_label.setGeometry(QtCore.QRect(50, 550, 80, 16))
        self.total_money_label.setObjectName("total_money_label")
        OfficeExpWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(OfficeExpWindow)
        QtCore.QMetaObject.connectSlotsByName(OfficeExpWindow)

    def retranslateUi(self, OfficeExpWindow):
        _translate = QtCore.QCoreApplication.translate
        OfficeExpWindow.setWindowTitle(_translate("OfficeExpWindow", "办公支出记录"))
        item = self.expListTable.horizontalHeaderItem(0)
        item.setText(_translate("OfficeExpWindow", "名称"))
        item = self.expListTable.horizontalHeaderItem(1)
        item.setText(_translate("OfficeExpWindow", "价格"))
        item = self.expListTable.horizontalHeaderItem(2)
        item.setText(_translate("OfficeExpWindow", "备注"))
        self.addBtn.setText(_translate("OfficeExpWindow", "添加"))
        self.editBtn.setText(_translate("OfficeExpWindow", "修改"))
        self.delBtn.setText(_translate("OfficeExpWindow", "删除"))
        self.label.setText(_translate("OfficeExpWindow", "搜索："))
        self.label_2.setText(_translate("OfficeExpWindow", "总计："))
        self.total_money_label.setText(_translate("OfficeExpWindow", "0"))


