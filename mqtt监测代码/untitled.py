# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(186, 168)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_temp = QLabel(self.centralwidget)
        self.label_temp.setObjectName(u"label_temp")

        self.verticalLayout.addWidget(self.label_temp)

        self.label_hum = QLabel(self.centralwidget)
        self.label_hum.setObjectName(u"label_hum")

        self.verticalLayout.addWidget(self.label_hum)

        self.label_light = QLabel(self.centralwidget)
        self.label_light.setObjectName(u"label_light")

        self.verticalLayout.addWidget(self.label_light)

        self.label_door = QLabel(self.centralwidget)
        self.label_door.setObjectName(u"label_door")

        self.verticalLayout.addWidget(self.label_door)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 186, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u667a\u80fd\u5bb6\u5c45\u63a7\u5236\u7cfb\u7edf\u540e\u53f0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55\u72b6\u6001", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u6e29\u5ea6\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u6e7f\u5ea6\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u667a\u80fd\u706f\u72b6\u6001\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8fdc\u7a0b\u63a7\u5236\u95e8\u72b6\u6001\uff1a", None))
        self.label_temp.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_hum.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_light.setText(QCoreApplication.translate("MainWindow", u"close", None))
        self.label_door.setText(QCoreApplication.translate("MainWindow", u"close", None))
    # retranslateUi

