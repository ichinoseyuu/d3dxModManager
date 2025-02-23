from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from ..ui import Ui_tooltip
from ...core.globals import *
from ...core.cenum import *
class CToolTip(QWidget, Ui_tooltip):
    '''提示标签'''
    def __init__(self):
        super().__init__()
        self.parent = None
        self.setupUi(self)
        self.tipBoard.setBorder((1, 1, 1, 1))
        self.tipBoard.setBorder((1, 1, 1, 1), 1, Theme.Dark)
        self.tipBoard.setBGColor(QColor(90, 90, 90), Theme.Dark)
        self.tipBoard.setBorderColors({Theme.Light: QColor(230, 230, 230), Theme.Dark: QColor(200, 200, 200)})
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool | Qt.WindowTransparentForInput)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self._init_Anim()


    def _init_Anim(self):
        self.anim_fade_in = QPropertyAnimation(self, b"windowOpacity")
        self.anim_fade_in.setDuration(200)
        self.anim_fade_in.setStartValue(0)
        self.anim_fade_in.setEndValue(1)

        self.anim_fade_out = QPropertyAnimation(self, b"windowOpacity")
        self.anim_fade_out.setDuration(200)
        self.anim_fade_out.setStartValue(1)
        self.anim_fade_out.setEndValue(0)

        self.anim_resize = QPropertyAnimation(self, b"size")
        self.anim_resize.setDuration(200)

        self.tracker_timer = QTimer()  # 跟踪鼠标的计时器
        self.tracker_timer.setInterval(int(1000/60))
        self.tracker_timer.timeout.connect(self.refreshPos)
        self.tracker_timer.start()


    def setTip(self, parent, tip: str):
        self.parent = parent
        self.tipLabel.setText(tip)


    def showTip(self):
        self.adjust_size()
        self.anim_fade_in.start()
        self.show()


    def hideTip(self):
        self.anim_fade_out.finished.connect(self.close)
        self.anim_fade_out.start()


    def adjust_size(self):
        """根据控件内容调整大小"""
        # 获取推荐的大小
        recommended_size = self.tipBoard.sizeHint()
        # 获取最小尺寸
        min_width = self.minimumWidth()
        min_height = self.minimumHeight()
        # 设置新尺寸，确保不小于最小尺寸
        new_width = max(recommended_size.width() + 36, min_width)
        new_height = max(recommended_size.height(), min_height)
        # 调整大小

        self.anim_resize.setStartValue(QSize(self.width(), self.height()))
        self.anim_resize.setEndValue(QSize(new_width, new_height))
        self.anim_resize.start()

    def refreshPos(self):
        pos = QCursor.pos()
        x, y = pos.x(), pos.y()
        left = x + TOOLTIP_OFFSET_X
        top = y - self.geometry().height() + TOOLTIP_OFFSET_Y
        if Var.objref['mainwindow'] != None:
            new_left = max(left, Var.objref['mainwindow'].geometry().left())
            new_top = max(top, Var.objref['mainwindow'].geometry().top())
            if new_left + self.width() > Var.objref['mainwindow'].geometry().right():
                new_left = min(left, Var.objref['mainwindow'].geometry().right()-self.width())
            if new_top + self.height() > Var.objref['mainwindow'].geometry().bottom():
                new_top = min(top, Var.objref['mainwindow'].geometry().bottom()-self.height())
            self.move(new_left, new_top)
        else:
            self.move(left, top)
