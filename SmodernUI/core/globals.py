from PySide6.QtCore import Signal, Slot, QObject
import enum
class Globals():
    class Theme(enum.Enum):
        Light = 0
        Dark = 1
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

    def changeTheme():
        Globals.theme = Globals.Theme.Dark if Globals.theme == Globals.Theme.Light else Globals.Theme.Light
        for btn in Globals.ObjRef['BTN']:
            btn.updateStyle(True)


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