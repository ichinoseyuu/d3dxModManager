from enum import Enum, auto

# 主题
class Theme(Enum):
    Light = auto()
    Dark = auto()


##################################################################################################
#region 样式表
class Border(Enum):
    """边框
    Attributes:
        top (str: 'border-top'): 上边框
        bottom (str: 'border-bottom'): 下边框
        left (str: 'border-left'): 左边框
        right (str: 'border-right'): 右边框
        all (str: 'border'): 全部边框
        ishad (int: auto()): 是否有边框
        color (int: auto()): 边框颜色
        width (int: auto()): 边框宽度
        pos (int: auto()): 边框位置
        """
    top = 'border-top'
    bottom = 'border-bottom'
    left = 'border-left'
    right = 'border-right'
    all = 'border'
    ishad = auto()
    color = auto()
    width = auto()
    pos = auto()

class Radius(Enum):
    """圆角
    Attributes:
        top_left (str: 'border-top-left-radius'): 左上角
        top_right (str: 'border-top-right-radius'): 右上角
        bottom_left (str: 'border-bottom-left-radius'): 左下角
        bottom_right (str: 'border-bottom-right-radius'): 右下角
        all (str: 'border-radius'): 全部
        ishad (int: auto()): 是否有圆角
        size (int: auto()): 圆角大小
        pos (int: auto()): 圆角位置
    """
    top_left = 'border-top-left-radius'
    top_right = 'border-top-right-radius'
    bottom_left = 'border-bottom-left-radius'
    bottom_right = 'border-bottom-right-radius'
    all = 'border-radius'
    ishad = auto()
    size = auto()
    pos = auto()

class Font(Enum):
    """
    Attributes:
        color (str: 'color'): 字体颜色
        family (str: 'font-family'): 字体
        size (str: 'font-size'): 字号
        weight (str: 'font-weight'): 字体粗细
        style (str: 'font-style'): 斜体/正常
    """
    color = 'color'
    family = 'font-family'
    size = 'font-size'
    weight = 'font-weight'
    style = 'font-style'

class Background(Enum):
    """背景颜色
    Attributes:
        bg_color (str: 'background-color'): 背景颜色
        hover_bg_color (str: 'background-color'): 鼠标悬停背景颜色
        pressed_bg_color (str: 'background-color'): 鼠标按下背景颜色
    """
    bg_color = 'background-color'
    hover_bg_color = auto()
    pressed_bg_color = auto()

class Sheet(Enum):
    """样式表
    Attributes:
        background (class: Background): 背景样式
        font (class: Font): 字体样式
        radius (class: Radius): 圆角样式
        border (class: Border): 边框样式
    """
    background = Background
    font = Font
    radius = Radius
    border = Border
#endregion

##################################################################################################
#region 字体
class FontWeight(Enum):
    """字体粗细
    Attributes:
        lighter (str: 'lighter'): 细
        normal (str: 'normal'): 正常
        bold (str: 'bold'): 粗
    """
    lighter = 'lighter'
    normal = 'normal'
    bold = 'bold'

class FontFamily(Enum):
    """字体
    Attributes:
        yahei (str: 'Microsoft YaHei'): 微软雅黑
        youyuan (str: '幼圆'): 幼圆
        arial (str: 'Arial'): Arial
        simsun (str: '宋体'): 宋体
    """
    yahei = 'Microsoft YaHei'
    youyuan = '幼圆'
    arial = 'Arial'
    simsun = '宋体'

class FontSize(Enum):
    """字号
    Attributes:
        tiny (int: 8): 小号字体
        small (int: 9): 小号字体
        medium (int: 10): 中号字体
        large (int: 11): 大号字体
        huge (int: 12): 大号字体
    """
    tiny = 8
    small = 9
    medium = 10
    large = 11
    huge = 12

class FontStyle(Enum):
    """字体样式
    Attributes:
        normal (str: 'normal'): 正常字体样式。
        italic (str: 'italic'): 斜体字体样式。
    """
    normal = 'normal'
    italic = 'italic'
#endregion

##################################################################################################
#region 控件状态
class BtnState(Enum):
    """按钮状态
    Attributes:
        normal (int: auto()): 正常状态
        hover (int: auto()): 鼠标悬停状态
        pressed (int: auto()): 鼠标按下状态"""
    Normal = auto()
    Hover = auto()
    Pressed = auto()