from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from enum import Enum
import copy
from ...core import Globals, Color

class CButton(QPushButton):
    class MapType(Enum):
        BG_color = 'bg_color'
        BG_color_hover = 'bg_color_hover'
        BG_color_pressed = 'bg_color_pressed'
        Border_color = 'border_color'
        Font_color = 'font_color'
    default_map = {
            MapType.BG_color:{
                Globals.Theme.Light: Color.light.Btn_normal.value,
                Globals.Theme.Dark: Color.dark.Btn_normal.value,
            },
            MapType.BG_color_hover:{
                Globals.Theme.Light: Color.light.Btn_hover.value,
                Globals.Theme.Dark: Color.dark.Btn_hover.value,
            },
            MapType.BG_color_pressed:{
                Globals.Theme.Light: Color.light.Btn_pressed.value,
                Globals.Theme.Dark: Color.dark.Btn_pressed.value,
            },
            MapType.Border_color:{
                Globals.Theme.Light: Color.light.Btn_border.value,
                Globals.Theme.Dark: Color.dark.Btn_border.value,
            },
            MapType.Font_color:{
                Globals.Theme.Light: Color.light.Btn_font.value,
                Globals.Theme.Dark: Color.dark.Btn_font.value,
            }
        }
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__map = copy.deepcopy(self.default_map)
        self.__tip_text = ''
        self.__init_color()
        self.__init_Anim()


    # region 属性
    @Property(QColor)
    def backgroundColor(self):
        return self.__bg_color
    @backgroundColor.setter
    def backgroundColor(self, color):
        self.__bg_color = color
        self.__updateStyleSheet()


    @Property(QColor)
    def borderColor(self):
        return self.__border_color
    @borderColor.setter
    def borderColor(self, color):
        self.__border_color = color
        self.__updateStyleSheet()


    @Property(QColor)
    def fontColor(self):
        return self.__font_color
    @fontColor.setter
    def fontColor(self, color):
        self.__font_color = color
        self.__updateStyleSheet()


    def __updateStyleSheet(self):
        style = f'''
        background-color: {Color.toHex(self.__bg_color)};
        border: 1px solid {Color.toHex(self.__border_color)};
        color: {Color.toHex(self.__font_color)};
        font-size: 10pt;
        border-radius: 4px;
        '''
        self.setStyleSheet(style)

    # endregion



    # region 私有方法

    def __init_color(self):
        '''初始化颜色'''
        self.__bg_color = self.__map[self.MapType.BG_color][Globals.theme]
        self.__font_color = self.__map[self.MapType.Font_color][Globals.theme]
        self.__border_color = self.__map[self.MapType.Border_color][Globals.theme]


    def __init_Anim(self):
        '''初始化动画'''
        self.__bg_color_anim = QPropertyAnimation(self, b"backgroundColor")
        self.__bg_color_anim.setDuration(250)
        self.__border_anim = QPropertyAnimation(self, b"borderColor")
        self.__border_anim.setDuration(250)
        self.__font_anim = QPropertyAnimation(self, b"fontColor")
        self.__font_anim.setDuration(250)

    def __playColorAnim(self, end: QColor):
        '''播放颜色切换动画'''
        self.__bg_color_anim.stop()
        self.__bg_color_anim.setStartValue(self.__bg_color)
        self.__bg_color_anim.setEndValue(end)
        self.__bg_color_anim.start()


    def __playBorderAnim(self, end: QColor):
        '''播放边框颜色切换动画'''
        self.__border_anim.stop()
        self.__border_anim.setStartValue(self.__border_color)
        self.__border_anim.setEndValue(end)
        self.__border_anim.start()

    def __playFontAnim(self, end: QColor):
        '''播放边框颜色切换动画'''
        self.__font_anim.stop()
        self.__font_anim.setStartValue(self.__font_color)
        self.__font_anim.setEndValue(end)
        self.__font_anim.start()

    # endregion


    # region 公共方法
    def setTipText(self, text: str):
        '''设置提示文本'''
        self.__tip_text= text


    def updateBGColor(self, playAnim=False):
        '''更新背景颜色'''
        if playAnim:
            self.__playColorAnim(self.__map[self.MapType.BG_color][Globals.theme])
        else:
            self.backgroundColor = self.__map[self.MapType.BG_color][Globals.theme]


    def updateBorderColor(self,playAnim=False):
        '''更新边框颜色'''
        if playAnim:
            self.__playBorderAnim(self.__map[self.MapType.Border_color][Globals.theme])
        else:
            self.borderColor = self.__map[self.MapType.Border_color][Globals.theme]


    def updateFontColor(self,playAnim=False):
        '''更新字体颜色'''
        if playAnim:
            self.__playFontAnim(self.__map[self.MapType.Font_color][Globals.theme])
        else:
            self.fontColor = self.__map[self.MapType.Font_color][Globals.theme]


    def updateStyle(self, playAnim=False):
        '''更新按钮样式'''
        self.updateBGColor(playAnim)
        self.updateBorderColor(playAnim)
        self.updateFontColor(playAnim)


    def setBGColor(self,theme: Globals.Theme, color: QColor, playAnim=False):
        """_summary_: 更改背景颜色及Map

        Args:
            theme (Globals.Theme):  主题
            color (QColor): 颜色
            playAnim (bool, optional): 是否播放动画. Defaults to False.
        """
        self.__map[self.MapType.BG_color][theme] = color
        if theme != Globals.theme: return
        self.updateBGColor(playAnim)


    def setBorderColor(self, theme: Globals.Theme, color: QColor, playAnim=False):
        """_summary_: 更改边框颜色及Map

        Args:
            theme (Globals.Theme):  主题
            color (QColor): 颜色
            playAnim (bool, optional): 是否播放动画. Defaults to False.
        """
        self.__map[self.MapType.Border_color][theme] = color
        if theme != Globals.theme: return
        self.updateBorderColor(playAnim)


    def setFontColor(self, theme: Globals.Theme, color: QColor, playAnim=False):
        """_summary_: 更改字体颜色及Map

        Args:
            theme (Globals.Theme):  主题
            color (QColor): 颜色
            playAnim (bool, optional): 是否播放动画. Defaults to False.
        """
        self.__map[self.MapType.Font_color][theme] = color
        if theme != Globals.theme: return
        self.updateFontColor(playAnim)


    def setBGTransparentAllTheme(self,haveAnim: bool = False):
        """_summary_: 设置该控件所有主题透明

        Args:
            haveAnim (bool, optional): 是否播放动画. Defaults to False.
        """
        self.__map[self.MapType.BG_color][Globals.Theme.Light] = Color.Base.Transparent.value
        self.__map[self.MapType.BG_color][Globals.Theme.Dark] = Color.Base.Transparent.value
        self.updateBGColor(haveAnim)


    def setBGTransparent(self, theme: Globals.Theme, haveAnim: bool = False):
        """_summary_: 设置该控件指定主题透明

        Args:
            theme (Globals.Theme):  主题
            haveAnim (bool, optional): 是否播放动画. Defaults to False.
        """
        self.__map[self.MapType.BG_color][theme] = Color.Base.Transparent.value
        if theme != Globals.theme: return
        self.updateBGColor(haveAnim)


    def removeBorderAllTheme(self, haveAnim: bool = False):
        """_summary_: 移除所有主题边框

        Args:
            haveAnim (bool, optional): 是否播放动画. Defaults to False.
        """
        self.__map[self.MapType.Border_color][Globals.Theme.Light] = Color.Base.Transparent.value
        self.__map[self.MapType.Border_color][Globals.Theme.Dark] = Color.Base.Transparent.value
        self.updateBorderColor(haveAnim)


    def removeBorder(self, theme: Globals.Theme, haveAnim: bool = False):
        """_summary_: 移除指定主题边框

        Args:
            theme (Globals.Theme):  主题
            haveAnim (bool, optional): 是否播放动画. Defaults to False.
        """
        self.__map[self.MapType.Border_color][theme] = Color.Base.Transparent.value
        if theme != Globals.theme: return
        self.updateBorderColor(haveAnim)


    def setDefaultStyle(self):
        """_summary_: 恢复默认样式"""
        self.__map = copy.deepcopy(CButton.default_map)
        self.updateStyle(True)


    def getColorFromMap(self, token: MapType, theme: Globals.Theme):
        """_summary_ 从map中获取颜色

        Args:
            token (BtnColorMap.MapType): 颜色类型
            theme (Globals.Theme): 主题

        Returns:
            _type_: QColor
        """
        return self.__map[token][theme]
    # endregion


    # region 事件
    def enterEvent(self, event):
        super().enterEvent(event)
        # 鼠标进入按钮时显示自定义信息
        if Globals.ObjRef['TOOLTIP'] is not None and self.__tip_text != '':
            Globals.ObjRef['TOOLTIP'].setTip(self, self.__tip_text)
            Globals.ObjRef['TOOLTIP'].showTip()

        # 触发动画改变背景颜色
        self.__playColorAnim(self.__map[self.MapType.BG_color_hover][Globals.theme])


    def leaveEvent(self, event):
        super().leaveEvent(event)
        # 鼠标离开按钮时隐藏标签
        if Globals.ObjRef['TOOLTIP'] is not None and self.__tip_text != '':
            Globals.ObjRef['TOOLTIP'].hideTip()
        # 触发动画改变背景颜色
        self.__playColorAnim(self.__map[self.MapType.BG_color][Globals.theme])


    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        # 触发动画改变背景颜色
        self.__playColorAnim(self.__map[self.MapType.BG_color_pressed][Globals.theme])


    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        # 触发动画改变背景颜色
        self.__playColorAnim(self.__map[self.MapType.BG_color_hover][Globals.theme])

    # endregion