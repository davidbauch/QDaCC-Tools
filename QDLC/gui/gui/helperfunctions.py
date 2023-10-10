from PySide6.QtGui import QIcon, QPainter, QColor

def changeIconColor(icon, color, size):
    pixmap = icon.pixmap(icon.actualSize(size))
    painter = QPainter(pixmap)
    painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
    painter.fillRect(pixmap.rect(), color)
    painter.end()
    return QIcon(pixmap)

def changePixmapColor(pixmap, color):
    painter = QPainter(pixmap)
    painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
    painter.fillRect(pixmap.rect(), color)
    painter.end()
    return pixmap

from PySide6.QtGui import QGradient, QLinearGradient

from PySide6.QtGui import QGradient, QLinearGradient, QColor

from math import sin, cos
def changePixmapGradient(pixmap, colors : list | tuple, angle : float = 0):
    painter = QPainter(pixmap)
    painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
    painter.setRenderHint(QPainter.Antialiasing)
    painter.setRenderHint(QPainter.SmoothPixmapTransform)
    painter.setRenderHint(QPainter.TextAntialiasing)
    w,h = pixmap.width(), pixmap.height()
    x0 = w * sin(angle*2*3.1415/360)
    y0 = h * cos(angle*2*3.1415/360)
    x1 = w * sin((angle+180)*2*3.1415/360)
    y1 = h * cos((angle+180)*2*3.1415/360)
    gradient = QLinearGradient(x0, y0, x1, y1)
    for i,color in enumerate(colors):
        val = i / (len(colors)-1)
        gradient.setColorAt(val, color)
    painter.setBrush(gradient)
    painter.drawRect(pixmap.rect())
    painter.end()
    return pixmap