import sys
from PySide6.QtWidgets import QApplication
from main import d3dxModManager

if __name__ == "__main__":
    app = QApplication(sys.argv)
    modManager = d3dxModManager()
    modManager.show()
    sys.exit(app.exec())