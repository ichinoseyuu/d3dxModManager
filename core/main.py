from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from core.ui_Main import Ui_mainWindow
from component.window import CMessage
class core(QMainWindow,Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.closeEvent)

    def closeEvent(self,event):
        #region 退出程序
        message = CMessage('退出', '您确定要退出吗？', self)
        reply = message.exec()
        if reply == 1:
            QApplication.instance().quit()
            event.accept()
        event.ignore()
        #endregion