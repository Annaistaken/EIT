# -*- coding:utf-8 -*-
import numpy as np
import time
import quamash
import datetime
import os
from operator import methodcaller
from scipy.interpolate import griddata
from algorithm import *
import sklearn.utils._cython_blas
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.animation as animation
from matplotlib.colors import Normalize
from matplotlib.patches import Polygon
from PyQt5.QtCore import QThread, QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

from ble import BLE
from emit import EmitThread
from savex10 import saveThread
from myfigure import MyFigure
from gui import Ui_MainWindow

class MyWindow(QMainWindow, Ui_MainWindow):
    """__主窗体类__
    1. 信号与槽函数的接口设置
    2. 图像显示
    3. 部分槽函数定义
    4. 鼠标移动实时捕捉功能
    
    """

    def __init__(self, app):
        super(MyWindow, self).__init__()
        self.setupUi(self)      #初始化GUI

        self.loop = quamash.QEventLoop(app)             # BLE协程循环
        self.ble = BLE(self)                            # 实例化BLE

        self.emit_thread = EmitThread(self)             # 实例化Emit对象
        self.emit_thread.signal.connect(self.image)     # 实时成像发射信号与槽函数连接

        self.save_thread = saveThread(self)             # 实例化save对象（连续测量10组实时数据）

        self.signal_slot()                              # 菜单栏的槽函数设置

        self.alg = 'svd'        # 默认调用灵敏度矩阵法
        self.disp = 'interp'    # 默认使用矩阵插值方式显示图像
        self.refedata = np.zeros(28)    # 空场参考值
        self.projdata = np.zeros(28)    # 历史测量值
        self.proj_d = np.zeros(28)      # 边界值差分（测量值-空场值）
        self.elem_data = np.zeros(576)  # 图像重建数值
        self.statusBar().showMessage('Ready')

        # 实例化MyFigure
        self.F = MyFigure(width=16, height=9, dpi=100)

        # ax1初始显示0
        self.cache1 = self.F.ax1.bar(range(28), np.zeros(28), color='deepskyblue')

        # 鼠标移动显示当前位置的图像重建数值大小
        plt.gcf().canvas.mpl_connect('motion_notify_event', self.motion_notify)

        # ax3初始显示为灰色
        self.cache3 = []
        for i in np.arange(8):
            for j in np.arange(i + 1, 8):
                cache, = self.F.ax3.plot([self.F.theta[i], self.F.theta[j]], [1, 1], color='dimgray')
                self.cache3.append(cache)

        plt.tight_layout()
        plt.ion()       #进入交互成像模式
        self.gridLayout.addWidget(self.F, 0, 1)     #将画布置于GUI界面中

    def signal_slot(self):
        """槽函数设置"""
        self.actionRefe.triggered.connect(self.loadrefe)
        self.actionData.triggered.connect(self.loadproj)
        self.actionOpenBLE.triggered.connect(self.ble.openble)
        self.actionStop.triggered.connect(self.ble.stop)
        self.actionNowForRefe.triggered.connect(self.nowforRefe)
        self.actionRun.triggered.connect(self.emit_thread.start)
        self.actionFrameNow.triggered.connect(self.savenow)
        self.actionBLEdata.triggered.connect(self.save_thread.start)
        #display
        self.actionFE_Filling.triggered.connect(lambda: self.select_disp('fe'))
        self.actionShading_Interp.triggered.connect(lambda: self.select_disp('interp'))
        self.actionContour_Filling.triggered.connect(lambda: self.select_disp('contour'))
        #Algorithm
        self.actionLBP.triggered.connect(lambda:self.select_alg('lbp'))
        self.actionSVD.triggered.connect(lambda:self.select_alg('svd'))
        self.actionNormalized_Sensitivity.triggered.connect(lambda:self.select_alg('norm_sens'))
        self.actionCG.triggered.connect(lambda:self.select_alg('cg'))
        self.actionBFGS.triggered.connect(lambda:self.select_alg('bfgs'))
        self.actionSLSQP.triggered.connect(lambda:self.select_alg('slsqp'))
        self.actionLanczos.triggered.connect(lambda:self.select_alg('lanczos'))
        self.actionTikhonov.triggered.connect(lambda:self.select_alg('tikhonov'))
        self.actionExit.triggered.connect(QCoreApplication.instance().quit)
    def select_alg(self, alg):
        """图像重建算法选择"""
        self.alg = alg
    def select_disp(self, disp):
        """重建图像显示模式选择"""
        self.disp = disp

    def nowforRefe(self):
        """将当前时刻BLE获取的场域边界值作为保存为nowforrefe.csv，以作为空场值使用"""
        np.savetxt("nowforrefe.csv", self.ble.projnow)
        self.statusBar().showMessage('已保存当前空场值到文件"nowforrefe.csv"')
    def loadrefe(self):
        """从文件选择一组数据作为空场值"""
        try:
            fileName, fileType = QFileDialog.getOpenFileName(self.centralwidget, "select refe data", os.getcwd(), "All Files(*);;Text Files(*.csv)")
            self.refedata = np.loadtxt(fileName, delimiter=",")
            self.statusBar().showMessage('已设定空场数据')
            QApplication.processEvents()
        except:
            pass
    def loadproj(self):
        """选择用于成像的数据"""
        try:
            fileName, fileType = QFileDialog.getOpenFileName(self.centralwidget, "select proj data", os.getcwd(), "All Files(*);;Text Files(*.csv)")
            self.projdata = np.loadtxt(fileName, delimiter=",")
            self.statusBar().showMessage('已设定待成像数据')
            self.image(self.projdata)
        except:
            pass
    def savenow(self):
        """保存当前时刻的边界差分值与成像结果"""
        now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        plt.savefig(now+".png")
        np.savetxt(now+".csv", self.proj_d)
        self.statusBar().showMessage('已保存当前数据及成像结果')

    def image(self, proj):
        """更新图像"""
        self.proj_d = proj-self.refedata        # 边界值差分

        # ax1：更新边界值柱状图
        self.cache1.remove()
        self.cache1 = self.F.ax1.bar(range(28), self.proj_d, color='deepskyblue')

        # 边界数据归一化
        if np.max(np.abs(self.proj_d)) != 0:
            proj_d = self.proj_d / np.max(np.abs(self.proj_d))
        else:
            proj_d = self.proj_d

        # ax3：更新反投影图
        for i in np.arange(28):
            self.cache3[i].set_color(plt.cm.RdBu_r(self.F.norm(proj_d[i])))

        # 图像重建算法，并将结果归一化
        self.elem_data = globals()[self.alg](proj_d)
        if np.max(np.abs(self.elem_data)) != 0:
            self.elem_data = self.elem_data / np.max(np.abs(self.elem_data))
            alphas = Normalize(0, 0.5, clip=True)(np.abs(self.elem_data))
            # alphas[alphas!=1] = 0
            self.elem_data = self.elem_data * alphas
        else:
            print('elem_data == 0')

        # ax2：图像重建更新
        self.F.ax2.cla()
        getattr(self.F, self.disp)(self.elem_data)
        #methodcaller(self.disp, elem_data)(self.F)
        # plt.show()
        # plt.gcf().canvas.mpl_connect('motion_notify_event', self.motion_notify)
        QApplication.processEvents()

    def motion_notify(self,event):
        """鼠标移动获取当前位置的数值大小"""

        if event.inaxes==self.F.ax2:
            tri = self.F.trifinder(event.xdata, event.ydata)
        else:
            tri = -1
        self.F.cb.set_ticks([-1, np.around(self.elem_data[tri], decimals=4), 1])
        self.F.cb.ax.get_yticklabels()[1].set_color("g")
        event.canvas.draw()
        QApplication.processEvents()


