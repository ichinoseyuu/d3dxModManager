from .globals import *
from .func import debug
from ..component.window.tooltip import CToolTip
from ..component.window.frameless_window import FramelessWindow
from ..component.widgets.button import CButton
from ..component.widgets.container import CContainer
from PySide6.QtCore import Qt
def initialize(window: FramelessWindow,title: str = 'SmodernUI'):
    """_summary_: 初始化ui框架

    Args:
        window (FramelessWindow): 主窗口
        title (str, optional): 窗口标题. Defaults to 'SmodernUI'.
    """
    debug('当前主题：',Var.theme)
    Var.objref['mainwindow'] = window
    debug(f"mainwindow: {Var.objref['mainwindow']}")

    Var.objref['tooltip'] = CToolTip()
    debug(f"tooltip: {Var.objref['tooltip']}")


    addObjList2Ref(findObjByType(Var.objref['mainwindow'], CButton),'btn')
    for btn in Var.objref['btn']:
        debug(f"btn: {btn}")

    addObjList2Ref(findObjByType(Var.objref['tooltip'], CContainer),'btn')
    addObjList2Ref(findObjByType(Var.objref['mainwindow'], CContainer),'container')
    for container in Var.objref['container']:
        debug(f"btn: {container}")


    window.titleBar.setTitle(title)
    debug(f"WindowTitle: {title}")


    window.setAttribute(Qt.WA_TranslucentBackground)
    #window.windowEffect.enableBlurBehindWindow(window.winId())
    window.setCenter()


