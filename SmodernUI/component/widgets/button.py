from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import copy
from ...core.color import *
from ...core.cenum import *
from ...core.globals import *

class CButton(QPushButton):
    '''按钮控件'''
    map = {
            Theme.Light:{
                Background.bg_color: QColor(225, 225, 225),
                Background.hover_bg_color: QColor(200, 200, 200),
                Background.pressed_bg_color: QColor(180, 180, 180),
                Border.ishad: True,
                Border.color: ColorBase.transparent.value,
                Radius.ishad: True,
                Radius.size: 4,
                Font.color: QColor(60, 60, 60),
                Font.size: FontSize.small.value,
                Font.family: FontFamily.yahei.value,
                Font.weight: FontWeight.normal.value,
            },
            Theme.Dark:{
                Background.bg_color: QColor(195, 195, 195),
                Background.hover_bg_color: QColor(160, 160, 160),
                Background.pressed_bg_color: QColor(140, 140, 140),
                Border.ishad: True,
                Border.color: ColorBase.transparent.value,
                Radius.ishad: True,
                Radius.size: 4,
                Font.color: ColorBase.whtite.value,
                Font.size: FontSize.small.value,
                Font.family: FontFamily.yahei.value,
                Font.weight: FontWeight.normal.value,
            }
        }

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self._init_props()
        self._init_Anim()
        self._updateStyleSheet()

    # region 属性

    @Property(QColor)# 背景颜色
    def backgroundColor(self):
        return self._bg_color

    @backgroundColor.setter
    def backgroundColor(self, color):
        self._bg_color = color
        self._scheduleUpdateStyleSheet()


    @Property(QColor)# 边框颜色
    def borderColor(self):
        return self._border_color

    @borderColor.setter
    def borderColor(self, color):
        self._border_color = color
        self._scheduleUpdateStyleSheet()


    @Property(int) #边框圆角
    def borderRadius(self):
        return self._border_radius

    @borderRadius.setter
    def borderRadius(self, radius):
        self._border_radius = radius
        self._scheduleUpdateStyleSheet()


    @Property(QColor)# 字体颜色
    def fontColor(self):
        return self._font_color

    @fontColor.setter
    def fontColor(self, color):
        self._font_color = color
        self._scheduleUpdateStyleSheet()



    def _scheduleUpdateStyleSheet(self):
        """ 调度一次更新样式的方法，避免重复调用 """
        if self._canUpdate:
            self._canUpdate = False
            QTimer.singleShot(0, self._updateStyleSheet)


    def _updateStyleSheet(self):
        try: object_name = self.objectName()
        except Exception as e: return
        sheet_parts = []
        if object_name:
            sheet_parts.append(f'#{object_name} {{ \n')
        sheet_parts.append(f'\t background-color: {toHex(self._bg_color)};\n')
        sheet_parts.append(f'\t color: {toHex(self._font_color)};\n')
        sheet_parts.append(f'\t font-family: {self._font_family};\n')
        sheet_parts.append(f'\t font-size: {self._font_size}pt;\n')
        sheet_parts.append(f'\t font-weight: {self._font_weight};\n')
        if self.withBorder:
            sheet_parts.append(f'\t border: 1px solid {toHex(self._border_color)};\n')
        if self.isRoundedRect:
            sheet_parts.append(f'\t border-radius: {self._border_radius}px;\n')
        if object_name:
            sheet_parts.append(f'\t }}')
        self.setStyleSheet(''.join(sheet_parts))
        self._canUpdate = True
        #print(''.join(sheet_parts))

    # endregion



    # region 私有方法

    def _init_props(self):
        '''初始化属性'''
        self._map = copy.deepcopy(CButton.map)
        self._tip_text = ''
        self._state = BtnState.Normal
        self._canUpdate = True # 是否可以更新样式

        self._bg_color = self._map[Var.theme][Background.bg_color]
        self._font_color = self._map[Var.theme][Font.color]
        self.withBorder = self._map[Var.theme][Border.ishad]
        self._border_color = self._map[Var.theme][Border.color]
        self.isRoundedRect = self._map[Var.theme][Radius.ishad]
        self._border_radius = self._map[Var.theme][Radius.size]
        self._font_size = self._map[Var.theme][Font.size]
        self._font_family = self._map[Var.theme][Font.family]
        self._font_weight = self._map[Var.theme][Font.weight]



    def _init_Anim(self):
        '''初始化动画'''
        self._bg_color_anim = QPropertyAnimation(self, b"backgroundColor")
        self._bg_color_anim.setDuration(250)
        self._border_anim = QPropertyAnimation(self, b"borderColor")
        self._border_anim.setDuration(250)
        self._font_anim = QPropertyAnimation(self, b"fontColor")
        self._font_anim.setDuration(250)



    def _playBGColorAnim(self, end: QColor):
        '''播放颜色切换动画'''
        self._bg_color_anim.stop()
        self._bg_color_anim.setStartValue(self._bg_color)
        self._bg_color_anim.setEndValue(end)
        self._bg_color_anim.start()



    def _playBorderColorAnim(self, end: QColor):
        '''播放边框颜色切换动画'''
        self._border_anim.stop()
        self._border_anim.setStartValue(self._border_color)
        self._border_anim.setEndValue(end)
        self._border_anim.start()



    def _playFontColorAnim(self, end: QColor):
        '''播放边框颜色切换动画'''
        self._font_anim.stop()
        self._font_anim.setStartValue(self._font_color)
        self._font_anim.setEndValue(end)
        self._font_anim.start()

    # endregion


    # region 公共方法
    def setTipText(self, text: str):
        '''设置提示文本'''
        self._tip_text = text



    def setDurationForAnim(self, duration: int):
        """设置动画时长
        Args:
            duration (int): 时长(ms)
        """
        self._bg_color_anim.setDuration(duration)
        self._border_anim.setDuration(duration)
        self._font_anim.setDuration(duration)



    def updateStyle(self, playAnim = False):
        '''更新按钮样式'''
        self._font_size = self._map[Var.theme][Font.size]
        self._border_radius = self._map[Var.theme][Radius.size]
        self._font_family = self._map[Var.theme][Font.family]
        self._font_weight = self._map[Var.theme][Font.weight]
        if playAnim:
            self._playBGColorAnim(self._map[Var.theme][Background.bg_color])
            self._playBorderColorAnim(self._map[Var.theme][Border.color])
            self._playFontColorAnim(self._map[Var.theme][Font.color])
        else:
            self.backgroundColor = self._map[Var.theme][Background.bg_color]
            self.borderColor = self._map[Var.theme][Border.color]
            self.fontColor = self._map[Var.theme][Font.color]




    def setBGColor(self, color: QColor, theme = Theme.Light, playAnim = False):
        """设置背景颜色"""
        self._map[theme][Background.bg_color] = color
        if theme != Var.theme: return
        if playAnim:
            self._playBGColorAnim(color)
            return
        self.backgroundColor = color


    def setBGColors(self, colors: dict, playAnim = False):
        """设置背景颜色
        Args:
            sizes ({Theme: QColor, ...}): 主题对应的背景颜色
        """
        for theme, color in colors.items():
            # 设置每个主题的背景颜色
            self.setBGColor(color, theme, playAnim)



    def setBGTransparent(self, playAnim = False):
        """设置未选中时所有主题的背景为透明效果"""
        self._map[Theme.Light][Background.bg_color] = ColorBase.transparent.value
        self._map[Theme.Dark][Background.bg_color] = ColorBase.transparent.value
        if playAnim:
            self._playBGColorAnim(ColorBase.transparent.value)
            return
        self.backgroundColor = ColorBase.transparent.value



    def setHoverBGColor(self, color: QColor, theme = Theme.Light, playAnim = False):
        """设置悬停时背景颜色"""
        self._map[theme][Background.hover_bg_color] = color
        if theme != Var.theme: return
        if self._state == BtnState.Hover and playAnim:
            self._playBGColorAnim(color)



    def setHoverBGColors(self, colors: dict, playAnim = False):
        """设置悬停时背景颜色
        Args:
            colors ({Theme: QColor, ...}): 主题对应的背景颜色
            """
        for theme, color in colors.items():
            # 设置每个主题的背景颜色
            self.setHoverBGColor(color, theme, playAnim)


    def setPressBGColor(self, color: QColor, theme = Theme.Light, playAnim = False):
        """设置按下时背景颜色"""
        self._map[theme][Background.pressed_bg_color] = color
        if theme != Var.theme: return
        if self._state == BtnState.Pressed and playAnim:
            self._playBGColorAnim(color)



    def setPressBGColors(self, colors: dict, playAnim = False):
        """设置按下时背景颜色
        Args:
            colors ({Theme: QColor, ...}): 主题对应的背景颜色
            """
        for theme, color in colors.items():
            # 设置每个主题的背景颜色
            self.setPressBGColor(color, theme, playAnim)



    def haveBorder(self, states: dict):
        """设置是否有边框
        Args:
            states ({Theme: bool, ...}): 不同主题对应的边框状态
        """
        for theme, state in states.items():
            self._map[theme][Border.ishad] = state
        self.withBorder = self._map[Var.theme][Border.ishad]
        self._scheduleUpdateStyleSheet()



    def setBorderColor(self, color: QColor, theme = Theme.Light, playAnim = False):
        """设置边框颜色"""
        self._map[theme][Border.color] = color
        if theme != Var.theme: return
        if playAnim:
            self._playBorderColorAnim(color)
            return
        self.borderColor = color



    def setBorderColors(self, colors: dict, playAnim=False):
        """设置边框颜色
        Args:
            colors ({Theme: QColor, ...}): 主题对应的颜色
        """
        for theme, color in colors.items():
            # 设置每个主题的背景颜色
            self.setBorderColor(color, theme, playAnim)



    def setFontColor(self, color: QColor, theme = Theme.Light, playAnim = False):
        """设置字体颜色"""
        self._map[theme][Font.color] = color
        if theme != Var.theme: return
        if playAnim:
            self._playFontColorAnim(color)
            return
        self.fontColor = color



    def setFontColors(self, colors: dict, playAnim = False):
        """设置字体颜色
        Args:
            colors ({Theme: QColor, ...}): 主题对应的字体颜色
        """
        for theme, color in colors.items():
            # 设置每个主题的背景颜色
            self.setBorderColor(color, theme, playAnim)



    def haveRadius(self, states: dict):
        """设置是否有圆角
        Args:
            states ({Theme: bool, ...}): 不同主题对应的圆角状态
        """
        for theme, state in states.items():
            self._map[theme][Radius.ishad] = state
        self.withBorder = self._map[Var.theme][Radius.ishad]
        self._scheduleUpdateStyleSheet()



    def setRadiusSize(self, size: int, theme = Theme.Light):
        """设置圆角大小"""
        self._map[theme][Radius.size] = size
        if theme != Var.theme: return
        self.borderRadius = size



    def setRadiusSizes(self, sizes: dict):
        """设置圆角大小
        Args:
            sizes ({Theme: int, ...}): 主题对应的圆角大小
        """
        for theme, size in sizes.items():
            # 设置每个主题的背景颜色
            self.setRadiusSize(size, theme)



    def setFontSize(self, size: FontSize, theme = Theme.Light):
        """设置字体大小"""
        self._map[theme][Font.size] = size.value
        if theme != Var.theme: return
        self.fontSize = size.value



    def setFontSizes(self, sizes: dict):
        """设置字体大小
        Args:
            sizes ({Theme: FontSize, ...}): 主题对应的字体大小
        """
        for theme, size in sizes.items():
            # 设置每个主题的背景颜色
            self.setFontSize(size, theme)



    def setFontFamily(self, family: FontFamily, theme = Theme.Light):
        """设置字体"""
        self._map[theme][Font.family] = family.value
        if theme != Var.theme: return
        self.fontFamily = family.value



    def setFontFamilys(self, families: dict):
        """设置字体
        Args:
            families ({Theme: FontFamily, ...}): 主题对应的字体
        """
        for theme, family in families.items():
            # 设置每个主题的背景颜色
            self.setFontSize(family, theme)



    def setFontWeight(self, weight: FontWeight, theme = Theme.Light):
        """设置字体粗细"""
        self._map[theme][Font.weight] = weight.value
        if theme != Var.theme: return
        self.fontWeight = weight.value



    def setFontWeights(self, weights: dict):
        """设置字体粗细
        Args:
            weights ({Theme: FontWeight, ...}): 主题对应的字体粗细
        """
        for theme, weight in weights.items():
            # 设置每个主题的背景颜色
            self.setFontSize(weight, theme)



    def setDefaultStyle(self, playAnim = False):
        """恢复默认样式"""
        self._map = copy.deepcopy(CButton.map)
        self.updateStyle(playAnim)

    # endregion


    # region 事件
    def enterEvent(self, event:QMouseEvent):
        self._state = BtnState.Hover
        self._playBGColorAnim(self._map[Var.theme][Background.hover_bg_color])

        if Var.objref['tooltip'] is not None and self._tip_text != '':
            Var.objref['tooltip'].setTip(self, self._tip_text)
            Var.objref['tooltip'].showTip()


    def leaveEvent(self, event:QMouseEvent):
        self._state = BtnState.Normal
        self._playBGColorAnim(self._map[Var.theme][Background.bg_color])

        if Var.objref['tooltip'] is not None and self._tip_text != '':
            Var.objref['tooltip'].hideTip()



    def mousePressEvent(self, event:QMouseEvent):
        self._state = BtnState.Pressed
        self._playBGColorAnim(self._map[Var.theme][Background.pressed_bg_color])



    def mouseReleaseEvent(self, event:QMouseEvent):
        #判断按下按钮鼠标还在不在按钮内
        if self.rect().contains(event.pos()):
            self.clicked.emit()#触发点击事件
            if self.isCheckable():#判断是否为可选中按钮
                self.setChecked(not self.isChecked())#切换选中状态
        mouse_pos = QCursor.pos()#获取鼠标当前位置
        
        # 判断鼠标是否在按钮区域内，必须用mapFromGlobal转换坐标，上面那种有bug
        if self.rect().contains(self.mapFromGlobal(mouse_pos)):
            # 如果鼠标在按钮内，保持 hover 状态
            self._state = BtnState.Hover
            self._playBGColorAnim(self._map[Var.theme][Background.hover_bg_color])
        else:
            # 如果鼠标不在按钮内，恢复 normal 状态
            self._state = BtnState.Normal
            self._playBGColorAnim(self._map[Var.theme][Background.bg_color])



    def mouseMoveEvent(self, event: QMouseEvent):
        pass
        # # 获取鼠标的当前位置
        # mouse_pos = event.position()
        # print(mouse_pos.toPoint())

    # endregion