# coding:utf-8
import sys
from ctypes import cast
from ctypes.wintypes import LPRECT, MSG

import win32api
import win32con
import win32gui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from .titlebar import CTitleBar
from .utils import win32_utils as win_utils
from .utils.win32_utils import Taskbar
from .utils.c_structures import LPNCCALCSIZE_PARAMS
from .utils.window_effect import WindowEffect



class FramelessWindow(QWidget):
    """  Frameless window for Windows system """

    border_width = 5

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.windowEffect = WindowEffect(self)
        self._isSystemButtonVisible = False
        self._isResizeEnabled = True
        self.updateFrameless()
        self.windowHandle().screenChanged.connect(self.__onScreenChanged)
        self.resize(500, 500)
        self.titleBar = CTitleBar(self)
        self.titleBar.raise_() #将标题显示在最上层

    def updateFrameless(self):
        """ 更新窗口标题栏 """

        self.setWindowFlags(Qt.FramelessWindowHint)
        # add DWM shadow and window animation
        self.windowEffect.addWindowAnimation(self.winId())
        if not isinstance(self, AcrylicWindow):
            self.windowEffect.addShadowEffect(self.winId())

    def setTitlebar(self, titlebar: QWidget):
        self.titleBar = titlebar
        self.layout().addWidget(self.titlebar)
        w = self.window().size().width()
        h = self.window().size().height() + self.titlebar.size().height()
        self.resize(w, h)
        self.window().setMinimumSize(QSize(w, h))

    def setTitleBar(self, titleBar: QWidget):
        self.titleBar.deleteLater()
        self.titleBar.hide()
        self.titleBar = titleBar
        self.titleBar.setParent(self)
        self.titleBar.raise_()

    def setCenter(self):
        ''' 将窗口居中 '''
        # 获取当前屏幕的尺寸
        screen = QApplication.primaryScreen()
        # 计算窗口应该放置的位置，使其位于屏幕中央
        x = (screen.geometry().width() - self.geometry().width()) // 2
        y = (screen.geometry().height() - self.geometry().height()) // 2
        # 设置窗口位置为屏幕中心
        self.move(x, y)

    def setResizeEnabled(self, isEnabled: bool):
        """ set whether resizing is enabled """
        self._isResizeEnabled = isEnabled

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self.titleBar.resize(self.width(), self.titleBar.height())

    def isSystemButtonVisible(self):
        """ Returns whether the system title bar button is visible """
        return self._isSystemButtonVisible

    def nativeEvent(self, eventType, message):
        """ Handle the Windows message """
        msg = MSG.from_address(message.__int__())
        if not msg.hWnd:
            return super().nativeEvent(eventType, message)

        if msg.message == win32con.WM_NCHITTEST and self._isResizeEnabled:
            pos = QCursor.pos()
            xPos = pos.x() - self.x()
            yPos = pos.y() - self.y()
            w = self.frameGeometry().width()
            h = self.frameGeometry().height()

            bw = 0 if win_utils.isMaximized(msg.hWnd) or win_utils.isFullScreen(msg.hWnd) else self.border_width
            lx = xPos < bw
            rx = xPos > w - bw
            ty = yPos < bw
            by = yPos > h - bw
            if lx and ty:
                return True, win32con.HTTOPLEFT
            elif rx and by:
                return True, win32con.HTBOTTOMRIGHT
            elif rx and ty:
                return True, win32con.HTTOPRIGHT
            elif lx and by:
                return True, win32con.HTBOTTOMLEFT
            elif ty:
                return True, win32con.HTTOP
            elif by:
                return True, win32con.HTBOTTOM
            elif lx:
                return True, win32con.HTLEFT
            elif rx:
                return True, win32con.HTRIGHT
        elif msg.message == win32con.WM_NCCALCSIZE:
            if msg.wParam:
                rect = cast(msg.lParam, LPNCCALCSIZE_PARAMS).contents.rgrc[0]
            else:
                rect = cast(msg.lParam, LPRECT).contents

            isMax = win_utils.isMaximized(msg.hWnd)
            isFull = win_utils.isFullScreen(msg.hWnd)

            # adjust the size of client rect
            if isMax and not isFull:
                ty = win_utils.getResizeBorderThickness(msg.hWnd, False)
                rect.top += ty
                rect.bottom -= ty

                tx = win_utils.getResizeBorderThickness(msg.hWnd, True)
                rect.left += tx
                rect.right -= tx

            # handle the situation that an auto-hide taskbar is enabled
            if (isMax or isFull) and Taskbar.isAutoHide():
                position = Taskbar.getPosition(msg.hWnd)
                if position == Taskbar.LEFT:
                    rect.top += Taskbar.AUTO_HIDE_THICKNESS
                elif position == Taskbar.BOTTOM:
                    rect.bottom -= Taskbar.AUTO_HIDE_THICKNESS
                elif position == Taskbar.LEFT:
                    rect.left += Taskbar.AUTO_HIDE_THICKNESS
                elif position == Taskbar.RIGHT:
                    rect.right -= Taskbar.AUTO_HIDE_THICKNESS

            result = 0 if not msg.wParam else win32con.WVR_REDRAW
            return True, result

        return super().nativeEvent(eventType, message)

    def __onScreenChanged(self):
        hWnd = int(self.windowHandle().winId())
        win32gui.SetWindowPos(hWnd, None, 0, 0, 0, 0, win32con.SWP_NOMOVE |
                            win32con.SWP_NOSIZE | win32con.SWP_FRAMECHANGED)

    def closeEvent(self, event):
        from .dialog import CDialog
        message = CDialog('退出', '您确定要退出吗？', self)
        result = message.exec()
        if result == 1:
            event.accept()
        else:
            event.ignore()


class AcrylicWindow(FramelessWindow):
    """ A frameless window with acrylic effect """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__closedByKey = False
        self.setStyleSheet("AcrylicWindow{background:transparent}")

    def updateFrameless(self):
        super().updateFrameless()
        self.windowEffect.enableBlurBehindWindow(self.winId())

        if win_utils.isWin7() and self.parent():
            self.setWindowFlags(self.parent().windowFlags() | Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)
        else:
            self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)

        self.windowEffect.addWindowAnimation(self.winId())

        if win_utils.isWin7():
            self.windowEffect.addShadowEffect(self.winId())
            self.windowEffect.setAeroEffect(self.winId())
        else:
            self.windowEffect.setAcrylicEffect(self.winId())
            if win_utils.isGreaterEqualWin11():
                self.windowEffect.addShadowEffect(self.winId())

    def nativeEvent(self, eventType, message):
        """ Handle the Windows message """
        msg = MSG.from_address(message.__int__())

        # handle Alt+F4
        if msg.message == win32con.WM_SYSKEYDOWN:
            if msg.wParam == win32con.VK_F4:
                self.__closedByKey = True
                QApplication.sendEvent(self, QCloseEvent())
                return False, 0

        return super().nativeEvent(eventType, message)

    def closeEvent(self, e):
        if not self.__closedByKey or QApplication.quitOnLastWindowClosed():
            self.__closedByKey = False
            return super().closeEvent(e)

        # system tray icon
        self.__closedByKey = False
        self.hide()
