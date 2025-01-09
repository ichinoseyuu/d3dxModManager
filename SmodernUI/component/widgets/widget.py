from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from ...core import Globals, Color

class CWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.isTransparent = True
        self.haveBorder = False
        self.isRounded = False


    @Property(QColor)
    def backgroundColor(self):
        return self.bg_color
    @backgroundColor.setter
    def backgroundColor(self, color):
        self.setStyleSheet(f'''
                        background-color: {Color.toHex(color)};
                        border:1px solid {Color.toHex(self.border_color)};
                        border-radius: 4px;
                        ''')

    @Property(QColor)
    def borderColor(self):
        return self.border_color
    @borderColor.setter
    def borderColor(self, color):
        self.setStyleSheet(f'''
                        border:1px solid {Color.toHex(color)};
                        border-radius: 4px;
                        ''')


    @Property(int)
    def round(self):
        return self.round_val
    @borderColor.setter
    def round(self, round_val):
        self.setStyleSheet(f'''
                        border:1px solid {Color.toHex(self.border_color)};
                        border-radius: {round_val}px;
                        ''')
