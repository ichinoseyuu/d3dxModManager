from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class CLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        