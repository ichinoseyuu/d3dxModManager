from PySide6.QtWidgets import QPushButton, QToolTip, QMenu
from PySide6.QtCore import Qt, QSize, QProcess, QEvent,QPropertyAnimation,Property
from PySide6.QtGui import QIcon,QMouseEvent, QCursor,QColor,QPalette
import os
from SmodernUI import ObjRef

class CButton(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        self.tip_text = ''

    def setTipText(self, text: str):
        self.tip_text = text

    def enterEvent(self, event):
        # 鼠标进入按钮时显示自定义信息
        if ObjRef['TOOLTIP'] is not None and self.tip_text != '':
            ObjRef['TOOLTIP'].setTip(self, self.tip_text)
            ObjRef['TOOLTIP'].showTip()
        # 让父类方法继续处理事件
        super().enterEvent(event)


    def leaveEvent(self, event):
        # 鼠标离开按钮时隐藏标签
        if ObjRef['TOOLTIP'] is not None and self.tip_text != '':
            ObjRef['TOOLTIP'].hideTip()
        super().leaveEvent(event)
