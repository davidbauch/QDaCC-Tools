# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_pulseqTJYUS.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

from .plotwidget import PlotWidget

class Ui_AddPulse(object):
    def setupUi(self, AddPulse):
        if not AddPulse.objectName():
            AddPulse.setObjectName(u"AddPulse")
        AddPulse.resize(1086, 558)
        self.gridLayout = QGridLayout(AddPulse)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(AddPulse)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 5)

        self.label_9 = QLabel(AddPulse)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.textinput_name = QLineEdit(AddPulse)
        self.textinput_name.setObjectName(u"textinput_name")
        self.textinput_name.setMinimumSize(QSize(150, 40))
        font = QFont()
        font.setPointSize(11)
        self.textinput_name.setFont(font)
        self.textinput_name.setFrame(True)
        self.textinput_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_name, 1, 1, 1, 1)

        self.button_load = QPushButton(AddPulse)
        self.button_load.setObjectName(u"button_load")
        self.button_load.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_load, 1, 2, 1, 1)

        self.plot_pulse = PlotWidget(AddPulse)
        self.plot_pulse.setObjectName(u"plot_pulse")
        self.plot_pulse.setMinimumSize(QSize(600, 0))

        self.gridLayout.addWidget(self.plot_pulse, 1, 3, 7, 2)

        self.textinput_transitions = QLineEdit(AddPulse)
        self.textinput_transitions.setObjectName(u"textinput_transitions")
        self.textinput_transitions.setMinimumSize(QSize(150, 40))
        self.textinput_transitions.setFont(font)
        self.textinput_transitions.setFrame(True)
        self.textinput_transitions.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_transitions, 2, 1, 1, 2)

        self.label_12 = QLabel(AddPulse)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_12, 3, 0, 1, 1)

        self.textinput_amp = QLineEdit(AddPulse)
        self.textinput_amp.setObjectName(u"textinput_amp")
        self.textinput_amp.setMinimumSize(QSize(150, 40))
        self.textinput_amp.setFont(font)
        self.textinput_amp.setFrame(True)
        self.textinput_amp.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_amp, 3, 1, 1, 2)

        self.label_10 = QLabel(AddPulse)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)

        self.textinput_energy = QLineEdit(AddPulse)
        self.textinput_energy.setObjectName(u"textinput_energy")
        self.textinput_energy.setMinimumSize(QSize(150, 40))
        self.textinput_energy.setFont(font)
        self.textinput_energy.setFrame(True)
        self.textinput_energy.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_energy, 4, 1, 1, 2)

        self.label_13 = QLabel(AddPulse)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_13, 5, 0, 1, 1)

        self.textinput_center = QLineEdit(AddPulse)
        self.textinput_center.setObjectName(u"textinput_center")
        self.textinput_center.setMinimumSize(QSize(150, 40))
        self.textinput_center.setFont(font)
        self.textinput_center.setFrame(True)
        self.textinput_center.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_center, 5, 1, 1, 2)

        self.label_14 = QLabel(AddPulse)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_14, 6, 0, 1, 1)

        self.textinput_width = QLineEdit(AddPulse)
        self.textinput_width.setObjectName(u"textinput_width")
        self.textinput_width.setMinimumSize(QSize(150, 40))
        self.textinput_width.setFont(font)
        self.textinput_width.setFrame(True)
        self.textinput_width.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_width, 6, 1, 1, 2)

        self.label_15 = QLabel(AddPulse)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_15, 7, 0, 1, 1)

        self.textinput_type = QLineEdit(AddPulse)
        self.textinput_type.setObjectName(u"textinput_type")
        self.textinput_type.setMinimumSize(QSize(150, 40))
        self.textinput_type.setFont(font)
        self.textinput_type.setFrame(True)
        self.textinput_type.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_type, 7, 1, 1, 2)

        self.label = QLabel(AddPulse)
        self.label.setObjectName(u"label")
        self.label.setLineWidth(1)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setMargin(22)

        self.gridLayout.addWidget(self.label, 8, 0, 1, 3)

        self.button_confirm = QPushButton(AddPulse)
        self.button_confirm.setObjectName(u"button_confirm")
        self.button_confirm.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_confirm, 9, 0, 1, 1)

        self.input_use_timeconfig = QCheckBox(AddPulse)
        self.input_use_timeconfig.setObjectName(u"input_use_timeconfig")
        self.input_use_timeconfig.setMinimumSize(QSize(150, 40))
        font1 = QFont()
        font1.setBold(True)
        self.input_use_timeconfig.setFont(font1)

        self.gridLayout.addWidget(self.input_use_timeconfig, 9, 3, 1, 1)

        self.button_plot = QPushButton(AddPulse)
        self.button_plot.setObjectName(u"button_plot")
        self.button_plot.setMinimumSize(QSize(150, 40))
        self.button_plot.setFont(font1)

        self.gridLayout.addWidget(self.button_plot, 9, 4, 1, 1)

        self.button_reset = QPushButton(AddPulse)
        self.button_reset.setObjectName(u"button_reset")
        self.button_reset.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_reset, 9, 2, 1, 1)

        self.button_confirm_replace = QPushButton(AddPulse)
        self.button_confirm_replace.setObjectName(u"button_confirm_replace")
        self.button_confirm_replace.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_confirm_replace, 9, 1, 1, 1)

        self.button_coupled_to = QPushButton(AddPulse)
        self.button_coupled_to.setObjectName(u"button_coupled_to")
        self.button_coupled_to.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_coupled_to, 2, 0, 1, 1)

        self.label_2.raise_()
        self.textinput_name.raise_()
        self.label_9.raise_()
        self.textinput_energy.raise_()
        self.label_10.raise_()
        self.textinput_transitions.raise_()
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
        self.button_reset.raise_()
        self.button_confirm.raise_()
        self.button_confirm_replace.raise_()
        self.button_coupled_to.raise_()
        QWidget.setTabOrder(self.textinput_name, self.textinput_transitions)
        QWidget.setTabOrder(self.textinput_transitions, self.textinput_amp)
        QWidget.setTabOrder(self.textinput_amp, self.textinput_energy)
        QWidget.setTabOrder(self.textinput_energy, self.textinput_center)
        QWidget.setTabOrder(self.textinput_center, self.textinput_width)
        QWidget.setTabOrder(self.textinput_width, self.textinput_type)
        QWidget.setTabOrder(self.textinput_type, self.button_confirm)
        QWidget.setTabOrder(self.button_confirm, self.button_load)
        QWidget.setTabOrder(self.button_load, self.input_use_timeconfig)
        QWidget.setTabOrder(self.input_use_timeconfig, self.button_plot)
        QWidget.setTabOrder(self.button_plot, self.button_reset)
        QWidget.setTabOrder(self.button_reset, self.button_confirm_replace)

        self.retranslateUi(AddPulse)

        QMetaObject.connectSlotsByName(AddPulse)
    # setupUi

    def retranslateUi(self, AddPulse):
        AddPulse.setWindowTitle(QCoreApplication.translate("AddPulse", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("AddPulse", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Add Optical Pulse</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("AddPulse", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Name</span></p></body></html>", None))
        self.textinput_name.setText("")
        self.textinput_name.setPlaceholderText(QCoreApplication.translate("AddPulse", u"Name", None))
        self.button_load.setText(QCoreApplication.translate("AddPulse", u"Load", None))
        self.textinput_transitions.setText("")
        self.textinput_transitions.setPlaceholderText(QCoreApplication.translate("AddPulse", u"List of Transitions", None))
        self.label_12.setText(QCoreApplication.translate("AddPulse", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Amplitude</span></p></body></html>", None))
        self.textinput_amp.setText("")
        self.textinput_amp.setPlaceholderText(QCoreApplication.translate("AddPulse", u"0", None))
        self.label_10.setText(QCoreApplication.translate("AddPulse", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Frequency</span></p></body></html>", None))
        self.textinput_energy.setText("")
        self.textinput_energy.setPlaceholderText(QCoreApplication.translate("AddPulse", u"0", None))
        self.label_13.setText(QCoreApplication.translate("AddPulse", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Temporal Center</span></p></body></html>", None))
        self.textinput_center.setText("")
        self.textinput_center.setPlaceholderText(QCoreApplication.translate("AddPulse", u"0", None))
        self.label_14.setText(QCoreApplication.translate("AddPulse", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Temporal Width</span></p></body></html>", None))
        self.textinput_width.setText("")
        self.textinput_width.setPlaceholderText(QCoreApplication.translate("AddPulse", u"0", None))
        self.label_15.setText(QCoreApplication.translate("AddPulse", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Type</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.textinput_type.setStatusTip(QCoreApplication.translate("AddPulse", u"Can be either of: gauss, cw", None))
#endif // QT_CONFIG(statustip)
        self.textinput_type.setPlaceholderText(QCoreApplication.translate("AddPulse", u"gauss or cw", None))
        self.label.setText(QCoreApplication.translate("AddPulse", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">The type can include any of cw, gauss, super(amp_freq), exponent(val), chirped(val), cutoff(val), chained via the + operator. This will be changed later. Pulse will also be plotted.</span></p></body></html>", None))
        self.button_confirm.setText(QCoreApplication.translate("AddPulse", u"Save", None))
        self.input_use_timeconfig.setText(QCoreApplication.translate("AddPulse", u"Use Timeconfig", None))
        self.button_plot.setText(QCoreApplication.translate("AddPulse", u"Plot", None))
        self.button_reset.setText(QCoreApplication.translate("AddPulse", u"Reset", None))
        self.button_confirm_replace.setText(QCoreApplication.translate("AddPulse", u"Overwrite Original", None))
        self.button_coupled_to.setText(QCoreApplication.translate("AddPulse", u"Coupled To", None))
    # retranslateUi

