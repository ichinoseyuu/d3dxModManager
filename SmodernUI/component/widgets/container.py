from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from ...core import Globals, CColor

class CContainer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)



    # region 属性
    @Property(QColor)
    def backgroundColor(self):
        return self.__bg_color

    @backgroundColor.setter
    def backgroundColor(self, color):
        self.__bg_color = color
        self.__updateStyleSheet()


    @Property(QColor)
    def borderColorL(self):
        return self.__border_color

    @borderColorL.setter
    def borderColorL(self, color):
        self.__border_color = color
        self.__updateStyleSheet()


    @Property(QColor)
    def borderColorR(self):
        return self.__border_color

    @borderColorR.setter
    def borderColorR(self, color):
        self.__border_color = color
        self.__updateStyleSheet()


    @Property(QColor)
    def borderColorT(self):
        return self.__border_color

    @borderColorR.setter
    def borderColorT(self, color):
        self.__border_color = color
        self.__updateStyleSheet()


    @Property(QColor)
    def borderColorB(self):
        return self.__border_color

    @borderColorR.setter
    def borderColorB(self, color):
        self.__border_color = color
        self.__updateStyleSheet()


    @Property(int)
    def borderRadiusTR(self):
        return self.__border_radius_left

    @borderRadiusTR.setter
    def borderRadiusLeft(self, left):
        self.__border_radius_left = left
        self.__updateStyleSheet()


    @Property(int)
    def borderRadiusTL(self):
        return self.__border_radius_right

    @borderRadiusTL.setter
    def borderRadiusTL(self, right):
        self.__border_radius_right = right
        self.__updateStyleSheet()


    @Property(int)
    def borderRadiusBR(self):
        return self.__border_radius_right

    @borderRadiusBR.setter
    def borderRadiusBR(self, right):
        self.__border_radius_right = right
        self.__updateStyleSheet()


    @Property(int)
    def borderRadiusBR(self):
        return self.__border_radius_right

    @borderRadiusBR.setter
    def borderRadiusBR(self, right):
        self.__border_radius_right = right
        self.__updateStyleSheet()
    # endregion



    # region 内部方法
    # endregion



    # region 外部方法
    # endregion



    # region 事件
    # endregion