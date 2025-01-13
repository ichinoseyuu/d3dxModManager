from PySide6.QtGui import QColor
from enum import Enum, unique

class CColor:
    '''颜色表'''
    @unique
    class Base(Enum):
        """_summary_: 基础颜色表

        Args:
            Enum (QColor): transparent = QColor(255, 255, 255, 0)
            Enum (QColor): magenta = QColor(255, 0, 255)
            Enum (QColor): pink = QColor(255, 192, 203)
            Enum (QColor): darkPink = QColor(255, 99, 134)
            Enum (QColor): purple = QColor(211, 155, 203)
            Enum (QColor): darkPurple = QColor(148, 0, 211)
            Enum (QColor): whtite = QColor(255, 255, 255)
        """
        transparent = QColor(255, 255, 255, 0)
        magenta = QColor(255, 0, 255)
        pink = QColor(255, 192, 203)
        darkPink = QColor(255, 99, 134)
        purple = QColor(211, 155, 203)
        darkPurple = QColor(148, 0, 211)
        whtite = QColor(255, 255, 255)

    class Presets(Enum):
        window_bg_light = QColor(250, 245, 245, 255)
        border_light = QColor(235, 235, 235)

    def toHex(color: QColor):
        return f"#{color.alpha():02x}{color.red():02x}{color.green():02x}{color.blue():02x}"