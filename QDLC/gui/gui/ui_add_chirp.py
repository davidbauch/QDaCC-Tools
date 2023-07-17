# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_chirpsvnLLQ.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QDialog,
    QFrame, QGridLayout, QLabel, QLineEdit,
    QListView, QPushButton, QSizePolicy, QWidget)

from .plotwidget import PlotWidget

class Ui_AddChirp(object):
    def setupUi(self, AddChirp):
        if not AddChirp.objectName():
            AddChirp.setObjectName(u"AddChirp")
        AddChirp.resize(986, 556)
        self.gridLayout = QGridLayout(AddChirp)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textinput_type = QLineEdit(AddChirp)
        self.textinput_type.setObjectName(u"textinput_type")
        self.textinput_type.setMinimumSize(QSize(150, 40))
        font = QFont()
        font.setPointSize(11)
        self.textinput_type.setFont(font)
        self.textinput_type.setFrame(True)
        self.textinput_type.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_type, 8, 1, 1, 2)

        self.button_add = QPushButton(AddChirp)
        self.button_add.setObjectName(u"button_add")
        self.button_add.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_add, 6, 0, 1, 3)

        self.button_coupled_to = QPushButton(AddChirp)
        self.button_coupled_to.setObjectName(u"button_coupled_to")
        self.button_coupled_to.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_coupled_to, 2, 0, 1, 1)

        self.button_load = QPushButton(AddChirp)
        self.button_load.setObjectName(u"button_load")
        self.button_load.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_load, 1, 2, 1, 1)

        self.textinput_energy = QLineEdit(AddChirp)
        self.textinput_energy.setObjectName(u"textinput_energy")
        self.textinput_energy.setMinimumSize(QSize(150, 40))
        self.textinput_energy.setFont(font)
        self.textinput_energy.setFrame(True)
        self.textinput_energy.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_energy, 5, 1, 1, 2)

        self.label_2 = QLabel(AddChirp)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 40))
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 5)

        self.button_setone = QPushButton(AddChirp)
        self.button_setone.setObjectName(u"button_setone")
        self.button_setone.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_setone, 3, 2, 1, 1)

        self.button_remove_points = QPushButton(AddChirp)
        self.button_remove_points.setObjectName(u"button_remove_points")
        self.button_remove_points.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_remove_points, 7, 0, 1, 3)

        self.button_plot = QPushButton(AddChirp)
        self.button_plot.setObjectName(u"button_plot")
        self.button_plot.setMinimumSize(QSize(150, 40))
        font1 = QFont()
        font1.setBold(True)
        self.button_plot.setFont(font1)

        self.gridLayout.addWidget(self.button_plot, 9, 4, 1, 1)

        self.textinput_state_couplings = QLineEdit(AddChirp)
        self.textinput_state_couplings.setObjectName(u"textinput_state_couplings")
        self.textinput_state_couplings.setMinimumSize(QSize(150, 40))
        self.textinput_state_couplings.setFont(font)
        self.textinput_state_couplings.setFrame(True)
        self.textinput_state_couplings.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_state_couplings, 3, 1, 1, 1)

        self.input_use_timeconfig = QCheckBox(AddChirp)
        self.input_use_timeconfig.setObjectName(u"input_use_timeconfig")
        self.input_use_timeconfig.setMinimumSize(QSize(150, 40))
        self.input_use_timeconfig.setFont(font1)
        self.input_use_timeconfig.setChecked(True)

        self.gridLayout.addWidget(self.input_use_timeconfig, 9, 3, 1, 1)

        self.button_reset = QPushButton(AddChirp)
        self.button_reset.setObjectName(u"button_reset")
        self.button_reset.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_reset, 9, 2, 1, 1)

        self.label_12 = QLabel(AddChirp)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)

        self.textinput_states = QLineEdit(AddChirp)
        self.textinput_states.setObjectName(u"textinput_states")
        self.textinput_states.setMinimumSize(QSize(150, 40))
        self.textinput_states.setFont(font)
        self.textinput_states.setFrame(True)
        self.textinput_states.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_states, 2, 1, 1, 2)

        self.textinput_time = QLineEdit(AddChirp)
        self.textinput_time.setObjectName(u"textinput_time")
        self.textinput_time.setMinimumSize(QSize(150, 40))
        self.textinput_time.setFont(font)
        self.textinput_time.setFrame(True)
        self.textinput_time.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_time, 4, 1, 1, 2)

        self.label_10 = QLabel(AddChirp)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)

        self.label_15 = QLabel(AddChirp)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_15, 8, 0, 1, 1)

        self.textinput_name = QLineEdit(AddChirp)
        self.textinput_name.setObjectName(u"textinput_name")
        self.textinput_name.setMinimumSize(QSize(150, 40))
        self.textinput_name.setFont(font)
        self.textinput_name.setFrame(True)
        self.textinput_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_name, 1, 1, 1, 1)

        self.label_13 = QLabel(AddChirp)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_13, 3, 0, 1, 1)

        self.button_confirm_replace = QPushButton(AddChirp)
        self.button_confirm_replace.setObjectName(u"button_confirm_replace")
        self.button_confirm_replace.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_confirm_replace, 9, 1, 1, 1)

        self.label_9 = QLabel(AddChirp)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.button_confirm = QPushButton(AddChirp)
        self.button_confirm.setObjectName(u"button_confirm")
        self.button_confirm.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_confirm, 9, 0, 1, 1)

        self.plot_chirp = PlotWidget(AddChirp)
        self.plot_chirp.setObjectName(u"plot_chirp")
        self.plot_chirp.setMinimumSize(QSize(500, 0))

        self.gridLayout.addWidget(self.plot_chirp, 1, 3, 5, 2)

        self.listView = QListView(AddChirp)
        self.listView.setObjectName(u"listView")
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout.addWidget(self.listView, 6, 3, 3, 2)

        self.label_2.raise_()
        self.textinput_name.raise_()
        self.label_9.raise_()
        self.textinput_energy.raise_()
        self.label_10.raise_()
        self.textinput_states.raise_()
        self.label_12.raise_()
        self.textinput_time.raise_()
        self.label_15.raise_()
        self.textinput_type.raise_()
        self.button_plot.raise_()
        self.plot_chirp.raise_()
        self.input_use_timeconfig.raise_()
        self.button_load.raise_()
        self.button_add.raise_()
        self.button_remove_points.raise_()
        self.label_13.raise_()
        self.textinput_state_couplings.raise_()
        self.button_setone.raise_()
        self.button_reset.raise_()
        self.button_confirm.raise_()
        self.button_confirm_replace.raise_()
        self.listView.raise_()
        self.button_coupled_to.raise_()
        QWidget.setTabOrder(self.textinput_name, self.textinput_states)
        QWidget.setTabOrder(self.textinput_states, self.textinput_state_couplings)
        QWidget.setTabOrder(self.textinput_state_couplings, self.textinput_time)
        QWidget.setTabOrder(self.textinput_time, self.textinput_energy)
        QWidget.setTabOrder(self.textinput_energy, self.textinput_type)
        QWidget.setTabOrder(self.textinput_type, self.button_add)
        QWidget.setTabOrder(self.button_add, self.button_confirm)
        QWidget.setTabOrder(self.button_confirm, self.button_load)
        QWidget.setTabOrder(self.button_load, self.button_setone)
        QWidget.setTabOrder(self.button_setone, self.button_remove_points)
        QWidget.setTabOrder(self.button_remove_points, self.button_confirm_replace)
        QWidget.setTabOrder(self.button_confirm_replace, self.button_reset)
        QWidget.setTabOrder(self.button_reset, self.input_use_timeconfig)
        QWidget.setTabOrder(self.input_use_timeconfig, self.button_plot)

        self.retranslateUi(AddChirp)

        QMetaObject.connectSlotsByName(AddChirp)
    # setupUi

    def retranslateUi(self, AddChirp):
        AddChirp.setWindowTitle(QCoreApplication.translate("AddChirp", u"Dialog", None))
