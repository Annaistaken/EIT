# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(1500, 850))
        self.groupBox.setMaximumSize(QtCore.QSize(1500, 850))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuRTR = QtWidgets.QMenu(self.menubar)
        self.menuRTR.setObjectName("menuRTR")
        self.menuSave = QtWidgets.QMenu(self.menubar)
        self.menuSave.setObjectName("menuSave")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRefe = QtWidgets.QAction(MainWindow)
        self.actionRefe.setObjectName("actionRefe")
        self.actionData = QtWidgets.QAction(MainWindow)
        self.actionData.setObjectName("actionData")
        self.actionOpenBLE = QtWidgets.QAction(MainWindow)
        self.actionOpenBLE.setObjectName("actionOpenBLE")
        self.actionNowForRefe = QtWidgets.QAction(MainWindow)
        self.actionNowForRefe.setObjectName("actionNowForRefe")
        self.actionRun = QtWidgets.QAction(MainWindow)
        self.actionRun.setObjectName("actionRun")
        self.actionFrameNow = QtWidgets.QAction(MainWindow)
        self.actionFrameNow.setObjectName("actionFrameNow")
        self.actionStop = QtWidgets.QAction(MainWindow)
        self.actionStop.setObjectName("actionStop")
        self.menuFile.addAction(self.actionRefe)
        self.menuFile.addAction(self.actionData)
        self.menuRTR.addAction(self.actionOpenBLE)
        self.menuRTR.addAction(self.actionNowForRefe)
        self.menuRTR.addAction(self.actionRun)
        self.menuRTR.addAction(self.actionStop)
        self.menuSave.addAction(self.actionFrameNow)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRTR.menuAction())
        self.menubar.addAction(self.menuSave.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EIT"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuRTR.setTitle(_translate("MainWindow", "RTR"))
        self.menuSave.setTitle(_translate("MainWindow", "Save"))
        self.actionRefe.setText(_translate("MainWindow", "Refe"))
        self.actionData.setText(_translate("MainWindow", "Data"))
        self.actionOpenBLE.setText(_translate("MainWindow", "OpenBLE"))
        self.actionNowForRefe.setText(_translate("MainWindow", "NowForRefe"))
        self.actionRun.setText(_translate("MainWindow", "Run"))
        self.actionFrameNow.setText(_translate("MainWindow", "FrameNow"))
        self.actionStop.setText(_translate("MainWindow", "Stop"))
