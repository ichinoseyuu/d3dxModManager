from PySide6.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve, QTimer, Signal, QObject
from PySide6.QtWidgets import QWidget, QApplication

class AnimationGroup(QObject):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.animations = []

    def addAnim(self, prop_name, startValue, endValue, duration, easing=QEasingCurve.Type.Linear):
        """
        添加动画到动画组
        :param target: 动画目标对象 (QObject)
        :param prop_name: 需要动画化的属性名称 (例如: "geometry", "opacity")
        :param start_value: 动画的起始值
        :param end_value: 动画的结束值
        :param duration: 动画持续时间（毫秒）
        :param easing: 动画的缓动效果（默认为线性）
        """
        animation = QPropertyAnimation(self.parent(), prop_name)
        animation.setStartValue(startValue)
        animation.setEndValue(endValue)
        animation.setDuration(duration)
        animation.setEasingCurve(easing)

        # 连接动画的finished信号，动画完成时调用一个槽函数
        animation.finished.connect(self.onAnimFinished)

        self.animations.append(animation)

    def play(self):
        """
        播放动画组中的所有动画
        """
        for animation in self.animations:
            animation.start()

    def onAnimFinished(self):
        """
        动画完成时的槽函数，清理动画组并删除对象
        """
        # 检查是否所有动画都已完成
        if all(animation.state() == QPropertyAnimation.Stopped for animation in self.animations):
            print("所有动画完成，准备删除 AnimationGroup")
            self.clear()

    def clear(self):
        """
        清除动画组中的所有动画并删除对象
        """
        print("清除动画组中的所有动画")
        self.animations.clear()
        self.deleteLater()  # 删除当前对象
