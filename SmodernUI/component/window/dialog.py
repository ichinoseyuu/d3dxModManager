from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from ..ui import Ui_dialog
from ...core import GenericFunc, CColor, Theme

class CDialog(QDialog, Ui_dialog) :
    '''对话框'''
    def __init__(self, title = '', dialog = '', parent=None):
        """
        Args:
            title (str, optional): 标题. Defaults to ''.
            dialog (str, optional): 问题. Defaults to ''.
            parent (_type_, optional): 父级窗口引用. Defaults to None.
        """
        super(CDialog, self).__init__()
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint) # 表示窗口没有边框
        self.setAttribute(Qt.WA_TranslucentBackground) # 表示窗口具有透明效果
        self.setModal(True)
        self.setWindowModality(Qt.ApplicationModal)

        self.title.setText(title)
        self.messageLabel.setText(dialog)
        # 自动调整窗口大小
        self.adjustSize()
        self.setGeometry(GenericFunc.calculateGlobalCenterPos(self.geometry(),self.parent.geometry()))

        self.__Ui_init()
        self.__btn_connect()
        self.__init_anim()
        self.__play_FadeAnim(0, 1)

    def __Ui_init(self):
        self.btnExit.setBGTransparentAllTheme()
        self.btnOk.setBGColor(Theme.Light,CColor.Base.purple.value)
        self.btnOk.setBGColor(Theme.Dark,CColor.Base.purple.value)
        self.btnOk.setFontColor(Theme.Light, CColor.Base.whtite.value)

    def __btn_connect(self):
        self.btnExit.clicked.connect(self.__cancel)
        self.btnCancel.clicked.connect(self.__cancel)
        self.btnOk.clicked.connect(self.__confirm)

    def __init_anim(self):
        self.fadeAnim = QPropertyAnimation(self, b"windowOpacity")
        self.fadeAnim.setDuration(200)


    def __play_FadeAnim(self,start: float, endValue: float):
        self.fadeAnim.stop()
        self.fadeAnim.setStartValue(start)
        self.fadeAnim.setEndValue(endValue)
        self.fadeAnim.start()
        
    def __play_FadeAnimToDo(self,start: float, endValue: float,finished: callable):
        self.fadeAnim.stop()
        self.fadeAnim.setStartValue(start)
        self.fadeAnim.setEndValue(endValue)
        self.fadeAnim.finished.connect(finished)
        self.fadeAnim.start()


    def exec(self):
        return super().exec()


    def __cancel(self):
        # 当点击退出按钮时，执行淡出动画并关闭窗口
        self.__play_FadeAnimToDo(1, 0, self.reject)


    def __confirm(self):
        # 当点击确定按钮时，执行淡出动画并关闭窗口
        self.__play_FadeAnimToDo(1, 0, self.accept)


    def mousePressEvent(self, event:QMouseEvent):
        GenericFunc.mousePressEvent(self, event)


    def mouseMoveEvent(self, event:QMouseEvent):
        GenericFunc.mouseMoveEvent(self, event)


    def mouseReleaseEvent(self, event:QMouseEvent):
        GenericFunc.mouseReleaseEvent(self, event)


    def paintEvent(self, event:QMouseEvent):
        super().paintEvent(event)
        GenericFunc.paintShadow(self)