# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/lunzi/Projects/Python/Kylin_Dealer/ui/add_cargo_type.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddCargoType(object):
    def setupUi(self, AddCargoType):
        AddCargoType.setObjectName("AddCargoType")
        AddCargoType.resize(244, 189)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddCargoType)
        self.buttonBox.setGeometry(QtCore.QRect(10, 140, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(AddCargoType)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AddCargoType)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AddCargoType)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(AddCargoType)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 81, 21))
        self.label_4.setObjectName("label_4")
        self.name = QtWidgets.QLineEdit(AddCargoType)
        self.name.setGeometry(QtCore.QRect(100, 10, 113, 21))
        self.name.setObjectName("name")
        self.unit = QtWidgets.QLineEdit(AddCargoType)
        self.unit.setGeometry(QtCore.QRect(100, 40, 113, 21))
        self.unit.setObjectName("unit")
        self.life = QtWidgets.QLineEdit(AddCargoType)
        self.life.setGeometry(QtCore.QRect(100, 70, 113, 21))
        self.life.setObjectName("life")
        self.price = QtWidgets.QLineEdit(AddCargoType)
        self.price.setGeometry(QtCore.QRect(100, 100, 113, 21))
        self.price.setObjectName("price")

        self.retranslateUi(AddCargoType)
        self.buttonBox.accepted.connect(AddCargoType.accept)
        self.buttonBox.rejected.connect(AddCargoType.reject)
        QtCore.QMetaObject.connectSlotsByName(AddCargoType)

    def retranslateUi(self, AddCargoType):
        _translate = QtCore.QCoreApplication.translate
        AddCargoType.setWindowTitle(_translate("AddCargoType", "添加货物种类"))
        self.label.setText(_translate("AddCargoType", "货物种类："))
        self.label_2.setText(_translate("AddCargoType", "单位："))
        self.label_3.setText(_translate("AddCargoType", "保质期(天)："))
        self.label_4.setText(_translate("AddCargoType", "售价："))
        self.unit.setText(_translate("AddCargoType", "箱"))
        self.life.setText(_translate("AddCargoType", "270"))
        self.price.setText(_translate("AddCargoType", "0.00"))


