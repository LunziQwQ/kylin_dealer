# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/lunzi/Projects/Python/Kylin_Dealer/ui/edit_cargo.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditCargo(object):
    def setupUi(self, EditCargo):
        EditCargo.setObjectName("EditCargo")
        EditCargo.resize(272, 291)
        self.buttonBox = QtWidgets.QDialogButtonBox(EditCargo)
        self.buttonBox.setGeometry(QtCore.QRect(40, 240, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(EditCargo)
        self.label.setGeometry(QtCore.QRect(20, 50, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(EditCargo)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(EditCargo)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(EditCargo)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 60, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(EditCargo)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 71, 21))
        self.label_5.setObjectName("label_5")
        self.cargoTypeLabel = QtWidgets.QLabel(EditCargo)
        self.cargoTypeLabel.setGeometry(QtCore.QRect(100, 20, 141, 21))
        self.cargoTypeLabel.setText("")
        self.cargoTypeLabel.setObjectName("cargoTypeLabel")
        self.unitLabel = QtWidgets.QLabel(EditCargo)
        self.unitLabel.setGeometry(QtCore.QRect(100, 110, 141, 21))
        self.unitLabel.setText("")
        self.unitLabel.setObjectName("unitLabel")
        self.productionDateEdit = QtWidgets.QDateEdit(EditCargo)
        self.productionDateEdit.setGeometry(QtCore.QRect(100, 50, 141, 24))
        self.productionDateEdit.setObjectName("productionDateEdit")
        self.countEdit = QtWidgets.QLineEdit(EditCargo)
        self.countEdit.setGeometry(QtCore.QRect(100, 80, 141, 21))
        self.countEdit.setObjectName("countEdit")
        self.commentEdit = QtWidgets.QTextEdit(EditCargo)
        self.commentEdit.setGeometry(QtCore.QRect(20, 160, 231, 71))
        self.commentEdit.setObjectName("commentEdit")

        self.retranslateUi(EditCargo)
        self.buttonBox.accepted.connect(EditCargo.accept)
        self.buttonBox.rejected.connect(EditCargo.reject)
        QtCore.QMetaObject.connectSlotsByName(EditCargo)

    def retranslateUi(self, EditCargo):
        _translate = QtCore.QCoreApplication.translate
        EditCargo.setWindowTitle(_translate("EditCargo", "进货"))
        self.label.setText(_translate("EditCargo", "生产日期："))
        self.label_2.setText(_translate("EditCargo", "数量："))
        self.label_3.setText(_translate("EditCargo", "单位："))
        self.label_4.setText(_translate("EditCargo", "备注："))
        self.label_5.setText(_translate("EditCargo", "货物种类："))


