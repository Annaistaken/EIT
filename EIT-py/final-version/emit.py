import numpy as np
import time
from PyQt5.QtCore import QThread, pyqtSignal


class EmitThread(QThread):
    """
    __实时成像线程__
    每隔0.2s发射一次pyqtSignal信号
    
    """
    signal = pyqtSignal(np.ndarray)     #定义一个pyqtSignal信号，其数据类型为nd.ndarray

    def __init__(self, ui):
        super().__init__()
        self.ui = ui

    def run(self):
        self.ui.statusBar().showMessage('正在实时成像')
        while self.ui.ble.BLE_status == 1:      #仅在BL串口打开的情况下执行
            self.signal.emit(self.ui.ble.projnow)
            time.sleep(0.2)