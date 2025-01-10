from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import copy
from ...core import Globals, Theme, ColorMap, CFont, CWidgetProps, CColor

class CButton(QPushButton):
    '''按钮控件'''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__map = copy.deepcopy(ColorMap(CWidgetProps.Btn).map)
        self.__tip_text = ''
        self.__init_style()
        self.__init_Anim()
        self.__updateStyleSheet()

    # region 属性

    @Property(QColor)# 背景颜色
    def backgroundColor(self):
        return self.__bg_color

    @backgroundColor.setter
    def backgroundColor(self, color):
        self.__bg_color = color
        self.__updateStyleSheet()


    @Property(QColor)# 边框颜色
    def borderColor(self):
        return self.__border_color

    @borderColor.setter
    def borderColor(self, color):
        self.__border_color = color
        self.__updateStyleSheet()


    @Property(int) #边框圆角
    def borderRadius(self):
        return self.__border_radius

    @borderRadius.setter
    def borderRadius(self, radius):
        self.__border_radius = radius
        self.__updateStyleSheet()


    @Property(QColor)# 字体颜色
    def fontColor(self):
        return self.__font_color

    @fontColor.setter
    def fontColor(self, color):
        self.__font_color = color
        self.__updateStyleSheet()


    @Property(int)# 字体大小
    def fontSize(self):
        return self.__font_size

    @fontSize.setter
    def fontSize(self, size):
        self.__font_size = size
        self.__updateStyleSheet()


    @Property(str)# 字体
    def fontFamily(self):
        return self.__font_family

    @fontFamily.setter
    def fontFamily(self, family):
        self.__font_family = family
        self.__updateStyleSheet()


    @Property(str)# 字体粗细
    def fontWeight(self):
        return self.__font_weight

    @fontWeight.setter
    def fontWeight(self, weight):
        self.__font_weight = weight
        self.__updateStyleSheet()

    def __updateStyleSheet(self):
        style = f'''
        background-color: {CColor.toHex(self.__bg_color)};
        border: 1px solid {CColor.toHex(self.__border_color)};
        border-radius: {self.__border_radius}px;
        color: {CColor.toHex(self.__font_color)};
        font-family: {self.__font_family};
        font-size: {self.__font_size}pt;
        font-weight: {self.__font_weight};
        '''
        self.setStyleSheet(style)

    # endregion



    # region 私有方法

    def __init_style(self):
        '''初始化颜色'''
        self.__bg_color = self.__map[Globals.theme][CWidgetProps.Btn.bg]
        self.__font_color = self.__map[Globals.theme][CWidgetProps.Btn.font_color]
        self.__border_color = self.__map[Globals.theme][CWidgetProps.Btn.border]
        self.__border_radius = self.__map[Globals.theme][CWidgetProps.Btn.border_radius]
        self.__font_size = self.__map[Globals.theme][CWidgetProps.Btn.font_size]
        self.__font_family = self.__map[Globals.theme][CWidgetProps.Btn.font_family]
        self.__font_weight = self.__map[Globals.theme][CWidgetProps.Btn.font_weight]


    def __init_Anim(self):
        '''初始化动画'''
        self.__bg_color_anim = QPropertyAnimation(self, b"backgroundColor")
        self.__bg_color_anim.setDuration(250)
        self.__border_anim = QPropertyAnimation(self, b"borderColor")
        self.__border_anim.setDuration(250)
        self.__font_anim = QPropertyAnimation(self, b"fontColor")
        self.__font_anim.setDuration(250)
        self.__font_size_anim = QPropertyAnimation(self, b"fontSize")
        self.__font_size_anim.setDuration(250)
        self.__border_radius_anim = QPropertyAnimation(self, b"borderRadius")
        self.__border_radius_anim.setDuration(250)


    def __playBGColorAnim(self, end: QColor):
        '''播放颜色切换动画'''
        self.__bg_color_anim.stop()
        self.__bg_color_anim.setStartValue(self.__bg_color)
        self.__bg_color_anim.setEndValue(end)
        self.__bg_color_anim.start()


    def __playBorderColorAnim(self, end: QColor):
        '''播放边框颜色切换动画'''
        self.__border_anim.stop()
        self.__border_anim.setStartValue(self.__border_color)
        self.__border_anim.setEndValue(end)
        self.__border_anim.start()

    def __playFontColorAnim(self, end: QColor):
        '''播放边框颜色切换动画'''
        self.__font_anim.stop()
        self.__font_anim.setStartValue(self.__font_color)
        self.__font_anim.setEndValue(end)
        self.__font_anim.start()

    def __playFontSizeAnim(self, end: QColor):
        '''播放字体大小切换动画'''
        self.__font_size_anim.stop()
        self.__font_size_anim.setStartValue(self.__font_size)
        self.__font_size_anim.setEndValue(end)
        self.__font_size_anim.start()

    def __playBorderRadiusAnim(self, end: QColor):
        '''播放边框圆角切换动画'''
        self.__border_radius_anim.stop()
        self.__border_radius_anim.setStartValue(self.__border_radius)
        self.__border_radius_anim.setEndValue(end)
        self.__border_radius_anim.start()
    # endregion


    # region 公共方法
    def setTipText(self, text: str):
        '''设置提示文本'''
        self.__tip_text = text

    def setDurationForAnim(self, duration: int):
        """_summary_: 设置动画时长

        Args:
            duration (int): 时长(ms)
        """
        self.__bg_color_anim.setDuration(duration)
        self.__border_anim.setDuration(duration)
        self.__font_anim.setDuration(duration)
        self.__font_size_anim.setDuration(duration)
        self.__border_radius_anim.setDuration(duration)


    def updateStyle(self, playAnim = False):
        '''更新按钮样式'''
        if playAnim:
            self.__playBGColorAnim(self.__map[Globals.theme][CWidgetProps.Btn.bg])
            self.__playBorderColorAnim(self.__map[Globals.theme][CWidgetProps.Btn.border])
            self.__playFontColorAnim(self.__map[Globals.theme][CWidgetProps.Btn.font_color])
            self.__playFontSizeAnim(self.__map[Globals.theme][CWidgetProps.Btn.font_size])
            self.__playBorderRadiusAnim(self.__map[Globals.theme][CWidgetProps.Btn.border_radius])
            self.fontFamily = self.__map[Globals.theme][CWidgetProps.Btn.font_family]
            self.fontWeight = self.__map[Globals.theme][CWidgetProps.Btn.font_weight]
            return
        self.backgroundColor = self.__map[Globals.theme][CWidgetProps.Btn.bg]
        self.borderColor = self.__map[Globals.theme][CWidgetProps.Btn.border]
        self.fontColor = self.__map[Globals.theme][CWidgetProps.Btn.font_color]
        self.fontSize = self.__map[Globals.theme][CWidgetProps.Btn.font_size]
        self.fontFamily = self.__map[Globals.theme][CWidgetProps.Btn.font_family]
        self.fontWeight = self.__map[Globals.theme][CWidgetProps.Btn.font_weight]
        self.borderRadius = self.__map[Globals.theme][CWidgetProps.Btn.border_radius]


    def setBGColor(self,theme: Theme, color: QColor, playAnim = False):
        """_summary_: 更改背景颜色及Map

        Args:
            theme (CWidgetProps.Theme):  主题
            color (QColor): 颜色
            playAnim (bool, optional): 是否播放动画. Defaults to False.
        """
        self.__map[theme][CWidgetProps.Btn.bg] = color
        if theme != Globals.theme: return
        if playAnim:
            self.__playBGColorAnim(self.__map[Globals.theme][CWidgetProps.Btn.bg])
            return
        self.backgroundColor = self.__map[Globals.theme][CWidgetProps.Btn.bg]


    def setBorderColor(self, theme: Theme, color: QColor, playAnim = False):
        """_summary_: 更改边框颜色及Map

        Args:
            theme (CWidgetProps.Theme):  主题
            color (QColor): 颜色
            playAnim (bool, optional): 是否播放动画. Defaults to False.
        """
        self.__map[theme][CWidgetProps.Btn.border] = color
        if theme != Globals.theme: return
        if playAnim:
            self.__playBorderColorAnim(self.__map[Globals.theme][CWidgetProps.Btn.border])
            return
        self.borderColor = self.__map[Globals.theme][CWidgetProps.Btn.border]


    def setFontColor(self, theme: Theme, color: QColor, playAnim = False):
        """_summary_: 更改字体颜色及Map

        Args:
            theme (CWidgetProps.Theme):  主题
            color (QColor): 颜色
            playAnim (bool, optional): 是否播放动画. Defaults to False.
        """
        self.__map[theme][CWidgetProps.Btn.font_color] = color
        if theme != Globals.theme: return
        if playAnim:
            self.__playFontColorAnim(self.__map[Globals.theme][CWidgetProps.Btn.font_color])
            return
        self.fontColor = self.__map[Globals.theme][CWidgetProps.Btn.font_color]


    def setBGTransparentAllTheme(self, playAnim = False):
        """_summary_: 设置该控件所有主题透明

        Args:
            playAnim (bool, optional): 是否播放动画. Defaults to False.
        """
        self.__map[Theme.Light][CWidgetProps.Btn.bg] = CColor.Base.transparent.value
        self.__map[Theme.Dark][CWidgetProps.Btn.bg] = CColor.Base.transparent.value
        if playAnim:
            self.__playBGColorAnim(self.__map[Globals.theme][CWidgetProps.Btn.bg])
            return
        self.backgroundColor = self.__map[Globals.theme][CWidgetProps.Btn.bg]


    def setBGTransparent(self, theme: Theme, playAnim = False):
        """_summary_: 设置该控件指定主题透明

        Args:
            theme (CWidgetProps.Theme):  主题
            playAnim (bool, optional): 是否播放动画. Defaults to False.
        """
        self.__map[theme][CWidgetProps.Btn.bg] = CColor.Base.transparent.value
        if theme != Globals.theme: return
        if playAnim:
            self.__playBGColorAnim(self.__map[Globals.theme][CWidgetProps.Btn.bg])
            return
        self.backgroundColor = self.__map[Globals.theme][CWidgetProps.Btn.bg]


    def removeBorderAllTheme(self, playAnim = False):
        """_summary_: 移除所有主题边框

        Args:
            playAnim (bool, optional): 是否播放动画. Defaults to False.
        """
        self.__map[Theme.Light][CWidgetProps.Btn.border] = CColor.Base.transparent.value
        self.__map[Theme.Dark][CWidgetProps.Btn.border] = CColor.Base.transparent.value
        if playAnim:
            self.__playBorderColorAnim(self.__map[Globals.theme][CWidgetProps.Btn.border])
            return
        self.borderColor = self.__map[Globals.theme][CWidgetProps.Btn.border]


    def removeBorder(self, theme: Theme, playAnim = False):
        """_summary_: 移除指定主题边框

        Args:
            theme (CWidgetProps.Theme): 主题
            playAnim (bool, optional): 是否播放动画. Defaults to False.
        """
        self.__map[theme][CWidgetProps.Btn.border] = CColor.Base.transparent.value
        if theme != Globals.theme: return
        if playAnim:
            self.__playBorderColorAnim(self.__map[Globals.theme][CWidgetProps.Btn.border])
            return
        self.borderColor = self.__map[Globals.theme][CWidgetProps.Btn.border]


    def setDefaultStyle(self, playAnim = False):
        """_summary_: 恢复默认样式"""
        self.__map = copy.deepcopy(ColorMap(CWidgetProps.Btn).map)
        self.updateStyle(playAnim)


    def getColorFromMap(self,theme: Theme, token: CWidgetProps.Btn,):
        """_summary_ 从map中获取颜色

        Args:
            theme (CWidgetProps.Theme): 主题
            token (CWidgetProps.Btn): 颜色类型

        Returns:
            _type_: QColor
        """
        return self.__map[theme][token]


    def setFontSize(self, theme: Theme, size: int, playAnim = False):
        """_summary_: 设置字体大小

        Args:
            theme (CWidgetProps.Theme):  主题
            size (int): 字体大小
            playAnim (bool, optional): 是否播放动画. Defaults to False.
        """
        self.__map[theme][CWidgetProps.Btn.font_size] = size
        if theme != Globals.theme: return
        if playAnim:
            self.__playFontSizeAnim(size)
            return
        self.fontSize = size


    def setBorderRadius(self, theme: Theme, radius: int, playAnim = False):
        """_summary_: 设置边框圆角

        Args:
            theme (CWidgetProps.Theme): 主题
            radius (int): 圆角大小
            playAnim (bool, optional): 是否播放动画. Defaults to False.
        """
        self.__map[theme][CWidgetProps.Btn.border_radius] = radius
        if theme != Globals.theme: return
        if playAnim:
            self.__playBorderRadiusAnim(radius)
            return
        self.borderRadius = radius


    def setFontFamily(self, theme: Theme, family: str):
        """_summary_: 设置字体

        Args:
            family (str): 字体
        """
        self.__map[theme][CWidgetProps.Btn.font_family] = family
        if theme != Globals.theme: return
        self.fontFamily = family


    def setFontWeight(self, theme: Theme, weight: str):
        """_summary_: 设置字体粗细

        Args:
            weight (int): 粗细
        """
        self.__map[theme][CWidgetProps.Btn.font_weight] = weight
        if theme != Globals.theme: return
        self.fontWeight = weight

    # endregion


    # region 事件
    def enterEvent(self, event:QMouseEvent):
        # 鼠标进入按钮时显示自定义信息
        if Globals.ObjRef['TOOLTIP'] is not None and self.__tip_text != '':
            Globals.ObjRef['TOOLTIP'].setTip(self, self.__tip_text)
            Globals.ObjRef['TOOLTIP'].showTip()

        # 触发动画改变背景颜色
        self.__playBGColorAnim(self.__map[Globals.theme][CWidgetProps.Btn.bg_hover])


    def leaveEvent(self, event:QMouseEvent):
        # 鼠标离开按钮时隐藏标签
        if Globals.ObjRef['TOOLTIP'] is not None and self.__tip_text != '':
            Globals.ObjRef['TOOLTIP'].hideTip()
        # 触发动画改变背景颜色
        self.__playBGColorAnim(self.__map[Globals.theme][CWidgetProps.Btn.bg])


    def mousePressEvent(self, event:QMouseEvent):
        # 触发动画改变背景颜色
        self.__playBGColorAnim(self.__map[Globals.theme][CWidgetProps.Btn.bg_pressed])


    def mouseReleaseEvent(self, event:QMouseEvent):
        if self.rect().contains(event.pos()):
            self.clicked.emit()
        mouse_pos = QCursor.pos()#获取鼠标当前位置
        # 判断鼠标是否在按钮区域内
        if self.rect().contains(self.mapFromGlobal(mouse_pos)):
            # 如果鼠标在按钮内，保持 hover 状态
            self.__playBGColorAnim(self.__map[Globals.theme][CWidgetProps.Btn.bg_hover])
        else:
            self.__playBGColorAnim(self.__map[Globals.theme][CWidgetProps.Btn.bg])

    def mouseMoveEvent(self, event: QMouseEvent):
        pass
        # # 获取鼠标的当前位置
        # mouse_pos = event.position()
        # print(mouse_pos.toPoint())

    # endregion