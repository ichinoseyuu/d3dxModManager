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
        self.setWindowFlags(Qt.FramelessWindowHint) # 表示窗口没有边框
        self.setAttribute(Qt.WA_TranslucentBackground) # 表示窗口具有透明效果
        self._Ui_init()
        self.btnConnect()


    def _Ui_init(self):
        btns = Globals.findObjByType(self, CButton)
        Globals.addObjList2Ref(btns,'BTN')
        for btn in btns:
            btn.updateStyle()
        self.btnMin.setBGTransparentAllTheme()
        self.btnExit.setBGTransparentAllTheme()
        self.btnHome.setBGTransparentAllTheme()
        self.btnModule.setBGTransparentAllTheme()
        self.btnFolder.setBGTransparentAllTheme()
        self.btnConfig.setBGTransparentAllTheme()
        self.btnAbout.setBGTransparentAllTheme()
        self.btnTheme.setBGTransparentAllTheme()
        self.btnSearch.setBorderColor(Globals.Theme.Light, QColor(211, 211, 211))
        self.btnSelect_1.setBorderColor(Globals.Theme.Light, QColor(211, 211, 211))
        self.btnSelect_2.setBorderColor(Globals.Theme.Light, QColor(211, 211, 211))
        self.btnPlay.setBGColor(Globals.Theme.Light,Color.Base.DarkPink.value)
        self.btnPlay.setBGColor(Globals.Theme.Dark,Color.Base.Purple.value)
        self.btnPlay.setFontColor(Globals.Theme.Light,Color.Base.Whtite.value)


    def btnConnect(self):
        #标题栏按钮
        self.btnMin.clicked.connect(self.showMinimized) #最小化
        self.btnExit.clicked.connect(self.quit) # 右上角退出

        #左侧菜单栏按钮
        self.btnHome.clicked.connect(lambda: self.swithPage(0))
        self.btnModule.clicked.connect(lambda: self.swithPage(1))
        self.btnFolder.clicked.connect(lambda: self.swithPage(2))
        self.btnConfig.clicked.connect(lambda: self.swithPage(3))
        self.btnAbout.clicked.connect(lambda: self.swithPage(4))
        self.btnTheme.clicked.connect(lambda: Globals.changeTheme())
        #self.btnTheme.clicked.connect(self.btnPlay.toggleTransparent)
        #self.btnTheme.clicked.connect(self.btnPlay.switchFontColor)

    def swithPage(self, index: int):
        self.stackedWidget.setCurrentIndex(index)


    def quit(self):
        message = CMessage('退出', '您确定要退出吗？', self)
        reply = message.exec()
        if reply == 1:
            QApplication.instance().quit()

    def mousePressEvent(self, event):
        GenericFunc.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        GenericFunc.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        GenericFunc.mouseReleaseEvent(self, event)

    def paintShadow(self):
        GenericFunc.paintShadow(self)
