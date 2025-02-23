from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from SmodernUI import *
from .Ui_mainwindow import Ui_mainwindow

class d3dxModManager(FramelessWindow,Ui_mainwindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._Ui_init()
        initialize(self,"d3dxModManager")
        self.btnConnect()



    def _Ui_init(self):
        self.btnHome.setBGTransparent()
        self.btnModule.setBGTransparent()
        self.btnFolder.setBGTransparent()
        self.btnConfig.setBGTransparent()
        self.btnAbout.setBGTransparent()
        self.btnTheme.setBGTransparent()
        self.btnSearch.setBorderColor(QColor(211, 211, 211))
        self.btnSelect_1.setBorderColor(QColor(211, 211, 211))
        self.btnSelect_2.setBorderColor(QColor(211, 211, 211))
        self.btnPlay.setBGColor(ColorBase.darkPink.value)
        self.btnPlay.setBGColor(ColorBase.purple.value, Theme.Dark)
        self.btnPlay.setFontColor(ColorBase.whtite.value)
        self.btnPlay.setFontSize(FontSize.large)
        
    def test(self):
        print('test')
        self.btnPlay.setRadiusSizes({Theme.Light: 20, Theme.Dark: 20})
        self.btnPlay.setFontSize(FontSize.large)
        self.btnPlay.setBGColor(ColorBase.purple.value,True)


    def btnConnect(self):
        #左侧菜单栏按钮
        self.btnHome.clicked.connect(lambda: self.swithPage(0))
        self.btnModule.clicked.connect(lambda: self.swithPage(1))
        self.btnFolder.clicked.connect(lambda: self.swithPage(2))
        self.btnConfig.clicked.connect(lambda: self.swithPage(3))
        self.btnAbout.clicked.connect(lambda: self.swithPage(4))
        self.btnTheme.clicked.connect(lambda: changeTheme())
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


