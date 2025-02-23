from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import copy
from ...core.cenum import *
from ...core.color import *
from ...core.globals import *

class CContainer(QWidget):
    count = 0
    map = {
            Theme.Light:{
                Background.bg_color: ColorPresets.window_bg_light.value,
                Border.color: ColorBase.transparent.value,
                Border.ishad: False,
                Border.pos: [],
                Border.width: 1,
                Radius.ishad: False,
                Radius.pos: [],
                Radius.size: 5
            },
            Theme.Dark:{
                Background.bg_color: ColorPresets.window_bg_dark.value,
                Border.color: ColorBase.transparent.value,
                Border.ishad: False,
                Border.pos: [],
                Border.width: 1,
                Radius.ishad: False,
                Radius.pos: [],
                Radius.size: 5
            }
        }

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self._init_props()
        self._init_anim()
        self._updateStyleSheet()
        self.style().polish(self) # 初始化样式表,避免产生默认样式的重影
        self.updateStyle()


    @Property(QColor)
    def backgroundColor(self):
        return self._bg_color

    @backgroundColor.setter
    def backgroundColor(self, color):
        self._bg_color = color
        self._scheduleUpdateStyleSheet()


    @Property(QColor)
    def borderColor(self):
        return self._border_color

    @borderColor.setter
    def borderColor(self, color):
        self._border_color = color
        self._scheduleUpdateStyleSheet()


    @Property(int)
    def borderRadius(self):
        return self._border_radius

    @borderRadius.setter
    def borderRadius(self, radius):
        self._border_radius = radius
        self._scheduleUpdateStyleSheet()


    def _scheduleUpdateStyleSheet(self):
        """ 调度一次更新样式的方法，避免重复调用 """
        if self._canUpdate:
            self._canUpdate = False
            QTimer.singleShot(0, self._updateStyleSheet)


    def _updateStyleSheet(self):
        object_name = self.objectName()
        sheet_parts = []
        if object_name:
            sheet_parts.append(f"#{object_name} {{\n")
        # 设置背景颜色
        sheet_parts.append(f'\t background-color: {toHex(self._bg_color)};\n')
        # 设置边框
        if not self.withBorder or not self._border_pos:
            sheet_parts.append(f'\t border: none;\n')
        else:
            for pos in self._border_pos:
                sheet_parts.append(f'\t {pos}: {self._border_width}px solid {toHex(self._border_color)};\n')
        # 设置边框圆角
        if self.isRoundedRect and self._radius_pos:
            for pos in self._radius_pos:
                sheet_parts.append(f'\t {pos}: {self._border_radius}px;\n')
        # 如果有对象名，关闭选择器
        if object_name:
            sheet_parts.append(f'\t }}')
        # 更新样式表
        self.setStyleSheet(''.join(sheet_parts))
        # 更新样式表后，重置flag，允许再次更新
        self._canUpdate = True
        #print(''.join(sheet_parts))
    # endregion




    # region 内部方法
    def _init_props(self):
        '''初始化属性'''
        self._map = copy.deepcopy(CContainer.map)
        self._canUpdate = True  # styleSheet是否已经可以更新，避免同一帧多次更新样式表

        self._bg_color = self._map[Var.theme][Background.bg_color]
        self._border_color = self._map[Var.theme][Border.color]
        self.withBorder = self._map[Var.theme][Border.ishad]
        self._border_pos = self._map[Var.theme][Border.pos]
        self._border_width = self._map[Var.theme][Border.width]
        self.isRoundedRect = self._map[Var.theme][Radius.ishad]
        self._radius_pos = self._map[Var.theme][Radius.pos]
        self._border_radius = self._map[Var.theme][Radius.size]



    def _init_anim(self):
        '''初始化动画'''
        self._bg_color_anim = QPropertyAnimation(self, b'backgroundColor')
        self._bg_color_anim.setDuration(250)
        self._border_anim = QPropertyAnimation(self, b'borderColor')
        self._border_anim.setDuration(250)



    def _playBGColorAnim(self, end: QColor):
        '''播放颜色切换动画'''
        self._bg_color_anim.stop()
        self._bg_color_anim.setStartValue(self._bg_color)
        self._bg_color_anim.setEndValue(end)
        self._bg_color_anim.start()


    def _playBorderAnim(self, end: QColor):
        '''播放左边框颜色切换动画'''
        self._border_anim.stop()
        self._border_anim.setStartValue(self._border_color)
        self._border_anim.setEndValue(end)
        self._border_anim.start()


    # endregion



    # region 外部方法

    def setDurationForAnim(self, duration: int):
        """设置动画时长
        Args:
            duration (int): 时长(ms)
        """
        self._bg_color_anim.setDuration(duration)
        self._border_anim.setDuration(duration)



    def updateStyle(self, playAnim = False):
        """更新样式"""
        self.withBorder = self._map[Var.theme][Border.ishad]
        self.isRoundedRect = self._map[Var.theme][Radius.ishad]
        self._border_radius = self._map[Var.theme][Radius.size]
        if playAnim:
            self._playBGColorAnim(self._map[Var.theme][Background.bg_color])
            self._playBorderAnim(self._map[Var.theme][Border.color])
        else:
            self.backgroundColor = self._map[Var.theme][Background.bg_color]
            self.borderColor = self._map[Var.theme][Border.color]



    def setBorderWidth(self, width: int = 1, theme = Theme.Light):
        """设置边框宽度"""
        self._map[theme][Border.width] = width
        if theme != Var.theme: return
        self._border_weight = width
        self._updateStyleSheet()



    def setBorderWidthes(self, widthes: dict):
        """设置边框宽度
        Args:
            sizes ({Theme: int, ...}): 主题对应的边框宽度
        """
        for theme, width in widthes.items():
            # 设置每个主题的背景颜色
            self.setRadiusSize(width, theme)



    def setBorder(self, edges: tuple = (0, 0, 0, 0), width: int = 1, theme = Theme.Light):
        """设置边框显示的位置
        Args:
            edges (top, bottom, right, left): 0 -> false; >=1 -> true.
        """
        border_positions = (Border.top.value, Border.bottom.value, Border.left.value, Border.right.value)
        self._map[theme][Border.width] = width
        self._border_pos.clear()
        self.withBorder = any(edges)
        self._map[theme][Border.ishad] = self.withBorder
        if all(edges):
            self._border_pos.append(Border.all.value)
        else:
            for i, e in enumerate(edges):
                if e: self._border_pos.append(border_positions[i])
        self._map[theme][Border.pos] = self._border_pos
        self._updateStyleSheet()




    def setRadiusSize(self, radius: int = 5, theme = Theme.Light):
        """设置圆角大小"""
        self._map[theme][Radius.size] = radius
        if theme != Var.theme: return
        self._border_weight = radius
        self._updateStyleSheet()



    def setRadiusSizes(self, sizes: dict):
        """设置圆角大小
        Args:
            sizes ({Theme: int, ...}): 主题对应的圆角大小
        """
        for theme, size in sizes.items():
            # 设置每个主题的背景颜色
            self.setRadiusSize(size, theme)



    def setRadius(self, coners: tuple = (0, 0, 0, 0), radius: int = 5, theme = Theme.Light):
        """设置圆角显示的位置
        Args:
            coners(top-left, top-right, bottom-left, bottom-right): 0 -> false; >=1 -> true..
        """
        border_positions = (Radius.top_left.value, Radius.top_right.value, Radius.bottom_left.value, Radius.bottom_right.value)
        self._map[theme][Radius.size] = radius
        self._radius_pos.clear()
        self.isRoundedRect = any(coners)
        self._map[theme][Radius.ishad] = self.isRoundedRect
        if all(coners):
            self._radius_pos.append(Radius.all.value)
        else:
            for i, c in enumerate(coners):
                if c: self._radius_pos.append(border_positions[i])
        self._map[theme][Radius.pos] = self._radius_pos
        self._updateStyleSheet()



    def setBGColor(self, color: QColor, theme = Theme.Light, playAnim = False):
        """设置背景颜色"""
        self._map[theme][Background.bg_color] = color
        if theme != Var.theme: return
        if playAnim:
            self._playBGColorAnim(color)
            return
        self.backgroundColor = color


    def setBGColors(self, colors: dict, playAnim=False):
        """设置背景颜色
        Args:
            colors ({Theme: QColor, ...}): 主题对应的颜色
        """
        for theme, color in colors.items():
            # 设置每个主题的背景颜色
            self.setBGColor(color, theme, playAnim)



    def setBorderColor(self, color: QColor, theme = Theme.Light, playAnim = False):
        """设置边框颜色"""
        self._map[theme][Border.color] = color
        if theme != Var.theme: return
        if playAnim:
            self._playBorderAnim(color)
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

    # endregion



    # region 事件
    def mouseMoveEvent(self, event):
        return super().mouseMoveEvent(event)


    def mousePressEvent(self, event):
        return super().mousePressEvent(event)


    def mouseReleaseEvent(self, event):
        return super().mouseReleaseEvent(event)


    def paintEvent(self, event):
        super().paintEvent(event)
        option = QStyleOption()
        option.initFrom(self)
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)
        # painter.setCompositionMode(QPainter.CompositionMode_Clear)  # 设置为完全透明
        # # 使用当前控件样式绘制控件的基础元素
        # self.style().drawPrimitive(self.style().PrimitiveElement.PE_Widget, option, painter, self)
        # 绘制背景，完全透明
        # painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
        # painter.fillRect(self.rect(), QColor(0, 0, 0, 0))  # 背景透明

        # # 绘制前景内容（例如，窗口内容）
        # painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
        # painter.setPen(Qt.black)  # 设置前景颜色为白色
        # painter.drawText(50, 50, "This is the foreground content!")
        # 不设置笔刷颜色，绘制仅有边框的圆角矩形
        # painter.drawRoundedRect(10, 10, self.width() - 20, self.height() - 20, 15, 15)
        painter.end()



    # endregion