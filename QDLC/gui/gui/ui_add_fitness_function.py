# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_fitness_functionvGVeCE.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_AddFitnessFunction(object):
    def setupUi(self, AddFitnessFunction):
        if not AddFitnessFunction.objectName():
            AddFitnessFunction.setObjectName(u"AddFitnessFunction")
        AddFitnessFunction.resize(1086, 610)
        self.gridLayout = QGridLayout(AddFitnessFunction)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textinput_variable = QLineEdit(AddFitnessFunction)
        self.textinput_variable.setObjectName(u"textinput_variable")
        self.textinput_variable.setMinimumSize(QSize(150, 40))
        font = QFont()
        font.setPointSize(11)
        self.textinput_variable.setFont(font)
        self.textinput_variable.setFrame(True)
        self.textinput_variable.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_variable, 5, 2, 1, 1)

        self.label_4 = QLabel(AddFitnessFunction)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 40))
        self.label_4.setFrameShape(QFrame.NoFrame)
        self.label_4.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 3)

        self.textbrowser_current_fitness_function = QTextEdit(AddFitnessFunction)
        self.textbrowser_current_fitness_function.setObjectName(u"textbrowser_current_fitness_function")
        self.textbrowser_current_fitness_function.setFrameShape(QFrame.NoFrame)
        self.textbrowser_current_fitness_function.setFrameShadow(QFrame.Plain)
        self.textbrowser_current_fitness_function.setReadOnly(False)

        self.gridLayout.addWidget(self.textbrowser_current_fitness_function, 1, 0, 1, 3)

        self.label_3 = QLabel(AddFitnessFunction)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 180))

        self.gridLayout.addWidget(self.label_3, 4, 0, 4, 2)

        self.combo_variable = QComboBox(AddFitnessFunction)
        self.combo_variable.addItem("")
        self.combo_variable.addItem("")
        self.combo_variable.addItem("")
        self.combo_variable.addItem("")
        self.combo_variable.addItem("")
        self.combo_variable.setObjectName(u"combo_variable")
        self.combo_variable.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.combo_variable, 4, 2, 1, 1)

        self.label_2 = QLabel(AddFitnessFunction)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 3)

        self.button_confirm = QPushButton(AddFitnessFunction)
        self.button_confirm.setObjectName(u"button_confirm")
        self.button_confirm.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.button_confirm, 7, 2, 1, 1)

        self.line = QFrame(AddFitnessFunction)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 3)

        self.textinput_variable_display = QLineEdit(AddFitnessFunction)
        self.textinput_variable_display.setObjectName(u"textinput_variable_display")
        self.textinput_variable_display.setMinimumSize(QSize(150, 40))
        self.textinput_variable_display.setFont(font)
        self.textinput_variable_display.setFrame(True)
        self.textinput_variable_display.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_variable_display, 6, 2, 1, 1)

        QWidget.setTabOrder(self.textbrowser_current_fitness_function, self.textinput_variable)
        QWidget.setTabOrder(self.textinput_variable, self.textinput_variable_display)
        QWidget.setTabOrder(self.textinput_variable_display, self.button_confirm)
        QWidget.setTabOrder(self.button_confirm, self.combo_variable)

        self.retranslateUi(AddFitnessFunction)

        QMetaObject.connectSlotsByName(AddFitnessFunction)
    # setupUi

    def retranslateUi(self, AddFitnessFunction):
        AddFitnessFunction.setWindowTitle(QCoreApplication.translate("AddFitnessFunction", u"Dialog", None))
        self.textinput_variable.setText("")
        self.textinput_variable.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("AddFitnessFunction", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Variables</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("AddFitnessFunction", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Parameters available (lower case = SI, upper case = number):</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">- Vx for any of the defined variables. For Vi, only Vj with j&lt;i  are available</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:"
                        "0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">- P[x] for any of the defined parameters</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">- Y[x], last(Y[x]),max(Y[x]),min(Y[x])</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">- g and G for Cavity-Coupling</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">- k and K for Cavity Losses</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">- y and Y for Radiative Decay</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; ma"
                        "rgin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">- d and D for Pure Dephasing</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">- T for Temperature</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">- np.function for all Numpy Functions</span></p></body></html>", None))
        self.combo_variable.setItemText(0, QCoreApplication.translate("AddFitnessFunction", u"V1", None))
        self.combo_variable.setItemText(1, QCoreApplication.translate("AddFitnessFunction", u"V2", None))
        self.combo_variable.setItemText(2, QCoreApplication.translate("AddFitnessFunction", u"V3", None))
        self.combo_variable.setItemText(3, QCoreApplication.translate("AddFitnessFunction", u"V4", None))
        self.combo_variable.setItemText(4, QCoreApplication.translate("AddFitnessFunction", u"V5", None))

        self.label_2.setText(QCoreApplication.translate("AddFitnessFunction", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Fitness Function</span></p></body></html>", None))
        self.button_confirm.setText(QCoreApplication.translate("AddFitnessFunction", u"Confirm", None))
        self.textinput_variable_display.setText("")
        self.textinput_variable_display.setPlaceholderText("")
    # retranslateUi

