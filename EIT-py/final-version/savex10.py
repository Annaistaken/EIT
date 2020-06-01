import numpy as np
import pandas as pd
import time
import os
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QFileDialog, QMessageBox

class saveThread(QThread):
    """连续保存10组BLE串口数据"""
    def __init__(self,ui):
        super().__init__()
        self.ui = ui
    def run(self):
        data10 = self.ui.ble.projnow
        for num in np.arange(9):
            time.sleep(1)
            data10 = np.c_[data10, self.ui.ble.projnow]
        data10 = pd.DataFrame(data10)
        filepath, filetype = QFileDialog.getSaveFileName(self.ui, 'save data×10', os.getcwd(), "Text Files(*.csv)")
        data10.to_csv(filepath, encoding='utf-8')
        self.ui.statusBar().showMessage('10组数据采集完成')