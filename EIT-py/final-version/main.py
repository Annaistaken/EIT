# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication

from mymainwindow_note import *

app = QApplication(sys.argv)

ui = MyWindow(app)
ui.show()
sys.exit(app.exec_())