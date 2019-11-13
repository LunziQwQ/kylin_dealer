# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/lunzi/Projects/Python/Kylin_Dealer/ui/bug_cargo.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BugCargo(object):
    def setupUi(self, BugCargo):
        BugCargo.setObjectName("BugCargo")
        BugCargo.resize(272, 291)
        self.buttonBox = QtWidgets.QDialogButtonBox(BugCargo)
        self.buttonBox.setGeometry(QtCore.QRect(40, 240, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(BugCargo)
        self.label.setGeometry(QtCore.QRect(20, 50, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(BugCargo)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(BugCargo)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(BugCargo)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 60, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(BugCargo)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 71, 21))
        self.label_5.setObjectName("label_5")
        self.cargoTypeLabel = QtWidgets.QLabel(BugCargo)
        self.cargoTypeLabel.setGeometry(QtCore.QRect(100, 20, 141, 21))
        self.cargoTypeLabel.setText("")
        self.cargoTypeLabel.setObjectName("cargoTypeLabel")
        self.unitLabel = QtWidgets.QLabel(BugCargo)
        self.unitLabel.setGeometry(QtCore.QRect(100, 110, 141, 21))
        self.unitLabel.setText("")
        self.unitLabel.setObjectName("unitLabel")
        self.productionDateEdit = QtWidgets.QDateEdit(BugCargo)
        self.productionDateEdit.setGeometry(QtCore.QRect(100, 50, 141, 24))
        self.productionDateEdit.setObjectName("productionDateEdit")
        self.countEdit = QtWidgets.QLineEdit(BugCargo)
        self.countEdit.setGeometry(QtCore.QRect(100, 80, 141, 21))
        self.countEdit.setObjectName("countEdit")
        self.commentEdit = QtWidgets.QTextEdit(BugCargo)
        self.commentEdit.setGeometry(QtCore.QRect(20, 160, 231, 71))
        self.commentEdit.setObjectName("commentEdit")

        self.retranslateUi(BugCargo)
        self.buttonBox.accepted.connect(BugCargo.accept)
        self.buttonBox.rejected.connect(BugCargo.reject)
        QtCore.QMetaObject.connectSlotsByName(BugCargo)

    def retranslateUi(self, BugCargo):
        _translate = QtCore.QCoreApplication.translate
        BugCargo.setWindowTitle(_translate("BugCargo", "进货"))
        self.label.setText(_translate("BugCargo", "生产日期："))
        self.label_2.setText(_translate("BugCargo", "数量："))
        self.label_3.setText(_translate("BugCargo", "单位："))
        self.label_4.setText(_translate("BugCargo", "备注："))
        self.label_5.setText(_translate("BugCargo", "货物种类："))


