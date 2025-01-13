from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ..ui import Ui_titlebar
# 使用方法
# self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint)
# self.setMenuWidget(CTitleBar())
# self.setWindowFlags(Qt.CustomizeWindowHint|Qt.FramelessWindowHint)
# self.setMenuWidget(CTitleBar())
class CTitleBar(QWidget,Ui_titlebar):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnMin.setBGTransparentAllTheme()
        self.btnMax.setBGTransparentAllTheme()
        self.btnExit.setBGTransparentAllTheme()
        self.btnMin.clicked.connect(self.minWindow)
        self.btnMax.clicked.connect(self.maxWindow)
        self.btnExit.clicked.connect(self.closeWindow)

        self.window().installEventFilter(self)

    def minWindow(self):
        self.window().showMinimized()

    def maxWindow(self):
        if self.window().isMaximized():
            self.window().showNormal()
        else:
            self.window().showMaximized()

    def closeWindow(self):
        self.window().close()

    def eventFilter(self, obj, e):
        if obj is self.window():
            if e.type() == QEvent.WindowStateChange:
                self.maxBtn.setMaxState(self.window().isMaximized())
                return False
        return super().eventFilter(obj, e)

    def mouseDoubleClickEvent(self, event):
        if event.button() != Qt.LeftButton:
            return
        self.maxWindow()

