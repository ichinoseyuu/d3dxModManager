from PySide6.QtCore import QObject
from .theme import Theme

class Globals():
    '''全局变量'''
    #全局obj引用
    ObjRef= {
        'TOOLTIP': None,
        'MAINWINDOW': None,
        'BTN':[],
    }
    theme = Theme.Light
    MAINWINDOW_MARGIN = 9
    TOOLTIP_OFFSET_X = -12
    TOOLTIP_OFFSET_Y = -1

    @classmethod
    def changeTheme(cls):
        cls.theme = Theme.Dark if cls.theme == Theme.Light else Theme.Light
        from ..component.widgets.button import CButton
        cls.addObjList2Ref(cls.findObjByType(cls.ObjRef['MAINWINDOW'], CButton),'BTN')
        for btn in cls.ObjRef['BTN']:
            btn.updateStyle(True)


    @staticmethod
    def addObjList2Ref(objs: list, token: str):
        """_summary_ 添加对象列表到引用

        Args:
            objs (list): 对象列表
            token (str): 引用标识
        """
        if not token in Globals.ObjRef:
            Globals.ObjRef[token] = objs
            return
        Globals.ObjRef[token].extend(objs)


    @staticmethod
    def findObjByType(target: QObject, type: object):
        """_summary_ 查找指定类型对象

        Args:
            target (_type_): 目标对象
            type (object):  类型

        Returns:
            _type_:  查找到的对象列表
        """
        obj_list = []
        for child in target.findChildren(type):
            if isinstance(child, type):
                obj_list.append(child)
        return obj_list


    @staticmethod
    def findObjByName(target: QObject, name: str):
        """_summary_ 查找指定名字的对象

        Args:
            target (_type_): 目标对象
            name (str): 名字

        Returns:
            _type_: 查找到的对象
        """
        children = Globals._get_all_children(target)
        for child in children:
            if child.objectName() == name:
                return child


    @staticmethod
    def _get_all_children(parent: QObject):
        all_children = []
        children = parent.children()  # 获取直接子对象
        if not children: 
            return all_children  # 如果没有子对象，直接返回空列表

        for child in children:
            all_children.append(child) # 将直接子对象添加到结果列表中
            # 递归获取子对象的子对象
            child_children = Globals._get_all_children(child)
            all_children.extend(child_children)  # 将非空的子对象的子对象添加到结果列表中

        return all_children


    @staticmethod
    def findObjByNames(target: QObject, names: list):
        """_summary_ 查找指定名字的对象

        Args:
            target (_type_): 目标对象
            names (list): 名字列表

        Returns:
            _type_: 查找到的对象列表
        """
        obj_list = []
        children = Globals._get_all_children(target)
        for child in children:
            if child.objectName() in names: 
                obj_list.append(child)
        return obj_list