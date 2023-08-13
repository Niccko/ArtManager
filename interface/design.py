# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\interface\design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1662, 891)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridFrame = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame.setGeometry(QtCore.QRect(10, 10, 431, 131))
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.txt_target_path = QtWidgets.QTextEdit(self.gridFrame)
        self.txt_target_path.setObjectName("txt_target_path")
        self.gridLayout.addWidget(self.txt_target_path, 3, 0, 1, 1)
        self.txt_source_path = QtWidgets.QTextEdit(self.gridFrame)
        self.txt_source_path.setEnabled(True)
        self.txt_source_path.setObjectName("txt_source_path")
        self.gridLayout.addWidget(self.txt_source_path, 1, 0, 1, 1)
        self.btn_target_path = QtWidgets.QPushButton(self.gridFrame)
        self.btn_target_path.setObjectName("btn_target_path")
        self.gridLayout.addWidget(self.btn_target_path, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridFrame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.btn_source_path = QtWidgets.QPushButton(self.gridFrame)
        self.btn_source_path.setObjectName("btn_source_path")
        self.gridLayout.addWidget(self.btn_source_path, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridFrame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 220, 381, 611))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lst_doubles_src = QtWidgets.QListWidget(self.tab)
        self.lst_doubles_src.setGeometry(QtCore.QRect(0, 0, 371, 581))
        self.lst_doubles_src.setObjectName("lst_doubles_src")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lst_doubles_trg = QtWidgets.QListWidget(self.tab_2)
        self.lst_doubles_trg.setGeometry(QtCore.QRect(0, 0, 371, 632))
        self.lst_doubles_trg.setObjectName("lst_doubles_trg")
        self.tabWidget.addTab(self.tab_2, "")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 140, 395, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridFrame1 = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame1.setGeometry(QtCore.QRect(470, 30, 221, 101))
        self.gridFrame1.setObjectName("gridFrame1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridFrame1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_compute_target = QtWidgets.QPushButton(self.gridFrame1)
        self.btn_compute_target.setObjectName("btn_compute_target")
        self.gridLayout_2.addWidget(self.btn_compute_target, 0, 0, 1, 1)
        self.btn_compute_source = QtWidgets.QPushButton(self.gridFrame1)
        self.btn_compute_source.setObjectName("btn_compute_source")
        self.gridLayout_2.addWidget(self.btn_compute_source, 1, 0, 1, 1)
        self.btn_compare = QtWidgets.QPushButton(self.gridFrame1)
        self.btn_compare.setObjectName("btn_compare")
        self.gridLayout_2.addWidget(self.btn_compare, 2, 0, 1, 1)
        self.lbl_status = QtWidgets.QLabel(self.centralwidget)
        self.lbl_status.setGeometry(QtCore.QRect(420, 140, 471, 23))
        self.lbl_status.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbl_status.setStyleSheet("background: rgb(255, 255, 255)")
        self.lbl_status.setText("")
        self.lbl_status.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_status.setObjectName("lbl_status")
        self.lbl_src_meta_status = QtWidgets.QLabel(self.centralwidget)
        self.lbl_src_meta_status.setGeometry(QtCore.QRect(720, 30, 81, 91))
        self.lbl_src_meta_status.setStyleSheet("background: rgb(255, 255, 255)")
        self.lbl_src_meta_status.setText("")
        self.lbl_src_meta_status.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_src_meta_status.setObjectName("lbl_src_meta_status")
        self.lbl_trg_meta_status = QtWidgets.QLabel(self.centralwidget)
        self.lbl_trg_meta_status.setGeometry(QtCore.QRect(810, 30, 81, 91))
        self.lbl_trg_meta_status.setStyleSheet("background: rgb(255, 255, 255)")
        self.lbl_trg_meta_status.setText("")
        self.lbl_trg_meta_status.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_trg_meta_status.setObjectName("lbl_trg_meta_status")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(726, 10, 71, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(815, 10, 71, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(550, 10, 71, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.lbl_image = QtWidgets.QLabel(self.centralwidget)
        self.lbl_image.setGeometry(QtCore.QRect(910, 10, 741, 821))
        self.lbl_image.setStyleSheet("background: rgb(255, 255, 255)")
        self.lbl_image.setText("")
        self.lbl_image.setObjectName("lbl_image")
        self.lst_doubles_info = QtWidgets.QListWidget(self.centralwidget)
        self.lst_doubles_info.setGeometry(QtCore.QRect(390, 246, 501, 581))
        self.lst_doubles_info.setObjectName("lst_doubles_info")
        self.btn_delete_marked = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete_marked.setGeometry(QtCore.QRect(420, 180, 151, 31))
        self.btn_delete_marked.setObjectName("btn_delete_marked")
        self.btn_start_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start_load.setGeometry(QtCore.QRect(580, 180, 151, 31))
        self.btn_start_load.setObjectName("btn_start_load")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1662, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_target_path.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "Source folder"))
        self.btn_source_path.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Target folder"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Source"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Target"))
        self.btn_compute_target.setText(_translate("MainWindow", "Compute target hashes"))
        self.btn_compute_source.setText(_translate("MainWindow", "Compute source hashes"))
        self.btn_compare.setText(_translate("MainWindow", "Compare folders"))
        self.label_3.setText(_translate("MainWindow", "Source meta"))
        self.label_4.setText(_translate("MainWindow", "Target meta"))
        self.label_5.setText(_translate("MainWindow", "Hashing"))
        self.btn_delete_marked.setText(_translate("MainWindow", "Delete marked"))
        self.btn_start_load.setText(_translate("MainWindow", "Load"))
