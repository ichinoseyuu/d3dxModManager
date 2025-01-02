from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt, QPropertyAnimation
from SmodernUI import Ui_message
from SmodernUI import GenericFunc

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

        self.btnExit.clicked.connect(self.cancel)
        self.btnCancel.clicked.connect(self.cancel)
        self.btnOk.clicked.connect(self.confirm)

        # 添加淡入效果 (通过调整窗口的透明度)
        self.fadeAnim = QPropertyAnimation(self, b"windowOpacity")
        self.fadeAnim.setDuration(200)
        self.fadeAnim.setStartValue(0)
        self.fadeAnim.setEndValue(1)
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