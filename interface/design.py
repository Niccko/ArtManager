# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        MainWindow.setMinimumSize(QtCore.QSize(900, 700))
        MainWindow.setMaximumSize(QtCore.QSize(900, 700))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 180, 901, 25))
        self.frame.setStyleSheet("background-color: #474747;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 931, 731))
        self.frame_2.setStyleSheet("background-color: #2f2f2f;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lblPath = QtWidgets.QLabel(self.frame_2)
        self.lblPath.setGeometry(QtCore.QRect(20, 20, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(10)
        self.lblPath.setFont(font)
        self.lblPath.setStyleSheet("color: white;\n"
"background-color: transparent;")
        self.lblPath.setObjectName("lblPath")
        self.lblLastValidation = QtWidgets.QLabel(self.frame_2)
        self.lblLastValidation.setGeometry(QtCore.QRect(20, 40, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(10)
        self.lblLastValidation.setFont(font)
        self.lblLastValidation.setStyleSheet("color: white;\n"
"background-color: transparent;")
        self.lblLastValidation.setObjectName("lblLastValidation")
        self.btnInvalidate = QtWidgets.QPushButton(self.frame_2)
        self.btnInvalidate.setGeometry(QtCore.QRect(20, 70, 221, 23))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(9)
        self.btnInvalidate.setFont(font)
        self.btnInvalidate.setStyleSheet("background-color: #1f1f1f;\n"
"color: white;\n"
"border-radius: 3px;")
        self.btnInvalidate.setObjectName("btnInvalidate")
        self.lblCurrentGrouping = QtWidgets.QLabel(self.frame_2)
        self.lblCurrentGrouping.setGeometry(QtCore.QRect(20, 100, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(10)
        self.lblCurrentGrouping.setFont(font)
        self.lblCurrentGrouping.setStyleSheet("color: white;\n"
"background-color: transparent;")
        self.lblCurrentGrouping.setObjectName("lblCurrentGrouping")
        self.menuGrouping = QtWidgets.QComboBox(self.frame_2)
        self.menuGrouping.setGeometry(QtCore.QRect(20, 130, 181, 22))
        self.menuGrouping.setStyleSheet("background-color: #1f1f1f;\n"
"border: 2px solid darkgray;\n"
"selection-background-color: lightgray;")
        self.menuGrouping.setObjectName("menuGrouping")
        self.frame1 = QtWidgets.QFrame(self.frame_2)
        self.frame1.setGeometry(QtCore.QRect(10, 10, 241, 161))
        self.frame1.setStyleSheet("background-color: #474747;\n"
"")
        self.frame1.setObjectName("frame1")
        self.btnConfirmGrouping = QtWidgets.QPushButton(self.frame1)
        self.btnConfirmGrouping.setGeometry(QtCore.QRect(200, 120, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(9)
        self.btnConfirmGrouping.setFont(font)
        self.btnConfirmGrouping.setStyleSheet("background-color: #1f1f1f;\n"
"color: green;\n"
"border-radius: 3px;")
        self.btnConfirmGrouping.setObjectName("btnConfirmGrouping")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(260, 10, 381, 161))
        self.frame_3.setStyleSheet("background-color: #474747;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.btnCheckCorrupted = QtWidgets.QPushButton(self.frame_3)
        self.btnCheckCorrupted.setGeometry(QtCore.QRect(10, 10, 131, 23))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(9)
        self.btnCheckCorrupted.setFont(font)
        self.btnCheckCorrupted.setStyleSheet("background-color: #1f1f1f;\n"
"color: white;\n"
"border-radius: 3px;")
        self.btnCheckCorrupted.setObjectName("btnCheckCorrupted")
        self.lblCorrupted = QtWidgets.QLabel(self.frame_3)
        self.lblCorrupted.setGeometry(QtCore.QRect(150, 10, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(10)
        self.lblCorrupted.setFont(font)
        self.lblCorrupted.setStyleSheet("color: white;\n"
"background-color: transparent;")
        self.lblCorrupted.setObjectName("lblCorrupted")
        self.btnChooseSource = QtWidgets.QPushButton(self.frame_3)
        self.btnChooseSource.setGeometry(QtCore.QRect(10, 40, 131, 23))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(9)
        self.btnChooseSource.setFont(font)
        self.btnChooseSource.setStyleSheet("background-color: #1f1f1f;\n"
"color: white;\n"
"border-radius: 3px;")
        self.btnChooseSource.setObjectName("btnChooseSource")
        self.lblSource = QtWidgets.QLabel(self.frame_3)
        self.lblSource.setGeometry(QtCore.QRect(150, 40, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(10)
        self.lblSource.setFont(font)
        self.lblSource.setStyleSheet("color: white;\n"
"background-color: transparent;")
        self.lblSource.setObjectName("lblSource")
        self.btnLoad = QtWidgets.QPushButton(self.frame_3)
        self.btnLoad.setGeometry(QtCore.QRect(10, 70, 361, 23))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(9)
        self.btnLoad.setFont(font)
        self.btnLoad.setStyleSheet("background-color: #1f1f1f;\n"
"color: white;\n"
"border-radius: 3px;")
        self.btnLoad.setObjectName("btnLoad")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(650, 10, 241, 161))
        self.frame_4.setStyleSheet("background-color: #474747;\n"
"")
        self.frame_4.setObjectName("frame_4")
        self.frame.raise_()
        self.lblPath.raise_()
        self.lblLastValidation.raise_()
        self.btnInvalidate.raise_()
        self.lblCurrentGrouping.raise_()
        self.menuGrouping.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.frame_2.raise_()
        self.frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSelect_folder = QtWidgets.QAction(MainWindow)
        self.actionSelect_folder.setObjectName("actionSelect_folder")
        self.menuFile.addAction(self.actionSelect_folder)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblPath.setText(_translate("MainWindow", "Path: *"))
        self.lblLastValidation.setText(_translate("MainWindow", "Last validation: *"))
        self.btnInvalidate.setText(_translate("MainWindow", "Invalidate"))
        self.lblCurrentGrouping.setText(_translate("MainWindow", "Grouping: date"))
        self.btnConfirmGrouping.setText(_translate("MainWindow", "Ok"))
        self.btnCheckCorrupted.setText(_translate("MainWindow", "Check corrupted files"))
        self.lblCorrupted.setText(_translate("MainWindow", "Found * corrupted files"))
        self.btnChooseSource.setText(_translate("MainWindow", "Choose source"))
        self.lblSource.setText(_translate("MainWindow", "Source path: *"))
        self.btnLoad.setText(_translate("MainWindow", "Load"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSelect_folder.setText(_translate("MainWindow", "Select folder"))