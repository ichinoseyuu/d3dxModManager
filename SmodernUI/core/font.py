from enum import Enum
class CFont:
    """summary: 字体类

    Class:
        Weight (Enum): 粗细
        Family (Enum): 字体
        Size (Enum): 字号
        Style (Enum): 样式
    """
    class Weight(Enum):
        """summary: 粗细

        Consts:
            Enum (str): lighter = 'lighter' 细
            Enum (str): normal = 'normal' 正常
            Enum (str): bold = 'bold' 粗
        """
        lighter = 'lighter'
        normal = 'normal'
        bold = 'bold'

    class Family(Enum):
        """summary: 字体

        Consts:
            Enum (str): yahei = 'Microsoft YaHei'
            Enum (str): youyuan = '幼圆'
            Enum (str): arial = 'Arial'
            Enum (str): simsun = '宋体'
        """
        yahei = 'Microsoft YaHei'
        youyuan = '幼圆'
        arial = 'Arial'
        simsun = '宋体'

    class Size(Enum):
        """summary: 字号

        Consts:
            Enum (int): tiny = 8
            Enum (int): small = 9
            Enum (int): medium = 10
            Enum (int): large = 11
            Enum (int): huge = 12
        """
        tiny = 8
        small = 9
        medium = 10
        large = 11
        huge = 12

    class Style(Enum):
        """summary: 样式

        Consts:
            Enum (str): normal = 'normal' 正常
            Enum (str): italic = 'italic' 斜体
        """
        normal = 'normal'
        italic = 'italic'
