from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QPainter, QPainterPath, QPen, QColor
from PySide6.QtWidgets import QVBoxLayout, QSlider, QWidget, QApplication


from PySide6.QtCore import Qt, QRectF, QPropertyAnimation, Property, QEasingCurve
from PySide6.QtGui import QPainter, QPainterPath, QPen, QColor
from PySide6.QtWidgets import QVBoxLayout, QSlider, QWidget, QApplication

class ProgressBar(QWidget):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.p=0
        self.setMinimumSize(100, 100)
        self.radius = 100
        self.outer_radius = 30
        self.animation = QPropertyAnimation(self, b"p")
        self.animation.setDuration(750)
        # Set smooth animation curve
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.color = "white"
        self.color_bar = "black"
        self.x0 = 0
        self.y0 = 0

    def updateRadius(self):
        w,h = self.width(), self.height()
        self.x0 = w/2
        self.y0 = h/2
        self.radius = min(w,h)/2 - self.outer_radius
        

    def setValue(self,pp):
        if pp > 1:
            pp /= 100
        if self.p == pp:
            return
        self.animation.setStartValue(self.p)
        self.animation.setEndValue(pp)
        self.animation.start()

    def paintEvent(self,e):
        self.updateRadius()
        pd = self.p * 360
        rd = 360 - pd
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        path, path2 = QPainterPath(),QPainterPath()
        path.moveTo(self.x0, self.y0 - self.radius)
        path.arcTo(QRectF(self.x0 - self.radius, self.y0 - self.radius, 2*self.radius, 2*self.radius), 90, -pd)
        pen, pen2 = QPen(), QPen()
        pen.setCapStyle(Qt.FlatCap)
        pen.setColor(self.color_bar)
        pen.setWidth(self.outer_radius)
        p.strokePath(path, pen)
        path2.moveTo(self.x0, self.y0 - self.radius)
        pen2.setWidth(self.outer_radius)
        pen2.setColor(self.color)
        pen2.setCapStyle(Qt.FlatCap)
        path2.arcTo(QRectF(self.x0 - self.radius, self.y0 - self.radius, 2*self.radius, 2*self.radius), 90, rd)
        p.strokePath(path2, pen2)

    def get_p(self):
        return self._p

    def set_p(self, value):
        if self._p == value:
            return
        self._p = value
        self.update()

    p = Property(float, get_p, set_p)
    _p = 0

if __name__ == '__main__':
    class Test(QWidget):
        def __init__(self):
            super().__init__()
            l = QVBoxLayout(self)
            p = ProgressBar()
            s = QSlider(Qt.Horizontal, self)
            s.setMinimum(0)
            s.setMaximum(100)
            l.addWidget(p)
            l.addWidget(s)
            self.setLayout(l)
            s.valueChanged.connect(lambda :p.upd(s.value()/s.maximum()))

    app = QApplication()
    main_widget = Test()
    main_widget.show()
    app.exec_()