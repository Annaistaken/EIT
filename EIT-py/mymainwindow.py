# -*- coding:utf-8 -*-
import numpy as np
import time
import os
import sys
import quamash
import asyncio
import matplotlib
import matplotlib.pyplot as plt
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QFileDialog

from lbp import lbp
from myfigure import MyFigure
from gui import Ui_MainWindow

app = QApplication(sys.argv)
loop = quamash.QEventLoop(app)

class EmitThread(QThread):
    signal = pyqtSignal(np.ndarray)
    def __init__(self):
        super().__init__()
    def run(self):
        while ui.BLE_status == 1:
            self.signal.emit(ui.proj)
            time.sleep(1)

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setupBLE()
        #实例化figure
        self.F = MyFigure(width=3, height=3, dpi=100)
        self.gridlayout = QGridLayout(self.groupBox)
        self.gridlayout.addWidget(self.F, 0, 1)
        self.theta = [2 * np.pi / 4, 1 * np.pi / 4, 0 * np.pi / 4, 7 * np.pi / 4, 6 * np.pi / 4, 5 * np.pi / 4, 4 * np.pi / 4, 3 * np.pi / 4]
        #BLE
        #self.ble_thread = BLEThread()
        #实例化Emit对象
        self.emit_thread = EmitThread()
        self.emit_thread.signal.connect(self.image)
        #signal & slot
        self.refedata = np.zeros((8, 7))
        self.projdata = np.zeros((8, 7))
        self.actionRefe.triggered.connect(self.loadrefe)
        self.actionData.triggered.connect(self.loadproj)
        self.actionFrameNow.triggered.connect(self.save)
        self.actionOpenBLE.triggered.connect(self.openble)
        self.actionNowForRefe.triggered.connect(self.nowforRefe)
        self.actionRun.triggered.connect(self.emit_thread.start)
        self.actionStop.triggered.connect(self.stop)
    def setupBLE(self):
        #self.BLE_status = 1
        self.proj = np.zeros((8, 7))
        self.address = "DF:5C:10:23:42:57"
        self.Char1_UUID = "19b10011-e8f2-537e-4f6c-d104768a1214"
        self.Char2_UUID = "19b10012-e8f2-537e-4f6c-d104768a1214"
        self.Char3_UUID = "19b10013-e8f2-537e-4f6c-d104768a1214"
        self.Char4_UUID = "19b10014-e8f2-537e-4f6c-d104768a1214"
        self.Char5_UUID = "19b10015-e8f2-537e-4f6c-d104768a1214"
        self.Char6_UUID = "19b10016-e8f2-537e-4f6c-d104768a1214"
        self.Char7_UUID = "19b10017-e8f2-537e-4f6c-d104768a1214"
        self.Char8_UUID = "19b10018-e8f2-537e-4f6c-d104768a1214"
        self.Char9_UUID = "19b10019-e8f2-537e-4f6c-d104768a1214"
        self.Char10_UUID = "19b1001a-e8f2-537e-4f6c-d104768a1214"
        self.Char11_UUID = "19b1001b-e8f2-537e-4f6c-d104768a1214"
        self.Char12_UUID = "19b1001c-e8f2-537e-4f6c-d104768a1214"
        self.Char13_UUID = "19b1001d-e8f2-537e-4f6c-d104768a1214"
        self.Char14_UUID = "19b1001e-e8f2-537e-4f6c-d104768a1214"
        self.Char15_UUID = "19b1001f-e8f2-537e-4f6c-d104768a1214"
        self.Char16_UUID = "19b10020-e8f2-537e-4f6c-d104768a1214"
        self.Char17_UUID = "19b10021-e8f2-537e-4f6c-d104768a1214"
        self.Char18_UUID = "19b10022-e8f2-537e-4f6c-d104768a1214"
        self.Char19_UUID = "19b10023-e8f2-537e-4f6c-d104768a1214"
        self.Char20_UUID = "19b10024-e8f2-537e-4f6c-d104768a1214"
        self.Char21_UUID = "19b10025-e8f2-537e-4f6c-d104768a1214"
        self.Char22_UUID = "19b10026-e8f2-537e-4f6c-d104768a1214"
        self.Char23_UUID = "19b10027-e8f2-537e-4f6c-d104768a1214"
        self.Char24_UUID = "19b10028-e8f2-537e-4f6c-d104768a1214"
        self.Char25_UUID = "19b10029-e8f2-537e-4f6c-d104768a1214"
        self.Char26_UUID = "19b1002a-e8f2-537e-4f6c-d104768a1214"
        self.Char27_UUID = "19b1002b-e8f2-537e-4f6c-d104768a1214"
        self.Char28_UUID = "19b1002c-e8f2-537e-4f6c-d104768a1214"
        self.Char_UUID = [self.Char1_UUID, self.Char2_UUID, self.Char3_UUID, self.Char4_UUID, self.Char5_UUID, self.Char6_UUID, self.Char7_UUID,
                          self.Char8_UUID, self.Char9_UUID, self.Char10_UUID, self.Char11_UUID, self.Char12_UUID, self.Char13_UUID, self.Char14_UUID,
                          self.Char15_UUID, self.Char16_UUID, self.Char17_UUID, self.Char18_UUID, self.Char19_UUID, self.Char20_UUID, self.Char21_UUID,
                          self.Char22_UUID, self.Char23_UUID, self.Char24_UUID, self.Char25_UUID, self.Char26_UUID, self.Char27_UUID, self.Char28_UUID]
    def callback(self, sender, data):
        if sender == self.Char1_UUID:
            self.proj[0, 0] = self.proj[1, 0] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char2_UUID:
            self.proj[0, 1] = self.proj[2, 0] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char3_UUID:
            self.proj[0, 2] = self.proj[3, 0] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char4_UUID:
            self.proj[0, 3] = self.proj[4, 0] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char5_UUID:
            self.proj[0, 4] = self.proj[5, 0] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char6_UUID:
            self.proj[0, 5] = self.proj[6, 0] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char7_UUID:
            self.proj[0, 6] = self.proj[7, 0] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char8_UUID:
            self.proj[1, 1] = self.proj[2, 1] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char9_UUID:
            self.proj[1, 2] = self.proj[3, 1] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char10_UUID:
            self.proj[1, 3] = self.proj[4, 1] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char11_UUID:
            self.proj[1, 4] = self.proj[5, 1] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char12_UUID:
            self.proj[1, 5] = self.proj[6, 1] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char13_UUID:
            self.proj[1, 6] = self.proj[7, 1] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char14_UUID:
            self.proj[2, 2] = self.proj[3, 2] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char15_UUID:
            self.proj[2, 3] = self.proj[4, 2] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char16_UUID:
            self.proj[2, 4] = self.proj[5, 2] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char17_UUID:
            self.proj[2, 5] = self.proj[6, 2] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char18_UUID:
            self.proj[2, 6] = self.proj[7, 2] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char19_UUID:
            self.proj[3, 3] = self.proj[4, 3] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char20_UUID:
            self.proj[3, 4] = self.proj[5, 3] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char21_UUID:
            self.proj[3, 5] = self.proj[6, 3] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char22_UUID:
            self.proj[3, 6] = self.proj[7, 3] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char23_UUID:
            self.proj[4, 4] = self.proj[5, 4] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char24_UUID:
            self.proj[4, 5] = self.proj[6, 4] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char25_UUID:
            self.proj[4, 6] = self.proj[7, 4] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char26_UUID:
            self.proj[5, 5] = self.proj[6, 5] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char27_UUID:
            self.proj[5, 6] = self.proj[7, 5] = int.from_bytes(data, byteorder='big')
        elif sender == self.Char28_UUID:
            self.proj[6, 6] = self.proj[7, 6] = int.from_bytes(data, byteorder='big')
    async def notify(self):
        from bleak import BleakClient
        print("开始连接")
        self.client = BleakClient(self.address, loop=loop)
        try:
            await self.client.connect()
            print("BLE连接成功")
            for i in np.arange(28):
                await self.client.start_notify(self.Char_UUID[i], self.callback)
            self.BLE_status = 1
            print("开始notify")
        except:
            print("连接失败")
            pass
        loop.stop()
    async def stopble(self):
        try:
            for i in np.arange(28):
                await self.client.stop_notify(self.Char_UUID[i])
            await self.client.disconnect()
        except:
            print('断开失败')
            pass
        loop.stop()
    def openble(self):
        asyncio.set_event_loop(loop)
        asyncio.ensure_future(self.notify())
        loop.run_forever()
    def stop(self):
        self.BLE_status = 0
        self.emit_thread.quit()
        asyncio.ensure_future(self.stopble())
        loop.run_forever()
    def nowforRefe(self):
        self.refedata = self.proj
    def loadrefe(self):
        try:
            fileName, fileType = QFileDialog.getOpenFileName(self.centralwidget, "selcet refe data", os.getcwd(), "All Files(*);;Text Files(*.txt)")
            self.refedata = np.loadtxt(fileName).reshape((8, 7))
            QApplication.processEvents()
        except:
            pass
    def loadproj(self):
        try:
            fileName, fileType = QFileDialog.getOpenFileName(self.centralwidget, "selcet proj data", os.getcwd(), "All Files(*);;Text Files(*.txt)")
            self.projdata = np.loadtxt(fileName).reshape((8, 7))
            self.image(self.projdata)
        except:
            pass
    def save(self):
        plt.savefig('frame_now.png')
    def image(self, proj):
        proj = proj-self.refedata
        plt.ion()
        #ax1
        #proj_triu = np.triu(proj, 0)
        proj28 = np.array([proj[i][j] for i in range(7) for j in np.arange(i, 7)])
        self.F.ax1.bar(range(28), proj28, color='b')
        #ax2
        backproj = lbp(proj)
        self.F.ax2.imshow(backproj.T, aspect=1, cmap=matplotlib.cm.RdBu, origin='lower')
        #ax3
        cmap3 = plt.cm.RdBu
        norm3 = matplotlib.colors.Normalize(vmin=np.min(proj), vmax=np.max(proj))
        for i in np.arange(8):
            for j in np.arange(i+1,8):
                self.F.ax3.plot([self.theta[i], self.theta[j]], [1,1], color=cmap3(norm3(proj[i, j-1])))
                self.F.ax3.scatter([self.theta[i], self.theta[j]], [1,1], color='b')
        #QApplication.processEvents()

ui = MyWindow()
ui.show()
sys.exit(app.exec_())