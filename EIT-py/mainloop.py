import sys
import quamash
import asyncio
from PyQt5.QtWidgets import QApplication

from mywindow import MyWindow

app = QApplication(sys.argv)
loop = quamash.QEventLoop(app)
asyncio.set_event_loop(loop)
with loop:
    ui = MyWindow(loop)
    ui.show()
    loop.run_forever()

sys.exit(app.exec_())


