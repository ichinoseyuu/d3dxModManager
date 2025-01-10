from PySide6.QtGui import QColor
from .color import CColor
from .theme import Theme
from .widget_props import CWidgetProps
from .font import CFont


class ColorMap:
    '''颜色索引图'''
    _instances = {}
    def __new__(cls, type:CWidgetProps):
        if type not in cls._instances:
            cls._instances[type] = super().__new__(cls)
            cls._instances[type]._initialize(type)
        return cls._instances[type]

    def _initialize(self, type:CWidgetProps):
        # 初始化映射逻辑
        if type == CWidgetProps.Btn:
            self.map = {
                Theme.Light:{
                    CWidgetProps.Btn.bg: QColor(235, 235, 235),
                    CWidgetProps.Btn.bg_hover: QColor(220, 220, 220),
                    CWidgetProps.Btn.bg_pressed: QColor(211, 211, 211),
                    CWidgetProps.Btn.border: CColor.Base.transparent.value,
                    CWidgetProps.Btn.font_color: QColor(60, 60, 60),
                    CWidgetProps.Btn.border_radius: 4,
                    CWidgetProps.Btn.font_size: CFont.Size.small.value,
                    CWidgetProps.Btn.font_family: CFont.Family.yahei.value,
                    CWidgetProps.Btn.font_weight: CFont.Weight.normal.value,
                },
                Theme.Dark:{
                    CWidgetProps.Btn.bg: QColor(211, 211, 211),
                    CWidgetProps.Btn.bg_hover: QColor(220, 220, 220),
                    CWidgetProps.Btn.bg_pressed: QColor(235, 235, 235),
                    CWidgetProps.Btn.border: CColor.Base.transparent.value,
                    CWidgetProps.Btn.font_color: CColor.Base.whtite.value,
                    CWidgetProps.Btn.border_radius: 4,
                    CWidgetProps.Btn.font_size: CFont.Size.small.value,
                    CWidgetProps.Btn.font_family: CFont.Family.yahei.value,
                    CWidgetProps.Btn.font_weight: CFont.Weight.normal.value,
                }
            }
        if type == CWidgetProps.Container:
            self.map = {
                CWidgetProps.Theme.light:{
                    CWidgetProps.Container.bg: CColor.Presets.window_bg_light.value,
                    CWidgetProps.Container.border_L: CColor.Presets.border_light.value,
                    CWidgetProps.Container.border_R: CColor.Presets.border_light.value,
                    CWidgetProps.Container.border_T: CColor.Presets.border_light.value,
                    CWidgetProps.Container.border_B: CColor.Presets.border_light.value,
                    CWidgetProps.Container.radius_T_L: 0,
                    CWidgetProps.Container.radius_T_R: 0,
                    CWidgetProps.Container.radius_B_L: 0,
                    CWidgetProps.Container.radius_B_R: 0,
                },
                CWidgetProps.Theme.dark:{
                    CWidgetProps.Container.bg: QColor(60, 60, 60),
                    CWidgetProps.Container.border_L: CColor.Base.transparent.value,
                    CWidgetProps.Container.border_R: CColor.Base.transparent.value,
                    CWidgetProps.Container.border_T: CColor.Base.transparent.value,
                    CWidgetProps.Container.border_B: CColor.Base.transparent.name,
                    CWidgetProps.Container.radius_T_L: 0,
                    CWidgetProps.Container.radius_T_R: 0,
                    CWidgetProps.Container.radius_B_L: 0,
                    CWidgetProps.Container.radius_B_R: 0,
                }
            }
    @classmethod
    def get_all_instances(cls):
        return cls._instances
# # 第一次创建时初始化映射，之后直接返回现有实例
# map = ColorMap(CType.Btn).map
# for key, values in map.items():
#     print(key)
#     for k, v in values.items():
#         print(k,v)
# print(ColorMap.get_all_instances())
