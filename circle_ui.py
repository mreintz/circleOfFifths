# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\CircleOfFifths.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 736)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BaseLabel = QtWidgets.QLabel(self.centralwidget)
        self.BaseLabel.setGeometry(QtCore.QRect(80, 80, 501, 501))
        self.BaseLabel.setText("")
        self.BaseLabel.setPixmap(QtGui.QPixmap(":/images/circle.png"))
        self.BaseLabel.setScaledContents(True)
        self.BaseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BaseLabel.setObjectName("BaseLabel")
        self.CLabel = myLabel(self.centralwidget)
        self.CLabel.setGeometry(QtCore.QRect(300, 60, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.CLabel.setFont(font)
        self.CLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CLabel.setObjectName("CLabel")
        self.ALabel = myLabel(self.centralwidget)
        self.ALabel.setGeometry(QtCore.QRect(560, 300, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.ALabel.setFont(font)
        self.ALabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ALabel.setObjectName("ALabel")
        self.EbLabel = myLabel(self.centralwidget)
        self.EbLabel.setGeometry(QtCore.QRect(50, 300, 60, 51))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.EbLabel.setFont(font)
        self.EbLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.EbLabel.setObjectName("EbLabel")
        self.FsLabel = myLabel(self.centralwidget)
        self.FsLabel.setGeometry(QtCore.QRect(300, 550, 60, 51))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.FsLabel.setFont(font)
        self.FsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.FsLabel.setObjectName("FsLabel")
        self.GLabel = myLabel(self.centralwidget)
        self.GLabel.setGeometry(QtCore.QRect(430, 90, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.GLabel.setFont(font)
        self.GLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GLabel.setObjectName("GLabel")
        self.DLabel = myLabel(self.centralwidget)
        self.DLabel.setGeometry(QtCore.QRect(520, 180, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.DLabel.setFont(font)
        self.DLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DLabel.setObjectName("DLabel")
        self.ELabel = myLabel(self.centralwidget)
        self.ELabel.setGeometry(QtCore.QRect(520, 430, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.ELabel.setFont(font)
        self.ELabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ELabel.setObjectName("ELabel")
        self.BLabel = myLabel(self.centralwidget)
        self.BLabel.setGeometry(QtCore.QRect(440, 520, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.BLabel.setFont(font)
        self.BLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BLabel.setObjectName("BLabel")
        self.DbLabel = myLabel(self.centralwidget)
        self.DbLabel.setGeometry(QtCore.QRect(160, 520, 60, 51))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.DbLabel.setFont(font)
        self.DbLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DbLabel.setObjectName("DbLabel")
        self.AbLabel = myLabel(self.centralwidget)
        self.AbLabel.setGeometry(QtCore.QRect(80, 430, 60, 51))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.AbLabel.setFont(font)
        self.AbLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AbLabel.setObjectName("AbLabel")
        self.BbLabel = myLabel(self.centralwidget)
        self.BbLabel.setGeometry(QtCore.QRect(80, 180, 60, 51))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.BbLabel.setFont(font)
        self.BbLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BbLabel.setObjectName("BbLabel")
        self.FLabel = myLabel(self.centralwidget)
        self.FLabel.setGeometry(QtCore.QRect(170, 90, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.FLabel.setFont(font)
        self.FLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.FLabel.setObjectName("FLabel")
        self.SharpFlatLabel = myLabel(self.centralwidget)
        self.SharpFlatLabel.setGeometry(QtCore.QRect(300, 300, 60, 51))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.SharpFlatLabel.setFont(font)
        self.SharpFlatLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SharpFlatLabel.setObjectName("SharpFlatLabel")
        self.chordLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.chordLabel1.setGeometry(QtCore.QRect(400, 150, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chordLabel1.setFont(font)
        self.chordLabel1.setText("")
        self.chordLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.chordLabel1.setObjectName("chordLabel1")
        self.chordLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.chordLabel2.setGeometry(QtCore.QRect(470, 220, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chordLabel2.setFont(font)
        self.chordLabel2.setText("")
        self.chordLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.chordLabel2.setObjectName("chordLabel2")
        self.chordLabel3 = QtWidgets.QLabel(self.centralwidget)
        self.chordLabel3.setGeometry(QtCore.QRect(490, 300, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chordLabel3.setFont(font)
        self.chordLabel3.setText("")
        self.chordLabel3.setAlignment(QtCore.Qt.AlignCenter)
        self.chordLabel3.setObjectName("chordLabel3")
        self.chordLabel4 = QtWidgets.QLabel(self.centralwidget)
        self.chordLabel4.setGeometry(QtCore.QRect(460, 400, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chordLabel4.setFont(font)
        self.chordLabel4.setText("")
        self.chordLabel4.setAlignment(QtCore.Qt.AlignCenter)
        self.chordLabel4.setObjectName("chordLabel4")
        self.chordLabel5 = QtWidgets.QLabel(self.centralwidget)
        self.chordLabel5.setGeometry(QtCore.QRect(410, 460, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chordLabel5.setFont(font)
        self.chordLabel5.setText("")
        self.chordLabel5.setAlignment(QtCore.Qt.AlignCenter)
        self.chordLabel5.setObjectName("chordLabel5")
        self.chordLabel6 = QtWidgets.QLabel(self.centralwidget)
        self.chordLabel6.setGeometry(QtCore.QRect(310, 490, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chordLabel6.setFont(font)
        self.chordLabel6.setText("")
        self.chordLabel6.setAlignment(QtCore.Qt.AlignCenter)
        self.chordLabel6.setObjectName("chordLabel6")
        self.chordLabel7 = QtWidgets.QLabel(self.centralwidget)
        self.chordLabel7.setGeometry(QtCore.QRect(210, 460, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chordLabel7.setFont(font)
        self.chordLabel7.setText("")
        self.chordLabel7.setAlignment(QtCore.Qt.AlignCenter)
        self.chordLabel7.setObjectName("chordLabel7")
        self.chordLabel8 = QtWidgets.QLabel(self.centralwidget)
        self.chordLabel8.setGeometry(QtCore.QRect(150, 400, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chordLabel8.setFont(font)
        self.chordLabel8.setText("")
        self.chordLabel8.setAlignment(QtCore.Qt.AlignCenter)
        self.chordLabel8.setObjectName("chordLabel8")
        self.chordLabel9 = QtWidgets.QLabel(self.centralwidget)
        self.chordLabel9.setGeometry(QtCore.QRect(120, 300, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chordLabel9.setFont(font)
        self.chordLabel9.setText("")
        self.chordLabel9.setAlignment(QtCore.Qt.AlignCenter)
        self.chordLabel9.setObjectName("chordLabel9")
        self.chordLabel10 = QtWidgets.QLabel(self.centralwidget)
        self.chordLabel10.setGeometry(QtCore.QRect(140, 220, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chordLabel10.setFont(font)
        self.chordLabel10.setText("")
        self.chordLabel10.setAlignment(QtCore.Qt.AlignCenter)
        self.chordLabel10.setObjectName("chordLabel10")
        self.chordLabel11 = QtWidgets.QLabel(self.centralwidget)
        self.chordLabel11.setGeometry(QtCore.QRect(210, 150, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chordLabel11.setFont(font)
        self.chordLabel11.setText("")
        self.chordLabel11.setAlignment(QtCore.Qt.AlignCenter)
        self.chordLabel11.setObjectName("chordLabel11")
        self.chordLabel0 = QtWidgets.QLabel(self.centralwidget)
        self.chordLabel0.setGeometry(QtCore.QRect(300, 120, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chordLabel0.setFont(font)
        self.chordLabel0.setText("")
        self.chordLabel0.setAlignment(QtCore.Qt.AlignCenter)
        self.chordLabel0.setObjectName("chordLabel0")
        self.modeBox = myDropdown(self.centralwidget)
        self.modeBox.setGeometry(QtCore.QRect(70, 16, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.modeBox.setFont(font)
        self.modeBox.setObjectName("modeBox")
        self.keyLabel = QtWidgets.QLabel(self.centralwidget)
        self.keyLabel.setGeometry(QtCore.QRect(10, 10, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.keyLabel.setFont(font)
        self.keyLabel.setText("")
        self.keyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.keyLabel.setObjectName("keyLabel")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 650, 651, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.onechord = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.onechord.setFont(font)
        self.onechord.setText("")
        self.onechord.setAlignment(QtCore.Qt.AlignCenter)
        self.onechord.setObjectName("onechord")
        self.horizontalLayout.addWidget(self.onechord)
        self.twochord = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.twochord.setFont(font)
        self.twochord.setText("")
        self.twochord.setAlignment(QtCore.Qt.AlignCenter)
        self.twochord.setObjectName("twochord")
        self.horizontalLayout.addWidget(self.twochord)
        self.threechord = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.threechord.setFont(font)
        self.threechord.setText("")
        self.threechord.setAlignment(QtCore.Qt.AlignCenter)
        self.threechord.setObjectName("threechord")
        self.horizontalLayout.addWidget(self.threechord)
        self.fourchord = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fourchord.setFont(font)
        self.fourchord.setText("")
        self.fourchord.setAlignment(QtCore.Qt.AlignCenter)
        self.fourchord.setObjectName("fourchord")
        self.horizontalLayout.addWidget(self.fourchord)
        self.fivechord = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fivechord.setFont(font)
        self.fivechord.setText("")
        self.fivechord.setAlignment(QtCore.Qt.AlignCenter)
        self.fivechord.setObjectName("fivechord")
        self.horizontalLayout.addWidget(self.fivechord)
        self.sixchord = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sixchord.setFont(font)
        self.sixchord.setText("")
        self.sixchord.setAlignment(QtCore.Qt.AlignCenter)
        self.sixchord.setObjectName("sixchord")
        self.horizontalLayout.addWidget(self.sixchord)
        self.sevenchord = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sevenchord.setFont(font)
        self.sevenchord.setText("")
        self.sevenchord.setAlignment(QtCore.Qt.AlignCenter)
        self.sevenchord.setObjectName("sevenchord")
        self.horizontalLayout.addWidget(self.sevenchord)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(459, 15, 201, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.modeSlider = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.modeSlider.setMaximum(1)
        self.modeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.modeSlider.setTickInterval(0)
        self.modeSlider.setObjectName("modeSlider")
        self.horizontalLayout_2.addWidget(self.modeSlider)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 680, 651, 31))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.onechord_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.onechord_2.setFont(font)
        self.onechord_2.setText("")
        self.onechord_2.setAlignment(QtCore.Qt.AlignCenter)
        self.onechord_2.setObjectName("onechord_2")
        self.horizontalLayout_3.addWidget(self.onechord_2)
        self.twochord_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.twochord_2.setFont(font)
        self.twochord_2.setText("")
        self.twochord_2.setAlignment(QtCore.Qt.AlignCenter)
        self.twochord_2.setObjectName("twochord_2")
        self.horizontalLayout_3.addWidget(self.twochord_2)
        self.threechord_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.threechord_2.setFont(font)
        self.threechord_2.setText("")
        self.threechord_2.setAlignment(QtCore.Qt.AlignCenter)
        self.threechord_2.setObjectName("threechord_2")
        self.horizontalLayout_3.addWidget(self.threechord_2)
        self.fourchord_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fourchord_2.setFont(font)
        self.fourchord_2.setText("")
        self.fourchord_2.setAlignment(QtCore.Qt.AlignCenter)
        self.fourchord_2.setObjectName("fourchord_2")
        self.horizontalLayout_3.addWidget(self.fourchord_2)
        self.fivechord_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fivechord_2.setFont(font)
        self.fivechord_2.setText("")
        self.fivechord_2.setAlignment(QtCore.Qt.AlignCenter)
        self.fivechord_2.setObjectName("fivechord_2")
        self.horizontalLayout_3.addWidget(self.fivechord_2)
        self.sixchord_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sixchord_2.setFont(font)
        self.sixchord_2.setText("")
        self.sixchord_2.setAlignment(QtCore.Qt.AlignCenter)
        self.sixchord_2.setObjectName("sixchord_2")
        self.horizontalLayout_3.addWidget(self.sixchord_2)
        self.sevenchord_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sevenchord_2.setFont(font)
        self.sevenchord_2.setText("")
        self.sevenchord_2.setAlignment(QtCore.Qt.AlignCenter)
        self.sevenchord_2.setObjectName("sevenchord_2")
        self.horizontalLayout_3.addWidget(self.sevenchord_2)
        self.ScaleLabel = QtWidgets.QLabel(self.centralwidget)
        self.ScaleLabel.setGeometry(QtCore.QRect(10, 620, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ScaleLabel.setFont(font)
        self.ScaleLabel.setText("")
        self.ScaleLabel.setObjectName("ScaleLabel")
        self.frameOfProgressions = QtWidgets.QFrame(self.centralwidget)
        self.frameOfProgressions.setGeometry(QtCore.QRect(190, 250, 291, 151))
        self.frameOfProgressions.setStyleSheet("border:0")
        self.frameOfProgressions.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameOfProgressions.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameOfProgressions.setObjectName("frameOfProgressions")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frameOfProgressions)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-10, 0, 301, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.boxOfProgressions = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.boxOfProgressions.setContentsMargins(0, 0, 0, 0)
        self.boxOfProgressions.setObjectName("boxOfProgressions")
        self.prog2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.prog2.setMinimumSize(QtCore.QSize(0, 0))
        self.prog2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.prog2.setFont(font)
        self.prog2.setText("")
        self.prog2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.prog2.setObjectName("prog2")
        self.boxOfProgressions.addWidget(self.prog2, 1, 0, 1, 1)
        self.chordprog3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.chordprog3.setFont(font)
        self.chordprog3.setText("")
        self.chordprog3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.chordprog3.setObjectName("chordprog3")
        self.boxOfProgressions.addWidget(self.chordprog3, 2, 2, 1, 1)
        self.prog3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.prog3.setMinimumSize(QtCore.QSize(0, 0))
        self.prog3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.prog3.setFont(font)
        self.prog3.setText("")
        self.prog3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.prog3.setObjectName("prog3")
        self.boxOfProgressions.addWidget(self.prog3, 2, 0, 1, 1)
        self.prog4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.prog4.setMinimumSize(QtCore.QSize(0, 0))
        self.prog4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.prog4.setFont(font)
        self.prog4.setText("")
        self.prog4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.prog4.setObjectName("prog4")
        self.boxOfProgressions.addWidget(self.prog4, 3, 0, 1, 1)
        self.prog1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.prog1.setMinimumSize(QtCore.QSize(0, 0))
        self.prog1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.prog1.setFont(font)
        self.prog1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.prog1.setObjectName("prog1")
        self.boxOfProgressions.addWidget(self.prog1, 0, 0, 1, 1)
        self.chordprog2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.chordprog2.setFont(font)
        self.chordprog2.setText("")
        self.chordprog2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.chordprog2.setObjectName("chordprog2")
        self.boxOfProgressions.addWidget(self.chordprog2, 1, 2, 1, 1)
        self.chordprog1 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.chordprog1.setFont(font)
        self.chordprog1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.chordprog1.setObjectName("chordprog1")
        self.boxOfProgressions.addWidget(self.chordprog1, 0, 2, 1, 1)
        self.chordprog4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.chordprog4.setFont(font)
        self.chordprog4.setText("")
        self.chordprog4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.chordprog4.setObjectName("chordprog4")
        self.boxOfProgressions.addWidget(self.chordprog4, 3, 2, 1, 1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(460, 600, 201, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.sharpsProgSlider = QtWidgets.QSlider(self.horizontalLayoutWidget_2)
        self.sharpsProgSlider.setMaximum(1)
        self.sharpsProgSlider.setOrientation(QtCore.Qt.Horizontal)
        self.sharpsProgSlider.setTickInterval(0)
        self.sharpsProgSlider.setObjectName("sharpsProgSlider")
        self.horizontalLayout_4.addWidget(self.sharpsProgSlider)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 674, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Circle of Fifths"))
        self.CLabel.setText(_translate("MainWindow", "C"))
        self.ALabel.setText(_translate("MainWindow", "A"))
        self.EbLabel.setText(_translate("MainWindow", "E<sub>♭</sub>"))
        self.FsLabel.setText(_translate("MainWindow", "F<sup>♯</sup>"))
        self.GLabel.setText(_translate("MainWindow", "G"))
        self.DLabel.setText(_translate("MainWindow", "D"))
        self.ELabel.setText(_translate("MainWindow", "E"))
        self.BLabel.setText(_translate("MainWindow", "B"))
        self.DbLabel.setText(_translate("MainWindow", "D<sub>♭</sub>"))
        self.AbLabel.setText(_translate("MainWindow", "A<sub>♭</sub>"))
        self.BbLabel.setText(_translate("MainWindow", "B<sub>♭</sub>"))
        self.FLabel.setText(_translate("MainWindow", "F"))
        self.SharpFlatLabel.setText(_translate("MainWindow", "♯"))
        self.label_2.setText(_translate("MainWindow", "Key"))
        self.label.setText(_translate("MainWindow", "Chord"))
        self.prog1.setText(_translate("MainWindow", "I - IV - V"))
        self.chordprog1.setText(_translate("MainWindow", "C - F - G"))
        self.label_3.setText(_translate("MainWindow", "♯ / ♭"))
        self.label_4.setText(_translate("MainWindow", "I - IV - V"))
from mydropdown import myDropdown
from mylabel import myLabel
import CircleOfFifths_rc
