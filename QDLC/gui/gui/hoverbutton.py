
from PySide6.QtCore import QAbstractAnimation, QPropertyAnimation, Property, QEasingCurve, QTimer
from PySide6.QtWidgets import QPushButton
from PySide6 import QtGui


class HoverButton(QPushButton):
    def __init__(self, *args):
        super().__init__(*args)
        self._value = 0
        self.__initUi()

    def __initUi(self):
        self.__animation = QPropertyAnimation(self, b"value")
        self.__animation.valueChanged.connect(self.__setvalue)
        self.__animation.setStartValue(0)
        self.__animation.setEndValue(1-0.001)
        self.__animation.setDuration(1000) # 500ms for 1 loop
        self.__animation.setLoopCount(1) # 2 loops
        self.__animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.__styleInit(0.0)


    def lerp(self,a,b,t):
        return a + (b-a)*t

    def __styleInit(self, value: float):
        angle = self.lerp(0, 360, value)
        style = f"""HoverButton {{
            background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 #F3F4F6, stop:1 #e6e8ec);
            color: #374151;
            border-radius: 3px;
            font-weight: bold;
            font-size: 16px;
            border-width: 2px;
            border-style: solid;
            border-color: qconicalgradient(cx:0.5, cy:0.5, angle:{angle}, stop:0 transparent, stop:{value} lightgray, stop:{value + 0.001} transparent);
        }}"""
        self.setStyleSheet(style)

    def enterEvent(self, e):
        self.__animation.setDirection(QAbstractAnimation.Forward)
        self.__animation.start()
        #QTimer.singleShot(1000, lambda: self.slowRotate()) # start slow rotation after 1s
        return super().enterEvent(e)

    def slowRotate(self):
        self.__slowAnimation = QPropertyAnimation(self, b"value")
        self.__slowAnimation.setDirection(QAbstractAnimation.Backward)
        self.__slowAnimation.valueChanged.connect(self.__setvalue)
        self.__slowAnimation.setStartValue(0)
        self.__slowAnimation.setEndValue(1-0.001)
        self.__slowAnimation.setDuration(10000) # 10s for 1 loop
        self.__slowAnimation.setLoopCount(-1) # infinite loops
        self.__slowAnimation.start()

    def leaveEvent(self, e):
        #if self.__slowAnimation:
        #    self.__slowAnimation.stop()
        #    self.__slowAnimation.updateCurrentValue(1)
        self.__animation.setDirection(QAbstractAnimation.Backward)
        self.__animation.start()
        return super().leaveEvent(e)

    def __setvalue(self, value):
        self.__styleInit(value)

    @Property(float)
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self._value = value