import numpy as np
import asyncio
from PyQt5.QtWidgets import QMessageBox

class BLE():
    """低功耗蓝牙连接与断开"""

    def __init__(self, ui):
        """设置外围设备的地址以及服务特征的UUID等"""

        self.projnow = np.zeros(28)             #28个边界测量数据
        self.ui = ui                            #用于在上层gui中显示通知信息
        self.BLE_status = 0                     #BLE串口的状态（0为关闭，1为打开并订阅状态）
        self.address = "CA:0F:A9:D6:81:67"      #外围设备地址
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
        self.Char_UUID = [self.Char1_UUID, self.Char2_UUID, self.Char3_UUID, self.Char4_UUID, self.Char5_UUID,
                          self.Char6_UUID, self.Char7_UUID, self.Char8_UUID, self.Char9_UUID, self.Char10_UUID,
                          self.Char11_UUID, self.Char12_UUID, self.Char13_UUID, self.Char14_UUID, self.Char15_UUID,
                          self.Char16_UUID, self.Char17_UUID, self.Char18_UUID, self.Char19_UUID, self.Char20_UUID,
                          self.Char21_UUID, self.Char22_UUID, self.Char23_UUID, self.Char24_UUID, self.Char25_UUID,
                          self.Char26_UUID, self.Char27_UUID, self.Char28_UUID]

    def callback(self, sender, data):
        """BLE订阅的回调函数——用于将接收的ASCII码转换为测量数值并存储在相应数组中"""

        self.projnow[self.Char_UUID.index(sender)] = int.from_bytes(data, byteorder='big')
        """
        for i in np.arange(28):
            if sender == self.Char_UUID[i]:
                #self.ui.emit_thread.projnow[i] = int.from_bytes(data, byteorder='big')
                self.projnow[i] = int.from_bytes(data, byteorder='big')
                break"""

    async def notify(self):
        """BLE连接与订阅"""

        from bleak import BleakClient
        self.client = BleakClient(self.address, loop=self.ui.loop)
        try:
            await self.client.connect()
            for i in np.arange(28):
                initdata = await self.client.read_gatt_char(self.Char_UUID[i])      #读取当前数据
                self.projnow[i] = int.from_bytes(initdata, byteorder='big')
                await self.client.start_notify(self.Char_UUID[i], self.callback)    #订阅
            self.BLE_status = 1     #将蓝牙串口状态置为1
            QMessageBox.information(self.ui, '提示', 'BLE连接成功并开始订阅广告', QMessageBox.Ok)
            self.ui.statusBar().showMessage('BLE连接成功并开始订阅广告')
        except:
            self.ui.statusBar().showMessage('BLE连接失败')
            pass
        self.ui.loop.stop()

    async def stopble(self):
        """停止订阅并断开连接"""
        try:
            for i in np.arange(28):
                await self.client.stop_notify(self.Char_UUID[i])        #停止BLE订阅
            await self.client.disconnect()                              #BLE断开连接
            QMessageBox.information(self.ui, '提示', 'BLE已断开', QMessageBox.Ok)
            self.ui.statusBar().showMessage('BLE已断开')
        except:
            self.ui.statusBar().showMessage('BLE断开失败')
            pass
        self.ui.loop.stop()

    def openble(self):
        """GUI槽函数——打开BLE并开始数据订阅"""
        self.ui.statusBar().showMessage('正在连接BLE')
        asyncio.set_event_loop(self.ui.loop)
        asyncio.ensure_future(self.notify())
        self.ui.loop.run_forever()

    def stop(self):
        """GUI槽函数——断开BLE并停止实时成像（图像停留在最后一帧）"""
        self.BLE_status = 0         #BLE串口状态置为0
        self.ui.emit_thread.quit()  #停止实时成像线程
        asyncio.ensure_future(self.stopble())   #断开连接
        self.ui.loop.run_forever()

