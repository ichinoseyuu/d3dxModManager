# coding:utf-8
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from SmodernUI import *


class MainWindow(FramelessWindow):

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.resize(800, 600)
        initialize(self)


    def setupUi(self):
        self.vlayout = QVBoxLayout(self)
        self.vlayout.setSpacing(0)
        self.vlayout.setContentsMargins(0, 36, 0, 0)

        self.board = CContainer(self)
        self.board.setObjectName(u"board")
        self.board.setBGColors({Theme.Dark: QColor(120, 120, 120), Theme.Light: QColor(200, 200, 200)})
        self.vlayout.addWidget(self.board)

        self.hlayout = QHBoxLayout(self.board)
        self.hlayout.setSpacing(6)
        self.hlayout.setContentsMargins(6, 6, 6, 6)


        self.left = CContainer(self.board)
        self.left.setObjectName(u"left")
        self.left.setRadius((1, 1, 1, 1), 8)
        self.left.setRadius((1, 1, 1, 1), 8, Theme.Dark)

        self.right = CContainer(self.board)
        self.right.setObjectName(u"right")
        self.vlayout2 = QVBoxLayout(self.left)
        self.vlayout3 = QVBoxLayout(self.right)
        self.vlayout2.setSpacing(6)
        self.vlayout2.setContentsMargins(6, 6, 6, 6)
        self.vlayout2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vlayout3.setSpacing(6)
        self.vlayout3.setContentsMargins(6, 6, 6, 6)
        self.vlayout3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hlayout.addWidget(self.left)
        self.hlayout.addWidget(self.right)

        self.btnTheme = CButton(self.board)
        self.btnTheme.setObjectName("btnTheme")
        self.btnTheme.setTipText("切换主题")
        self.btnTheme.setMinimumSize(QSize(80, 80))
        self.btnTheme.setMaximumSize(QSize(80, 80))
        icon5 = QIcon()
        icon5.addFile(u":/iamge_pack/tab/dark_theme.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/iamge_pack/tab/light_theme.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnTheme.setIcon(icon5)
        self.btnTheme.setIconSize(QSize(24, 24))
        self.btnTheme.setCheckable(True)
        self.btnTheme.setChecked(False)
        self.btnTheme.clicked.connect(lambda: self.changeTheme())
        #self.btnTheme.clicked.connect(self._updateSheet)
        self.vlayout2.addWidget(self.btnTheme)

        self.btnTest1 = CButton(self.board)
        self.btnTest1.setObjectName("btnTest1")
        self.btnTest1.setTipText("测试按钮")
        self.btnTest1.setMinimumSize(QSize(80, 80))
        self.btnTest1.setMaximumSize(QSize(80, 80))
        self.vlayout2.addWidget(self.btnTest1)

        self.textedit = QTextEdit(self.board)
        self.textedit.setStyleSheet(u"background-color: rgb(233, 233, 233);")
        self.textedit.setPlaceholderText("请输入内容")
        self.textedit.setReadOnly(False)
        self.vlayout3.addWidget(self.textedit)
        self.btnTest2 = CButton(self.board)
        self.btnTest2.setObjectName("btnTest2")
        self.btnTest2.setTipText("测试按钮")
        self.btnTest2.setMinimumSize(QSize(80, 80))
        self.vlayout3.addWidget(self.btnTest2)
    def changeTheme(self):
        changeTheme()

if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)
    window = MainWindow()
    window.show()
    app.exec()
