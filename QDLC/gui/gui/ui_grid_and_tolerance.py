# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'grid_and_toleranceqVjUfb.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

from .plotwidget import PlotWidget

class Ui_AddGridTolerance(object):
    def setupUi(self, AddGridTolerance):
        if not AddGridTolerance.objectName():
            AddGridTolerance.setObjectName(u"AddGridTolerance")
        AddGridTolerance.resize(860, 488)
        self.label_2 = QLabel(AddGridTolerance)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 821, 51))
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setFrameShadow(QFrame.Plain)
        self.label_10 = QLabel(AddGridTolerance)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 120, 181, 40))
        self.label_10.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px;")
        self.button_reset = QPushButton(AddGridTolerance)
        self.button_reset.setObjectName(u"button_reset")
        self.button_reset.setGeometry(QRect(200, 445, 180, 36))
        self.button_reset.setStyleSheet(u"border-top-left-radius: 0px; border-bottom-left-radius: 0px; border-left-width: 0px;")
        self.button_confirm = QPushButton(AddGridTolerance)
        self.button_confirm.setObjectName(u"button_confirm")
        self.button_confirm.setGeometry(QRect(20, 445, 180, 36))
        self.button_confirm.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px;")
        self.label_12 = QLabel(AddGridTolerance)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 70, 181, 40))
        self.label_12.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px;")
        self.textinput_time = QLineEdit(AddGridTolerance)
        self.textinput_time.setObjectName(u"textinput_time")
        self.textinput_time.setGeometry(QRect(200, 70, 641, 40))
        font = QFont()
        font.setPointSize(11)
        self.textinput_time.setFont(font)
        self.textinput_time.setStyleSheet(u"border-top-left-radius: 0px; border-bottom-left-radius: 0px; border-left-width: 0px;")
        self.textinput_time.setFrame(True)
        self.textinput_time.setAlignment(Qt.AlignCenter)
        self.label_info = QLabel(AddGridTolerance)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setGeometry(QRect(20, 170, 361, 261))
        self.label_info.setStyleSheet(u"padding: 5%;")
        self.label_info.setLineWidth(1)
        self.label_info.setWordWrap(True)
        self.button_plot = QPushButton(AddGridTolerance)
        self.button_plot.setObjectName(u"button_plot")
        self.button_plot.setGeometry(QRect(720, 440, 121, 40))
        font1 = QFont()
        font1.setBold(True)
        self.button_plot.setFont(font1)
        self.button_plot.setStyleSheet(u"border-top-left-radius: 0px; border-bottom-left-radius: 0px; border-left-width: 0px;")
        self.plot_points = PlotWidget(AddGridTolerance)
        self.plot_points.setObjectName(u"plot_points")
        self.plot_points.setGeometry(QRect(390, 170, 451, 256))
        self.input_use_timeconfig = QCheckBox(AddGridTolerance)
        self.input_use_timeconfig.setObjectName(u"input_use_timeconfig")
        self.input_use_timeconfig.setGeometry(QRect(590, 440, 131, 40))
        self.input_use_timeconfig.setFont(font1)
        self.input_use_timeconfig.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px;")
        self.input_use_timeconfig.setChecked(True)
        self.textinput_value = QLineEdit(AddGridTolerance)
        self.textinput_value.setObjectName(u"textinput_value")
        self.textinput_value.setGeometry(QRect(200, 120, 641, 40))
        self.textinput_value.setFont(font)
        self.textinput_value.setStyleSheet(u"border-top-left-radius: 0px; border-bottom-left-radius: 0px; border-left-width: 0px;")
        self.textinput_value.setFrame(True)
        self.textinput_value.setAlignment(Qt.AlignCenter)
        self.label_2.raise_()
        self.label_10.raise_()
        self.button_confirm.raise_()
        self.button_reset.raise_()
        self.label_12.raise_()
        self.textinput_time.raise_()
        self.label_info.raise_()
        self.button_plot.raise_()
        self.plot_points.raise_()
        self.input_use_timeconfig.raise_()
        self.textinput_value.raise_()
        QWidget.setTabOrder(self.textinput_time, self.textinput_value)
        QWidget.setTabOrder(self.textinput_value, self.button_confirm)
        QWidget.setTabOrder(self.button_confirm, self.button_reset)
        QWidget.setTabOrder(self.button_reset, self.button_plot)
        QWidget.setTabOrder(self.button_plot, self.input_use_timeconfig)

        self.retranslateUi(AddGridTolerance)

        QMetaObject.connectSlotsByName(AddGridTolerance)
    # setupUi

    def retranslateUi(self, AddGridTolerance):
        AddGridTolerance.setWindowTitle(QCoreApplication.translate("AddGridTolerance", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("AddGridTolerance", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Title</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("AddGridTolerance", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Value</span></p></body></html>", None))
        self.button_reset.setText(QCoreApplication.translate("AddGridTolerance", u"Reset", None))
        self.button_confirm.setText(QCoreApplication.translate("AddGridTolerance", u"Confirm", None))
        self.label_12.setText(QCoreApplication.translate("AddGridTolerance", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Time</span></p></body></html>", None))
        self.textinput_time.setText("")
        self.textinput_time.setPlaceholderText(QCoreApplication.translate("AddGridTolerance", u"0", None))
        self.label_info.setText(QCoreApplication.translate("AddGridTolerance", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Add or remove any number of point-value pairs. Both the Time and Value fields contain comma-seperated value arrays. Preview and Confirm.</span></p></body></html>", None))
        self.button_plot.setText(QCoreApplication.translate("AddGridTolerance", u"Plot", None))
#if QT_CONFIG(statustip)
        self.input_use_timeconfig.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_use_timeconfig.setText(QCoreApplication.translate("AddGridTolerance", u"Use Timeconfig", None))
        self.textinput_value.setText("")
        self.textinput_value.setPlaceholderText(QCoreApplication.translate("AddGridTolerance", u"0", None))
    # retranslateUi

