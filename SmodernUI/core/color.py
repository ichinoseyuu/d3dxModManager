from PySide6.QtGui import QColor
from PySide6.QtCore import Signal,QObject
from enum import Enum, auto
from .globals import Globals

class Color():
    class Base(Enum):
        Transparent = QColor(255, 255, 255, 0)
        Magenta = QColor(255, 0, 255)
        Pink = QColor(255, 192, 203)
        DarkPink = QColor(255, 99, 134)
        Purple = QColor(211, 155, 203)
        DarkPurple = QColor(148, 0, 211)
        Whtite = QColor(255, 255, 255)
    class light(Enum):
        Titlebar = QColor(250, 245, 245)

        Btn_hover = QColor(220, 220, 220)
        Btn_pressed = QColor(211, 211, 211)
        Btn_normal = QColor(235, 235, 235)
        Btn_border = QColor(255, 255, 255, 0)
        Btn_font = QColor(60, 60, 60)
    class dark(Enum):
        Titlebar = QColor(255, 255, 255)

        Btn_hover = QColor(220, 220, 220)
        Btn_pressed = QColor(235, 235, 235)
        Btn_normal = QColor(211, 211, 211)
        Btn_border = QColor(255, 255, 255, 0)
        Btn_font = QColor(255, 255, 255)

    def toHex(color: QColor):
        return f"#{color.alpha():02x}{color.red():02x}{color.green():02x}{color.blue():02x}"