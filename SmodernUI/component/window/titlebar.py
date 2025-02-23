from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ..ui import Ui_titlebar
from ..widgets.container import CContainer
from ...core.globals import Theme
from ...core.color import *
from .utils import startSystemMove

class CTitleBar(QWidget,Ui_titlebar):
    '''标题栏'''
    def __init__(self, parent = None):
        super().__init__()
        if parent is not None:
            self.setParent(parent)
        self.setupUi(self)
        self.titleWidget.setBGColor(QColor(250, 245, 245))
        self.btnMin.setBGTransparent()
        self.btnMax.setBGTransparent()
        self.btnExit.setBGTransparent()
        self.btnExit.setHoverBGColors({Theme.Light: QColor(255, 64, 16), Theme.Dark: QColor(255, 64, 16)})
        self.btnMin.clicked.connect(self.minWindow)
        self.btnMax.clicked.connect(self.maxWindow)
        self.btnExit.clicked.connect(self.closeWindow)

    def minWindow(self):
        '''最小化窗口'''
        self.window().showMinimized()

    def maxWindow(self):
        '''最大化窗口'''
        if self.window().isMaximized():
            self.window().showNormal()
        else:
            self.window().showMaximized()

    def closeWindow(self):
        '''关闭窗口'''
        self.window().close()

    def hideMinBtn(self):
        '''隐藏最小化按钮'''
        self.btnMin.hide()


    def hideMaxBtn(self):
        '''隐藏最大化按钮'''
        self.btnMax.hide()


    def hideIcon(self):
        '''隐藏图标'''
        self.icon.hide()


    def hideTitle(self):
        '''隐藏标题'''
        self.title.hide()
        self.title.setVisible(False)


    def setTitle(self, title: str):
        '''设置标题'''
        self.title.setText(title)


    def mouseDoubleClickEvent(self, event: QMouseEvent):
        if event.button() != Qt.LeftButton:
            return
        self.btnMax.click()


    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton and not self.window().isMaximized():
            # 记录鼠标按下时的位置
            self.dragPosition = event.globalPosition().toPoint() - self.parent().frameGeometry().topLeft()
            event.accept()


    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.LeftButton and not self.window().isMaximized():
            # 窗口跟随鼠标移动
            self.parent().move(event.globalPosition().toPoint() - self.dragPosition)
            event.accept()

