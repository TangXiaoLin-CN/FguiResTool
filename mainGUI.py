# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\pyProject\FguiResTool\gui/mainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 588)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(0, 520, 75, 23))
        self.btnSearch.setObjectName("btnSearch")
        self.listShow = QtWidgets.QListView(self.centralwidget)
        self.listShow.setGeometry(QtCore.QRect(280, 0, 271, 391))
        self.listShow.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listShow.setObjectName("listShow")
        self.listAll = QtWidgets.QListView(self.centralwidget)
        self.listAll.setGeometry(QtCore.QRect(0, 0, 269, 331))
        self.listAll.setObjectName("listAll")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 440, 271, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnSave = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnSave.setObjectName("btnSave")
        self.verticalLayout.addWidget(self.btnSave)
        self.btnMerge = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnMerge.setObjectName("btnMerge")
        self.verticalLayout.addWidget(self.btnMerge)
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.setGeometry(QtCore.QRect(470, 520, 75, 23))
        self.btnClose.setObjectName("btnClose")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 340, 271, 171))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setObjectName("groupBox")
        self.labelImg = QtWidgets.QLabel(self.groupBox)
        self.labelImg.setGeometry(QtCore.QRect(10, 20, 251, 141))
        self.labelImg.setAutoFillBackground(False)
        self.labelImg.setText("")
        self.labelImg.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImg.setObjectName("labelImg")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(420, 400, 125, 38))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnSelectAll = QtWidgets.QToolButton(self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/全选.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSelectAll.setIcon(icon1)
        self.btnSelectAll.setIconSize(QtCore.QSize(30, 30))
        self.btnSelectAll.setObjectName("btnSelectAll")
        self.horizontalLayout.addWidget(self.btnSelectAll)
        self.btnReverse = QtWidgets.QToolButton(self.layoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/反选.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReverse.setIcon(icon2)
        self.btnReverse.setIconSize(QtCore.QSize(30, 30))
        self.btnReverse.setObjectName("btnReverse")
        self.horizontalLayout.addWidget(self.btnReverse)
        self.btnCancelAll = QtWidgets.QToolButton(self.layoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/取消.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelAll.setIcon(icon3)
        self.btnCancelAll.setIconSize(QtCore.QSize(30, 30))
        self.btnCancelAll.setObjectName("btnCancelAll")
        self.horizontalLayout.addWidget(self.btnCancelAll)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(560, 0, 271, 541))
        self.groupBox_2.setObjectName("groupBox_2")
        self.listRef = QtWidgets.QListView(self.groupBox_2)
        self.listRef.setGeometry(QtCore.QRect(0, 20, 271, 521))
        self.listRef.setObjectName("listRef")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnSearch.setText(_translate("MainWindow", "搜索"))
        self.btnSave.setText(_translate("MainWindow", "设置为保留资源"))
        self.btnMerge.setText(_translate("MainWindow", "合并选中资源"))
        self.btnClose.setText(_translate("MainWindow", "关闭"))
        self.groupBox.setTitle(_translate("MainWindow", "图片预览"))
        self.btnSelectAll.setToolTip(_translate("MainWindow", "全选"))
        self.btnSelectAll.setText(_translate("MainWindow", "..."))
        self.btnReverse.setToolTip(_translate("MainWindow", "反向选择"))
        self.btnReverse.setText(_translate("MainWindow", "..."))
        self.btnCancelAll.setToolTip(_translate("MainWindow", "取消全选"))
        self.btnCancelAll.setText(_translate("MainWindow", "..."))
        self.groupBox_2.setTitle(_translate("MainWindow", "依赖引用"))
import res_rc
