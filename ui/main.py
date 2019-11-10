# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/lunzi/Projects/Python/Kylin_Dealer/ui/view/main.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 502)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.welcomeLabel.setGeometry(QtCore.QRect(10, 10, 531, 81))
        self.welcomeLabel.setAutoFillBackground(False)
        self.welcomeLabel.setTextFormat(QtCore.Qt.AutoText)
        self.welcomeLabel.setScaledContents(False)
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setWordWrap(False)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.stockBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stockBtn.setGeometry(QtCore.QRect(0, 100, 551, 101))
        self.stockBtn.setObjectName("stockBtn")
        self.orderBtn = QtWidgets.QPushButton(self.centralwidget)
        self.orderBtn.setGeometry(QtCore.QRect(0, 200, 551, 101))
        self.orderBtn.setObjectName("orderBtn")
        self.customBtn = QtWidgets.QPushButton(self.centralwidget)
        self.customBtn.setGeometry(QtCore.QRect(0, 300, 551, 101))
        self.customBtn.setObjectName("customBtn")
        self.settingBtn = QtWidgets.QPushButton(self.centralwidget)
        self.settingBtn.setGeometry(QtCore.QRect(0, 400, 551, 101))
        self.settingBtn.setObjectName("settingBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kylin Dealer"))
        self.welcomeLabel.setText(_translate("MainWindow", "欢迎使用Kylin进销存"))
        self.stockBtn.setText(_translate("MainWindow", "库存管理"))
        self.orderBtn.setText(_translate("MainWindow", "订单管理"))
        self.customBtn.setText(_translate("MainWindow", "客户管理"))
        self.settingBtn.setText(_translate("MainWindow", "设置"))


