# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fretboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from overloadedQtClasses import QLineEditTabReact


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2111, 717)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(220, 40, 1311, 272))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tuning_5 = QLineEditTabReact(self.gridLayoutWidget)
        self.tuning_5.setMinimumSize(QtCore.QSize(40, 40))
        self.tuning_5.setMaximumSize(QtCore.QSize(40, 16777215))
        self.tuning_5.setAlignment(QtCore.Qt.AlignCenter)
        self.tuning_5.setObjectName("tuning_5")
        self.gridLayout.addWidget(self.tuning_5, 4, 0, 1, 1)
        self.tuning_6 = QLineEditTabReact(self.gridLayoutWidget)
        self.tuning_6.setMinimumSize(QtCore.QSize(40, 40))
        self.tuning_6.setMaximumSize(QtCore.QSize(40, 16777215))
        self.tuning_6.setAlignment(QtCore.Qt.AlignCenter)
        self.tuning_6.setObjectName("tuning_6")
        self.gridLayout.addWidget(self.tuning_6, 5, 0, 1, 1)
        self.tuning_4 = QLineEditTabReact(self.gridLayoutWidget)
        self.tuning_4.setMinimumSize(QtCore.QSize(40, 40))
        self.tuning_4.setMaximumSize(QtCore.QSize(40, 16777215))
        self.tuning_4.setAlignment(QtCore.Qt.AlignCenter)
        self.tuning_4.setObjectName("tuning_4")
        self.gridLayout.addWidget(self.tuning_4, 3, 0, 1, 1)
        self.tuning_2 = QLineEditTabReact(self.gridLayoutWidget)
        self.tuning_2.setMinimumSize(QtCore.QSize(40, 40))
        self.tuning_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.tuning_2.setAlignment(QtCore.Qt.AlignCenter)
        self.tuning_2.setObjectName("tuning_2")
        self.gridLayout.addWidget(self.tuning_2, 1, 0, 1, 1)
        self.tuning_1 = QLineEditTabReact(self.gridLayoutWidget)
        self.tuning_1.setMinimumSize(QtCore.QSize(40, 40))
        self.tuning_1.setMaximumSize(QtCore.QSize(40, 16777215))
        self.tuning_1.setAlignment(QtCore.Qt.AlignCenter)
        self.tuning_1.setObjectName("tuning_1")
        self.gridLayout.addWidget(self.tuning_1, 0, 0, 1, 1)
        self.tuning_3 = QLineEditTabReact(self.gridLayoutWidget)
        self.tuning_3.setMinimumSize(QtCore.QSize(40, 40))
        self.tuning_3.setMaximumSize(QtCore.QSize(40, 16777215))
        self.tuning_3.setAlignment(QtCore.Qt.AlignCenter)
        self.tuning_3.setObjectName("tuning_3")
        self.gridLayout.addWidget(self.tuning_3, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tuning_1, self.tuning_2)
        MainWindow.setTabOrder(self.tuning_2, self.tuning_3)
        MainWindow.setTabOrder(self.tuning_3, self.tuning_4)
        MainWindow.setTabOrder(self.tuning_4, self.tuning_5)
        MainWindow.setTabOrder(self.tuning_5, self.tuning_6)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

