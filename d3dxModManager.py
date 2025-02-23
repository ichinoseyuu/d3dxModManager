import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from main import d3dxModManager

if __name__ == "__main__":
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)
    window = d3dxModManager()
    window.show()
    app.exec()