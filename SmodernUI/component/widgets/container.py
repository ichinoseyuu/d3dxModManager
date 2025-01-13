from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import copy
from enum import Enum, auto
from ...core import Globals, CColor, Theme

class CContainer(QWidget):
    class Props(Enum):
        """summary: 容器相关属性

        Consts:
            Enum (auto): bg, border_top, border_right, border_bottom, border_left,

            border_T_R_radius, border_B_R_radius, border_B_L_radius, border_T_L_radius
        """
        bg = auto()                 # Background color
        border_T = auto()           # Top border style
        border_L = auto()           # Left border style
        border_R = auto()           # Right border style
        border_B = auto()           # Bottom border style
        radius_T_L = auto()         # Top left border radius
        radius_T_R = auto()         # Top right border radius
        radius_B_L = auto()         # Bottom left border radius
        radius_B_R = auto()         # Bottom right border radius

    map = {
            Theme.Light:{
                Props.bg: CColor.Presets.window_bg_light.value,
                Props.border_L: CColor.Presets.border_light.value,
                Props.border_R: CColor.Presets.border_light.value,
                Props.border_T: CColor.Presets.border_light.value,
                Props.border_B: CColor.Presets.border_light.value,
                Props.radius_T_L: 0,
                Props.radius_T_R: 0,
                Props.radius_B_L: 0,
                Props.radius_B_R: 0,
            },
            Theme.Dark:{
                Props.bg: QColor(60, 60, 60),
                Props.border_L: CColor.Base.transparent.value,
                Props.border_R: CColor.Base.transparent.value,
                Props.border_T: CColor.Base.transparent.value,
                Props.border_B: CColor.Base.transparent.name,
                Props.radius_T_L: 0,
                Props.radius_T_R: 0,
                Props.radius_B_L: 0,
                Props.radius_B_R: 0,
            }
        }

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__map = copy.deepcopy(CContainer.map)
        self.__init_props()
        self.__init_anim()
        self.__updateStyleSheet()


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
        return self.__border_L

    @borderColorL.setter
    def borderColorL(self, color):
        self.__border_L = color
        self.__updateStyleSheet()


    @Property(QColor)
    def borderColorR(self):
        return self.__border_R

    @borderColorR.setter
    def borderColorR(self, color):
        self.__border_R = color
        self.__updateStyleSheet()


    @Property(QColor)
    def borderColorT(self):
        return self.__border_T

    @borderColorR.setter
    def borderColorT(self, color):
        self.__border_T = color
        self.__updateStyleSheet()


    @Property(QColor)
    def borderColorB(self):
        return self.__border_B

    @borderColorR.setter
    def borderColorB(self, color):
        self.__border_B = color
        self.__updateStyleSheet()


    @Property(int)
    def borderRadiusTR(self):
        return self.__radius_T_R

    @borderRadiusTR.setter
    def borderRadiusTR(self, radius):
        self.__radius_T_R = radius
        self.__updateStyleSheet()


    @Property(int)
    def borderRadiusTL(self):
        return self.__radius_T_L

    @borderRadiusTL.setter
    def borderRadiusTL(self, radius):
        self.__radius_T_L = radius
        self.__updateStyleSheet()


    @Property(int)
    def borderRadiusBR(self):
        return self.__radius_B_R

    @borderRadiusBR.setter
    def borderRadiusBR(self, radius):
        self.__radius_B_R = radius
        self.__updateStyleSheet()


    @Property(int)
    def borderRadiusBL(self):
        return self.__radius_B_L

    @borderRadiusBR.setter
    def borderRadiusBL(self, radius):
        self.__radius_B_L = radius
        self.__updateStyleSheet()
    
    def __updateStyleSheet(self):
        style = f'''
            background-color: {CColor.toHex(self.__bg_color)};
            border-left: {CColor.toHex(self.__border_L)};
            border-right: {CColor.toHex(self.__border_R)};
            border-top: {CColor.toHex(self.__border_T)};
            border-bottom: {CColor.toHex(self.__border_B)};
            border-top-left-radius: {self.__radius_T_L}px;
            border-top-right-radius: {self.__radius_T_R}px;
            border-bottom-left-radius: {self.__radius_B_L}px;
            border-bottom-right-radius: {self.__radius_B_R}px;
        '''
        self.setStyleSheet(style)
    # endregion



    # region 内部方法
    def __init_props(self):
        '''初始化属性'''
        self.__bg_color = self.__map[Globals.theme][self.Props.bg]
        self.__border_L = self.__map[Globals.theme][self.Props.border_L]
        self.__border_R = self.__map[Globals.theme][self.Props.border_R]
        self.__border_T = self.__map[Globals.theme][self.Props.border_T]
        self.__border_B = self.__map[Globals.theme][self.Props.border_B]
        self.__radius_T_L = self.__map[Globals.theme][self.Props.radius_T_L]
        self.__radius_T_R = self.__map[Globals.theme][self.Props.radius_T_R]
        self.__radius_B_L = self.__map[Globals.theme][self.Props.radius_B_L]
        self.__radius_B_R = self.__map[Globals.theme][self.Props.radius_B_R]



    def __init_anim(self):
        '''初始化动画'''
        self.__bg_color_anim = QPropertyAnimation(self, b'backgroundColor')
        self.__bg_color_anim.setDuration(250)
        self.__border_L_anim = QPropertyAnimation(self, b'borderColorL')
        self.__border_L_anim.setDuration(250)
        self.__border_R_anim = QPropertyAnimation(self, b'borderColorR')
        self.__border_R_anim.setDuration(250)
        self.__border_T_anim = QPropertyAnimation(self, b'borderColorT')
        self.__border_T_anim.setDuration(250)
        self.__border_B_anim = QPropertyAnimation(self, b'borderColorB')
        self.__border_B_anim.setDuration(250)
        self.__radius_T_L_anim = QPropertyAnimation(self, b'borderRadiusTL')
        self.__radius_T_L_anim.setDuration(250)
        self.__radius_T_R_anim = QPropertyAnimation(self, b'borderRadiusTR')
        self.__radius_T_R_anim.setDuration(250)
        self.__radius_B_L_anim = QPropertyAnimation(self, b'borderRadiusBL')
        self.__radius_B_L_anim.setDuration(250)
        self.__radius_B_R_anim = QPropertyAnimation(self, b'borderRadiusBR')
        self.__radius_B_R_anim.setDuration(250)

    def __playBGColorAnim(self, end: QColor):
        '''播放颜色切换动画'''
        self.__bg_color_anim.stop()
        self.__bg_color_anim.setStartValue(self.__bg_color)
        self.__bg_color_anim.setEndValue(end)
        self.__bg_color_anim.start()

    def __playBorderLAnim(self, end: QColor):
        '''播放左边框颜色切换动画'''
        self.__border_L_anim.stop()
        self.__border_L_anim.setStartValue(self.__border_L)
        self.__border_L_anim.setEndValue(end)
        self.__border_L_anim.start()

    def __playBorderRAnim(self, end: QColor):
        '''播放右边框颜色切换动画'''
        self.__border_R_anim.stop()
        self.__border_R_anim.setStartValue(self.__border_R)
        self.__border_R_anim.setEndValue(end)
        self.__border_R_anim.start()

    def __playBorderTAnim(self, end: QColor):
        '''播放上边框颜色切换动画'''
        self.__border_T_anim.stop()
        self.__border_T_anim.setStartValue(self.__border_T)
        self.__border_T_anim.setEndValue(end)
        self.__border_T_anim.start()

    def __playBorderBAnim(self, end: QColor):
        '''播放下边框颜色切换动画'''
        self.__border_B_anim.stop()
        self.__border_B_anim.setStartValue(self.__border_B)
        self.__border_B_anim.setEndValue(end)
        self.__border_B_anim.start()
        
    def __playRadiusTLAnim(self, end: int):
        '''播放左上角圆角切换动画'''
        self.__radius_T_L_anim.stop()
        self.__radius_T_L_anim.setStartValue(self.__radius_T_L)
        self.__radius_T_L_anim.setEndValue(end)
        self.__radius_T_L_anim.start()
        
    def __playRadiusTRAnim(self, end: int):
        '''播放右上角圆角切换动画'''
        self.__radius_T_R_anim.stop()
        self.__radius_T_R_anim.setStartValue(self.__radius_T_R)
        self.__radius_T_R_anim.setEndValue(end)
        self.__radius_T_R_anim.start()

    def __playRadiusBLAnim(self, end: int):
        '''播放左下角圆角切换动画'''
        self.__radius_B_L_anim.stop()
        self.__radius_B_L_anim.setStartValue(self.__radius_B_L)
        self.__radius_B_L_anim.setEndValue(end)
        self.__radius_B_L_anim.start()

    def __playRadiusBRAnim(self, end: int):
        '''播放右下角圆角切换动画'''
        self.__radius_B_R_anim.stop()
        self.__radius_B_R_anim.setStartValue(self.__radius_B_R)
        self.__radius_B_R_anim.setEndValue(end)
        self.__radius_B_R_anim.start()

    # endregion



    # region 外部方法
    def setDurationForAnim(self, duration: int):
        """_summary_: 设置动画时长

        Args:
            duration (int): 时长(ms)
        """
        self.__bg_color_anim.setDuration(duration)
        self.__border_L_anim.setDuration(duration)
        self.__border_R_anim.setDuration(duration)
        self.__border_T_anim.setDuration(duration)
        self.__border_B_anim.setDuration(duration)
        self.__radius_T_L_anim.setDuration(duration)
        self.__radius_T_R_anim.setDuration(duration)
        self.__radius_B_L_anim.setDuration(duration)
        self.__radius_B_R_anim.setDuration(duration)


    def updateStyle(self, playAnim = False):
        if playAnim:
            self.__playBGColorAnim(self.__map[Globals.theme][self.Props.bg])
            self.__playBorderLAnim(self.map[Globals.theme][self.Props.border_L])
            self.__playBorderRAnim(self.map[Globals.theme][self.Props.border_R])
            self.__playBorderTAnim(self.map[Globals.theme][self.Props.border_T])
            self.__playBorderBAnim(self.map[Globals.theme][self.Props.border_B])
            self.__playRadiusTLAnim(self.map[Globals.theme][self.Props.radius_T_L])
            self.__playRadiusTRAnim(self.map[Globals.theme][self.Props.radius_T_R])
            self.__playRadiusBLAnim(self.map[Globals.theme][self.Props.radius_B_L])
            self.__playRadiusBRAnim(self.map[Globals.theme][self.Props.radius_B_R])
        else:
            self.backgroundColor = self.__map[Globals.theme][self.Props.bg]
            self.borderColorL = self.map[Globals.theme][self.Props.border_L]
            self.borderColorR = self.map[Globals.theme][self.Props.border_R]
            self.borderColorT = self.map[Globals.theme][self.Props.border_T]
            self.borderColorB = self.map[Globals.theme][self.Props.border_B]
            self.borderRadiusTL = self.map[Globals.theme][self.Props.radius_T_L]
            self.borderRadiusTR = self.map[Globals.theme][self.Props.radius_T_R]
            self.borderRadiusBL = self.map[Globals.theme][self.Props.radius_B_L]
            self.borderRadiusBR = self.map[Globals.theme][self.Props.radius_B_R]


    def setBgColor(self, theme: Theme, color: QColor, playAnim = False):
        self.__map[theme][self.Props.bg] = color
        if playAnim:
            self.__playBGColorAnim(color)
        else:
            self.backgroundColor = color


    def setBorderColor(self, theme: Theme, color: QColor,playAnim = False):
        self.setBorderColorT(theme, color, playAnim)
        self.setBorderColorB(theme, color, playAnim)
        self.setBorderColorL(theme, color, playAnim)
        self.setBorderColorR(theme, color, playAnim)


    def setBorderColorT(self, theme: Theme, color: QColor,playAnim = False):
        self.__map[theme][self.Props.border_T] = color
        if playAnim:
            self.__playBorderTAnim(color)
        else:
            self.borderColorT = color


    def setBorderColorL(self, theme: Theme, color: QColor, playAnim = False):
        self.__map[theme][self.Props.border_L] = color
        if playAnim:
            self.__playBorderLAnim(color)
        else:
            self.borderColorL = color


    def setBorderColorR(self, theme: Theme, color: QColor, playAnim = False):
        self.__map[theme][self.Props.border_R] = color
        if playAnim:
            self.__playBorderRAnim(color)
        else:
            self.borderColorR = color


    def setBorderColorB(self, theme: Theme, color: QColor, playAnim = False):
        self.__map[theme][self.Props.border_B] = color
        if playAnim:
            self.__playBorderBAnim(color)
        else:
            self.borderColorB = color



    def setBorderRadius(self, theme: Theme, radius: int, playAnim = False):
        self.setBorderRadiusTL(theme, radius, playAnim)
        self.setBorderRadiusTR(theme, radius, playAnim)
        self.setBorderRadiusBL(theme, radius, playAnim)
        self.setBorderRadiusBR(theme, radius, playAnim)


    def setBorderRadiusTL(self, theme: Theme, radius: int, playAnim = False):
        self.__map[theme][self.Props.radius_T_L] = radius
        if playAnim:
            self.__playRadiusTLAnim(radius)
        else:
            self.borderRadiusTL = radius


    def setBorderRadiusTR(self, theme: Theme, radius: int, playAnim = False):
        self.__map[theme][self.Props.radius_T_R] = radius
        if playAnim:
            self.__playRadiusTRAnim(radius)
        else:
            self.borderRadiusTR = radius


    def setBorderRadiusBL(self, theme: Theme, radius: int, playAnim = False):
        self.__map[theme][self.Props.radius_B_L] = radius
        if playAnim:
            self.__playRadiusBLAnim(radius)
        else:
            self.borderRadiusBL = radius


    def setBorderRadiusBR(self, theme: Theme, radius: int, playAnim = False):
        self.__map[theme][self.Props.radius_B_R] = radius
        if playAnim:
            self.__playRadiusBRAnim(radius)
        else:
            self.borderRadiusBR = radius

    # endregion



    # region 事件
    def mouseMoveEvent(self, event):
        return super().mouseMoveEvent(event)


    def mousePressEvent(self, event):
        return super().mousePressEvent(event)


    def mouseReleaseEvent(self, event):
        return super().mouseReleaseEvent(event)

    def dragEnterEvent(self, event):
        return super().dragEnterEvent(event)

    def dragLeaveEvent(self, event):
        return super().dragLeaveEvent(event)

    def dragMoveEvent(self, event):
        return super().dragMoveEvent(event)

    def paintEvent(self, event):
        super().paintEvent(event)



    # endregion