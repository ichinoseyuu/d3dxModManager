from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from SmodernUI import *
from .Ui_mainWindow import Ui_mainWindow

class d3dxModManager(QMainWindow,Ui_mainWindow):
    def __init__(self):
        super().__init__()
        Globals.ObjRef['TOOLTIP'] = CToolTip()
        self.setupUi(self)
        Globals.ObjRef['MAINWINDOW'] = self
        self.setWindowFlags(Qt.CustomizeWindowHint|Qt.FramelessWindowHint)
        self.setMenuWidget(CTitleBar())
        self._Ui_init()
        self.btnConnect()



    def _Ui_init(self):
        self.btnHome.setBGTransparentAllTheme()
        self.btnModule.setBGTransparentAllTheme()
        self.btnFolder.setBGTransparentAllTheme()
        self.btnConfig.setBGTransparentAllTheme()
        self.btnAbout.setBGTransparentAllTheme()
        self.btnTheme.setBGTransparentAllTheme()
        self.btnSearch.setBorderColor(Theme.Light, QColor(211, 211, 211))
        self.btnSelect_1.setBorderColor(Theme.Light, QColor(211, 211, 211))
        self.btnSelect_2.setBorderColor(Theme.Light, QColor(211, 211, 211))
        self.btnPlay.setBGColor(Theme.Light, CColor.Base.darkPink.value)
        self.btnPlay.setBGColor(Theme.Dark, CColor.Base.purple.value)
        self.btnPlay.setFontColor(Theme.Light, CColor.Base.whtite.value)
        self.btnPlay.setFontSize(Theme.Light,CFont.Size.large.value)
        
    def test(self):
        print('test')
        self.btnPlay.setBorderRadius(Theme.Light, 20,True)
        self.btnPlay.setFontSize(Theme.Light, 15,True)
        self.btnPlay.setBGColor(Theme.Light, CColor.Base.purple.value,True)


    def btnConnect(self):
        #左侧菜单栏按钮
        self.btnHome.clicked.connect(lambda: self.swithPage(0))
        self.btnModule.clicked.connect(lambda: self.swithPage(1))
        self.btnFolder.clicked.connect(lambda: self.swithPage(2))
        self.btnConfig.clicked.connect(lambda: self.swithPage(3))
        self.btnAbout.clicked.connect(lambda: self.swithPage(4))
        self.btnTheme.clicked.connect(lambda: Globals.changeTheme())
        # self.btnTheme.clicked.connect(self.test)


    def swithPage(self, index: int):
        self.stackedWidget.setCurrentIndex(index)


    def closeEvent(self, event):
        message = CDialog('退出', '您确定要退出吗？', self)
        reply = message.exec()
        if reply == 1:
            event.accept()
        else:
            event.ignore()

    def mousePressEvent(self, event):
        GenericFunc.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        GenericFunc.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        GenericFunc.mouseReleaseEvent(self, event)

    def paintShadow(self):
        GenericFunc.paintShadow(self)


