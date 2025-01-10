from enum import Enum, auto, unique
class CWidgetProps:
    '''各种控件的相关属性'''
    @unique
    class Btn(Enum):
        """summary: 按钮相关属性

        Consts:
            Enum (auto): bg, bg_hover, bg_pressed, border, border_radius, font_family, font_size, font_color, font_weight
        """
        bg = auto()                 # Background color
        bg_hover = auto()           # Background color on hover
        bg_pressed = auto()         # Background color when pressed
        border = auto()             # Border style
        border_radius = auto()      # Border radius
        font_family = auto()        # Font family
        font_size = auto()          # Font size
        font_color = auto()         # Font color
        font_weight = auto()        # Font weight

    @unique
    class Container(Enum):
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

    @unique
    class Label(Enum):
        """_summary_: 标签相关属性

        Consts:
            Enum (auto): bg, border, border_radius, font_family, font_size, font_color
        """
        bg = auto()                 # Background color
        border = auto()             # Border style
        border_radius = auto()      # Border radius
        font_family = auto()        # Font family
        font_size = auto()          # Font size
        font_color = auto()         # Font color

    @classmethod
    def get_all_btn_values(cls):
        '''获取所有按钮类型的值'''
        return [item.name for item in cls.Btn]

    @classmethod
    def get_all_container_values(cls):
        '''获取所有容器类型的值'''
        return [item.name for item in cls.Container]

    @classmethod
    def get_all_label_values(cls):
        '''获取所有标签类型的值'''
        return [item.name for item in cls.Label]


# Example usage
# btn_values = CType.get_all_btn_values()
# print(btn_values)
