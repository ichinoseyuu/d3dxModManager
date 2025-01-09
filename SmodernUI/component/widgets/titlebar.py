from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
# 使用方法
# self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint)
# self.setMenuWidget(CTitleBar())
class CTitleBar(QWidget):
    def __init__(self):
        super().__init__()

        # 设置标题栏的样式
        self.setStyleSheet("background-color: #2C3E50; color: white; height: 30px;")

        # 布局：水平布局（按钮 + 标题文本）
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # 标题文本
        self.titleLabel = QLabel("自定义标题栏", self)
        layout.addWidget(self.titleLabel)

        # 关闭按钮
        self.closeButton = QPushButton("X", self)
        self.closeButton.clicked.connect(self.closeWindow)
        layout.addWidget(self.closeButton)

        self.setLayout(layout)

    def closeWindow(self):
        self.window().close()