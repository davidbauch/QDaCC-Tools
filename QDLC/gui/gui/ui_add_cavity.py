# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_cavityduijPt.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_AddCavity(object):
    def setupUi(self, AddCavity):
        if not AddCavity.objectName():
            AddCavity.setObjectName(u"AddCavity")
        AddCavity.resize(480, 416)
        self.gridLayout = QGridLayout(AddCavity)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(AddCavity)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 40))
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 3)

        self.label_9 = QLabel(AddCavity)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.textinput_name = QLineEdit(AddCavity)
        self.textinput_name.setObjectName(u"textinput_name")
        self.textinput_name.setMinimumSize(QSize(150, 40))
        font = QFont()
        font.setPointSize(11)
        self.textinput_name.setFont(font)
        self.textinput_name.setFrame(True)
        self.textinput_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_name, 1, 1, 1, 1)

        self.button_load = QPushButton(AddCavity)
        self.button_load.setObjectName(u"button_load")
        self.button_load.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_load, 1, 2, 1, 1)

        self.label_10 = QLabel(AddCavity)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)

        self.textinput_energy = QLineEdit(AddCavity)
        self.textinput_energy.setObjectName(u"textinput_energy")
        self.textinput_energy.setMinimumSize(QSize(150, 40))
        self.textinput_energy.setFont(font)
        self.textinput_energy.setFrame(True)
        self.textinput_energy.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_energy, 2, 1, 1, 2)

        self.textinput_transitions = QLineEdit(AddCavity)
        self.textinput_transitions.setObjectName(u"textinput_transitions")
        self.textinput_transitions.setMinimumSize(QSize(150, 40))
        self.textinput_transitions.setFont(font)
        self.textinput_transitions.setFrame(True)
        self.textinput_transitions.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_transitions, 3, 1, 1, 2)

        self.label_12 = QLabel(AddCavity)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)

        self.textinput_transition_scalings = QLineEdit(AddCavity)
        self.textinput_transition_scalings.setObjectName(u"textinput_transition_scalings")
        self.textinput_transition_scalings.setMinimumSize(QSize(150, 40))
        self.textinput_transition_scalings.setFont(font)
        self.textinput_transition_scalings.setFrame(True)
        self.textinput_transition_scalings.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_transition_scalings, 4, 1, 1, 1)

        self.button_setone = QPushButton(AddCavity)
        self.button_setone.setObjectName(u"button_setone")
        self.button_setone.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_setone, 4, 2, 1, 1)

        self.label_13 = QLabel(AddCavity)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_13, 5, 0, 1, 1)

        self.textinput_decay = QLineEdit(AddCavity)
        self.textinput_decay.setObjectName(u"textinput_decay")
        self.textinput_decay.setMinimumSize(QSize(150, 40))
        self.textinput_decay.setFont(font)
        self.textinput_decay.setFrame(True)
        self.textinput_decay.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_decay, 5, 1, 1, 2)

        self.label_14 = QLabel(AddCavity)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_14, 6, 0, 1, 1)

        self.textinput_photonnumber = QLineEdit(AddCavity)
        self.textinput_photonnumber.setObjectName(u"textinput_photonnumber")
        self.textinput_photonnumber.setMinimumSize(QSize(150, 40))
        self.textinput_photonnumber.setFont(font)
        self.textinput_photonnumber.setFrame(True)
        self.textinput_photonnumber.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_photonnumber, 6, 1, 1, 2)

        self.button_confirm = QPushButton(AddCavity)
        self.button_confirm.setObjectName(u"button_confirm")
        self.button_confirm.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_confirm, 7, 0, 1, 1)

        self.button_reset = QPushButton(AddCavity)
        self.button_reset.setObjectName(u"button_reset")
        self.button_reset.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_reset, 7, 2, 1, 1)

        self.button_confirm_replace = QPushButton(AddCavity)
        self.button_confirm_replace.setObjectName(u"button_confirm_replace")
        self.button_confirm_replace.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_confirm_replace, 7, 1, 1, 1)

        self.button_coupled_to = QPushButton(AddCavity)
        self.button_coupled_to.setObjectName(u"button_coupled_to")
        self.button_coupled_to.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_coupled_to, 3, 0, 1, 1)

        self.label_2.raise_()
        self.textinput_name.raise_()
        self.label_9.raise_()
        self.textinput_energy.raise_()
        self.label_10.raise_()
        self.textinput_transitions.raise_()
        self.button_confirm.raise_()
        self.button_reset.raise_()
        self.textinput_transition_scalings.raise_()
        self.label_13.raise_()
        self.textinput_decay.raise_()
        self.label_12.raise_()
        self.label_14.raise_()
        self.textinput_photonnumber.raise_()
        self.button_setone.raise_()
        self.button_load.raise_()
        self.button_confirm_replace.raise_()
        self.button_coupled_to.raise_()
        QWidget.setTabOrder(self.textinput_name, self.textinput_energy)
        QWidget.setTabOrder(self.textinput_energy, self.textinput_transitions)
        QWidget.setTabOrder(self.textinput_transitions, self.textinput_transition_scalings)
        QWidget.setTabOrder(self.textinput_transition_scalings, self.textinput_decay)
        QWidget.setTabOrder(self.textinput_decay, self.textinput_photonnumber)
        QWidget.setTabOrder(self.textinput_photonnumber, self.button_confirm)
        QWidget.setTabOrder(self.button_confirm, self.button_load)
        QWidget.setTabOrder(self.button_load, self.button_setone)
        QWidget.setTabOrder(self.button_setone, self.button_confirm_replace)
        QWidget.setTabOrder(self.button_confirm_replace, self.button_reset)

        self.retranslateUi(AddCavity)

        QMetaObject.connectSlotsByName(AddCavity)
    # setupUi

    def retranslateUi(self, AddCavity):
        AddCavity.setWindowTitle(QCoreApplication.translate("AddCavity", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("AddCavity", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Add Optical Cavity</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("AddCavity", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Name</span></p></body></html>", None))
        self.textinput_name.setText("")
        self.textinput_name.setPlaceholderText(QCoreApplication.translate("AddCavity", u"Name", None))
        self.button_load.setText(QCoreApplication.translate("AddCavity", u"Load", None))
        self.label_10.setText(QCoreApplication.translate("AddCavity", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Energy</span></p></body></html>", None))
        self.textinput_energy.setText("")
        self.textinput_energy.setPlaceholderText(QCoreApplication.translate("AddCavity", u"0", None))
        self.textinput_transitions.setText("")
        self.textinput_transitions.setPlaceholderText(QCoreApplication.translate("AddCavity", u"List of Transitions", None))
        self.label_12.setText(QCoreApplication.translate("AddCavity", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Scaling</span></p></body></html>", None))
        self.textinput_transition_scalings.setText("")
        self.textinput_transition_scalings.setPlaceholderText(QCoreApplication.translate("AddCavity", u"List of Scalings", None))
        self.button_setone.setText(QCoreApplication.translate("AddCavity", u"Set 1", None))
        self.label_13.setText(QCoreApplication.translate("AddCavity", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Decay Scaling</span></p></body></html>", None))
        self.textinput_decay.setText(QCoreApplication.translate("AddCavity", u"1", None))
        self.textinput_decay.setPlaceholderText(QCoreApplication.translate("AddCavity", u"1", None))
        self.label_14.setText(QCoreApplication.translate("AddCavity", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Photon Number</span></p></body></html>", None))
        self.textinput_photonnumber.setText("")
        self.textinput_photonnumber.setPlaceholderText(QCoreApplication.translate("AddCavity", u"Maximum Photons", None))
        self.button_confirm.setText(QCoreApplication.translate("AddCavity", u"Save", None))
        self.button_reset.setText(QCoreApplication.translate("AddCavity", u"Reset", None))
        self.button_confirm_replace.setText(QCoreApplication.translate("AddCavity", u"Overwrite Original", None))
        self.button_coupled_to.setText(QCoreApplication.translate("AddCavity", u"Coupled To", None))
    # retranslateUi

