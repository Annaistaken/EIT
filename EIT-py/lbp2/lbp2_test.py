# -*- coding:utf-8 -*-
import numpy as np
import sys
import time
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget,  QGridLayout

from imgGUI import Ui_EIT_RTR
matplotlib.use("Qt5Agg")
D=np.load("smat.npz")
S = [np.zeros((33, 33)) for i in range(8)]
backproj = np.zeros((33, 33))

global a
a = 0
def start():
    global a
    a = 1
def close():
    global a
    a = 0
def save():
    plt.savefig('frame_now.png')

class MyFigure(FigureCanvas):
    def __init__(self,width, height, dpi):
        self.fig = plt.figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot()
        self.axes.set_title("EIT-realtime-image")
        plt.axis('off')
        super(MyFigure,self).__init__(self.fig)

class MyWindow(QWidget, Ui_EIT_RTR):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.F = MyFigure(width=3, height=2, dpi=100)
        self.gridlayout = QGridLayout(self.groupBox)
        self.gridlayout.addWidget(self.F, 0, 1)

    def update_item_data(self, data):
        plt.ion()
        self.F.axes.imshow(data, interpolation='none', cmap=matplotlib.cm.RdBu)
        #QApplication.processEvents()

class UpdateData(QThread):

    update_date = pyqtSignal(np.ndarray)

    def run(self):
        while True:
            while a:
                #proj = np.random.randint(0,10,(8,7))
                proj = np.loadtxt("proj.txt")
                proj = proj.reshape((8,7))
                S[0] = D['S0']
                S[1] = D['S1']
                S[2] = D['S2']
                S[3] = D['S3']
                S[4] = D['S4']
                S[5] = D['S5']
                S[6] = D['S6']
                S[7] = D['S7']
                backproj = np.zeros((33, 33))
                for i in range(8):
                    for j in range(7):
                        S[i][S[i] == j + 1] = proj[i, j]
                    backproj = backproj + S[i]
                self.update_date.emit(backproj)
                time.sleep(1)

app = QApplication(sys.argv)
ui = MyWindow()

update_data_thread = UpdateData()
update_data_thread.update_date.connect(ui.update_item_data)
update_data_thread.start()

ui.show()
ui.startButton.clicked.connect(start)
ui.closeButton.clicked.connect(close)
ui.saveButton.clicked.connect(save)
sys.exit(app.exec_())
