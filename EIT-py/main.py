import numpy as np
np.set_printoptions(threshold=np.inf)
import sys
import time
import threading
import asyncio
from bleak import BleakClient
import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget,  QGridLayout, QMainWindow

from lbp import lbp
from imgGUI import Ui_EIT_RTR

"""Thread-notify
Char1_UUID = "19b10011-e8f2-537e-4f6c-d104768a1214"
Char2_UUID = "19b10012-e8f2-537e-4f6c-d104768a1214"
Char3_UUID = "19b10013-e8f2-537e-4f6c-d104768a1214"
Char4_UUID = "19b10014-e8f2-537e-4f6c-d104768a1214"
Char5_UUID = "19b10015-e8f2-537e-4f6c-d104768a1214"
Char6_UUID = "19b10016-e8f2-537e-4f6c-d104768a1214"
Char7_UUID = "19b10017-e8f2-537e-4f6c-d104768a1214"
Char8_UUID = "19b10018-e8f2-537e-4f6c-d104768a1214"
Char9_UUID = "19b10019-e8f2-537e-4f6c-d104768a1214"
Char10_UUID = "19b1001a-e8f2-537e-4f6c-d104768a1214"
Char11_UUID = "19b1001b-e8f2-537e-4f6c-d104768a1214"
Char12_UUID = "19b1001c-e8f2-537e-4f6c-d104768a1214"
Char13_UUID = "19b1001d-e8f2-537e-4f6c-d104768a1214"
Char14_UUID = "19b1001e-e8f2-537e-4f6c-d104768a1214"
Char15_UUID = "19b1001f-e8f2-537e-4f6c-d104768a1214"
Char16_UUID = "19b10020-e8f2-537e-4f6c-d104768a1214"
Char17_UUID = "19b10021-e8f2-537e-4f6c-d104768a1214"
Char18_UUID = "19b10022-e8f2-537e-4f6c-d104768a1214"
Char19_UUID = "19b10023-e8f2-537e-4f6c-d104768a1214"
Char20_UUID = "19b10024-e8f2-537e-4f6c-d104768a1214"
Char21_UUID = "19b10025-e8f2-537e-4f6c-d104768a1214"
Char22_UUID = "19b10026-e8f2-537e-4f6c-d104768a1214"
Char23_UUID = "19b10027-e8f2-537e-4f6c-d104768a1214"
Char24_UUID = "19b10028-e8f2-537e-4f6c-d104768a1214"
Char25_UUID = "19b10029-e8f2-537e-4f6c-d104768a1214"
Char26_UUID = "19b1002a-e8f2-537e-4f6c-d104768a1214"
Char27_UUID = "19b1002b-e8f2-537e-4f6c-d104768a1214"
Char28_UUID = "19b1002c-e8f2-537e-4f6c-d104768a1214"
Char_UUID = [Char1_UUID, Char2_UUID, Char3_UUID, Char4_UUID, Char5_UUID, Char6_UUID, Char7_UUID, Char8_UUID, Char9_UUID, Char10_UUID, Char11_UUID, Char12_UUID, Char13_UUID, Char14_UUID, Char15_UUID, Char16_UUID, Char17_UUID, Char18_UUID, Char19_UUID, Char20_UUID, Char21_UUID, Char22_UUID, Char23_UUID, Char24_UUID, Char25_UUID, Char26_UUID, Char27_UUID, Char28_UUID]
#proj = np.mat(size=(8, 7))
proj = np.zeros((8, 7))

def callback(sender, data):
    if sender == Char1_UUID:
        proj[0, 0] = proj[1, 0] = int.from_bytes(data, byteorder='big')
    elif sender == Char2_UUID:
        proj[0, 1] = proj[2, 0] = int.from_bytes(data, byteorder='big')
    elif sender == Char3_UUID:
        proj[0, 2] = proj[3, 0] = int.from_bytes(data, byteorder='big')
    elif sender == Char4_UUID:
        proj[0, 3] = proj[4, 0] = int.from_bytes(data, byteorder='big')
    elif sender == Char5_UUID:
        proj[0, 4] = proj[5, 0] = int.from_bytes(data, byteorder='big')
    elif sender == Char6_UUID:
        proj[0, 5] = proj[6, 0] = int.from_bytes(data, byteorder='big')
    elif sender == Char7_UUID:
        proj[0, 6] = proj[7, 0] = int.from_bytes(data, byteorder='big')
    elif sender == Char8_UUID:
        proj[1, 1] = proj[2, 1] = int.from_bytes(data, byteorder='big')
    elif sender == Char9_UUID:
        proj[1, 2] = proj[3, 1] = int.from_bytes(data, byteorder='big')
    elif sender == Char10_UUID:
        proj[1, 3] = proj[4, 1] = int.from_bytes(data, byteorder='big')
    elif sender == Char11_UUID:
        proj[1, 4] = proj[5, 1] = int.from_bytes(data, byteorder='big')
    elif sender == Char12_UUID:
        proj[1, 5] = proj[6, 1] = int.from_bytes(data, byteorder='big')
    elif sender == Char13_UUID:
        proj[1, 6] = proj[7, 1] = int.from_bytes(data, byteorder='big')
    elif sender == Char14_UUID:
        proj[2, 2] = proj[3, 2] = int.from_bytes(data, byteorder='big')
    elif sender == Char15_UUID:
        proj[2, 3] = proj[4, 2] = int.from_bytes(data, byteorder='big')
    elif sender == Char16_UUID:
        proj[2, 4] = proj[5, 2] = int.from_bytes(data, byteorder='big')
    elif sender == Char17_UUID:
        proj[2, 5] = proj[6, 2] = int.from_bytes(data, byteorder='big')
    elif sender == Char18_UUID:
        proj[2, 6] = proj[7, 2] = int.from_bytes(data, byteorder='big')
    elif sender == Char19_UUID:
        proj[3, 3] = proj[4, 3] = int.from_bytes(data, byteorder='big')
    elif sender == Char20_UUID:
        proj[3, 4] = proj[5, 3] = int.from_bytes(data, byteorder='big')
    elif sender == Char21_UUID:
        proj[3, 5] = proj[6, 3] = int.from_bytes(data, byteorder='big')
    elif sender == Char22_UUID:
        proj[3, 6] = proj[7, 3] = int.from_bytes(data, byteorder='big')
    elif sender == Char23_UUID:
        proj[4, 4] = proj[5, 4] = int.from_bytes(data, byteorder='big')
    elif sender == Char24_UUID:
        proj[4, 5] = proj[6, 4] = int.from_bytes(data, byteorder='big')
    elif sender == Char25_UUID:
        proj[4, 6] = proj[7, 4] = int.from_bytes(data, byteorder='big')
    elif sender == Char26_UUID:
        proj[5, 5] = proj[6, 5] = int.from_bytes(data, byteorder='big')
    elif sender == Char27_UUID:
        proj[5, 6] = proj[7, 5] = int.from_bytes(data, byteorder='big')
    elif sender == Char28_UUID:
        proj[6, 6] = proj[7, 6] = int.from_bytes(data, byteorder='big')
async def run(address, loop):
    print("开始连接")
    async with BleakClient(address, loop=loop) as client:
        print("BLE连接成功")
        for i in np.arange(28):
            await client.start_notify(Char_UUID[i], callback)
        print("开始notify")
        a = input("输入1以退出：")
        a = int(a)
        if a == 1:
            for i in np.arange(28):
                await client.stop_notify(Char_UUID[i])
def notify():
    address = "DF:5C:10:23:42:57"
    #loop = asyncio.get_event_loop()  替换为下两行
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run(address, loop))
thread_notify = threading.Thread(target=notify,name='notifyThread')
thread_notify.start()
Thread-notify end"""

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
        self.axes.set_title("EIT实时成像")
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
        self.F.axes.imshow(data.T, extent=(0, 35, 0, 35), cmap=matplotlib.cm.RdBu, origin='lower')
        #QApplication.processEvents()

class UpdateData(QThread):
    #更新数据类
    update_date = pyqtSignal(np.ndarray)

    def run(self):
        while True:
            while a:
                proj = np.random.randint(0,10,(8,7))
                f_ave = lbp(proj)
                self.update_date.emit(f_ave)  # 发射信号
                time.sleep(1)

app = QApplication(sys.argv)
ui = MyWindow()

# 启动更新线程
update_data_thread = UpdateData()
update_data_thread.update_date.connect(ui.update_item_data)  # 链接信号
update_data_thread.start()

ui.show()
ui.startButton.clicked.connect(start)
ui.closeButton.clicked.connect(close)
ui.saveButton.clicked.connect(save)
sys.exit(app.exec_())


"""
img = lbp(proj)
#绘制热图
imgshow = plt.imshow(img.T, extent=(0, 35, 0, 35), cmap=matplotlib.cm.RdBu, origin='lower')
plt.ion()

while True:
    img = lbp(proj)
    imgshow.set_data(img.T)
    plt.pause(0.1)

plt.ioff()
plt.show()
"""