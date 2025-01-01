import enum
from PySide6.QtGui import QColor

class BtnColor(enum.Enum):
    Normal = QColor(255, 240, 254)
    Hover = QColor(241, 230, 243)
    Pressed = QColor(231, 220, 233)
    Text = QColor(0, 0, 0)