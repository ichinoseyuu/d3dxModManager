import sys
from PySide6.QtWidgets import QApplication
from core import core

if __name__ == "__main__":
    app = QApplication(sys.argv)
    core = core()
    core.show()
    sys.exit(app.exec())