#if QT_CONFIG(statustip)
        self.textinput_type.setStatusTip(QCoreApplication.translate("AddChirp", u"Can be either of: gauss, sine", None))
#endif // QT_CONFIG(statustip)
        self.textinput_type.setText(QCoreApplication.translate("AddChirp", u"monotone", None))
        self.textinput_type.setPlaceholderText(QCoreApplication.translate("AddChirp", u"gauss or sine", None))
        self.button_add.setText(QCoreApplication.translate("AddChirp", u"Add Point(s)", None))
        self.button_coupled_to.setText(QCoreApplication.translate("AddChirp", u"Coupled To", None))
        self.button_load.setText(QCoreApplication.translate("AddChirp", u"Load", None))
        self.textinput_energy.setText("")
        self.textinput_energy.setPlaceholderText(QCoreApplication.translate("AddChirp", u"0", None))
        self.label_2.setText(QCoreApplication.translate("AddChirp", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Add Shift</span></p></body></html>", None))
        self.button_setone.setText(QCoreApplication.translate("AddChirp", u"Set 1", None))
        self.button_remove_points.setText(QCoreApplication.translate("AddChirp", u"Remove Point(s)", None))
        self.button_plot.setText(QCoreApplication.translate("AddChirp", u"Plot", None))
        self.textinput_state_couplings.setText("")
        self.textinput_state_couplings.setPlaceholderText(QCoreApplication.translate("AddChirp", u"List of Scalings", None))
#if QT_CONFIG(statustip)
        self.input_use_timeconfig.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_use_timeconfig.setText(QCoreApplication.translate("AddChirp", u"Use Timeconfig", None))
        self.button_reset.setText(QCoreApplication.translate("AddChirp", u"Reset", None))
        self.label_12.setText(QCoreApplication.translate("AddChirp", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Time</span></p></body></html>", None))
        self.textinput_states.setText("")
        self.textinput_states.setPlaceholderText(QCoreApplication.translate("AddChirp", u"List of States or Cavities", None))
        self.textinput_time.setText("")
        self.textinput_time.setPlaceholderText(QCoreApplication.translate("AddChirp", u"0", None))
        self.label_10.setText(QCoreApplication.translate("AddChirp", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Energy</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("AddChirp", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Type</span></p></body></html>", None))
        self.textinput_name.setText("")
        self.textinput_name.setPlaceholderText(QCoreApplication.translate("AddChirp", u"Name", None))
        self.label_13.setText(QCoreApplication.translate("AddChirp", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Coupling Factors</span></p></body></html>", None))
        self.button_confirm_replace.setText(QCoreApplication.translate("AddChirp", u"Overwrite Original", None))
        self.label_9.setText(QCoreApplication.translate("AddChirp", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Name</span></p></body></html>", None))
        self.button_confirm.setText(QCoreApplication.translate("AddChirp", u"Save", None))
    # retranslateUi

