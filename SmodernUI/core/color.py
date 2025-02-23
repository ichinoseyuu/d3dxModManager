from PySide6.QtGui import QColor
from enum import Enum, unique

class ColorBase(Enum):
    """基础颜色表
    Attributes:
        transparent(QColor(255, 255, 255, 0)): 透明色
        magenta(QColor(255, 0, 255)): 洋红色
        pink(QColor(255, 192, 203)): 粉红色
        darkPink(QColor(255, 99, 134)): 深粉红色
        purple(QColor(211, 155, 203)): 紫色
        darkPurple(QColor(148, 0, 211)): 深紫色
        whtite(QColor(255, 255, 255)): 白色
    """
    transparent = QColor(255, 255, 255, 0)
    magenta = QColor(255, 0, 255)
    pink = QColor(255, 192, 203)
    darkPink = QColor(255, 99, 134)
    purple = QColor(211, 155, 203)
    darkPurple = QColor(148, 0, 211)
    whtite = QColor(255, 255, 255)

class ColorPresets(Enum):
    """预设颜色表
    Attributes:
        window_bg_light(QColor(250, 245, 245, 255)): 浅色背景色
        border_light(QColor(235, 235, 235)): 浅色边框色
        window_bg_dark(QColor(60, 60, 60, 255)): 深色背景色
    """
    window_bg_light = QColor(250, 245, 245, 255)
    border_light = QColor(235, 235, 235)
    window_bg_dark = QColor(60, 60, 60, 255)
    btn_exit_hover =  QColor(255, 0, 0, 150)

def toHex(color: QColor):
    """将颜色转换为16进制字符串
    Args:
        color(QColor): 需要转换的颜色
    Returns:
        str: 转换后的16进制字符串
    """
    return f"#{color.alpha():02x}{color.red():02x}{color.green():02x}{color.blue():02x}"