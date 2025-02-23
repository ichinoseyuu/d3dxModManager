from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from .frameless_window import FramelessWindow
from ..ui import Ui_dialog
from ..window.titlebar import CTitleBar
from ...core import GenericFunc, Theme, ColorBase

class CDialog(FramelessWindow, Ui_dialog) :
    '''对话框'''
    def __init__(self, title:str, dialog = '', parent: QWidget = None):
        super().__init__()
        self._parent_window = parent
        self._result = 0
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint) # 表示窗口没有边框
        self.setWindowModality(Qt.ApplicationModal) # 表示该窗口为模态窗口
        #self.setAttribute(Qt.WA_TranslucentBackground)

        self.messageLabel.setText(dialog) # 设置对话框内容
        # 自动调整窗口大小
        self.adjustSize()
        self.setGeometry(GenericFunc.calculateGlobalCenterPos(self.geometry(),self._parent_window.geometry()))

        self._init_ui()
        self._setupTitleBar(title)
        self._btn_connect()
        self._init_anim()
        self._play_FadeAnim(0, 1)


    def _init_ui(self):
        self.btnOk.setBGColor(ColorBase.purple.value)
        self.btnOk.setBGColor(ColorBase.pink.value,Theme.Dark)
        self.btnOk.setFontColor(ColorBase.whtite.value,Theme.Light)

    def _setupTitleBar(self,title:str):
        self.titleBar = CTitleBar(self)
        self.titleBar.hideMaxBtn()
        self.titleBar.hideIcon()
        self.titleBar.setTitle(title)
        self.titleBar.raise_()

    def _btn_connect(self):
        self.btnCancel.clicked.connect(self._cancel)
        self.btnOk.clicked.connect(self._confirm)

    def _init_anim(self):
        self.fadeAnim = QPropertyAnimation(self, b"windowOpacity")
        self.fadeAnim.setDuration(200)


    def _play_FadeAnim(self,start: float, endValue: float):
        self.fadeAnim.stop()
        self.fadeAnim.setStartValue(start)
        self.fadeAnim.setEndValue(endValue)
        self.fadeAnim.start()
        
    def _play_FadeAnimToDo(self,start: float, endValue: float,finished: callable = None):
        self.fadeAnim.stop()
        self.fadeAnim.setStartValue(start)
        self.fadeAnim.setEndValue(endValue)
        self.fadeAnim.finished.connect(finished)
        self.fadeAnim.start()


    def _cancel(self):
        # 当点击退出按钮时，执行淡出动画并关闭窗口
        self._play_FadeAnimToDo(1, 0, self.reject)


    def _confirm(self):
        # 当点击确定按钮时，执行淡出动画并关闭窗口
        self._play_FadeAnimToDo(1, 0, self.accept)


    def showEvent(self, event):
        if self._parent_window:
            # 禁用父窗口
            self._parent_window.setEnabled(False)
            # 创建遮罩层
            # self.mask = QWidget(self._parent_window)
            # self.mask.setGeometry(self._parent_window.rect())
            # self.mask.setStyleSheet("background-color: rgba(0, 0, 0, 25);")  # 半透明黑色
            # self.mask.show()
            # self.mask.raise_()  # 确保遮罩层在最上层
        self.raise_()  # 确保模态窗口在最上层
        self.activateWindow()  # 激活窗口，使其成为活动窗口
        super().showEvent(event)

    def closeEvent(self, event: QEvent):
        if self._parent_window:
            # 重新启用父窗口
            self._parent_window.setEnabled(True)
            # 移除遮罩层
            # self.mask.close()
            event.accept()
            self.deleteLater()


    def exec(self):
        self.show()
        loop = QEventLoop()
        self.destroyed.connect(loop.quit)  # 连接到事件循环的退出方法
        loop.exec()  # 启动事件循环，直到窗口被销毁
        return self._result

    def accept(self):
        self._result = 1
        self.close()

    def reject(self):
        self._result = 0
        self.close()