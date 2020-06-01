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
        self.menuAlgorithm = QtWidgets.QMenu(self.menubar)
        self.menuAlgorithm.setObjectName("menuAlgorithm")
        self.menuDisplay = QtWidgets.QMenu(self.menubar)
        self.menuDisplay.setObjectName("menuDisplay")
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
        self.actionProjNow = QtWidgets.QAction(MainWindow)
        self.actionProjNow.setObjectName("actionProjNow")
        self.actionSVD = QtWidgets.QAction(MainWindow)
        self.actionSVD.setObjectName("actionSVD")
        self.actionLBP = QtWidgets.QAction(MainWindow)
        self.actionLBP.setObjectName("actionLBP")
        self.actionNormalized_Sensitivity = QtWidgets.QAction(MainWindow)
        self.actionNormalized_Sensitivity.setObjectName("actionNormalized_Sensitivity")
        self.actionCG = QtWidgets.QAction(MainWindow)
        self.actionCG.setObjectName("actionCG")
        self.actionBFGS = QtWidgets.QAction(MainWindow)
        self.actionBFGS.setObjectName("actionBFGS")
        self.actionSLSQP = QtWidgets.QAction(MainWindow)
        self.actionSLSQP.setObjectName("actionSLSQP")
        self.actionLanczos = QtWidgets.QAction(MainWindow)
        self.actionLanczos.setObjectName("actionLanczos")
        self.actionTikhonov = QtWidgets.QAction(MainWindow)
        self.actionTikhonov.setObjectName("actionTikhonov")
        self.actionLasso = QtWidgets.QAction(MainWindow)
        self.actionLasso.setObjectName("actionLasso")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSensitivityMat = QtWidgets.QAction(MainWindow)
        self.actionSensitivityMat.setObjectName("actionSensitivityMat")
        self.actionFE_Filling = QtWidgets.QAction(MainWindow)
        self.actionFE_Filling.setObjectName("actionFE_Filling")
        self.actionNephogram = QtWidgets.QAction(MainWindow)
        self.actionNephogram.setObjectName("actionNephogram")
        self.actionIsogram = QtWidgets.QAction(MainWindow)
        self.actionIsogram.setObjectName("actionIsogram")
        self.actionShading_Interp = QtWidgets.QAction(MainWindow)
        self.actionShading_Interp.setObjectName("actionShading_Interp")
        self.actionContour_Filling = QtWidgets.QAction(MainWindow)
        self.actionContour_Filling.setObjectName("actionContour_Filling")
        self.actionBLEdata = QtWidgets.QAction(MainWindow)
        self.actionBLEdata.setObjectName("actionBLEdata")
        self.menuFile.addAction(self.actionRefe)
        self.menuFile.addAction(self.actionData)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuRTR.addAction(self.actionOpenBLE)
        self.menuRTR.addAction(self.actionNowForRefe)
        self.menuRTR.addAction(self.actionRun)
        self.menuRTR.addAction(self.actionStop)
        self.menuSave.addAction(self.actionFrameNow)
        self.menuSave.addAction(self.actionBLEdata)
        self.menuAlgorithm.addAction(self.actionLBP)
        self.menuAlgorithm.addAction(self.actionSVD)
        self.menuAlgorithm.addAction(self.actionNormalized_Sensitivity)
        self.menuAlgorithm.addSeparator()
        self.menuAlgorithm.addAction(self.actionCG)
        self.menuAlgorithm.addAction(self.actionBFGS)
        self.menuAlgorithm.addAction(self.actionSLSQP)
        self.menuAlgorithm.addAction(self.actionLanczos)
        self.menuAlgorithm.addSeparator()
        self.menuAlgorithm.addAction(self.actionTikhonov)
        self.menuDisplay.addAction(self.actionFE_Filling)
        self.menuDisplay.addAction(self.actionShading_Interp)
        self.menuDisplay.addAction(self.actionContour_Filling)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRTR.menuAction())
        self.menubar.addAction(self.menuAlgorithm.menuAction())
        self.menubar.addAction(self.menuDisplay.menuAction())
        self.menubar.addAction(self.menuSave.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EIT"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuRTR.setTitle(_translate("MainWindow", "RTR"))
        self.menuSave.setTitle(_translate("MainWindow", "Save"))
        self.menuAlgorithm.setTitle(_translate("MainWindow", "Algorithm"))
        self.menuDisplay.setTitle(_translate("MainWindow", "Display"))
        self.actionRefe.setText(_translate("MainWindow", "Refe"))
        self.actionData.setText(_translate("MainWindow", "Data"))
        self.actionOpenBLE.setText(_translate("MainWindow", "OpenBLE"))
        self.actionNowForRefe.setText(_translate("MainWindow", "NowForRefe"))
        self.actionRun.setText(_translate("MainWindow", "Run"))
        self.actionFrameNow.setText(_translate("MainWindow", "FrameNow"))
        self.actionStop.setText(_translate("MainWindow", "Stop"))
        self.actionProjNow.setText(_translate("MainWindow", "ProjNow"))
        self.actionSVD.setText(_translate("MainWindow", "SVD"))
        self.actionLBP.setText(_translate("MainWindow", "LBP"))
        self.actionNormalized_Sensitivity.setText(_translate("MainWindow", "Normalized Sensitivity"))
        self.actionCG.setText(_translate("MainWindow", "CG"))
        self.actionBFGS.setText(_translate("MainWindow", "BFGS"))
        self.actionSLSQP.setText(_translate("MainWindow", "SLSQP"))
        self.actionLanczos.setText(_translate("MainWindow", "Lanczos"))
        self.actionTikhonov.setText(_translate("MainWindow", "Tikhonov regularization"))
        self.actionLasso.setText(_translate("MainWindow", "Lasso"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSensitivityMat.setText(_translate("MainWindow", "SensitivityMat"))
        self.actionFE_Filling.setText(_translate("MainWindow", "FE Filling"))
        self.actionNephogram.setText(_translate("MainWindow", "Nephogram"))
        self.actionIsogram.setText(_translate("MainWindow", "Isogram"))
        self.actionShading_Interp.setText(_translate("MainWindow", "Shading Interp"))
        self.actionContour_Filling.setText(_translate("MainWindow", "Contour Filling"))
        self.actionBLEdata.setText(_translate("MainWindow", "BLEdata"))