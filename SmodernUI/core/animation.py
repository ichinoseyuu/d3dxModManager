from PySide6.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve, QTimer, Signal, QObject
from PySide6.QtWidgets import QWidget, QApplication
import collections

class CAnimPool(QObject):
    def __init__(self, pool_size=10):
        self.__anim_pool = collections.deque()
        self.__pool_size = pool_size
        # 预生成指定数量的QPropertyAnimation对象并加入池中
        for _ in range(pool_size):
            self.__anim_pool.append(QPropertyAnimation())

    def getAnim(self, obj, prop):
        # 如果池中有可用的动画对象
        if self.__anim_pool:
            anim = self.__anim_pool.popleft()
        else:
            # 池中没有可用的动画，创建一个新的动画对象
            anim = QPropertyAnimation()
        anim.setTargetObject(obj)
        anim.setPropertyName(prop.encode())
        return anim

    def releaseAnim(self, anim):
        if len(self.__anim_pool) < self.__pool_size:
            self.__anim_pool.append(anim)

    def animate(self, obj, prop, start, end, duration=1000):
        anim = self.getAnim(obj, prop)
        anim.setStartValue(start)
        anim.setEndValue(end)
        anim.setDuration(duration)
        anim.start()
        anim.finished.connect(lambda: self.releaseAnim(anim))

class CAnimTion(QObject):
    def __init__(self, parent=None):
        pass