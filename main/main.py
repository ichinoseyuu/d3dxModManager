from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from SmodernUI import CMessage, CToolTip, ObjRef
from .Ui_mainWindow import Ui_mainWindow


class d3dxModManager(QMainWindow,Ui_mainWindow):
    def __init__(self):
        super().__init__()
        ObjRef['TOOLTIP'] = CToolTip()
        self.setupUi(self)


    def closeEvent(self,event):
        #region 退出程序
        message = CMessage('退出', '您确定要退出吗？', self)
        reply = message.exec()
        if reply == 1:
            QApplication.instance().quit()
            event.accept()
        event.ignore()
        #endregion