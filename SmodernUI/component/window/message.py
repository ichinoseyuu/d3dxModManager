from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from ..ui import Ui_message
from ...core import GenericFunc,Globals,Color

class CMessage(QDialog, Ui_message) :
    def __init__(self, tip = '', message = '', parent=None):
        super(CMessage, self).__init__()
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint) # 表示窗口没有边框
        self.setAttribute(Qt.WA_TranslucentBackground) # 表示窗口具有透明效果
        self.setModal(True)
        self.setWindowModality(Qt.ApplicationModal)

        self.title.setText(tip)
        self.messageLabel.setText(message)
        # 自动调整窗口大小
        self.adjustSize()
        self.setGeometry(GenericFunc.calculateGlobalCenterPos(self.geometry(),self.parent.geometry()))

        self._Ui_init()
        self._btn_connect()
        self._init_anim()
        self._play_FadeAnim(0, 1.0)

    def _Ui_init(self):
        self.btnExit.setBGTransparentAllTheme()
        self.btnOk.setBGColor(Globals.Theme.Light,Color.Base.Purple.value)
        self.btnOk.setFontColor(Globals.Theme.Light, Color.Base.Whtite.value)

    def _btn_connect(self):
        self.btnExit.clicked.connect(self.cancel)
        self.btnCancel.clicked.connect(self.cancel)
        self.btnOk.clicked.connect(self.confirm)

    def _init_anim(self):
        self.fadeAnim = QPropertyAnimation(self, b"windowOpacity")
        self.fadeAnim.setDuration(200)


    def _play_FadeAnim(self,start: float, endValue: float):
        self.fadeAnim.stop()
        self.fadeAnim.setStartValue(start)
        self.fadeAnim.setEndValue(endValue)
        self.fadeAnim.start()


    def exec(self):
        return super().exec()


    def cancel(self):
        # 当点击退出按钮时，执行淡出动画并关闭窗口
        self.fadeAnim.setStartValue(1)  # 当前为不透明
        self.fadeAnim.setEndValue(0)  # 淡出到透明
        self.fadeAnim.finished.connect(self.reject)  # 动画完成后关闭窗口
        self.fadeAnim.start()  # 启动动画


    def confirm(self):
        # 当点击确定按钮时，执行淡出动画并关闭窗口
        self.fadeAnim.setStartValue(1)  # 当前为不透明
        self.fadeAnim.setEndValue(0)  # 淡出到透明
        self.fadeAnim.finished.connect(self.accept)  # 动画完成后关闭窗口
        self.fadeAnim.start()  # 启动动画


    def mousePressEvent(self, event):
        GenericFunc.mousePressEvent(self, event)


    def mouseMoveEvent(self, event):
        GenericFunc.mouseMoveEvent(self, event)


    def mouseReleaseEvent(self, event):
        GenericFunc.mouseReleaseEvent(self, event)


    def paintEvent(self, event):
        super().paintEvent(event)
        GenericFunc.paintShadow(self)