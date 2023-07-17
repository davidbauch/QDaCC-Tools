# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_pulseUSGvFF.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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

class Ui_AddPulse(object):
    def setupUi(self, AddPulse):
        if not AddPulse.objectName():
            AddPulse.setObjectName(u"AddPulse")
        AddPulse.resize(860, 558)
        AddPulse.setStyleSheet(u"QWidget {background-color: #F3F4F8;}\n"
"\n"
"QPushButton {background-color: #88282A3A;  color: #FFFFFF; border-radius: 8px;  font-weight: bold; font-size: 16px; }\n"
"QPushButton::hover {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #D2D4DA, stop:0.91 #88282A3A);}\n"
"QPushButton[objectName^=\"button_next_tab\"] {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #f4501e, stop:0.91 #8d2f13);  color: #FFFFFF; border-radius: 8px; }\n"
"QPushButton[objectName^=\"button_next_tab\"]::hover {background-color: #aaf4501e; transition: 2.5s;}\n"
"\n"
"QTextEdit {background-color: #D2D4DA;}\n"
"QTextEdit::hover {background-color: #D2D4DA}\n"
"\n"
"QLabel {background-color: #282A3A; border-radius: 8px; color: #FFFFFF;}\n"
"QLabel[objectName^=\"label_title\"] {background-color: #44282A3A; border-radius: 8px; color: #000000; border-bottom-right-radius: 0; border-bottom-left-radius: 0; border-bottom-width: 2px; border-bottom-color: #000000;}\n"
"QLabel[objectName^=\"label_output\"] {backgr"
                        "ound-color: #44282A3A; border-radius: 8px; color: #000000; border-top-right-radius: 0; border-top-left-radius: 0; }\n"
"QLabel[objectName^=\"label_plot\"] {background-color: #44282A3A; border-radius: 8px; color: #000000;  border-top-right-radius: 0; border-top-left-radius: 0; }\n"
"\n"
"QLineEdit {border-radius: 8px;background-color: #D2D4DA; }\n"
"QLineEdit::hover {background-color: #D2D4DA}\n"
"\n"
"QComboBox {border-radius: 8px; background-color: #D2D4DA;  padding-left: 10% }\n"
"QComboBox::hover {background-color: #D2D4DA}\n"
"\n"
"QCheckBox {background-color: #D2D4DA;border-radius: 8px; padding-left:10% }\n"
"QCheckBox::hover {background-color: #D2D4DA}\n"
"\n"
"QTextBrowser {background-color: #D2D4DA; }\n"
"QTextBrowser[objectName^=\"text_output\"] {background-color: #44282A3A; border-radius: 8px; color: #000000; }\n"
"\n"
"QTabWidget::tab-bar {   border: 0px solid #282A3A;}\n"
"QTabBar::tab {  background-color: #88282A3A;  color: white;  padding-left: 10px; padding-right:10px; padding-bottom: 10px; padd"
                        "ing-top: 5px; font-weight: bold;}\n"
"QTabBar::tab:selected { background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #282A3A, stop:0.91 #88282A3A); padding-right:50px; padding-left:50px; border-width: 2px; border-color: black}\n"
"\n"
"QScrollBar::handle:vertical {background-color: #282A3A; min-height: 30px;max-height: 20%;border-radius: 7px; margin: 0}\n"
"QScrollBar::handle:vertical:hover{background-color: #88282A3A;}\n"
"QScrollBar::handle:vertical:pressed {background-color: #f4501e;}\n"
"QScrollBar::sub-line:vertical {border: none;background-color: #f4501e;height: 15px;border-top-left-radius: 7px;border-top-right-radius: 7px;subcontrol-position: top;subcontrol-origin: 0;max-height: 20%;}\n"
"QScrollBar::sub-line:vertical:hover {background-color: #88282A3A;}\n"
"QScrollBar::sub-line:vertical:pressed {background-color: #f4501e;}\n"
"QScrollBar::add-line:vertical {border: none;background-color: #f4501e;height: 15px;border-bottom-left-radius: 7px;border-bottom-right-radius: 7px;subcontrol-position: "
                        "bottom;subcontrol-origin: 0;max-height: 20%;}\n"
"QScrollBar::add-line:vertical:hover {background-color: #88282A3A;}\n"
"QScrollBar::add-line:vertical:pressed {background-color: #f4501e;}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {background: none;}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {background: none;}")
        self.label_2 = QLabel(AddPulse)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 821, 51))
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setFrameShadow(QFrame.Plain)
        self.textinput_name = QLineEdit(AddPulse)
        self.textinput_name.setObjectName(u"textinput_name")
        self.textinput_name.setGeometry(QRect(200, 70, 131, 40))
        font = QFont()
        font.setPointSize(11)
        self.textinput_name.setFont(font)
        self.textinput_name.setStyleSheet(u"border-radius: 0px; border-left-width: 0px; border-right-width: 0px;")
        self.textinput_name.setFrame(True)
        self.textinput_name.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(AddPulse)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 70, 181, 40))
        self.label_9.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px;")
        self.textinput_energy = QLineEdit(AddPulse)
        self.textinput_energy.setObjectName(u"textinput_energy")
        self.textinput_energy.setGeometry(QRect(200, 220, 181, 40))
        self.textinput_energy.setFont(font)
        self.textinput_energy.setStyleSheet(u"border-top-left-radius: 0px; border-bottom-left-radius: 0px; border-left-width: 0px;")
        self.textinput_energy.setFrame(True)
        self.textinput_energy.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(AddPulse)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 220, 181, 40))
        self.label_10.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px;")
        self.label_11 = QLabel(AddPulse)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 120, 181, 40))
        self.label_11.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px;")
        self.textinput_transitions = QLineEdit(AddPulse)
        self.textinput_transitions.setObjectName(u"textinput_transitions")
        self.textinput_transitions.setGeometry(QRect(200, 120, 181, 40))
        self.textinput_transitions.setFont(font)
        self.textinput_transitions.setStyleSheet(u"border-top-left-radius: 0px; border-bottom-left-radius: 0px; border-left-width: 0px;")
        self.textinput_transitions.setFrame(True)
        self.textinput_transitions.setAlignment(Qt.AlignCenter)
        self.button_reset = QPushButton(AddPulse)
        self.button_reset.setObjectName(u"button_reset")
        self.button_reset.setGeometry(QRect(140, 500, 120, 36))
        self.button_reset.setStyleSheet(u"border-radius: 0px; border-left-width: 0px; border-right-width: 0px;")
        self.button_confirm = QPushButton(AddPulse)
        self.button_confirm.setObjectName(u"button_confirm")
        self.button_confirm.setGeometry(QRect(20, 500, 120, 36))
        self.button_confirm.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px;")
        self.label_12 = QLabel(AddPulse)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 170, 181, 40))
        self.label_12.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px;")
        self.textinput_amp = QLineEdit(AddPulse)
        self.textinput_amp.setObjectName(u"textinput_amp")
        self.textinput_amp.setGeometry(QRect(200, 170, 181, 40))
        self.textinput_amp.setFont(font)
        self.textinput_amp.setStyleSheet(u"border-top-left-radius: 0px; border-bottom-left-radius: 0px; border-left-width: 0px;")
        self.textinput_amp.setFrame(True)
        self.textinput_amp.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(AddPulse)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 270, 181, 40))
        self.label_13.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px;")
        self.textinput_center = QLineEdit(AddPulse)
        self.textinput_center.setObjectName(u"textinput_center")
        self.textinput_center.setGeometry(QRect(200, 270, 181, 40))
        self.textinput_center.setFont(font)
        self.textinput_center.setStyleSheet(u"border-top-left-radius: 0px; border-bottom-left-radius: 0px; border-left-width: 0px;")
        self.textinput_center.setFrame(True)
        self.textinput_center.setAlignment(Qt.AlignCenter)
        self.textinput_width = QLineEdit(AddPulse)
        self.textinput_width.setObjectName(u"textinput_width")
        self.textinput_width.setGeometry(QRect(200, 320, 181, 40))
        self.textinput_width.setFont(font)
        self.textinput_width.setStyleSheet(u"border-top-left-radius: 0px; border-bottom-left-radius: 0px; border-left-width: 0px;")
        self.textinput_width.setFrame(True)
        self.textinput_width.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(AddPulse)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 320, 181, 40))
        self.label_14.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px;")
        self.label_15 = QLabel(AddPulse)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 370, 181, 40))
        self.label_15.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px;")
        self.textinput_type = QLineEdit(AddPulse)
        self.textinput_type.setObjectName(u"textinput_type")
        self.textinput_type.setGeometry(QRect(200, 370, 181, 40))
        self.textinput_type.setFont(font)
        self.textinput_type.setStyleSheet(u"border-top-left-radius: 0px; border-bottom-left-radius: 0px; border-left-width: 0px;")
        self.textinput_type.setFrame(True)
        self.textinput_type.setAlignment(Qt.AlignCenter)
        self.label = QLabel(AddPulse)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 420, 361, 71))
        self.label.setStyleSheet(u"padding: 5%;")
        self.label.setLineWidth(1)
        self.label.setWordWrap(True)
        self.button_plot = QPushButton(AddPulse)
        self.button_plot.setObjectName(u"button_plot")
        self.button_plot.setGeometry(QRect(720, 500, 121, 40))
        font1 = QFont()
        font1.setBold(True)
        self.button_plot.setFont(font1)
        self.button_plot.setStyleSheet(u"border-top-left-radius: 0px; border-bottom-left-radius: 0px; border-left-width: 0px;")
        self.plot_pulse = PlotWidget(AddPulse)
        self.plot_pulse.setObjectName(u"plot_pulse")
        self.plot_pulse.setGeometry(QRect(390, 70, 451, 341))
        self.input_use_timeconfig = QCheckBox(AddPulse)
        self.input_use_timeconfig.setObjectName(u"input_use_timeconfig")
        self.input_use_timeconfig.setGeometry(QRect(590, 500, 131, 40))
        self.input_use_timeconfig.setFont(font1)
        self.input_use_timeconfig.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px;")
        self.button_load = QPushButton(AddPulse)
        self.button_load.setObjectName(u"button_load")
        self.button_load.setGeometry(QRect(330, 70, 51, 40))
        self.button_load.setStyleSheet(u"border-top-left-radius: 0px; border-bottom-left-radius: 0px; border-left-width: 0px;")
        self.button_remove = QPushButton(AddPulse)
        self.button_remove.setObjectName(u"button_remove")
        self.button_remove.setGeometry(QRect(260, 500, 120, 36))
        self.button_remove.setStyleSheet(u"border-top-left-radius: 0px; border-bottom-left-radius: 0px; border-left-width: 0px;")
        self.label_11.raise_()
        self.label_2.raise_()
        self.textinput_name.raise_()
        self.label_9.raise_()
        self.textinput_energy.raise_()
        self.label_10.raise_()
        self.textinput_transitions.raise_()
        self.button_confirm.raise_()
        self.button_reset.raise_()
        self.label_12.raise_()
        self.textinput_amp.raise_()
        self.label_13.raise_()
        self.textinput_center.raise_()
        self.textinput_width.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.textinput_type.raise_()
        self.label.raise_()
        self.button_plot.raise_()
        self.plot_pulse.raise_()
        self.input_use_timeconfig.raise_()
        self.button_load.raise_()
        self.button_remove.raise_()

        self.retranslateUi(AddPulse)

        QMetaObject.connectSlotsByName(AddPulse)
    # setupUi

    def retranslateUi(self, AddPulse):
        AddPulse.setWindowTitle(QCoreApplication.translate("AddPulse", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("AddPulse", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Add Optical Pulse</span></p></body></html>", None))
        self.textinput_name.setText("")
        self.textinput_name.setPlaceholderText(QCoreApplication.translate("AddPulse", u"Name", None))
        self.label_9.setText(QCoreApplication.translate("AddPulse", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Name</span></p></body></html>", None))
        self.textinput_energy.setText("")
        self.textinput_energy.setPlaceholderText(QCoreApplication.translate("AddPulse", u"0", None))
        self.label_10.setText(QCoreApplication.translate("AddPulse", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Frequency</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("AddPulse", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Coupled To</span></p></body></html>", None))
        self.textinput_transitions.setText("")
        self.textinput_transitions.setPlaceholderText(QCoreApplication.translate("AddPulse", u"List of Transitions", None))
        self.button_reset.setText(QCoreApplication.translate("AddPulse", u"Reset", None))
        self.button_confirm.setText(QCoreApplication.translate("AddPulse", u"Add", None))
        self.label_12.setText(QCoreApplication.translate("AddPulse", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Amplitude</span></p></body></html>", None))
        self.textinput_amp.setText("")
        self.textinput_amp.setPlaceholderText(QCoreApplication.translate("AddPulse", u"0", None))
        self.label_13.setText(QCoreApplication.translate("AddPulse", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Temporal Center</span></p></body></html>", None))
        self.textinput_center.setText("")
        self.textinput_center.setPlaceholderText(QCoreApplication.translate("AddPulse", u"0", None))
        self.textinput_width.setText("")
        self.textinput_width.setPlaceholderText(QCoreApplication.translate("AddPulse", u"0", None))
        self.label_14.setText(QCoreApplication.translate("AddPulse", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Temporal Width</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("AddPulse", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Type</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.textinput_type.setStatusTip(QCoreApplication.translate("AddPulse", u"Can be either of: gauss, sine", None))
#endif // QT_CONFIG(statustip)
        self.textinput_type.setPlaceholderText(QCoreApplication.translate("AddPulse", u"gauss or sine", None))
        self.label.setText(QCoreApplication.translate("AddPulse", u"<html><head/><body><p align=\"justify\"><span style=\" font-weight:700;\">The type can include any of cw, gauss, super(amp_freq), exponent(val), chirped(val), cutoff(val), chained via the + operator. This will be changed later. Pulse will also be plotted.</span></p></body></html>", None))
        self.button_plot.setText(QCoreApplication.translate("AddPulse", u"Plot", None))
        self.input_use_timeconfig.setText(QCoreApplication.translate("AddPulse", u"Use Timeconfig", None))
        self.button_load.setText(QCoreApplication.translate("AddPulse", u"Load", None))
        self.button_remove.setText(QCoreApplication.translate("AddPulse", u"Remove", None))
    # retranslateUi

