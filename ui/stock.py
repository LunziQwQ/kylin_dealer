# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/lunzi/Projects/Python/Kylin_Dealer/ui/stock.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StockWindow(object):
    def setupUi(self, StockWindow):
        StockWindow.setObjectName("StockWindow")
        StockWindow.resize(1092, 488)
        self.cargoTypeListTable = QtWidgets.QTableWidget(StockWindow)
        self.cargoTypeListTable.setGeometry(QtCore.QRect(10, 80, 521, 401))
        self.cargoTypeListTable.setObjectName("cargoTypeListTable")
        self.cargoTypeListTable.setColumnCount(5)
        self.cargoTypeListTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.cargoTypeListTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cargoTypeListTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.cargoTypeListTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.cargoTypeListTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.cargoTypeListTable.setHorizontalHeaderItem(4, item)
        self.cargoListTable = QtWidgets.QTableWidget(StockWindow)
        self.cargoListTable.setGeometry(QtCore.QRect(540, 80, 541, 401))
        self.cargoListTable.setObjectName("cargoListTable")
        self.cargoListTable.setColumnCount(3)
        self.cargoListTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.cargoListTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cargoListTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.cargoListTable.setHorizontalHeaderItem(2, item)
        self.buyBtn = QtWidgets.QPushButton(StockWindow)
        self.buyBtn.setGeometry(QtCore.QRect(10, 20, 111, 51))
        self.buyBtn.setObjectName("buyBtn")
        self.saleBtn = QtWidgets.QPushButton(StockWindow)
        self.saleBtn.setGeometry(QtCore.QRect(130, 20, 111, 51))
        self.saleBtn.setObjectName("saleBtn")

        self.retranslateUi(StockWindow)
        QtCore.QMetaObject.connectSlotsByName(StockWindow)

    def retranslateUi(self, StockWindow):
        _translate = QtCore.QCoreApplication.translate
        StockWindow.setWindowTitle(_translate("StockWindow", "Form"))
        item = self.cargoTypeListTable.horizontalHeaderItem(0)
        item.setText(_translate("StockWindow", "货物种类"))
        item = self.cargoTypeListTable.horizontalHeaderItem(1)
        item.setText(_translate("StockWindow", "单位"))
        item = self.cargoTypeListTable.horizontalHeaderItem(2)
        item.setText(_translate("StockWindow", "数量"))
        item = self.cargoTypeListTable.horizontalHeaderItem(3)
        item.setText(_translate("StockWindow", "保质期"))
        item = self.cargoTypeListTable.horizontalHeaderItem(4)
        item.setText(_translate("StockWindow", "售价"))
        item = self.cargoListTable.horizontalHeaderItem(0)
        item.setText(_translate("StockWindow", "生产日期"))
        item = self.cargoListTable.horizontalHeaderItem(1)
        item.setText(_translate("StockWindow", "数量"))
        item = self.cargoListTable.horizontalHeaderItem(2)
        item.setText(_translate("StockWindow", "备注"))
        self.buyBtn.setText(_translate("StockWindow", "进货"))
        self.saleBtn.setText(_translate("StockWindow", "出货"))


