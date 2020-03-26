# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imgGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EIT_RTR(object):
    def setupUi(self, EIT_RTR):
        EIT_RTR.setObjectName("EIT_RTR")
        EIT_RTR.resize(1000, 800)
        self.gridLayout = QtWidgets.QGridLayout(EIT_RTR)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(EIT_RTR)
        self.widget.setMinimumSize(QtCore.QSize(500, 500))
        self.widget.setMaximumSize(QtCore.QSize(500, 500))
        self.widget.setObjectName("widget")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.groupBox.setMinimumSize(QtCore.QSize(500, 500))
        self.groupBox.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout.addWidget(self.widget, 0, 0, 3, 1)
        self.startButton = QtWidgets.QPushButton(EIT_RTR)
        self.startButton.setMinimumSize(QtCore.QSize(200, 80))
        self.startButton.setMaximumSize(QtCore.QSize(200, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.gridLayout.addWidget(self.startButton, 0, 1, 1, 1)
        self.saveButton = QtWidgets.QPushButton(EIT_RTR)
        self.saveButton.setMinimumSize(QtCore.QSize(200, 80))
        self.saveButton.setMaximumSize(QtCore.QSize(200, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 1, 1, 1, 1)
        self.closeButton = QtWidgets.QPushButton(EIT_RTR)
        self.closeButton.setMinimumSize(QtCore.QSize(200, 80))
        self.closeButton.setMaximumSize(QtCore.QSize(200, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        self.closeButton.setFont(font)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 2, 1, 1, 1)

        self.retranslateUi(EIT_RTR)
        QtCore.QMetaObject.connectSlotsByName(EIT_RTR)

    def retranslateUi(self, EIT_RTR):
        _translate = QtCore.QCoreApplication.translate
        EIT_RTR.setWindowTitle(_translate("EIT_RTR", "Form"))
        self.startButton.setText(_translate("EIT_RTR", "start"))
        self.saveButton.setText(_translate("EIT_RTR", "save"))
        self.closeButton.setText(_translate("EIT_RTR", "close"))
