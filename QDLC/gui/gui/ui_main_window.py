# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowxhsPvT.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGraphicsView, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListView, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QStatusBar, QTabWidget, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)

from .plotwidget import PlotWidget
from .progressbar import ProgressBar
from .textbrowserexternal import TextBrowserExternal

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1425, 843)
        MainWindow.setIconSize(QSize(64, 64))
        self.actionLoad_QDaCC_Command = QAction(MainWindow)
        self.actionLoad_QDaCC_Command.setObjectName(u"actionLoad_QDaCC_Command")
        self.actionExport_QDaCC_Command = QAction(MainWindow)
        self.actionExport_QDaCC_Command.setObjectName(u"actionExport_QDaCC_Command")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_14 = QGridLayout(self.centralwidget)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.main_logo = QLabel(self.centralwidget)
        self.main_logo.setObjectName(u"main_logo")
        self.main_logo.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_14.addWidget(self.main_logo, 0, 0, 1, 1)

        self.main_descriptor = QLabel(self.centralwidget)
        self.main_descriptor.setObjectName(u"main_descriptor")

        self.gridLayout_14.addWidget(self.main_descriptor, 0, 1, 1, 1)

        self.main_tab_widget = QTabWidget(self.centralwidget)
        self.main_tab_widget.setObjectName(u"main_tab_widget")
        self.main_tab_widget.setTabPosition(QTabWidget.West)
        self.main_tab_widget.setTabShape(QTabWidget.Rounded)
        self.tab_system = QWidget()
        self.tab_system.setObjectName(u"tab_system")
        self.gridLayout_26 = QGridLayout(self.tab_system)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.frame_10 = QFrame(self.tab_system)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_10)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.label_output_system = QGraphicsView(self.frame_10)
        self.label_output_system.setObjectName(u"label_output_system")

        self.gridLayout_24.addWidget(self.label_output_system, 0, 0, 1, 1)


        self.gridLayout_26.addWidget(self.frame_10, 0, 0, 2, 1)

        self.frame_7 = QFrame(self.tab_system)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.button_add_cavity = QPushButton(self.frame_7)
        self.button_add_cavity.setObjectName(u"button_add_cavity")
        self.button_add_cavity.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.button_add_cavity, 1, 0, 1, 2)

        self.button_add_electronic_shift = QPushButton(self.frame_7)
        self.button_add_electronic_shift.setObjectName(u"button_add_electronic_shift")
        self.button_add_electronic_shift.setMinimumSize(QSize(0, 0))
        self.button_add_electronic_shift.setMouseTracking(True)

        self.gridLayout_2.addWidget(self.button_add_electronic_shift, 3, 0, 1, 2)

        self.button_add_optical_pulse = QPushButton(self.frame_7)
        self.button_add_optical_pulse.setObjectName(u"button_add_optical_pulse")
        self.button_add_optical_pulse.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.button_add_optical_pulse, 2, 0, 1, 2)

        self.button_add_electronic_state = QPushButton(self.frame_7)
        self.button_add_electronic_state.setObjectName(u"button_add_electronic_state")
        self.button_add_electronic_state.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.button_add_electronic_state, 0, 0, 1, 2)

        self.input_initial_state = QPushButton(self.frame_7)
        self.input_initial_state.setObjectName(u"input_initial_state")

        self.gridLayout_2.addWidget(self.input_initial_state, 4, 0, 1, 1)

        self.textinput_initial_state = QLineEdit(self.frame_7)
        self.textinput_initial_state.setObjectName(u"textinput_initial_state")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.textinput_initial_state.setFont(font)
        self.textinput_initial_state.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")
        self.textinput_initial_state.setFrame(True)
        self.textinput_initial_state.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.textinput_initial_state, 4, 1, 1, 1)


        self.gridLayout_26.addWidget(self.frame_7, 0, 1, 1, 1)

        self.frame_11 = QFrame(self.tab_system)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_11)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.list_components = QListView(self.frame_11)
        self.list_components.setObjectName(u"list_components")
        self.list_components.setMinimumSize(QSize(0, 40))
        self.list_components.setMaximumSize(QSize(200, 16777215))
        self.list_components.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list_components.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list_components.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list_components.setDefaultDropAction(Qt.IgnoreAction)
        self.list_components.setViewMode(QListView.ListMode)

        self.gridLayout_25.addWidget(self.list_components, 0, 0, 1, 1)


        self.gridLayout_26.addWidget(self.frame_11, 1, 1, 1, 1)

        self.frame_9 = QFrame(self.tab_system)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.slider_state_separator = QSlider(self.frame_9)
        self.slider_state_separator.setObjectName(u"slider_state_separator")
        self.slider_state_separator.setMinimumSize(QSize(0, 40))
        self.slider_state_separator.setMinimum(1)
        self.slider_state_separator.setMaximum(100)
        self.slider_state_separator.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.slider_state_separator)

        self.slider_state_x_seperation = QSlider(self.frame_9)
        self.slider_state_x_seperation.setObjectName(u"slider_state_x_seperation")
        self.slider_state_x_seperation.setMinimumSize(QSize(0, 40))
        self.slider_state_x_seperation.setMinimum(1)
        self.slider_state_x_seperation.setMaximum(100)
        self.slider_state_x_seperation.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.slider_state_x_seperation)

        self.slider_state_grouping = QSlider(self.frame_9)
        self.slider_state_grouping.setObjectName(u"slider_state_grouping")
        self.slider_state_grouping.setMinimumSize(QSize(0, 40))
        self.slider_state_grouping.setMinimum(1)
        self.slider_state_grouping.setMaximum(100)
        self.slider_state_grouping.setValue(50)
        self.slider_state_grouping.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.slider_state_grouping)


        self.gridLayout_26.addWidget(self.frame_9, 2, 0, 1, 1)

        self.frame_8 = QFrame(self.tab_system)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_8)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.button_modify_edit = QPushButton(self.frame_8)
        self.button_modify_edit.setObjectName(u"button_modify_edit")
        self.button_modify_edit.setFlat(False)

        self.gridLayout_23.addWidget(self.button_modify_edit, 0, 0, 1, 1)

        self.button_modify_delete = QPushButton(self.frame_8)
        self.button_modify_delete.setObjectName(u"button_modify_delete")
        self.button_modify_delete.setFlat(False)

        self.gridLayout_23.addWidget(self.button_modify_delete, 1, 0, 1, 1)

        self.button_modify_clear = QPushButton(self.frame_8)
        self.button_modify_clear.setObjectName(u"button_modify_clear")
        self.button_modify_clear.setFlat(False)

        self.gridLayout_23.addWidget(self.button_modify_clear, 2, 0, 1, 1)

        self.input_draw_details = QCheckBox(self.frame_8)
        self.input_draw_details.setObjectName(u"input_draw_details")
        self.input_draw_details.setChecked(False)

        self.gridLayout_23.addWidget(self.input_draw_details, 3, 0, 1, 1)


        self.gridLayout_26.addWidget(self.frame_8, 2, 1, 1, 1)

        self.main_tab_widget.addTab(self.tab_system, "")
        self.tab_environment = QWidget()
        self.tab_environment.setObjectName(u"tab_environment")
        self.gridLayout_22 = QGridLayout(self.tab_environment)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.frame = QFrame(self.tab_environment)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.textinput_rates_radiative_decay = QLineEdit(self.frame)
        self.textinput_rates_radiative_decay.setObjectName(u"textinput_rates_radiative_decay")
        self.textinput_rates_radiative_decay.setMinimumSize(QSize(0, 0))
        self.textinput_rates_radiative_decay.setFont(font)
        self.textinput_rates_radiative_decay.setFrame(True)
        self.textinput_rates_radiative_decay.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_rates_radiative_decay, 3, 1, 1, 1)

        self.textinput_rates_pure_dephasing = QLineEdit(self.frame)
        self.textinput_rates_pure_dephasing.setObjectName(u"textinput_rates_pure_dephasing")
        self.textinput_rates_pure_dephasing.setMinimumSize(QSize(0, 0))
        self.textinput_rates_pure_dephasing.setFont(font)
        self.textinput_rates_pure_dephasing.setFrame(True)
        self.textinput_rates_pure_dephasing.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_rates_pure_dephasing, 4, 1, 1, 1)

        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 0))

        self.gridLayout_3.addWidget(self.label_19, 2, 0, 1, 1)

        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 0))

        self.gridLayout_3.addWidget(self.label_18, 1, 0, 1, 1)

        self.textinput_rates_cavity_loss = QLineEdit(self.frame)
        self.textinput_rates_cavity_loss.setObjectName(u"textinput_rates_cavity_loss")
        self.textinput_rates_cavity_loss.setMinimumSize(QSize(0, 0))
        self.textinput_rates_cavity_loss.setFont(font)
        self.textinput_rates_cavity_loss.setFrame(True)
        self.textinput_rates_cavity_loss.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_rates_cavity_loss, 2, 1, 1, 1)

        self.label_21 = QLabel(self.frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 0))

        self.gridLayout_3.addWidget(self.label_21, 4, 0, 1, 1)

        self.textinput_rates_cavity_coupling = QLineEdit(self.frame)
        self.textinput_rates_cavity_coupling.setObjectName(u"textinput_rates_cavity_coupling")
        self.textinput_rates_cavity_coupling.setMinimumSize(QSize(0, 0))
        self.textinput_rates_cavity_coupling.setFont(font)
        self.textinput_rates_cavity_coupling.setFrame(True)
        self.textinput_rates_cavity_coupling.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_rates_cavity_coupling, 1, 1, 1, 1)

        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 0))

        self.gridLayout_3.addWidget(self.label_20, 3, 0, 1, 1)

        self.label_title_rates = QLabel(self.frame)
        self.label_title_rates.setObjectName(u"label_title_rates")
        self.label_title_rates.setMinimumSize(QSize(0, 0))
        self.label_title_rates.setMaximumSize(QSize(16777215, 40))
        self.label_title_rates.setFrameShape(QFrame.NoFrame)
        self.label_title_rates.setFrameShadow(QFrame.Plain)

        self.gridLayout_3.addWidget(self.label_title_rates, 0, 0, 1, 2)


        self.gridLayout_22.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.tab_environment)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_30 = QLabel(self.frame_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 0))

        self.gridLayout_9.addWidget(self.label_30, 2, 0, 1, 1)

        self.label_22 = QLabel(self.frame_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 0))

        self.gridLayout_9.addWidget(self.label_22, 1, 0, 1, 1)

        self.label_23 = QLabel(self.frame_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 0))

        self.gridLayout_9.addWidget(self.label_23, 3, 0, 1, 1)

        self.input_phonons_approximation = QComboBox(self.frame_2)
        self.input_phonons_approximation.addItem("")
        self.input_phonons_approximation.addItem("")
        self.input_phonons_approximation.addItem("")
        self.input_phonons_approximation.addItem("")
        self.input_phonons_approximation.addItem("")
        self.input_phonons_approximation.setObjectName(u"input_phonons_approximation")
        self.input_phonons_approximation.setMinimumSize(QSize(0, 0))
        self.input_phonons_approximation.setFont(font)
        self.input_phonons_approximation.setFocusPolicy(Qt.WheelFocus)
        self.input_phonons_approximation.setFrame(True)

        self.gridLayout_9.addWidget(self.input_phonons_approximation, 3, 1, 1, 1)

        self.textinput_phonons_sd_ohmamp = QLineEdit(self.frame_2)
        self.textinput_phonons_sd_ohmamp.setObjectName(u"textinput_phonons_sd_ohmamp")
        self.textinput_phonons_sd_ohmamp.setMinimumSize(QSize(0, 0))
        self.textinput_phonons_sd_ohmamp.setFont(font)
        self.textinput_phonons_sd_ohmamp.setFrame(True)
        self.textinput_phonons_sd_ohmamp.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.textinput_phonons_sd_ohmamp, 2, 1, 1, 1)

        self.textinput_phonons_temperature = QLineEdit(self.frame_2)
        self.textinput_phonons_temperature.setObjectName(u"textinput_phonons_temperature")
        self.textinput_phonons_temperature.setMinimumSize(QSize(0, 0))
        self.textinput_phonons_temperature.setFont(font)
        self.textinput_phonons_temperature.setFrame(True)
        self.textinput_phonons_temperature.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.textinput_phonons_temperature, 1, 1, 1, 1)

        self.label_title_phonons = QLabel(self.frame_2)
        self.label_title_phonons.setObjectName(u"label_title_phonons")
        self.label_title_phonons.setMinimumSize(QSize(0, 0))
        self.label_title_phonons.setMaximumSize(QSize(16777215, 40))
        self.label_title_phonons.setFrameShape(QFrame.NoFrame)
        self.label_title_phonons.setFrameShadow(QFrame.Plain)

        self.gridLayout_9.addWidget(self.label_title_phonons, 0, 0, 1, 2)

        self.label_title_phonons_5 = QLabel(self.frame_2)
        self.label_title_phonons_5.setObjectName(u"label_title_phonons_5")
        self.label_title_phonons_5.setMinimumSize(QSize(0, 0))
        self.label_title_phonons_5.setMaximumSize(QSize(16777215, 40))
        self.label_title_phonons_5.setStyleSheet(u"background-color: none;")
        self.label_title_phonons_5.setFrameShape(QFrame.NoFrame)
        self.label_title_phonons_5.setFrameShadow(QFrame.Plain)

        self.gridLayout_9.addWidget(self.label_title_phonons_5, 4, 0, 1, 2)


        self.gridLayout_22.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.tab_environment)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_3)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_title_phonons_2 = QLabel(self.frame_3)
        self.label_title_phonons_2.setObjectName(u"label_title_phonons_2")
        self.label_title_phonons_2.setMinimumSize(QSize(0, 0))
        self.label_title_phonons_2.setMaximumSize(QSize(16777215, 40))
        self.label_title_phonons_2.setFrameShape(QFrame.NoFrame)
        self.label_title_phonons_2.setFrameShadow(QFrame.Plain)

        self.gridLayout_18.addWidget(self.label_title_phonons_2, 0, 0, 1, 2)

        self.label_37 = QLabel(self.frame_3)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(0, 0))

        self.gridLayout_18.addWidget(self.label_37, 1, 0, 1, 1)

        self.textinput_phonons_iterator_stepsize = QLineEdit(self.frame_3)
        self.textinput_phonons_iterator_stepsize.setObjectName(u"textinput_phonons_iterator_stepsize")
        self.textinput_phonons_iterator_stepsize.setMinimumSize(QSize(0, 0))
        self.textinput_phonons_iterator_stepsize.setFont(font)
        self.textinput_phonons_iterator_stepsize.setFrame(True)
        self.textinput_phonons_iterator_stepsize.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.textinput_phonons_iterator_stepsize, 1, 1, 1, 1)

        self.label_27 = QLabel(self.frame_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 0))

        self.gridLayout_18.addWidget(self.label_27, 2, 0, 1, 1)

        self.textinput_phonons_sd_wcutoff = QLineEdit(self.frame_3)
        self.textinput_phonons_sd_wcutoff.setObjectName(u"textinput_phonons_sd_wcutoff")
        self.textinput_phonons_sd_wcutoff.setMinimumSize(QSize(0, 0))
        self.textinput_phonons_sd_wcutoff.setFont(font)
        self.textinput_phonons_sd_wcutoff.setFrame(True)
        self.textinput_phonons_sd_wcutoff.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.textinput_phonons_sd_wcutoff, 2, 1, 1, 1)

        self.label_28 = QLabel(self.frame_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 0))

        self.gridLayout_18.addWidget(self.label_28, 3, 0, 1, 1)

        self.textinput_phonons_sd_wdelta = QLineEdit(self.frame_3)
        self.textinput_phonons_sd_wdelta.setObjectName(u"textinput_phonons_sd_wdelta")
        self.textinput_phonons_sd_wdelta.setMinimumSize(QSize(0, 0))
        self.textinput_phonons_sd_wdelta.setFont(font)
        self.textinput_phonons_sd_wdelta.setFrame(True)
        self.textinput_phonons_sd_wdelta.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.textinput_phonons_sd_wdelta, 3, 1, 1, 1)

        self.label_29 = QLabel(self.frame_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 0))

        self.gridLayout_18.addWidget(self.label_29, 4, 0, 1, 1)

        self.textinput_phonons_sd_tcutoff = QLineEdit(self.frame_3)
        self.textinput_phonons_sd_tcutoff.setObjectName(u"textinput_phonons_sd_tcutoff")
        self.textinput_phonons_sd_tcutoff.setMinimumSize(QSize(0, 0))
        self.textinput_phonons_sd_tcutoff.setFont(font)
        self.textinput_phonons_sd_tcutoff.setFrame(True)
        self.textinput_phonons_sd_tcutoff.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.textinput_phonons_sd_tcutoff, 4, 1, 1, 1)


        self.gridLayout_22.addWidget(self.frame_3, 0, 2, 1, 1)

        self.frame_4 = QFrame(self.tab_environment)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_4)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_26 = QLabel(self.frame_4)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 0))

        self.gridLayout_19.addWidget(self.label_26, 1, 0, 1, 1)

        self.textinput_phonons_sd_alpha = QLineEdit(self.frame_4)
        self.textinput_phonons_sd_alpha.setObjectName(u"textinput_phonons_sd_alpha")
        self.textinput_phonons_sd_alpha.setMinimumSize(QSize(0, 0))
        self.textinput_phonons_sd_alpha.setFont(font)
        self.textinput_phonons_sd_alpha.setFrame(True)
        self.textinput_phonons_sd_alpha.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.textinput_phonons_sd_alpha, 1, 1, 1, 1)

        self.label_title_adjust_rates = QLabel(self.frame_4)
        self.label_title_adjust_rates.setObjectName(u"label_title_adjust_rates")
        self.label_title_adjust_rates.setMinimumSize(QSize(0, 0))

        self.gridLayout_19.addWidget(self.label_title_adjust_rates, 2, 0, 1, 1)

        self.input_phonons_adjust_radiativeloss = QCheckBox(self.frame_4)
        self.input_phonons_adjust_radiativeloss.setObjectName(u"input_phonons_adjust_radiativeloss")
        self.input_phonons_adjust_radiativeloss.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setBold(True)
        self.input_phonons_adjust_radiativeloss.setFont(font1)
        self.input_phonons_adjust_radiativeloss.setChecked(True)

        self.gridLayout_19.addWidget(self.input_phonons_adjust_radiativeloss, 2, 1, 1, 1)

        self.label_title_adjust_rates_2 = QLabel(self.frame_4)
        self.label_title_adjust_rates_2.setObjectName(u"label_title_adjust_rates_2")
        self.label_title_adjust_rates_2.setMinimumSize(QSize(0, 0))

        self.gridLayout_19.addWidget(self.label_title_adjust_rates_2, 3, 0, 1, 1)

        self.input_phonons_adjust_pure_dephasing = QCheckBox(self.frame_4)
        self.input_phonons_adjust_pure_dephasing.setObjectName(u"input_phonons_adjust_pure_dephasing")
        self.input_phonons_adjust_pure_dephasing.setMinimumSize(QSize(0, 0))
        self.input_phonons_adjust_pure_dephasing.setFont(font1)

        self.gridLayout_19.addWidget(self.input_phonons_adjust_pure_dephasing, 3, 1, 1, 1)

        self.label_title_adjust_rates_3 = QLabel(self.frame_4)
        self.label_title_adjust_rates_3.setObjectName(u"label_title_adjust_rates_3")
        self.label_title_adjust_rates_3.setMinimumSize(QSize(0, 0))

        self.gridLayout_19.addWidget(self.label_title_adjust_rates_3, 4, 0, 1, 1)

        self.input_phonons_adjust_renormalization = QCheckBox(self.frame_4)
        self.input_phonons_adjust_renormalization.setObjectName(u"input_phonons_adjust_renormalization")
        self.input_phonons_adjust_renormalization.setMinimumSize(QSize(0, 0))
        self.input_phonons_adjust_renormalization.setFont(font1)
        self.input_phonons_adjust_renormalization.setChecked(True)

        self.gridLayout_19.addWidget(self.input_phonons_adjust_renormalization, 4, 1, 1, 1)

        self.label_title_phonons_3 = QLabel(self.frame_4)
        self.label_title_phonons_3.setObjectName(u"label_title_phonons_3")
        self.label_title_phonons_3.setMinimumSize(QSize(0, 0))
        self.label_title_phonons_3.setMaximumSize(QSize(16777215, 40))
        self.label_title_phonons_3.setFrameShape(QFrame.NoFrame)
        self.label_title_phonons_3.setFrameShadow(QFrame.Plain)

        self.gridLayout_19.addWidget(self.label_title_phonons_3, 0, 0, 1, 2)


        self.gridLayout_22.addWidget(self.frame_4, 0, 3, 1, 1)

        self.frame_5 = QFrame(self.tab_environment)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_5)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_31 = QLabel(self.frame_5)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(0, 0))

        self.gridLayout_20.addWidget(self.label_31, 2, 0, 1, 1)

        self.textinput_phonons_sd_qd_de = QLineEdit(self.frame_5)
        self.textinput_phonons_sd_qd_de.setObjectName(u"textinput_phonons_sd_qd_de")
        self.textinput_phonons_sd_qd_de.setEnabled(False)
        self.textinput_phonons_sd_qd_de.setMinimumSize(QSize(0, 0))
        self.textinput_phonons_sd_qd_de.setFont(font)
        self.textinput_phonons_sd_qd_de.setFrame(True)
        self.textinput_phonons_sd_qd_de.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.textinput_phonons_sd_qd_de, 2, 1, 1, 1)

        self.label_32 = QLabel(self.frame_5)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(0, 0))

        self.gridLayout_20.addWidget(self.label_32, 2, 2, 1, 1)

        self.textinput_phonons_sd_qd_dh = QLineEdit(self.frame_5)
        self.textinput_phonons_sd_qd_dh.setObjectName(u"textinput_phonons_sd_qd_dh")
        self.textinput_phonons_sd_qd_dh.setEnabled(False)
        self.textinput_phonons_sd_qd_dh.setMinimumSize(QSize(0, 0))
        self.textinput_phonons_sd_qd_dh.setFont(font)
        self.textinput_phonons_sd_qd_dh.setFrame(True)
        self.textinput_phonons_sd_qd_dh.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.textinput_phonons_sd_qd_dh, 2, 3, 1, 1)

        self.label_33 = QLabel(self.frame_5)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(0, 0))

        self.gridLayout_20.addWidget(self.label_33, 3, 0, 1, 1)

        self.textinput_phonons_sd_qd_rho = QLineEdit(self.frame_5)
        self.textinput_phonons_sd_qd_rho.setObjectName(u"textinput_phonons_sd_qd_rho")
        self.textinput_phonons_sd_qd_rho.setEnabled(False)
        self.textinput_phonons_sd_qd_rho.setMinimumSize(QSize(0, 0))
        self.textinput_phonons_sd_qd_rho.setFont(font)
        self.textinput_phonons_sd_qd_rho.setFrame(True)
        self.textinput_phonons_sd_qd_rho.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.textinput_phonons_sd_qd_rho, 3, 1, 1, 1)

        self.label_34 = QLabel(self.frame_5)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(0, 0))

        self.gridLayout_20.addWidget(self.label_34, 3, 2, 1, 1)

        self.textinput_phonons_sd_qd_cs = QLineEdit(self.frame_5)
        self.textinput_phonons_sd_qd_cs.setObjectName(u"textinput_phonons_sd_qd_cs")
        self.textinput_phonons_sd_qd_cs.setEnabled(False)
        self.textinput_phonons_sd_qd_cs.setMinimumSize(QSize(0, 0))
        self.textinput_phonons_sd_qd_cs.setFont(font)
        self.textinput_phonons_sd_qd_cs.setFrame(True)
        self.textinput_phonons_sd_qd_cs.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.textinput_phonons_sd_qd_cs, 3, 3, 1, 1)

        self.label_35 = QLabel(self.frame_5)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(0, 0))

        self.gridLayout_20.addWidget(self.label_35, 4, 0, 1, 1)

        self.textinput_phonons_sd_qd_aeah_ratio = QLineEdit(self.frame_5)
        self.textinput_phonons_sd_qd_aeah_ratio.setObjectName(u"textinput_phonons_sd_qd_aeah_ratio")
        self.textinput_phonons_sd_qd_aeah_ratio.setEnabled(False)
        self.textinput_phonons_sd_qd_aeah_ratio.setMinimumSize(QSize(0, 0))
        self.textinput_phonons_sd_qd_aeah_ratio.setFont(font)
        self.textinput_phonons_sd_qd_aeah_ratio.setFrame(True)
        self.textinput_phonons_sd_qd_aeah_ratio.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.textinput_phonons_sd_qd_aeah_ratio, 4, 1, 1, 1)

        self.label_36 = QLabel(self.frame_5)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(0, 0))

        self.gridLayout_20.addWidget(self.label_36, 4, 2, 1, 1)

        self.textinput_phonons_sd_qd_size = QLineEdit(self.frame_5)
        self.textinput_phonons_sd_qd_size.setObjectName(u"textinput_phonons_sd_qd_size")
        self.textinput_phonons_sd_qd_size.setEnabled(False)
        self.textinput_phonons_sd_qd_size.setMinimumSize(QSize(0, 0))
        self.textinput_phonons_sd_qd_size.setFont(font)
        self.textinput_phonons_sd_qd_size.setFrame(True)
        self.textinput_phonons_sd_qd_size.setCursorPosition(4)
        self.textinput_phonons_sd_qd_size.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.textinput_phonons_sd_qd_size, 4, 3, 1, 1)

        self.label_title_phonons_4 = QLabel(self.frame_5)
        self.label_title_phonons_4.setObjectName(u"label_title_phonons_4")
        self.label_title_phonons_4.setMinimumSize(QSize(0, 0))
        self.label_title_phonons_4.setMaximumSize(QSize(16777215, 40))
        self.label_title_phonons_4.setFrameShape(QFrame.NoFrame)
        self.label_title_phonons_4.setFrameShadow(QFrame.Plain)

        self.gridLayout_20.addWidget(self.label_title_phonons_4, 0, 0, 1, 4)

        self.input_phonons_use_qd = QCheckBox(self.frame_5)
        self.input_phonons_use_qd.setObjectName(u"input_phonons_use_qd")
        self.input_phonons_use_qd.setMinimumSize(QSize(0, 0))
        self.input_phonons_use_qd.setFont(font)

        self.gridLayout_20.addWidget(self.input_phonons_use_qd, 1, 0, 1, 4)


        self.gridLayout_22.addWidget(self.frame_5, 1, 0, 1, 2)

        self.frame_6 = QFrame(self.tab_environment)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_6)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_39 = QLabel(self.frame_6)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(0, 0))

        self.gridLayout_21.addWidget(self.label_39, 0, 0, 1, 1)

        self.label_plot_spectral_density = PlotWidget(self.frame_6)
        self.label_plot_spectral_density.setObjectName(u"label_plot_spectral_density")

        self.gridLayout_21.addWidget(self.label_plot_spectral_density, 1, 0, 1, 1)


        self.gridLayout_22.addWidget(self.frame_6, 1, 2, 1, 2)

        self.main_tab_widget.addTab(self.tab_environment, "")
        self.tab_timeline = QWidget()
        self.tab_timeline.setObjectName(u"tab_timeline")
        self.gridLayout_29 = QGridLayout(self.tab_timeline)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.frame_12 = QFrame(self.tab_timeline)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_12)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.button_time_config_grid = QPushButton(self.frame_12)
        self.button_time_config_grid.setObjectName(u"button_time_config_grid")
        self.button_time_config_grid.setMinimumSize(QSize(0, 0))
        self.button_time_config_grid.setFont(font1)

        self.gridLayout_4.addWidget(self.button_time_config_grid, 4, 0, 1, 1)

        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 0))

        self.gridLayout_4.addWidget(self.label_11, 3, 0, 1, 1)

        self.button_time_config_tol = QPushButton(self.frame_12)
        self.button_time_config_tol.setObjectName(u"button_time_config_tol")
        self.button_time_config_tol.setMinimumSize(QSize(0, 0))
        self.button_time_config_tol.setFont(font1)

        self.gridLayout_4.addWidget(self.button_time_config_tol, 5, 0, 1, 1)

        self.label_9 = QLabel(self.frame_12)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 0))

        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)

        self.textinput_time_timestep = QLineEdit(self.frame_12)
        self.textinput_time_timestep.setObjectName(u"textinput_time_timestep")
        self.textinput_time_timestep.setMinimumSize(QSize(0, 0))
        self.textinput_time_timestep.setFont(font)
        self.textinput_time_timestep.setFrame(True)
        self.textinput_time_timestep.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.textinput_time_timestep, 3, 1, 1, 1)

        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 0))

        self.gridLayout_4.addWidget(self.label_10, 2, 0, 1, 1)

        self.textinput_time_endtime = QLineEdit(self.frame_12)
        self.textinput_time_endtime.setObjectName(u"textinput_time_endtime")
        self.textinput_time_endtime.setMinimumSize(QSize(0, 0))
        self.textinput_time_endtime.setFont(font)
        self.textinput_time_endtime.setFrame(True)
        self.textinput_time_endtime.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.textinput_time_endtime, 2, 1, 1, 1)

        self.textinput_time_gridresolution = QLineEdit(self.frame_12)
        self.textinput_time_gridresolution.setObjectName(u"textinput_time_gridresolution")
        self.textinput_time_gridresolution.setMinimumSize(QSize(0, 0))
        self.textinput_time_gridresolution.setFont(font)
        self.textinput_time_gridresolution.setFrame(True)
        self.textinput_time_gridresolution.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.textinput_time_gridresolution, 4, 1, 1, 1)

        self.textinput_time_startingtime = QLineEdit(self.frame_12)
        self.textinput_time_startingtime.setObjectName(u"textinput_time_startingtime")
        self.textinput_time_startingtime.setMinimumSize(QSize(0, 0))
        self.textinput_time_startingtime.setFont(font)
        self.textinput_time_startingtime.setFrame(True)
        self.textinput_time_startingtime.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.textinput_time_startingtime, 1, 1, 1, 1)

        self.textinput_time_tolerance = QLineEdit(self.frame_12)
        self.textinput_time_tolerance.setObjectName(u"textinput_time_tolerance")
        self.textinput_time_tolerance.setMinimumSize(QSize(0, 0))
        self.textinput_time_tolerance.setFont(font)
        self.textinput_time_tolerance.setFrame(True)
        self.textinput_time_tolerance.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.textinput_time_tolerance, 5, 1, 1, 1)

        self.label_title_time = QLabel(self.frame_12)
        self.label_title_time.setObjectName(u"label_title_time")
        self.label_title_time.setMinimumSize(QSize(0, 0))
        self.label_title_time.setMaximumSize(QSize(16777215, 40))
        self.label_title_time.setFrameShape(QFrame.NoFrame)
        self.label_title_time.setFrameShadow(QFrame.Plain)

        self.gridLayout_4.addWidget(self.label_title_time, 0, 0, 1, 2)


        self.gridLayout_29.addWidget(self.frame_12, 0, 0, 1, 1)

        self.frame_13 = QFrame(self.tab_timeline)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_13)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.label_title_solver = QLabel(self.frame_13)
        self.label_title_solver.setObjectName(u"label_title_solver")
        self.label_title_solver.setMinimumSize(QSize(0, 0))
        self.label_title_solver.setMaximumSize(QSize(16777215, 40))
        self.label_title_solver.setFrameShape(QFrame.NoFrame)
        self.label_title_solver.setFrameShadow(QFrame.Plain)

        self.gridLayout_27.addWidget(self.label_title_solver, 0, 0, 1, 2)

        self.label_12 = QLabel(self.frame_13)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 0))

        self.gridLayout_27.addWidget(self.label_12, 1, 0, 1, 1)

        self.input_rungekutta_order = QComboBox(self.frame_13)
        self.input_rungekutta_order.addItem("")
        self.input_rungekutta_order.addItem("")
        self.input_rungekutta_order.addItem("")
        self.input_rungekutta_order.addItem("")
        self.input_rungekutta_order.setObjectName(u"input_rungekutta_order")
        self.input_rungekutta_order.setMinimumSize(QSize(0, 0))
        self.input_rungekutta_order.setFont(font)
        self.input_rungekutta_order.setFocusPolicy(Qt.WheelFocus)

        self.gridLayout_27.addWidget(self.input_rungekutta_order, 1, 1, 1, 1)

        self.label_14 = QLabel(self.frame_13)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 0))

        self.gridLayout_27.addWidget(self.label_14, 2, 0, 1, 1)

        self.input_interpolator_t = QComboBox(self.frame_13)
        self.input_interpolator_t.addItem("")
        self.input_interpolator_t.addItem("")
        self.input_interpolator_t.addItem("")
        self.input_interpolator_t.addItem("")
        self.input_interpolator_t.setObjectName(u"input_interpolator_t")
        self.input_interpolator_t.setMinimumSize(QSize(0, 0))
        self.input_interpolator_t.setFont(font)
        self.input_interpolator_t.setFocusPolicy(Qt.WheelFocus)
        self.input_interpolator_t.setFrame(True)

        self.gridLayout_27.addWidget(self.input_interpolator_t, 2, 1, 1, 1)

        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 0))

        self.gridLayout_27.addWidget(self.label_15, 3, 0, 1, 1)

        self.input_interpolator_tau = QComboBox(self.frame_13)
        self.input_interpolator_tau.addItem("")
        self.input_interpolator_tau.addItem("")
        self.input_interpolator_tau.setObjectName(u"input_interpolator_tau")
        self.input_interpolator_tau.setMinimumSize(QSize(0, 0))
        self.input_interpolator_tau.setFont(font)
        self.input_interpolator_tau.setFocusPolicy(Qt.WheelFocus)
        self.input_interpolator_tau.setFrame(True)

        self.gridLayout_27.addWidget(self.input_interpolator_tau, 3, 1, 1, 1)

        self.label_38 = QLabel(self.frame_13)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(0, 0))

        self.gridLayout_27.addWidget(self.label_38, 4, 0, 1, 1)

        self.textinput_phonons_nc = QLineEdit(self.frame_13)
        self.textinput_phonons_nc.setObjectName(u"textinput_phonons_nc")
        self.textinput_phonons_nc.setMinimumSize(QSize(0, 0))
        self.textinput_phonons_nc.setFont(font)
        self.textinput_phonons_nc.setFrame(True)
        self.textinput_phonons_nc.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.textinput_phonons_nc, 4, 1, 1, 1)

        self.label_41 = QLabel(self.frame_13)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(0, 0))

        self.gridLayout_27.addWidget(self.label_41, 5, 0, 1, 1)

        self.textinput_phonons_tsteppath = QLineEdit(self.frame_13)
        self.textinput_phonons_tsteppath.setObjectName(u"textinput_phonons_tsteppath")
        self.textinput_phonons_tsteppath.setMinimumSize(QSize(0, 0))
        self.textinput_phonons_tsteppath.setFont(font)
        self.textinput_phonons_tsteppath.setFrame(True)
        self.textinput_phonons_tsteppath.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.textinput_phonons_tsteppath, 5, 1, 1, 1)


        self.gridLayout_29.addWidget(self.frame_13, 0, 1, 1, 1)

        self.frame_14 = QFrame(self.tab_timeline)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_14)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_title_predicted_timeline = QLabel(self.frame_14)
        self.label_title_predicted_timeline.setObjectName(u"label_title_predicted_timeline")
        self.label_title_predicted_timeline.setMinimumSize(QSize(0, 0))
        self.label_title_predicted_timeline.setMaximumSize(QSize(16777215, 40))
        self.label_title_predicted_timeline.setFrameShape(QFrame.NoFrame)
        self.label_title_predicted_timeline.setFrameShadow(QFrame.Plain)

        self.gridLayout_28.addWidget(self.label_title_predicted_timeline, 0, 0, 1, 1)

        self.button_timeline_force_calculate_time = QPushButton(self.frame_14)
        self.button_timeline_force_calculate_time.setObjectName(u"button_timeline_force_calculate_time")
        self.button_timeline_force_calculate_time.setMinimumSize(QSize(0, 0))
        self.button_timeline_force_calculate_time.setFont(font1)

        self.gridLayout_28.addWidget(self.button_timeline_force_calculate_time, 0, 1, 1, 1)

        self.label_plot_time_prediction = PlotWidget(self.frame_14)
        self.label_plot_time_prediction.setObjectName(u"label_plot_time_prediction")

        self.gridLayout_28.addWidget(self.label_plot_time_prediction, 1, 0, 1, 2)


        self.gridLayout_29.addWidget(self.frame_14, 1, 0, 1, 2)

        self.main_tab_widget.addTab(self.tab_timeline, "")
        self.tab_statistics = QWidget()
        self.tab_statistics.setObjectName(u"tab_statistics")
        self.gridLayout_17 = QGridLayout(self.tab_statistics)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.statistics_tab_widget = QTabWidget(self.tab_statistics)
        self.statistics_tab_widget.setObjectName(u"statistics_tab_widget")
        self.subtab_spectrum = QWidget()
        self.subtab_spectrum.setObjectName(u"subtab_spectrum")
        self.gridLayout_31 = QGridLayout(self.subtab_spectrum)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.frame_15 = QFrame(self.subtab_spectrum)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_15)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_title_set_spectrum = QLabel(self.frame_15)
        self.label_title_set_spectrum.setObjectName(u"label_title_set_spectrum")
        self.label_title_set_spectrum.setMinimumSize(QSize(0, 0))
        self.label_title_set_spectrum.setMaximumSize(QSize(16777215, 40))
        self.label_title_set_spectrum.setFrameShape(QFrame.NoFrame)
        self.label_title_set_spectrum.setFrameShadow(QFrame.Plain)

        self.gridLayout_15.addWidget(self.label_title_set_spectrum, 0, 0, 1, 3)

        self.button_add_spectrum_mode = QPushButton(self.frame_15)
        self.button_add_spectrum_mode.setObjectName(u"button_add_spectrum_mode")
        self.button_add_spectrum_mode.setMinimumSize(QSize(0, 0))
        self.button_add_spectrum_mode.setFont(font1)

        self.gridLayout_15.addWidget(self.button_add_spectrum_mode, 1, 0, 1, 1)

        self.textinput_spectrum_modes = QLineEdit(self.frame_15)
        self.textinput_spectrum_modes.setObjectName(u"textinput_spectrum_modes")
        self.textinput_spectrum_modes.setMinimumSize(QSize(0, 0))
        self.textinput_spectrum_modes.setFont(font)
        self.textinput_spectrum_modes.setFrame(True)
        self.textinput_spectrum_modes.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.textinput_spectrum_modes, 1, 1, 1, 1)

        self.text_output_list_of_spectra = QListView(self.frame_15)
        self.text_output_list_of_spectra.setObjectName(u"text_output_list_of_spectra")
        self.text_output_list_of_spectra.setMinimumSize(QSize(0, 40))

        self.gridLayout_15.addWidget(self.text_output_list_of_spectra, 1, 2, 7, 1)

        self.label_48 = QLabel(self.frame_15)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(0, 0))

        self.gridLayout_15.addWidget(self.label_48, 2, 0, 1, 1)

        self.textinput_spectrum_range = QLineEdit(self.frame_15)
        self.textinput_spectrum_range.setObjectName(u"textinput_spectrum_range")
        self.textinput_spectrum_range.setMinimumSize(QSize(0, 0))
        self.textinput_spectrum_range.setFont(font)
        self.textinput_spectrum_range.setFrame(True)
        self.textinput_spectrum_range.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.textinput_spectrum_range, 2, 1, 1, 1)

        self.label_47 = QLabel(self.frame_15)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(0, 0))

        self.gridLayout_15.addWidget(self.label_47, 3, 0, 1, 1)

        self.textinput_spectrum_center = QLineEdit(self.frame_15)
        self.textinput_spectrum_center.setObjectName(u"textinput_spectrum_center")
        self.textinput_spectrum_center.setMinimumSize(QSize(0, 0))
        self.textinput_spectrum_center.setFont(font)
        self.textinput_spectrum_center.setFrame(True)
        self.textinput_spectrum_center.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.textinput_spectrum_center, 3, 1, 1, 1)

        self.label_49 = QLabel(self.frame_15)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(0, 0))

        self.gridLayout_15.addWidget(self.label_49, 4, 0, 1, 1)

        self.textinput_spectrum_res = QLineEdit(self.frame_15)
        self.textinput_spectrum_res.setObjectName(u"textinput_spectrum_res")
        self.textinput_spectrum_res.setMinimumSize(QSize(0, 0))
        self.textinput_spectrum_res.setFont(font)
        self.textinput_spectrum_res.setFrame(True)
        self.textinput_spectrum_res.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.textinput_spectrum_res, 4, 1, 1, 1)

        self.label_50 = QLabel(self.frame_15)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(0, 0))

        self.gridLayout_15.addWidget(self.label_50, 5, 0, 1, 1)

        self.input_spectrum_order = QComboBox(self.frame_15)
        self.input_spectrum_order.addItem("")
        self.input_spectrum_order.addItem("")
        self.input_spectrum_order.setObjectName(u"input_spectrum_order")
        self.input_spectrum_order.setMinimumSize(QSize(0, 0))
        self.input_spectrum_order.setFont(font)

        self.gridLayout_15.addWidget(self.input_spectrum_order, 5, 1, 1, 1)

        self.label_51 = QLabel(self.frame_15)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(0, 0))

        self.gridLayout_15.addWidget(self.label_51, 6, 0, 1, 1)

        self.input_spectrum_normalize = QCheckBox(self.frame_15)
        self.input_spectrum_normalize.setObjectName(u"input_spectrum_normalize")
        self.input_spectrum_normalize.setMinimumSize(QSize(0, 0))
        self.input_spectrum_normalize.setFont(font)
        self.input_spectrum_normalize.setChecked(False)

        self.gridLayout_15.addWidget(self.input_spectrum_normalize, 6, 1, 1, 1)

        self.button_add_spectrum_to_output = QPushButton(self.frame_15)
        self.button_add_spectrum_to_output.setObjectName(u"button_add_spectrum_to_output")
        self.button_add_spectrum_to_output.setMinimumSize(QSize(0, 0))
        self.button_add_spectrum_to_output.setFont(font1)

        self.gridLayout_15.addWidget(self.button_add_spectrum_to_output, 7, 0, 1, 1)

        self.button_remove_spectrum_from_output = QPushButton(self.frame_15)
        self.button_remove_spectrum_from_output.setObjectName(u"button_remove_spectrum_from_output")
        self.button_remove_spectrum_from_output.setMinimumSize(QSize(0, 0))
        self.button_remove_spectrum_from_output.setFont(font1)

        self.gridLayout_15.addWidget(self.button_remove_spectrum_from_output, 7, 1, 1, 1)


        self.gridLayout_31.addWidget(self.frame_15, 0, 0, 1, 1)

        self.frame_16 = QFrame(self.subtab_spectrum)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_16)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.label_title_predicted_spectral = QLabel(self.frame_16)
        self.label_title_predicted_spectral.setObjectName(u"label_title_predicted_spectral")
        self.label_title_predicted_spectral.setMinimumSize(QSize(0, 0))
        self.label_title_predicted_spectral.setMaximumSize(QSize(16777215, 40))
        self.label_title_predicted_spectral.setFrameShape(QFrame.NoFrame)
        self.label_title_predicted_spectral.setFrameShadow(QFrame.Plain)

        self.gridLayout_30.addWidget(self.label_title_predicted_spectral, 0, 0, 1, 1)

        self.button_timeline_force_calculate_spectra = QPushButton(self.frame_16)
        self.button_timeline_force_calculate_spectra.setObjectName(u"button_timeline_force_calculate_spectra")
        self.button_timeline_force_calculate_spectra.setMinimumSize(QSize(0, 0))

        self.gridLayout_30.addWidget(self.button_timeline_force_calculate_spectra, 0, 1, 1, 1)

        self.label_plot_spectral_prediction = PlotWidget(self.frame_16)
        self.label_plot_spectral_prediction.setObjectName(u"label_plot_spectral_prediction")

        self.gridLayout_30.addWidget(self.label_plot_spectral_prediction, 1, 0, 1, 2)


        self.gridLayout_31.addWidget(self.frame_16, 1, 0, 1, 1)

        self.statistics_tab_widget.addTab(self.subtab_spectrum, "")
        self.subtab_indist = QWidget()
        self.subtab_indist.setObjectName(u"subtab_indist")
        self.gridLayout_33 = QGridLayout(self.subtab_indist)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.frame_17 = QFrame(self.subtab_indist)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_17)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_title_set_indists = QLabel(self.frame_17)
        self.label_title_set_indists.setObjectName(u"label_title_set_indists")
        self.label_title_set_indists.setMinimumSize(QSize(0, 0))
        self.label_title_set_indists.setFrameShape(QFrame.NoFrame)
        self.label_title_set_indists.setFrameShadow(QFrame.Plain)

        self.gridLayout_16.addWidget(self.label_title_set_indists, 0, 0, 1, 3)

        self.button_add_indist_mode = QPushButton(self.frame_17)
        self.button_add_indist_mode.setObjectName(u"button_add_indist_mode")
        self.button_add_indist_mode.setMinimumSize(QSize(0, 0))
        self.button_add_indist_mode.setFont(font1)

        self.gridLayout_16.addWidget(self.button_add_indist_mode, 1, 0, 1, 1)

        self.textinput_indist_modes = QLineEdit(self.frame_17)
        self.textinput_indist_modes.setObjectName(u"textinput_indist_modes")
        self.textinput_indist_modes.setMinimumSize(QSize(0, 0))
        self.textinput_indist_modes.setFont(font)
        self.textinput_indist_modes.setFrame(True)
        self.textinput_indist_modes.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.textinput_indist_modes, 1, 1, 1, 2)

        self.button_add_indist_to_output = QPushButton(self.frame_17)
        self.button_add_indist_to_output.setObjectName(u"button_add_indist_to_output")
        self.button_add_indist_to_output.setMinimumSize(QSize(0, 0))
        self.button_add_indist_to_output.setFont(font1)

        self.gridLayout_16.addWidget(self.button_add_indist_to_output, 2, 0, 2, 2)

        self.button_remove_indist_from_output = QPushButton(self.frame_17)
        self.button_remove_indist_from_output.setObjectName(u"button_remove_indist_from_output")
        self.button_remove_indist_from_output.setMinimumSize(QSize(0, 0))
        self.button_remove_indist_from_output.setFont(font1)

        self.gridLayout_16.addWidget(self.button_remove_indist_from_output, 3, 2, 1, 1)

        self.text_output_list_of_indists = QListView(self.frame_17)
        self.text_output_list_of_indists.setObjectName(u"text_output_list_of_indists")
        self.text_output_list_of_indists.setMinimumSize(QSize(0, 40))

        self.gridLayout_16.addWidget(self.text_output_list_of_indists, 4, 0, 1, 3)


        self.gridLayout_33.addWidget(self.frame_17, 0, 0, 1, 1)

        self.frame_20 = QFrame(self.subtab_indist)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_18 = QFrame(self.frame_20)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_18)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_title_set_concurrences = QLabel(self.frame_18)
        self.label_title_set_concurrences.setObjectName(u"label_title_set_concurrences")
        self.label_title_set_concurrences.setMinimumSize(QSize(0, 0))
        self.label_title_set_concurrences.setMaximumSize(QSize(16777215, 40))
        self.label_title_set_concurrences.setFrameShape(QFrame.NoFrame)
        self.label_title_set_concurrences.setFrameShadow(QFrame.Plain)

        self.gridLayout_5.addWidget(self.label_title_set_concurrences, 0, 0, 1, 2)

        self.button_add_concurrence_mode_1 = QPushButton(self.frame_18)
        self.button_add_concurrence_mode_1.setObjectName(u"button_add_concurrence_mode_1")
        self.button_add_concurrence_mode_1.setMinimumSize(QSize(0, 0))
        self.button_add_concurrence_mode_1.setFont(font1)

        self.gridLayout_5.addWidget(self.button_add_concurrence_mode_1, 1, 0, 1, 1)

        self.textinput_concurrence_first = QLineEdit(self.frame_18)
        self.textinput_concurrence_first.setObjectName(u"textinput_concurrence_first")
        self.textinput_concurrence_first.setMinimumSize(QSize(0, 0))
        self.textinput_concurrence_first.setFont(font)
        self.textinput_concurrence_first.setFrame(True)
        self.textinput_concurrence_first.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.textinput_concurrence_first, 1, 1, 1, 1)

        self.button_add_concurrence_mode_2 = QPushButton(self.frame_18)
        self.button_add_concurrence_mode_2.setObjectName(u"button_add_concurrence_mode_2")
        self.button_add_concurrence_mode_2.setMinimumSize(QSize(0, 0))
        self.button_add_concurrence_mode_2.setFont(font1)

        self.gridLayout_5.addWidget(self.button_add_concurrence_mode_2, 2, 0, 1, 1)

        self.textinput_concurrence_second = QLineEdit(self.frame_18)
        self.textinput_concurrence_second.setObjectName(u"textinput_concurrence_second")
        self.textinput_concurrence_second.setMinimumSize(QSize(0, 0))
        self.textinput_concurrence_second.setFont(font)
        self.textinput_concurrence_second.setFrame(True)
        self.textinput_concurrence_second.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.textinput_concurrence_second, 2, 1, 1, 1)

        self.button_add_concurrence_to_output = QPushButton(self.frame_18)
        self.button_add_concurrence_to_output.setObjectName(u"button_add_concurrence_to_output")
        self.button_add_concurrence_to_output.setMinimumSize(QSize(0, 0))
        self.button_add_concurrence_to_output.setFont(font1)

        self.gridLayout_5.addWidget(self.button_add_concurrence_to_output, 3, 0, 1, 1)

        self.button_remove_concurrence_from_output = QPushButton(self.frame_18)
        self.button_remove_concurrence_from_output.setObjectName(u"button_remove_concurrence_from_output")
        self.button_remove_concurrence_from_output.setMinimumSize(QSize(0, 0))
        self.button_remove_concurrence_from_output.setFont(font1)

        self.gridLayout_5.addWidget(self.button_remove_concurrence_from_output, 3, 1, 1, 1)

        self.text_output_list_of_concurrences = QListView(self.frame_18)
        self.text_output_list_of_concurrences.setObjectName(u"text_output_list_of_concurrences")
        self.text_output_list_of_concurrences.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.text_output_list_of_concurrences, 4, 0, 1, 2)


        self.verticalLayout.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_20)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.frame_19)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.label_title_set_concurrences_2 = QLabel(self.frame_19)
        self.label_title_set_concurrences_2.setObjectName(u"label_title_set_concurrences_2")
        self.label_title_set_concurrences_2.setMinimumSize(QSize(0, 0))
        self.label_title_set_concurrences_2.setMaximumSize(QSize(16777215, 40))
        self.label_title_set_concurrences_2.setFrameShape(QFrame.NoFrame)
        self.label_title_set_concurrences_2.setFrameShadow(QFrame.Plain)

        self.gridLayout_32.addWidget(self.label_title_set_concurrences_2, 0, 0, 1, 2)

        self.label_113 = QLabel(self.frame_19)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMinimumSize(QSize(0, 0))
        self.label_113.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_32.addWidget(self.label_113, 2, 0, 1, 1)

        self.textinput_concurrence_spec_freq = QLineEdit(self.frame_19)
        self.textinput_concurrence_spec_freq.setObjectName(u"textinput_concurrence_spec_freq")
        self.textinput_concurrence_spec_freq.setEnabled(False)
        self.textinput_concurrence_spec_freq.setMinimumSize(QSize(0, 0))
        self.textinput_concurrence_spec_freq.setFont(font)
        self.textinput_concurrence_spec_freq.setFrame(True)
        self.textinput_concurrence_spec_freq.setAlignment(Qt.AlignCenter)

        self.gridLayout_32.addWidget(self.textinput_concurrence_spec_freq, 2, 1, 1, 1)

        self.label_114 = QLabel(self.frame_19)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setMinimumSize(QSize(0, 0))
        self.label_114.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_32.addWidget(self.label_114, 3, 0, 1, 1)

        self.textinput_concurrence_spec_range = QLineEdit(self.frame_19)
        self.textinput_concurrence_spec_range.setObjectName(u"textinput_concurrence_spec_range")
        self.textinput_concurrence_spec_range.setEnabled(False)
        self.textinput_concurrence_spec_range.setMinimumSize(QSize(0, 0))
        self.textinput_concurrence_spec_range.setFont(font)
        self.textinput_concurrence_spec_range.setFrame(True)
        self.textinput_concurrence_spec_range.setAlignment(Qt.AlignCenter)

        self.gridLayout_32.addWidget(self.textinput_concurrence_spec_range, 3, 1, 1, 1)

        self.label_115 = QLabel(self.frame_19)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setMinimumSize(QSize(0, 0))
        self.label_115.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_32.addWidget(self.label_115, 4, 0, 1, 1)

        self.textinput_concurrence_spec_res = QLineEdit(self.frame_19)
        self.textinput_concurrence_spec_res.setObjectName(u"textinput_concurrence_spec_res")
        self.textinput_concurrence_spec_res.setEnabled(False)
        self.textinput_concurrence_spec_res.setMinimumSize(QSize(0, 0))
        self.textinput_concurrence_spec_res.setFont(font)
        self.textinput_concurrence_spec_res.setFrame(True)
        self.textinput_concurrence_spec_res.setAlignment(Qt.AlignCenter)

        self.gridLayout_32.addWidget(self.textinput_concurrence_spec_res, 4, 1, 1, 1)

        self.input_concurrence_add_spectra = QCheckBox(self.frame_19)
        self.input_concurrence_add_spectra.setObjectName(u"input_concurrence_add_spectra")
        self.input_concurrence_add_spectra.setMinimumSize(QSize(0, 0))
        self.input_concurrence_add_spectra.setFont(font)
        self.input_concurrence_add_spectra.setChecked(False)

        self.gridLayout_32.addWidget(self.input_concurrence_add_spectra, 1, 0, 1, 2)


        self.verticalLayout.addWidget(self.frame_19)


        self.gridLayout_33.addWidget(self.frame_20, 0, 1, 2, 1)

        self.frame_21 = QFrame(self.subtab_indist)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_21)
        self.gridLayout.setObjectName(u"gridLayout")
        self.text_output_list_of_gfuncs = QListView(self.frame_21)
        self.text_output_list_of_gfuncs.setObjectName(u"text_output_list_of_gfuncs")
        self.text_output_list_of_gfuncs.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.text_output_list_of_gfuncs, 1, 2, 4, 1)

        self.button_add_gfunc_mode = QPushButton(self.frame_21)
        self.button_add_gfunc_mode.setObjectName(u"button_add_gfunc_mode")
        self.button_add_gfunc_mode.setMinimumSize(QSize(0, 0))
        self.button_add_gfunc_mode.setFont(font1)

        self.gridLayout.addWidget(self.button_add_gfunc_mode, 1, 0, 1, 1)

        self.button_remove_gfunc_from_output = QPushButton(self.frame_21)
        self.button_remove_gfunc_from_output.setObjectName(u"button_remove_gfunc_from_output")
        self.button_remove_gfunc_from_output.setMinimumSize(QSize(0, 0))
        self.button_remove_gfunc_from_output.setFont(font1)

        self.gridLayout.addWidget(self.button_remove_gfunc_from_output, 4, 1, 1, 1)

        self.label_116 = QLabel(self.frame_21)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setMinimumSize(QSize(0, 0))
        self.label_116.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.label_116, 3, 0, 1, 1)

        self.label_57 = QLabel(self.frame_21)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(0, 0))
        self.label_57.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.label_57, 2, 0, 1, 1)

        self.input_gfunc_integration = QComboBox(self.frame_21)
        self.input_gfunc_integration.addItem("")
        self.input_gfunc_integration.addItem("")
        self.input_gfunc_integration.addItem("")
        self.input_gfunc_integration.setObjectName(u"input_gfunc_integration")
        self.input_gfunc_integration.setMinimumSize(QSize(0, 0))
        self.input_gfunc_integration.setFont(font)

        self.gridLayout.addWidget(self.input_gfunc_integration, 3, 1, 1, 1)

        self.textinput_correlation_modes = QLineEdit(self.frame_21)
        self.textinput_correlation_modes.setObjectName(u"textinput_correlation_modes")
        self.textinput_correlation_modes.setMinimumSize(QSize(0, 0))
        self.textinput_correlation_modes.setFont(font)
        self.textinput_correlation_modes.setFrame(True)
        self.textinput_correlation_modes.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_correlation_modes, 1, 1, 1, 1)

        self.input_gfunc_order = QComboBox(self.frame_21)
        self.input_gfunc_order.addItem("")
        self.input_gfunc_order.addItem("")
        self.input_gfunc_order.setObjectName(u"input_gfunc_order")
        self.input_gfunc_order.setMinimumSize(QSize(0, 0))
        self.input_gfunc_order.setFont(font)

        self.gridLayout.addWidget(self.input_gfunc_order, 2, 1, 1, 1)

        self.button_add_gfunc_to_output = QPushButton(self.frame_21)
        self.button_add_gfunc_to_output.setObjectName(u"button_add_gfunc_to_output")
        self.button_add_gfunc_to_output.setMinimumSize(QSize(0, 0))
        self.button_add_gfunc_to_output.setFont(font1)

        self.gridLayout.addWidget(self.button_add_gfunc_to_output, 4, 0, 1, 1)

        self.label_title_set_g1g2funcs = QLabel(self.frame_21)
        self.label_title_set_g1g2funcs.setObjectName(u"label_title_set_g1g2funcs")
        self.label_title_set_g1g2funcs.setMinimumSize(QSize(0, 0))
        self.label_title_set_g1g2funcs.setMaximumSize(QSize(16777215, 40))
        self.label_title_set_g1g2funcs.setFrameShape(QFrame.NoFrame)
        self.label_title_set_g1g2funcs.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.label_title_set_g1g2funcs, 0, 0, 1, 3)


        self.gridLayout_33.addWidget(self.frame_21, 1, 0, 1, 1)

        self.statistics_tab_widget.addTab(self.subtab_indist, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_35 = QGridLayout(self.tab_5)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.frame_23 = QFrame(self.tab_5)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_23)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_title_set_detector = QLabel(self.frame_23)
        self.label_title_set_detector.setObjectName(u"label_title_set_detector")
        self.label_title_set_detector.setMinimumSize(QSize(0, 0))
        self.label_title_set_detector.setMaximumSize(QSize(16777215, 40))
        self.label_title_set_detector.setFrameShape(QFrame.NoFrame)
        self.label_title_set_detector.setFrameShadow(QFrame.Plain)

        self.gridLayout_8.addWidget(self.label_title_set_detector, 0, 0, 1, 3)

        self.label_117 = QLabel(self.frame_23)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setMinimumSize(QSize(0, 0))
        self.label_117.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_8.addWidget(self.label_117, 1, 0, 1, 1)

        self.textinput_detector_t0 = QLineEdit(self.frame_23)
        self.textinput_detector_t0.setObjectName(u"textinput_detector_t0")
        self.textinput_detector_t0.setMinimumSize(QSize(0, 0))
        self.textinput_detector_t0.setFont(font)
        self.textinput_detector_t0.setFrame(True)
        self.textinput_detector_t0.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.textinput_detector_t0, 1, 1, 1, 1)

        self.text_output_list_of_detector_time = QListView(self.frame_23)
        self.text_output_list_of_detector_time.setObjectName(u"text_output_list_of_detector_time")

        self.gridLayout_8.addWidget(self.text_output_list_of_detector_time, 1, 2, 4, 1)

        self.label_128 = QLabel(self.frame_23)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setMinimumSize(QSize(0, 0))
        self.label_128.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_8.addWidget(self.label_128, 2, 0, 1, 1)

        self.textinput_detector_t1 = QLineEdit(self.frame_23)
        self.textinput_detector_t1.setObjectName(u"textinput_detector_t1")
        self.textinput_detector_t1.setMinimumSize(QSize(0, 0))
        self.textinput_detector_t1.setFont(font)
        self.textinput_detector_t1.setFrame(True)
        self.textinput_detector_t1.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.textinput_detector_t1, 2, 1, 1, 1)

        self.label_118 = QLabel(self.frame_23)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMinimumSize(QSize(0, 0))
        self.label_118.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_8.addWidget(self.label_118, 3, 0, 1, 1)

        self.textinput_detector_tpower = QLineEdit(self.frame_23)
        self.textinput_detector_tpower.setObjectName(u"textinput_detector_tpower")
        self.textinput_detector_tpower.setMinimumSize(QSize(0, 0))
        self.textinput_detector_tpower.setFont(font)
        self.textinput_detector_tpower.setFrame(True)
        self.textinput_detector_tpower.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.textinput_detector_tpower, 3, 1, 1, 1)

        self.button_add_detector_time = QPushButton(self.frame_23)
        self.button_add_detector_time.setObjectName(u"button_add_detector_time")
        self.button_add_detector_time.setMinimumSize(QSize(0, 0))
        self.button_add_detector_time.setFont(font1)

        self.gridLayout_8.addWidget(self.button_add_detector_time, 4, 0, 1, 1)

        self.button_remove_detector_time = QPushButton(self.frame_23)
        self.button_remove_detector_time.setObjectName(u"button_remove_detector_time")
        self.button_remove_detector_time.setMinimumSize(QSize(0, 0))
        self.button_remove_detector_time.setFont(font1)

        self.gridLayout_8.addWidget(self.button_remove_detector_time, 4, 1, 1, 1)


        self.gridLayout_35.addWidget(self.frame_23, 0, 0, 1, 1)

        self.frame_22 = QFrame(self.tab_5)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_22)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_title_set_detector_3 = QLabel(self.frame_22)
        self.label_title_set_detector_3.setObjectName(u"label_title_set_detector_3")
        self.label_title_set_detector_3.setMinimumSize(QSize(0, 0))
        self.label_title_set_detector_3.setMaximumSize(QSize(16777215, 40))
        self.label_title_set_detector_3.setFrameShape(QFrame.NoFrame)
        self.label_title_set_detector_3.setFrameShadow(QFrame.Plain)

        self.gridLayout_7.addWidget(self.label_title_set_detector_3, 0, 0, 1, 3)

        self.button_add_wigner_mode = QPushButton(self.frame_22)
        self.button_add_wigner_mode.setObjectName(u"button_add_wigner_mode")
        self.button_add_wigner_mode.setMinimumSize(QSize(0, 0))
        self.button_add_wigner_mode.setFont(font1)

        self.gridLayout_7.addWidget(self.button_add_wigner_mode, 1, 0, 1, 1)

        self.textinput_wigner_modes = QLineEdit(self.frame_22)
        self.textinput_wigner_modes.setObjectName(u"textinput_wigner_modes")
        self.textinput_wigner_modes.setMinimumSize(QSize(0, 0))
        self.textinput_wigner_modes.setFont(font)
        self.textinput_wigner_modes.setFrame(True)
        self.textinput_wigner_modes.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.textinput_wigner_modes, 1, 1, 1, 1)

        self.text_output_list_of_wigner_funcs = QListView(self.frame_22)
        self.text_output_list_of_wigner_funcs.setObjectName(u"text_output_list_of_wigner_funcs")

        self.gridLayout_7.addWidget(self.text_output_list_of_wigner_funcs, 1, 2, 6, 1)

        self.label_123 = QLabel(self.frame_22)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setMinimumSize(QSize(0, 0))
        self.label_123.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_7.addWidget(self.label_123, 2, 0, 1, 1)

        self.textinput_wigner_x = QLineEdit(self.frame_22)
        self.textinput_wigner_x.setObjectName(u"textinput_wigner_x")
        self.textinput_wigner_x.setMinimumSize(QSize(0, 0))
        self.textinput_wigner_x.setFont(font)
        self.textinput_wigner_x.setFrame(True)
        self.textinput_wigner_x.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.textinput_wigner_x, 2, 1, 1, 1)

        self.label_124 = QLabel(self.frame_22)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setMinimumSize(QSize(0, 0))
        self.label_124.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_7.addWidget(self.label_124, 3, 0, 1, 1)

        self.textinput_wigner_y = QLineEdit(self.frame_22)
        self.textinput_wigner_y.setObjectName(u"textinput_wigner_y")
        self.textinput_wigner_y.setMinimumSize(QSize(0, 0))
        self.textinput_wigner_y.setFont(font)
        self.textinput_wigner_y.setFrame(True)
        self.textinput_wigner_y.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.textinput_wigner_y, 3, 1, 1, 1)

        self.label_125 = QLabel(self.frame_22)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setMinimumSize(QSize(0, 0))
        self.label_125.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_7.addWidget(self.label_125, 4, 0, 1, 1)

        self.textinput_wigner_resolution = QLineEdit(self.frame_22)
        self.textinput_wigner_resolution.setObjectName(u"textinput_wigner_resolution")
        self.textinput_wigner_resolution.setMinimumSize(QSize(0, 0))
        self.textinput_wigner_resolution.setFont(font)
        self.textinput_wigner_resolution.setFrame(True)
        self.textinput_wigner_resolution.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.textinput_wigner_resolution, 4, 1, 1, 1)

        self.label_126 = QLabel(self.frame_22)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setMinimumSize(QSize(0, 0))
        self.label_126.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_7.addWidget(self.label_126, 5, 0, 1, 1)

        self.textinput_wigner_skip = QLineEdit(self.frame_22)
        self.textinput_wigner_skip.setObjectName(u"textinput_wigner_skip")
        self.textinput_wigner_skip.setMinimumSize(QSize(0, 0))
        self.textinput_wigner_skip.setFont(font)
        self.textinput_wigner_skip.setFrame(True)
        self.textinput_wigner_skip.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.textinput_wigner_skip, 5, 1, 1, 1)

        self.button_add_wigner = QPushButton(self.frame_22)
        self.button_add_wigner.setObjectName(u"button_add_wigner")
        self.button_add_wigner.setMinimumSize(QSize(0, 0))
        self.button_add_wigner.setFont(font1)

        self.gridLayout_7.addWidget(self.button_add_wigner, 6, 0, 1, 1)

        self.button_remove_wigner = QPushButton(self.frame_22)
        self.button_remove_wigner.setObjectName(u"button_remove_wigner")
        self.button_remove_wigner.setMinimumSize(QSize(0, 0))
        self.button_remove_wigner.setFont(font1)

        self.gridLayout_7.addWidget(self.button_remove_wigner, 6, 1, 1, 1)


        self.gridLayout_35.addWidget(self.frame_22, 0, 1, 2, 1)

        self.frame_24 = QFrame(self.tab_5)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_34 = QGridLayout(self.frame_24)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.label_title_set_detector_2 = QLabel(self.frame_24)
        self.label_title_set_detector_2.setObjectName(u"label_title_set_detector_2")
        self.label_title_set_detector_2.setMinimumSize(QSize(0, 0))
        self.label_title_set_detector_2.setMaximumSize(QSize(16777215, 40))
        self.label_title_set_detector_2.setFrameShape(QFrame.NoFrame)
        self.label_title_set_detector_2.setFrameShadow(QFrame.Plain)

        self.gridLayout_34.addWidget(self.label_title_set_detector_2, 0, 0, 1, 3)

        self.label_121 = QLabel(self.frame_24)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setMinimumSize(QSize(0, 0))

        self.gridLayout_34.addWidget(self.label_121, 1, 0, 1, 1)

        self.textinput_detector_wcenter = QLineEdit(self.frame_24)
        self.textinput_detector_wcenter.setObjectName(u"textinput_detector_wcenter")
        self.textinput_detector_wcenter.setMinimumSize(QSize(0, 0))
        self.textinput_detector_wcenter.setFont(font)
        self.textinput_detector_wcenter.setFrame(True)
        self.textinput_detector_wcenter.setAlignment(Qt.AlignCenter)

        self.gridLayout_34.addWidget(self.textinput_detector_wcenter, 1, 1, 1, 1)

        self.text_output_list_of_detector_spec = QListView(self.frame_24)
        self.text_output_list_of_detector_spec.setObjectName(u"text_output_list_of_detector_spec")

        self.gridLayout_34.addWidget(self.text_output_list_of_detector_spec, 1, 2, 5, 1)

        self.label_119 = QLabel(self.frame_24)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setMinimumSize(QSize(0, 0))

        self.gridLayout_34.addWidget(self.label_119, 2, 0, 1, 1)

        self.textinput_detector_wrange = QLineEdit(self.frame_24)
        self.textinput_detector_wrange.setObjectName(u"textinput_detector_wrange")
        self.textinput_detector_wrange.setMinimumSize(QSize(0, 0))
        self.textinput_detector_wrange.setFont(font)
        self.textinput_detector_wrange.setFrame(True)
        self.textinput_detector_wrange.setAlignment(Qt.AlignCenter)

        self.gridLayout_34.addWidget(self.textinput_detector_wrange, 2, 1, 1, 1)

        self.label_127 = QLabel(self.frame_24)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setMinimumSize(QSize(0, 0))

        self.gridLayout_34.addWidget(self.label_127, 3, 0, 1, 1)

        self.textinput_detector_wnum = QLineEdit(self.frame_24)
        self.textinput_detector_wnum.setObjectName(u"textinput_detector_wnum")
        self.textinput_detector_wnum.setMinimumSize(QSize(0, 0))
        self.textinput_detector_wnum.setFont(font)
        self.textinput_detector_wnum.setFrame(True)
        self.textinput_detector_wnum.setAlignment(Qt.AlignCenter)

        self.gridLayout_34.addWidget(self.textinput_detector_wnum, 3, 1, 1, 1)

        self.label_120 = QLabel(self.frame_24)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setMinimumSize(QSize(0, 0))

        self.gridLayout_34.addWidget(self.label_120, 4, 0, 1, 1)

        self.textinput_detector_wpower = QLineEdit(self.frame_24)
        self.textinput_detector_wpower.setObjectName(u"textinput_detector_wpower")
        self.textinput_detector_wpower.setMinimumSize(QSize(0, 0))
        self.textinput_detector_wpower.setFont(font)
        self.textinput_detector_wpower.setFrame(True)
        self.textinput_detector_wpower.setAlignment(Qt.AlignCenter)

        self.gridLayout_34.addWidget(self.textinput_detector_wpower, 4, 1, 1, 1)

        self.button_add_detector_spectral = QPushButton(self.frame_24)
        self.button_add_detector_spectral.setObjectName(u"button_add_detector_spectral")
        self.button_add_detector_spectral.setMinimumSize(QSize(0, 0))
        self.button_add_detector_spectral.setFont(font1)

        self.gridLayout_34.addWidget(self.button_add_detector_spectral, 5, 0, 1, 1)

        self.button_remove_detector_spectral = QPushButton(self.frame_24)
        self.button_remove_detector_spectral.setObjectName(u"button_remove_detector_spectral")
        self.button_remove_detector_spectral.setMinimumSize(QSize(0, 0))
        self.button_remove_detector_spectral.setFont(font1)

        self.gridLayout_34.addWidget(self.button_remove_detector_spectral, 5, 1, 1, 1)


        self.gridLayout_35.addWidget(self.frame_24, 1, 0, 1, 1)

        self.statistics_tab_widget.addTab(self.tab_5, "")

        self.gridLayout_17.addWidget(self.statistics_tab_widget, 0, 0, 1, 1)

        self.main_tab_widget.addTab(self.tab_statistics, "")
        self.tab_output = QWidget()
        self.tab_output.setObjectName(u"tab_output")
        self.gridLayout_39 = QGridLayout(self.tab_output)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.frame_26 = QFrame(self.tab_output)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_36 = QGridLayout(self.frame_26)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.label_67 = QLabel(self.frame_26)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(0, 0))
        self.label_67.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_36.addWidget(self.label_67, 0, 0, 1, 2)

        self.label_63 = QLabel(self.frame_26)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(0, 0))
        self.label_63.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_36.addWidget(self.label_63, 1, 0, 1, 1)

        self.input_dm_mode = QComboBox(self.frame_26)
        self.input_dm_mode.addItem("")
        self.input_dm_mode.addItem("")
        self.input_dm_mode.addItem("")
        self.input_dm_mode.setObjectName(u"input_dm_mode")
        self.input_dm_mode.setMinimumSize(QSize(0, 0))
        self.input_dm_mode.setFont(font)
        self.input_dm_mode.setFocusPolicy(Qt.WheelFocus)
        self.input_dm_mode.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-right-radius: 0px; border-bottom-left-radius: 0px;")
        self.input_dm_mode.setFrame(True)

        self.gridLayout_36.addWidget(self.input_dm_mode, 1, 1, 1, 1)

        self.label_64 = QLabel(self.frame_26)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(0, 0))
        self.label_64.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_36.addWidget(self.label_64, 2, 0, 1, 1)

        self.input_dm_frame = QComboBox(self.frame_26)
        self.input_dm_frame.addItem("")
        self.input_dm_frame.addItem("")
        self.input_dm_frame.setObjectName(u"input_dm_frame")
        self.input_dm_frame.setMinimumSize(QSize(0, 0))
        self.input_dm_frame.setFont(font)
        self.input_dm_frame.setFocusPolicy(Qt.WheelFocus)
        self.input_dm_frame.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-top-right-radius: 0px; border-bottom-left-radius: 0px; border-top-width: 0px;")
        self.input_dm_frame.setFrame(True)

        self.gridLayout_36.addWidget(self.input_dm_frame, 2, 1, 1, 1)


        self.gridLayout_39.addWidget(self.frame_26, 0, 0, 1, 1)

        self.frame_25 = QFrame(self.tab_output)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_25)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_61 = QLabel(self.frame_25)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(0, 0))
        self.label_61.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_10.addWidget(self.label_61, 2, 0, 1, 1)

        self.textinput_cpucores = QLineEdit(self.frame_25)
        self.textinput_cpucores.setObjectName(u"textinput_cpucores")
        self.textinput_cpucores.setMinimumSize(QSize(0, 0))
        self.textinput_cpucores.setFont(font)
        self.textinput_cpucores.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")
        self.textinput_cpucores.setFrame(True)
        self.textinput_cpucores.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.textinput_cpucores, 2, 1, 1, 1)

        self.label_62 = QLabel(self.frame_25)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(0, 0))
        self.label_62.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_10.addWidget(self.label_62, 1, 0, 1, 1)

        self.input_logginglevel = QComboBox(self.frame_25)
        self.input_logginglevel.addItem("")
        self.input_logginglevel.addItem("")
        self.input_logginglevel.addItem("")
        self.input_logginglevel.setObjectName(u"input_logginglevel")
        self.input_logginglevel.setMinimumSize(QSize(0, 0))
        self.input_logginglevel.setFont(font)
        self.input_logginglevel.setFocusPolicy(Qt.WheelFocus)
        self.input_logginglevel.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")

        self.gridLayout_10.addWidget(self.input_logginglevel, 1, 1, 1, 1)

        self.label_66 = QLabel(self.frame_25)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(0, 0))
        self.label_66.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_10.addWidget(self.label_66, 0, 0, 1, 2)


        self.gridLayout_39.addWidget(self.frame_25, 0, 1, 1, 1)

        self.frame_27 = QFrame(self.tab_output)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.gridLayout_37 = QGridLayout(self.frame_27)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.label_60 = QLabel(self.frame_27)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(0, 0))

        self.gridLayout_37.addWidget(self.label_60, 0, 0, 1, 4)

        self.input_add_output_eigenvalues = QCheckBox(self.frame_27)
        self.input_add_output_eigenvalues.setObjectName(u"input_add_output_eigenvalues")
        self.input_add_output_eigenvalues.setMinimumSize(QSize(0, 0))
        self.input_add_output_eigenvalues.setFont(font1)
        self.input_add_output_eigenvalues.setChecked(False)

        self.gridLayout_37.addWidget(self.input_add_output_eigenvalues, 1, 0, 1, 1)

        self.input_add_output_operators = QCheckBox(self.frame_27)
        self.input_add_output_operators.setObjectName(u"input_add_output_operators")
        self.input_add_output_operators.setMinimumSize(QSize(0, 0))
        self.input_add_output_operators.setFont(font1)
        self.input_add_output_operators.setChecked(False)

        self.gridLayout_37.addWidget(self.input_add_output_operators, 1, 1, 1, 1)

        self.input_add_output_rkerror = QCheckBox(self.frame_27)
        self.input_add_output_rkerror.setObjectName(u"input_add_output_rkerror")
        self.input_add_output_rkerror.setMinimumSize(QSize(0, 0))
        self.input_add_output_rkerror.setFont(font1)
        self.input_add_output_rkerror.setChecked(False)

        self.gridLayout_37.addWidget(self.input_add_output_rkerror, 1, 2, 1, 1)

        self.input_add_output_vonneumannpath = QCheckBox(self.frame_27)
        self.input_add_output_vonneumannpath.setObjectName(u"input_add_output_vonneumannpath")
        self.input_add_output_vonneumannpath.setMinimumSize(QSize(0, 0))
        self.input_add_output_vonneumannpath.setFont(font1)
        self.input_add_output_vonneumannpath.setChecked(False)

        self.gridLayout_37.addWidget(self.input_add_output_vonneumannpath, 1, 3, 1, 1)

        self.input_add_output_detecotrtrafo = QCheckBox(self.frame_27)
        self.input_add_output_detecotrtrafo.setObjectName(u"input_add_output_detecotrtrafo")
        self.input_add_output_detecotrtrafo.setMinimumSize(QSize(0, 0))
        self.input_add_output_detecotrtrafo.setFont(font1)
        self.input_add_output_detecotrtrafo.setChecked(False)

        self.gridLayout_37.addWidget(self.input_add_output_detecotrtrafo, 2, 0, 1, 1)

        self.input_add_output_chirp_fourier = QCheckBox(self.frame_27)
        self.input_add_output_chirp_fourier.setObjectName(u"input_add_output_chirp_fourier")
        self.input_add_output_chirp_fourier.setMinimumSize(QSize(0, 0))
        self.input_add_output_chirp_fourier.setFont(font1)
        self.input_add_output_chirp_fourier.setChecked(False)

        self.gridLayout_37.addWidget(self.input_add_output_chirp_fourier, 2, 1, 1, 1)

        self.input_add_output_pulse_fourier = QCheckBox(self.frame_27)
        self.input_add_output_pulse_fourier.setObjectName(u"input_add_output_pulse_fourier")
        self.input_add_output_pulse_fourier.setMinimumSize(QSize(0, 0))
        self.input_add_output_pulse_fourier.setFont(font1)
        self.input_add_output_pulse_fourier.setChecked(False)

        self.gridLayout_37.addWidget(self.input_add_output_pulse_fourier, 2, 2, 1, 1)

        self.input_add_output_phononj = QCheckBox(self.frame_27)
        self.input_add_output_phononj.setObjectName(u"input_add_output_phononj")
        self.input_add_output_phononj.setMinimumSize(QSize(0, 0))
        self.input_add_output_phononj.setFont(font1)
        self.input_add_output_phononj.setChecked(False)

        self.gridLayout_37.addWidget(self.input_add_output_phononj, 2, 3, 1, 1)

        self.input_add_output_greenf = QCheckBox(self.frame_27)
        self.input_add_output_greenf.setObjectName(u"input_add_output_greenf")
        self.input_add_output_greenf.setMinimumSize(QSize(0, 0))
        self.input_add_output_greenf.setFont(font1)
        self.input_add_output_greenf.setChecked(False)

        self.gridLayout_37.addWidget(self.input_add_output_greenf, 3, 0, 1, 1)

        self.input_add_output_phononcoeffs = QCheckBox(self.frame_27)
        self.input_add_output_phononcoeffs.setObjectName(u"input_add_output_phononcoeffs")
        self.input_add_output_phononcoeffs.setMinimumSize(QSize(0, 0))
        self.input_add_output_phononcoeffs.setFont(font1)
        self.input_add_output_phononcoeffs.setChecked(False)

        self.gridLayout_37.addWidget(self.input_add_output_phononcoeffs, 3, 1, 1, 1)

        self.input_add_output_tpm = QCheckBox(self.frame_27)
        self.input_add_output_tpm.setObjectName(u"input_add_output_tpm")
        self.input_add_output_tpm.setMinimumSize(QSize(0, 0))
        self.input_add_output_tpm.setFont(font1)
        self.input_add_output_tpm.setChecked(False)

        self.gridLayout_37.addWidget(self.input_add_output_tpm, 3, 2, 1, 1)

        self.input_add_output_concurrence_eigs = QCheckBox(self.frame_27)
        self.input_add_output_concurrence_eigs.setObjectName(u"input_add_output_concurrence_eigs")
        self.input_add_output_concurrence_eigs.setMinimumSize(QSize(0, 0))
        self.input_add_output_concurrence_eigs.setFont(font1)
        self.input_add_output_concurrence_eigs.setChecked(False)

        self.gridLayout_37.addWidget(self.input_add_output_concurrence_eigs, 3, 3, 1, 1)

        self.input_add_output_photon_expv = QCheckBox(self.frame_27)
        self.input_add_output_photon_expv.setObjectName(u"input_add_output_photon_expv")
        self.input_add_output_photon_expv.setMinimumSize(QSize(0, 0))
        self.input_add_output_photon_expv.setFont(font1)
        self.input_add_output_photon_expv.setChecked(False)

        self.gridLayout_37.addWidget(self.input_add_output_photon_expv, 4, 0, 1, 1)


        self.gridLayout_39.addWidget(self.frame_27, 1, 0, 1, 2)

        self.frame_28 = QFrame(self.tab_output)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout_38 = QGridLayout(self.frame_28)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.label_65 = QLabel(self.frame_28)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(0, 0))
        self.label_65.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_38.addWidget(self.label_65, 0, 0, 1, 2)

        self.button_add_custom_expval_matrix = QPushButton(self.frame_28)
        self.button_add_custom_expval_matrix.setObjectName(u"button_add_custom_expval_matrix")
        self.button_add_custom_expval_matrix.setMinimumSize(QSize(0, 0))
        self.button_add_custom_expval_matrix.setFont(font1)

        self.gridLayout_38.addWidget(self.button_add_custom_expval_matrix, 1, 0, 1, 1)

        self.text_output_list_of_custom_expvals = QListView(self.frame_28)
        self.text_output_list_of_custom_expvals.setObjectName(u"text_output_list_of_custom_expvals")

        self.gridLayout_38.addWidget(self.text_output_list_of_custom_expvals, 1, 1, 2, 1)

        self.button_remove_custom_expval_matrix = QPushButton(self.frame_28)
        self.button_remove_custom_expval_matrix.setObjectName(u"button_remove_custom_expval_matrix")
        self.button_remove_custom_expval_matrix.setMinimumSize(QSize(0, 0))
        self.button_remove_custom_expval_matrix.setFont(font1)

        self.gridLayout_38.addWidget(self.button_remove_custom_expval_matrix, 2, 0, 1, 1)


        self.gridLayout_39.addWidget(self.frame_28, 2, 0, 1, 2)

        self.main_tab_widget.addTab(self.tab_output, "")
        self.tab_generate = QWidget()
        self.tab_generate.setObjectName(u"tab_generate")
        self.gridLayout_56 = QGridLayout(self.tab_generate)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.frame_29 = QFrame(self.tab_generate)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_29)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.text_output_program_main = TextBrowserExternal(self.frame_29)
        self.text_output_program_main.setObjectName(u"text_output_program_main")
        self.text_output_program_main.setFrameShape(QFrame.NoFrame)
        self.text_output_program_main.setLineWrapMode(QTextEdit.NoWrap)
        self.text_output_program_main.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.text_output_program_main.setOpenExternalLinks(True)
        self.text_output_program_main.setOpenLinks(True)

        self.gridLayout_12.addWidget(self.text_output_program_main, 0, 0, 1, 1)


        self.gridLayout_56.addWidget(self.frame_29, 0, 0, 1, 1)

        self.frame_35 = QFrame(self.tab_generate)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.gridLayout_44 = QGridLayout(self.frame_35)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.text_output_program_qdacc_command = QTextBrowser(self.frame_35)
        self.text_output_program_qdacc_command.setObjectName(u"text_output_program_qdacc_command")
        self.text_output_program_qdacc_command.setMinimumSize(QSize(500, 0))
        self.text_output_program_qdacc_command.setFrameShape(QFrame.NoFrame)
        self.text_output_program_qdacc_command.setReadOnly(False)

        self.gridLayout_44.addWidget(self.text_output_program_qdacc_command, 0, 0, 1, 1)


        self.gridLayout_56.addWidget(self.frame_35, 0, 1, 1, 1)

        self.frame_30 = QFrame(self.tab_generate)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.gridLayout_40 = QGridLayout(self.frame_30)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.button_generate_run = QPushButton(self.frame_30)
        self.button_generate_run.setObjectName(u"button_generate_run")
        self.button_generate_run.setEnabled(True)
        self.button_generate_run.setMinimumSize(QSize(0, 0))
        self.button_generate_run.setFont(font1)
        self.button_generate_run.setStyleSheet(u"QPushButton {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #f4771e, stop:0.91 #4f2609); color: #ffffff;}\n"
"QPushButton::hover {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #f7954f, stop:0.91 #4f2609); color: #ffffff;}")
        self.button_generate_run.setCheckable(False)
        self.button_generate_run.setChecked(False)

        self.gridLayout_40.addWidget(self.button_generate_run, 0, 0, 1, 1)

        self.button_run_and_plot = QPushButton(self.frame_30)
        self.button_run_and_plot.setObjectName(u"button_run_and_plot")
        self.button_run_and_plot.setEnabled(True)
        self.button_run_and_plot.setMinimumSize(QSize(0, 0))
        self.button_run_and_plot.setFont(font1)
        self.button_run_and_plot.setStyleSheet(u"QPushButton {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #1e6cf4, stop:0.91 #133e8d); color: #ffffff;}\n"
"QPushButton::hover {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #5d94f5, stop:0.91 #133e8d); color: #ffffff;}")
        self.button_run_and_plot.setCheckable(False)
        self.button_run_and_plot.setChecked(False)

        self.gridLayout_40.addWidget(self.button_run_and_plot, 1, 1, 1, 1)

        self.button_run_program = QPushButton(self.frame_30)
        self.button_run_program.setObjectName(u"button_run_program")
        self.button_run_program.setEnabled(True)
        self.button_run_program.setMinimumSize(QSize(0, 0))
        self.button_run_program.setFont(font1)
        self.button_run_program.setStyleSheet(u"QPushButton {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #288c14, stop:0.91 #0d3006); color: #ffffff;}\n"
"QPushButton::hover {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #55ba41, stop:0.91 #0d3006); color: #ffffff;}")
        self.button_run_program.setIconSize(QSize(32, 32))
        self.button_run_program.setCheckable(False)
        self.button_run_program.setChecked(False)

        self.gridLayout_40.addWidget(self.button_run_program, 1, 0, 1, 1)

        self.input_plot_mode = QComboBox(self.frame_30)
        self.input_plot_mode.addItem("")
        self.input_plot_mode.addItem("")
        self.input_plot_mode.addItem("")
        self.input_plot_mode.setObjectName(u"input_plot_mode")
        self.input_plot_mode.setMinimumSize(QSize(0, 0))
        self.input_plot_mode.setStyleSheet(u"QComboBox {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #3f1d5c, stop:0.91 #1c0d29); color: #ffffff;}\n"
"QComboBox::hover {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #582980, stop:0.91 #1c0d29); color: #ffffff;}")
        self.input_plot_mode.setFrame(False)

        self.gridLayout_40.addWidget(self.input_plot_mode, 3, 1, 1, 1)

        self.button_run_external = QPushButton(self.frame_30)
        self.button_run_external.setObjectName(u"button_run_external")
        self.button_run_external.setEnabled(True)
        self.button_run_external.setMinimumSize(QSize(0, 0))
        self.button_run_external.setFont(font1)
        self.button_run_external.setStyleSheet(u"QPushButton {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #888888, stop:0.91 black); color: #aaaaaa;}")
        self.button_run_external.setCheckable(False)
        self.button_run_external.setChecked(False)

        self.gridLayout_40.addWidget(self.button_run_external, 2, 1, 1, 1)

        self.button_run_kill = QPushButton(self.frame_30)
        self.button_run_kill.setObjectName(u"button_run_kill")
        self.button_run_kill.setEnabled(True)
        self.button_run_kill.setMinimumSize(QSize(0, 0))
        self.button_run_kill.setFont(font1)
        self.button_run_kill.setStyleSheet(u"QPushButton {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #f4331e, stop:0.91 #450f0a); color: #ffffff;}\n"
"QPushButton::hover {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #a62214, stop:0.91 #450f0a); color: #ffffff;}")
        self.button_run_kill.setCheckable(False)
        self.button_run_kill.setChecked(False)

        self.gridLayout_40.addWidget(self.button_run_kill, 2, 0, 1, 1)

        self.button_generate_copy = QPushButton(self.frame_30)
        self.button_generate_copy.setObjectName(u"button_generate_copy")
        self.button_generate_copy.setEnabled(True)
        self.button_generate_copy.setMinimumSize(QSize(0, 0))
        self.button_generate_copy.setFont(font1)
        self.button_generate_copy.setStyleSheet(u"QPushButton {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #f4771e, stop:0.91 #4f2609); color: #ffffff;}\n"
"QPushButton::hover {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #f7954f, stop:0.91 #4f2609); color: #ffffff;}")
        self.button_generate_copy.setCheckable(False)
        self.button_generate_copy.setChecked(False)

        self.gridLayout_40.addWidget(self.button_generate_copy, 0, 1, 1, 1)

        self.button_plot_everything = QPushButton(self.frame_30)
        self.button_plot_everything.setObjectName(u"button_plot_everything")
        self.button_plot_everything.setMinimumSize(QSize(0, 0))
        self.button_plot_everything.setStyleSheet(u"QPushButton {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #3f1d5c, stop:0.91 #1c0d29); color: #ffffff;}\n"
"QPushButton::hover {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #582980, stop:0.91 #1c0d29); color: #ffffff;}")
        self.button_plot_everything.setIconSize(QSize(32, 32))

        self.gridLayout_40.addWidget(self.button_plot_everything, 3, 0, 1, 1)


        self.gridLayout_56.addWidget(self.frame_30, 1, 1, 1, 1)

        self.frame_34 = QFrame(self.tab_generate)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_31 = QFrame(self.frame_34)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.gridLayout_41 = QGridLayout(self.frame_31)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.input_path_to_qdacc = QPushButton(self.frame_31)
        self.input_path_to_qdacc.setObjectName(u"input_path_to_qdacc")
        self.input_path_to_qdacc.setMinimumSize(QSize(0, 0))

        self.gridLayout_41.addWidget(self.input_path_to_qdacc, 0, 0, 1, 1)

        self.textinput_file_qdacc = QLineEdit(self.frame_31)
        self.textinput_file_qdacc.setObjectName(u"textinput_file_qdacc")
        self.textinput_file_qdacc.setMinimumSize(QSize(0, 0))
        self.textinput_file_qdacc.setFont(font)
        self.textinput_file_qdacc.setFrame(True)
        self.textinput_file_qdacc.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_41.addWidget(self.textinput_file_qdacc, 0, 1, 1, 1)

        self.input_destination = QPushButton(self.frame_31)
        self.input_destination.setObjectName(u"input_destination")
        self.input_destination.setMinimumSize(QSize(0, 0))

        self.gridLayout_41.addWidget(self.input_destination, 1, 0, 1, 1)

        self.textinput_file_destination = QLineEdit(self.frame_31)
        self.textinput_file_destination.setObjectName(u"textinput_file_destination")
        self.textinput_file_destination.setMinimumSize(QSize(0, 0))
        self.textinput_file_destination.setFont(font)
        self.textinput_file_destination.setFrame(True)
        self.textinput_file_destination.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_41.addWidget(self.textinput_file_destination, 1, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_34)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_42 = QGridLayout(self.frame_32)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.button_open_destination_folder = QPushButton(self.frame_32)
        self.button_open_destination_folder.setObjectName(u"button_open_destination_folder")
        self.button_open_destination_folder.setMinimumSize(QSize(0, 0))

        self.gridLayout_42.addWidget(self.button_open_destination_folder, 0, 0, 1, 1)

        self.button_empty_destination_folder = QPushButton(self.frame_32)
        self.button_empty_destination_folder.setObjectName(u"button_empty_destination_folder")
        self.button_empty_destination_folder.setMinimumSize(QSize(0, 0))

        self.gridLayout_42.addWidget(self.button_empty_destination_folder, 1, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_34)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_43 = QGridLayout(self.frame_33)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.button_change_rungstring_to_settingfile = QPushButton(self.frame_33)
        self.button_change_rungstring_to_settingfile.setObjectName(u"button_change_rungstring_to_settingfile")
        self.button_change_rungstring_to_settingfile.setMinimumSize(QSize(0, 0))

        self.gridLayout_43.addWidget(self.button_change_rungstring_to_settingfile, 0, 0, 1, 1)

        self.input_escape_output_command = QCheckBox(self.frame_33)
        self.input_escape_output_command.setObjectName(u"input_escape_output_command")
        self.input_escape_output_command.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.input_escape_output_command.setFont(font2)
        self.input_escape_output_command.setChecked(False)

        self.gridLayout_43.addWidget(self.input_escape_output_command, 1, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_33)


        self.gridLayout_56.addWidget(self.frame_34, 3, 0, 1, 2)

        self.frame_46 = QFrame(self.tab_generate)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.gridLayout_45 = QGridLayout(self.frame_46)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.label_68 = QLabel(self.frame_46)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMinimumSize(QSize(0, 0))
        self.label_68.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_45.addWidget(self.label_68, 0, 0, 1, 1)

        self.label_69 = QLabel(self.frame_46)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMinimumSize(QSize(0, 0))
        self.label_69.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_45.addWidget(self.label_69, 0, 1, 1, 1)

        self.label_70 = QLabel(self.frame_46)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMinimumSize(QSize(0, 0))
        self.label_70.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_45.addWidget(self.label_70, 0, 2, 1, 1)

        self.progressBar = ProgressBar(self.frame_46)
        self.progressBar.setObjectName(u"progressBar")

        self.gridLayout_45.addWidget(self.progressBar, 1, 0, 1, 1)

        self.progressBarCPU = ProgressBar(self.frame_46)
        self.progressBarCPU.setObjectName(u"progressBarCPU")

        self.gridLayout_45.addWidget(self.progressBarCPU, 1, 1, 1, 1)

        self.progressBarRAM = ProgressBar(self.frame_46)
        self.progressBarRAM.setObjectName(u"progressBarRAM")

        self.gridLayout_45.addWidget(self.progressBarRAM, 1, 2, 1, 1)


        self.gridLayout_56.addWidget(self.frame_46, 1, 0, 2, 1)

        self.main_tab_widget.addTab(self.tab_generate, "")
        self.tab_scanner = QWidget()
        self.tab_scanner.setObjectName(u"tab_scanner")
        self.gridLayout_51 = QGridLayout(self.tab_scanner)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.frame_36 = QFrame(self.tab_scanner)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_36)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_title_qdsystem_2 = QLabel(self.frame_36)
        self.label_title_qdsystem_2.setObjectName(u"label_title_qdsystem_2")
        self.label_title_qdsystem_2.setMinimumSize(QSize(0, 0))
        self.label_title_qdsystem_2.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_2.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_2.setFrameShadow(QFrame.Plain)

        self.gridLayout_6.addWidget(self.label_title_qdsystem_2, 0, 0, 1, 1)

        self.checkbox_activate_scan_parameter_1 = QCheckBox(self.frame_36)
        self.checkbox_activate_scan_parameter_1.setObjectName(u"checkbox_activate_scan_parameter_1")
        self.checkbox_activate_scan_parameter_1.setMinimumSize(QSize(0, 0))

        self.gridLayout_6.addWidget(self.checkbox_activate_scan_parameter_1, 0, 1, 1, 1)

        self.label_title_qdsystem_4 = QLabel(self.frame_36)
        self.label_title_qdsystem_4.setObjectName(u"label_title_qdsystem_4")
        self.label_title_qdsystem_4.setMinimumSize(QSize(0, 0))
        self.label_title_qdsystem_4.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_4.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_4.setFrameShadow(QFrame.Plain)

        self.gridLayout_6.addWidget(self.label_title_qdsystem_4, 1, 0, 1, 1)

        self.textinput_scan_parameter_1_from = QLineEdit(self.frame_36)
        self.textinput_scan_parameter_1_from.setObjectName(u"textinput_scan_parameter_1_from")
        self.textinput_scan_parameter_1_from.setMinimumSize(QSize(0, 0))

        self.gridLayout_6.addWidget(self.textinput_scan_parameter_1_from, 1, 1, 1, 1)

        self.label_title_qdsystem_5 = QLabel(self.frame_36)
        self.label_title_qdsystem_5.setObjectName(u"label_title_qdsystem_5")
        self.label_title_qdsystem_5.setMinimumSize(QSize(0, 0))
        self.label_title_qdsystem_5.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_5.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_5.setFrameShadow(QFrame.Plain)

        self.gridLayout_6.addWidget(self.label_title_qdsystem_5, 2, 0, 1, 1)

        self.textinput_scan_parameter_1_to = QLineEdit(self.frame_36)
        self.textinput_scan_parameter_1_to.setObjectName(u"textinput_scan_parameter_1_to")
        self.textinput_scan_parameter_1_to.setMinimumSize(QSize(0, 0))

        self.gridLayout_6.addWidget(self.textinput_scan_parameter_1_to, 2, 1, 1, 1)

        self.label_title_qdsystem_12 = QLabel(self.frame_36)
        self.label_title_qdsystem_12.setObjectName(u"label_title_qdsystem_12")
        self.label_title_qdsystem_12.setMinimumSize(QSize(0, 0))
        self.label_title_qdsystem_12.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_12.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_12.setFrameShadow(QFrame.Plain)

        self.gridLayout_6.addWidget(self.label_title_qdsystem_12, 3, 0, 1, 1)

        self.textinput_scan_parameter_1_points = QLineEdit(self.frame_36)
        self.textinput_scan_parameter_1_points.setObjectName(u"textinput_scan_parameter_1_points")
        self.textinput_scan_parameter_1_points.setMinimumSize(QSize(0, 0))

        self.gridLayout_6.addWidget(self.textinput_scan_parameter_1_points, 3, 1, 1, 1)

        self.combobox_p1_input = QComboBox(self.frame_36)
        self.combobox_p1_input.addItem("")
        self.combobox_p1_input.addItem("")
        self.combobox_p1_input.addItem("")
        self.combobox_p1_input.addItem("")
        self.combobox_p1_input.addItem("")
        self.combobox_p1_input.setObjectName(u"combobox_p1_input")
        self.combobox_p1_input.setMinimumSize(QSize(0, 0))

        self.gridLayout_6.addWidget(self.combobox_p1_input, 4, 0, 1, 1)

        self.textinput_scan_parameter_1_lambda = QLineEdit(self.frame_36)
        self.textinput_scan_parameter_1_lambda.setObjectName(u"textinput_scan_parameter_1_lambda")
        self.textinput_scan_parameter_1_lambda.setMinimumSize(QSize(0, 0))

        self.gridLayout_6.addWidget(self.textinput_scan_parameter_1_lambda, 4, 1, 1, 1)


        self.gridLayout_51.addWidget(self.frame_36, 0, 2, 2, 1)

        self.frame_37 = QFrame(self.tab_scanner)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.gridLayout_46 = QGridLayout(self.frame_37)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.label_title_qdsystem_8 = QLabel(self.frame_37)
        self.label_title_qdsystem_8.setObjectName(u"label_title_qdsystem_8")
        self.label_title_qdsystem_8.setMinimumSize(QSize(0, 0))
        self.label_title_qdsystem_8.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_8.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_8.setFrameShadow(QFrame.Plain)

        self.gridLayout_46.addWidget(self.label_title_qdsystem_8, 0, 0, 1, 1)

        self.checkbox_activate_scan_parameter_2 = QCheckBox(self.frame_37)
        self.checkbox_activate_scan_parameter_2.setObjectName(u"checkbox_activate_scan_parameter_2")
        self.checkbox_activate_scan_parameter_2.setMinimumSize(QSize(0, 0))

        self.gridLayout_46.addWidget(self.checkbox_activate_scan_parameter_2, 0, 1, 1, 1)

        self.label_title_qdsystem_9 = QLabel(self.frame_37)
        self.label_title_qdsystem_9.setObjectName(u"label_title_qdsystem_9")
        self.label_title_qdsystem_9.setMinimumSize(QSize(0, 0))
        self.label_title_qdsystem_9.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_9.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_9.setFrameShadow(QFrame.Plain)

        self.gridLayout_46.addWidget(self.label_title_qdsystem_9, 1, 0, 1, 1)

        self.textinput_scan_parameter_2_from = QLineEdit(self.frame_37)
        self.textinput_scan_parameter_2_from.setObjectName(u"textinput_scan_parameter_2_from")
        self.textinput_scan_parameter_2_from.setMinimumSize(QSize(0, 0))

        self.gridLayout_46.addWidget(self.textinput_scan_parameter_2_from, 1, 1, 1, 1)

        self.label_title_qdsystem_10 = QLabel(self.frame_37)
        self.label_title_qdsystem_10.setObjectName(u"label_title_qdsystem_10")
        self.label_title_qdsystem_10.setMinimumSize(QSize(0, 0))
        self.label_title_qdsystem_10.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_10.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_10.setFrameShadow(QFrame.Plain)

        self.gridLayout_46.addWidget(self.label_title_qdsystem_10, 2, 0, 1, 1)

        self.textinput_scan_parameter_2_to = QLineEdit(self.frame_37)
        self.textinput_scan_parameter_2_to.setObjectName(u"textinput_scan_parameter_2_to")
        self.textinput_scan_parameter_2_to.setMinimumSize(QSize(0, 0))
        self.textinput_scan_parameter_2_to.setStyleSheet(u"b")

        self.gridLayout_46.addWidget(self.textinput_scan_parameter_2_to, 2, 1, 1, 1)

        self.label_title_qdsystem_13 = QLabel(self.frame_37)
        self.label_title_qdsystem_13.setObjectName(u"label_title_qdsystem_13")
        self.label_title_qdsystem_13.setMinimumSize(QSize(0, 0))
        self.label_title_qdsystem_13.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_13.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_13.setFrameShadow(QFrame.Plain)

        self.gridLayout_46.addWidget(self.label_title_qdsystem_13, 3, 0, 1, 1)

        self.textinput_scan_parameter_2_points = QLineEdit(self.frame_37)
        self.textinput_scan_parameter_2_points.setObjectName(u"textinput_scan_parameter_2_points")
        self.textinput_scan_parameter_2_points.setMinimumSize(QSize(0, 0))
        self.textinput_scan_parameter_2_points.setStyleSheet(u"b")

        self.gridLayout_46.addWidget(self.textinput_scan_parameter_2_points, 3, 1, 1, 1)

        self.combobox_p2_input = QComboBox(self.frame_37)
        self.combobox_p2_input.addItem("")
        self.combobox_p2_input.addItem("")
        self.combobox_p2_input.addItem("")
        self.combobox_p2_input.addItem("")
        self.combobox_p2_input.addItem("")
        self.combobox_p2_input.setObjectName(u"combobox_p2_input")
        self.combobox_p2_input.setMinimumSize(QSize(0, 0))

        self.gridLayout_46.addWidget(self.combobox_p2_input, 4, 0, 1, 1)

        self.textinput_scan_parameter_2_lambda = QLineEdit(self.frame_37)
        self.textinput_scan_parameter_2_lambda.setObjectName(u"textinput_scan_parameter_2_lambda")
        self.textinput_scan_parameter_2_lambda.setMinimumSize(QSize(0, 0))
        self.textinput_scan_parameter_2_lambda.setStyleSheet(u"b")

        self.gridLayout_46.addWidget(self.textinput_scan_parameter_2_lambda, 4, 1, 1, 1)


        self.gridLayout_51.addWidget(self.frame_37, 2, 2, 1, 1)

        self.frame_41 = QFrame(self.tab_scanner)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.gridLayout_50 = QGridLayout(self.frame_41)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.label_3 = QLabel(self.frame_41)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))

        self.gridLayout_50.addWidget(self.label_3, 0, 0, 1, 1)


        self.gridLayout_51.addWidget(self.frame_41, 3, 0, 2, 2)

        self.frame_40 = QFrame(self.tab_scanner)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.gridLayout_49 = QGridLayout(self.frame_40)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.plot_sweep_parameter_first = PlotWidget(self.frame_40)
        self.plot_sweep_parameter_first.setObjectName(u"plot_sweep_parameter_first")
        self.plot_sweep_parameter_first.setMinimumSize(QSize(400, 150))

        self.gridLayout_49.addWidget(self.plot_sweep_parameter_first, 0, 0, 1, 1)

        self.plot_sweep_parameter_second = PlotWidget(self.frame_40)
        self.plot_sweep_parameter_second.setObjectName(u"plot_sweep_parameter_second")
        self.plot_sweep_parameter_second.setMinimumSize(QSize(400, 150))

        self.gridLayout_49.addWidget(self.plot_sweep_parameter_second, 0, 1, 1, 1)


        self.gridLayout_51.addWidget(self.frame_40, 3, 2, 2, 1)

        self.frame_39 = QFrame(self.tab_scanner)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.gridLayout_48 = QGridLayout(self.frame_39)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.text_output_program_qdacc_command_sweep_display = QTextBrowser(self.frame_39)
        self.text_output_program_qdacc_command_sweep_display.setObjectName(u"text_output_program_qdacc_command_sweep_display")
        self.text_output_program_qdacc_command_sweep_display.setMinimumSize(QSize(0, 150))
        self.text_output_program_qdacc_command_sweep_display.setFrameShape(QFrame.NoFrame)
        self.text_output_program_qdacc_command_sweep_display.setLineWrapMode(QTextEdit.NoWrap)
        self.text_output_program_qdacc_command_sweep_display.setReadOnly(True)

        self.gridLayout_48.addWidget(self.text_output_program_qdacc_command_sweep_display, 0, 0, 1, 2)

        self.button_set_setting_file_path = QPushButton(self.frame_39)
        self.button_set_setting_file_path.setObjectName(u"button_set_setting_file_path")
        self.button_set_setting_file_path.setMinimumSize(QSize(0, 0))

        self.gridLayout_48.addWidget(self.button_set_setting_file_path, 1, 0, 1, 1)

        self.textinput_path_to_settingfile = QLineEdit(self.frame_39)
        self.textinput_path_to_settingfile.setObjectName(u"textinput_path_to_settingfile")
        self.textinput_path_to_settingfile.setMinimumSize(QSize(0, 0))
        self.textinput_path_to_settingfile.setFont(font)
        self.textinput_path_to_settingfile.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")
        self.textinput_path_to_settingfile.setFrame(True)
        self.textinput_path_to_settingfile.setAlignment(Qt.AlignCenter)

        self.gridLayout_48.addWidget(self.textinput_path_to_settingfile, 1, 1, 1, 1)


        self.gridLayout_51.addWidget(self.frame_39, 2, 0, 1, 2)

        self.frame_38 = QFrame(self.tab_scanner)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.gridLayout_47 = QGridLayout(self.frame_38)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.label_title_qdsystem_3 = QLabel(self.frame_38)
        self.label_title_qdsystem_3.setObjectName(u"label_title_qdsystem_3")
        self.label_title_qdsystem_3.setMinimumSize(QSize(0, 0))
        self.label_title_qdsystem_3.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_3.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_3.setFrameShadow(QFrame.Plain)

        self.gridLayout_47.addWidget(self.label_title_qdsystem_3, 0, 0, 1, 1)

        self.button_sweeper_plot = QPushButton(self.frame_38)
        self.button_sweeper_plot.setObjectName(u"button_sweeper_plot")
        self.button_sweeper_plot.setMinimumSize(QSize(0, 0))
        self.button_sweeper_plot.setStyleSheet(u"QPushButton {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #f4771e, stop:0.91 #4f2609); color: #ffffff;}\n"
"QPushButton::hover {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #f7954f, stop:0.91 #4f2609); color: #ffffff;}")

        self.gridLayout_47.addWidget(self.button_sweeper_plot, 3, 0, 1, 1)

        self.button_sweeper_get_runstring = QPushButton(self.frame_38)
        self.button_sweeper_get_runstring.setObjectName(u"button_sweeper_get_runstring")
        self.button_sweeper_get_runstring.setMinimumSize(QSize(0, 0))

        self.gridLayout_47.addWidget(self.button_sweeper_get_runstring, 3, 1, 1, 1)

        self.text_output_program_qdacc_command_sweep = QTextBrowser(self.frame_38)
        self.text_output_program_qdacc_command_sweep.setObjectName(u"text_output_program_qdacc_command_sweep")
        self.text_output_program_qdacc_command_sweep.setMinimumSize(QSize(0, 150))
        self.text_output_program_qdacc_command_sweep.setFrameShape(QFrame.NoFrame)
        self.text_output_program_qdacc_command_sweep.setReadOnly(False)

        self.gridLayout_47.addWidget(self.text_output_program_qdacc_command_sweep, 1, 0, 2, 2)


        self.gridLayout_51.addWidget(self.frame_38, 0, 0, 2, 2)

        self.main_tab_widget.addTab(self.tab_scanner, "")
        self.tab_optimizer = QWidget()
        self.tab_optimizer.setObjectName(u"tab_optimizer")
        self.gridLayout_55 = QGridLayout(self.tab_optimizer)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.frame_42 = QFrame(self.tab_optimizer)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_42)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.text_output_program_qdacc_command_sweep_2 = QTextBrowser(self.frame_42)
        self.text_output_program_qdacc_command_sweep_2.setObjectName(u"text_output_program_qdacc_command_sweep_2")
        self.text_output_program_qdacc_command_sweep_2.setFrameShape(QFrame.NoFrame)
        self.text_output_program_qdacc_command_sweep_2.setReadOnly(False)

        self.gridLayout_11.addWidget(self.text_output_program_qdacc_command_sweep_2, 0, 0, 1, 1)

        self.button_optimizer_get_runstring = QPushButton(self.frame_42)
        self.button_optimizer_get_runstring.setObjectName(u"button_optimizer_get_runstring")
        self.button_optimizer_get_runstring.setMinimumSize(QSize(0, 0))

        self.gridLayout_11.addWidget(self.button_optimizer_get_runstring, 1, 0, 1, 1)

        self.button_optimizer_optimize = QPushButton(self.frame_42)
        self.button_optimizer_optimize.setObjectName(u"button_optimizer_optimize")
        self.button_optimizer_optimize.setMinimumSize(QSize(0, 0))
        self.button_optimizer_optimize.setStyleSheet(u"QPushButton {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #288c14, stop:0.91 #0d3006); color: #ffffff;}\n"
"QPushButton::hover {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #55ba41, stop:0.91 #0d3006); color: #ffffff;}")

        self.gridLayout_11.addWidget(self.button_optimizer_optimize, 2, 0, 1, 1)

        self.button_optimizer_runstring_to_main = QPushButton(self.frame_42)
        self.button_optimizer_runstring_to_main.setObjectName(u"button_optimizer_runstring_to_main")
        self.button_optimizer_runstring_to_main.setMinimumSize(QSize(0, 0))

        self.gridLayout_11.addWidget(self.button_optimizer_runstring_to_main, 3, 0, 1, 1)


        self.gridLayout_55.addWidget(self.frame_42, 0, 0, 2, 1)

        self.frame_44 = QFrame(self.tab_optimizer)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.gridLayout_53 = QGridLayout(self.frame_44)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.text_output_program_qdacc_command_sweep_display_2 = QTextBrowser(self.frame_44)
        self.text_output_program_qdacc_command_sweep_display_2.setObjectName(u"text_output_program_qdacc_command_sweep_display_2")
        self.text_output_program_qdacc_command_sweep_display_2.setFrameShape(QFrame.NoFrame)
        self.text_output_program_qdacc_command_sweep_display_2.setLineWrapMode(QTextEdit.NoWrap)
        self.text_output_program_qdacc_command_sweep_display_2.setReadOnly(True)

        self.gridLayout_53.addWidget(self.text_output_program_qdacc_command_sweep_display_2, 0, 0, 1, 1)


        self.gridLayout_55.addWidget(self.frame_44, 0, 1, 1, 1)

        self.frame_43 = QFrame(self.tab_optimizer)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.gridLayout_52 = QGridLayout(self.frame_43)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.button_optimizer_files = QPushButton(self.frame_43)
        self.button_optimizer_files.setObjectName(u"button_optimizer_files")
        self.button_optimizer_files.setMinimumSize(QSize(0, 0))

        self.gridLayout_52.addWidget(self.button_optimizer_files, 0, 0, 1, 1)

        self.textinput_optimizer_files = QLineEdit(self.frame_43)
        self.textinput_optimizer_files.setObjectName(u"textinput_optimizer_files")
        self.textinput_optimizer_files.setMinimumSize(QSize(0, 0))

        self.gridLayout_52.addWidget(self.textinput_optimizer_files, 0, 1, 1, 1)

        self.button_optimizer_files_2 = QPushButton(self.frame_43)
        self.button_optimizer_files_2.setObjectName(u"button_optimizer_files_2")
        self.button_optimizer_files_2.setMinimumSize(QSize(0, 0))

        self.gridLayout_52.addWidget(self.button_optimizer_files_2, 1, 0, 1, 1)

        self.textinput_optimizer_file_indices = QLineEdit(self.frame_43)
        self.textinput_optimizer_file_indices.setObjectName(u"textinput_optimizer_file_indices")
        self.textinput_optimizer_file_indices.setMinimumSize(QSize(0, 0))

        self.gridLayout_52.addWidget(self.textinput_optimizer_file_indices, 1, 1, 1, 1)

        self.label_title_qdsystem_16 = QLabel(self.frame_43)
        self.label_title_qdsystem_16.setObjectName(u"label_title_qdsystem_16")
        self.label_title_qdsystem_16.setMinimumSize(QSize(0, 0))
        self.label_title_qdsystem_16.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_16.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_16.setFrameShadow(QFrame.Plain)

        self.gridLayout_52.addWidget(self.label_title_qdsystem_16, 2, 0, 1, 1)

        self.textinput_optimizer_legend = QLineEdit(self.frame_43)
        self.textinput_optimizer_legend.setObjectName(u"textinput_optimizer_legend")
        self.textinput_optimizer_legend.setMinimumSize(QSize(0, 0))

        self.gridLayout_52.addWidget(self.textinput_optimizer_legend, 2, 1, 1, 1)

        self.label_title_qdsystem_14 = QLabel(self.frame_43)
        self.label_title_qdsystem_14.setObjectName(u"label_title_qdsystem_14")
        self.label_title_qdsystem_14.setMinimumSize(QSize(0, 0))
        self.label_title_qdsystem_14.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_14.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_14.setFrameShadow(QFrame.Plain)

        self.gridLayout_52.addWidget(self.label_title_qdsystem_14, 3, 0, 1, 1)

        self.textinput_optimizer_initial_parameters = QLineEdit(self.frame_43)
        self.textinput_optimizer_initial_parameters.setObjectName(u"textinput_optimizer_initial_parameters")
        self.textinput_optimizer_initial_parameters.setMinimumSize(QSize(0, 0))

        self.gridLayout_52.addWidget(self.textinput_optimizer_initial_parameters, 3, 1, 1, 1)

        self.label_title_qdsystem_6 = QLabel(self.frame_43)
        self.label_title_qdsystem_6.setObjectName(u"label_title_qdsystem_6")
        self.label_title_qdsystem_6.setMinimumSize(QSize(0, 0))
        self.label_title_qdsystem_6.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_6.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_6.setFrameShadow(QFrame.Plain)

        self.gridLayout_52.addWidget(self.label_title_qdsystem_6, 4, 0, 1, 1)

        self.textinput_optimizer_parameter_bounds = QLineEdit(self.frame_43)
        self.textinput_optimizer_parameter_bounds.setObjectName(u"textinput_optimizer_parameter_bounds")
        self.textinput_optimizer_parameter_bounds.setMinimumSize(QSize(0, 0))

        self.gridLayout_52.addWidget(self.textinput_optimizer_parameter_bounds, 4, 1, 1, 1)

        self.label_title_qdsystem_17 = QLabel(self.frame_43)
        self.label_title_qdsystem_17.setObjectName(u"label_title_qdsystem_17")
        self.label_title_qdsystem_17.setMinimumSize(QSize(0, 0))
        self.label_title_qdsystem_17.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_17.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_17.setFrameShadow(QFrame.Plain)

        self.gridLayout_52.addWidget(self.label_title_qdsystem_17, 5, 0, 1, 1)

        self.textinput_optimizer_parameter_names = QLineEdit(self.frame_43)
        self.textinput_optimizer_parameter_names.setObjectName(u"textinput_optimizer_parameter_names")
        self.textinput_optimizer_parameter_names.setMinimumSize(QSize(0, 0))

        self.gridLayout_52.addWidget(self.textinput_optimizer_parameter_names, 5, 1, 1, 1)

        self.button_optimizer_fitness_function = QPushButton(self.frame_43)
        self.button_optimizer_fitness_function.setObjectName(u"button_optimizer_fitness_function")
        self.button_optimizer_fitness_function.setMinimumSize(QSize(0, 0))

        self.gridLayout_52.addWidget(self.button_optimizer_fitness_function, 6, 0, 1, 1)

        self.textinput_optimizer_fitnessfunction = QLineEdit(self.frame_43)
        self.textinput_optimizer_fitnessfunction.setObjectName(u"textinput_optimizer_fitnessfunction")
        self.textinput_optimizer_fitnessfunction.setMinimumSize(QSize(0, 0))

        self.gridLayout_52.addWidget(self.textinput_optimizer_fitnessfunction, 6, 1, 1, 1)

        self.label_title_qdsystem_19 = QLabel(self.frame_43)
        self.label_title_qdsystem_19.setObjectName(u"label_title_qdsystem_19")
        self.label_title_qdsystem_19.setMinimumSize(QSize(0, 0))
        self.label_title_qdsystem_19.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_19.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_19.setFrameShadow(QFrame.Plain)

        self.gridLayout_52.addWidget(self.label_title_qdsystem_19, 7, 0, 1, 1)

        self.textinput_optimizer_formatfunction = QLineEdit(self.frame_43)
        self.textinput_optimizer_formatfunction.setObjectName(u"textinput_optimizer_formatfunction")
        self.textinput_optimizer_formatfunction.setMinimumSize(QSize(0, 0))

        self.gridLayout_52.addWidget(self.textinput_optimizer_formatfunction, 7, 1, 1, 1)

        self.label_title_qdsystem_20 = QLabel(self.frame_43)
        self.label_title_qdsystem_20.setObjectName(u"label_title_qdsystem_20")
        self.label_title_qdsystem_20.setMinimumSize(QSize(0, 0))
        self.label_title_qdsystem_20.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_20.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_20.setFrameShadow(QFrame.Plain)

        self.gridLayout_52.addWidget(self.label_title_qdsystem_20, 8, 0, 1, 1)

        self.textinput_optimizer_tol = QLineEdit(self.frame_43)
        self.textinput_optimizer_tol.setObjectName(u"textinput_optimizer_tol")
        self.textinput_optimizer_tol.setMinimumSize(QSize(0, 0))

        self.gridLayout_52.addWidget(self.textinput_optimizer_tol, 8, 1, 1, 1)

        self.label_title_qdsystem_21 = QLabel(self.frame_43)
        self.label_title_qdsystem_21.setObjectName(u"label_title_qdsystem_21")
        self.label_title_qdsystem_21.setMinimumSize(QSize(0, 0))
        self.label_title_qdsystem_21.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_21.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_21.setFrameShadow(QFrame.Plain)

        self.gridLayout_52.addWidget(self.label_title_qdsystem_21, 9, 0, 1, 1)

        self.textinput_optimizer_eps = QLineEdit(self.frame_43)
        self.textinput_optimizer_eps.setObjectName(u"textinput_optimizer_eps")
        self.textinput_optimizer_eps.setMinimumSize(QSize(0, 0))

        self.gridLayout_52.addWidget(self.textinput_optimizer_eps, 9, 1, 1, 1)

        self.label_title_qdsystem_22 = QLabel(self.frame_43)
        self.label_title_qdsystem_22.setObjectName(u"label_title_qdsystem_22")
        self.label_title_qdsystem_22.setMinimumSize(QSize(0, 0))
        self.label_title_qdsystem_22.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_22.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_22.setFrameShadow(QFrame.Plain)

        self.gridLayout_52.addWidget(self.label_title_qdsystem_22, 10, 0, 1, 1)

        self.textinput_optimizer_maxit = QLineEdit(self.frame_43)
        self.textinput_optimizer_maxit.setObjectName(u"textinput_optimizer_maxit")
        self.textinput_optimizer_maxit.setMinimumSize(QSize(0, 0))

        self.gridLayout_52.addWidget(self.textinput_optimizer_maxit, 10, 1, 1, 1)

        self.label_title_qdsystem_23 = QLabel(self.frame_43)
        self.label_title_qdsystem_23.setObjectName(u"label_title_qdsystem_23")
        self.label_title_qdsystem_23.setMinimumSize(QSize(0, 0))
        self.label_title_qdsystem_23.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_23.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_23.setFrameShadow(QFrame.Plain)

        self.gridLayout_52.addWidget(self.label_title_qdsystem_23, 11, 0, 1, 1)

        self.textinput_optimizer_maxit_2 = QLineEdit(self.frame_43)
        self.textinput_optimizer_maxit_2.setObjectName(u"textinput_optimizer_maxit_2")
        self.textinput_optimizer_maxit_2.setMinimumSize(QSize(0, 0))

        self.gridLayout_52.addWidget(self.textinput_optimizer_maxit_2, 11, 1, 1, 1)

        self.optimizer_call_plotscript = QCheckBox(self.frame_43)
        self.optimizer_call_plotscript.setObjectName(u"optimizer_call_plotscript")
        self.optimizer_call_plotscript.setMinimumSize(QSize(0, 0))

        self.gridLayout_52.addWidget(self.optimizer_call_plotscript, 12, 0, 1, 2)


        self.gridLayout_55.addWidget(self.frame_43, 1, 1, 2, 1)

        self.frame_45 = QFrame(self.tab_optimizer)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.gridLayout_54 = QGridLayout(self.frame_45)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.label_plot_optimizer_1 = PlotWidget(self.frame_45)
        self.label_plot_optimizer_1.setObjectName(u"label_plot_optimizer_1")
        self.label_plot_optimizer_1.setMinimumSize(QSize(300, 0))
        self.label_plot_optimizer_1.setStyleSheet(u"background-color: b")

        self.gridLayout_54.addWidget(self.label_plot_optimizer_1, 0, 0, 2, 1)

        self.label_plot_optimizer_2 = PlotWidget(self.frame_45)
        self.label_plot_optimizer_2.setObjectName(u"label_plot_optimizer_2")
        self.label_plot_optimizer_2.setMinimumSize(QSize(300, 150))
        self.label_plot_optimizer_2.setStyleSheet(u"background-color: b")

        self.gridLayout_54.addWidget(self.label_plot_optimizer_2, 0, 1, 1, 1)

        self.label_plot_optimizer_3 = PlotWidget(self.frame_45)
        self.label_plot_optimizer_3.setObjectName(u"label_plot_optimizer_3")
        self.label_plot_optimizer_3.setMinimumSize(QSize(300, 150))
        self.label_plot_optimizer_3.setStyleSheet(u"background-color: b")

        self.gridLayout_54.addWidget(self.label_plot_optimizer_3, 1, 1, 1, 1)


        self.gridLayout_55.addWidget(self.frame_45, 2, 0, 1, 1)

        self.main_tab_widget.addTab(self.tab_optimizer, "")
        self.tab_howto = QWidget()
        self.tab_howto.setObjectName(u"tab_howto")
        self.gridLayout_13 = QGridLayout(self.tab_howto)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.output_howto = QTextBrowser(self.tab_howto)
        self.output_howto.setObjectName(u"output_howto")
        self.output_howto.setOpenLinks(False)

        self.gridLayout_13.addWidget(self.output_howto, 0, 0, 1, 1)

        self.main_tab_widget.addTab(self.tab_howto, "")

        self.gridLayout_14.addWidget(self.main_tab_widget, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1425, 22))
        self.menu_main = QMenu(self.menubar)
        self.menu_main.setObjectName(u"menu_main")
        self.menu_main.setGeometry(QRect(269, 131, 135, 59))
        self.menu_functions = QMenu(self.menubar)
        self.menu_functions.setObjectName(u"menu_functions")
        self.menu_developer_tools = QMenu(self.menubar)
        self.menu_developer_tools.setObjectName(u"menu_developer_tools")
        self.menu_tools = QMenu(self.menubar)
        self.menu_tools.setObjectName(u"menu_tools")
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.textinput_optimizer_files, self.textinput_optimizer_file_indices)
        QWidget.setTabOrder(self.textinput_optimizer_file_indices, self.textinput_optimizer_legend)
        QWidget.setTabOrder(self.textinput_optimizer_legend, self.textinput_optimizer_initial_parameters)
        QWidget.setTabOrder(self.textinput_optimizer_initial_parameters, self.textinput_optimizer_parameter_bounds)
        QWidget.setTabOrder(self.textinput_optimizer_parameter_bounds, self.textinput_optimizer_parameter_names)
        QWidget.setTabOrder(self.textinput_optimizer_parameter_names, self.textinput_optimizer_fitnessfunction)
        QWidget.setTabOrder(self.textinput_optimizer_fitnessfunction, self.textinput_optimizer_formatfunction)
        QWidget.setTabOrder(self.textinput_optimizer_formatfunction, self.textinput_optimizer_tol)
        QWidget.setTabOrder(self.textinput_optimizer_tol, self.textinput_optimizer_eps)
        QWidget.setTabOrder(self.textinput_optimizer_eps, self.textinput_optimizer_maxit)
        QWidget.setTabOrder(self.textinput_optimizer_maxit, self.text_output_program_qdacc_command_sweep_display_2)
        QWidget.setTabOrder(self.text_output_program_qdacc_command_sweep_display_2, self.text_output_program_qdacc_command_sweep_2)
        QWidget.setTabOrder(self.text_output_program_qdacc_command_sweep_2, self.button_optimizer_optimize)
        QWidget.setTabOrder(self.button_optimizer_optimize, self.button_optimizer_runstring_to_main)
        QWidget.setTabOrder(self.button_optimizer_runstring_to_main, self.button_optimizer_get_runstring)
        QWidget.setTabOrder(self.button_optimizer_get_runstring, self.textinput_phonons_sd_wcutoff)
        QWidget.setTabOrder(self.textinput_phonons_sd_wcutoff, self.textinput_phonons_sd_wdelta)
        QWidget.setTabOrder(self.textinput_phonons_sd_wdelta, self.textinput_phonons_sd_tcutoff)
        QWidget.setTabOrder(self.textinput_phonons_sd_tcutoff, self.textinput_phonons_sd_alpha)
        QWidget.setTabOrder(self.textinput_phonons_sd_alpha, self.input_phonons_use_qd)
        QWidget.setTabOrder(self.input_phonons_use_qd, self.textinput_phonons_sd_qd_de)
        QWidget.setTabOrder(self.textinput_phonons_sd_qd_de, self.textinput_phonons_sd_qd_rho)
        QWidget.setTabOrder(self.textinput_phonons_sd_qd_rho, self.textinput_phonons_sd_qd_aeah_ratio)
        QWidget.setTabOrder(self.textinput_phonons_sd_qd_aeah_ratio, self.textinput_phonons_sd_qd_dh)
        QWidget.setTabOrder(self.textinput_phonons_sd_qd_dh, self.textinput_phonons_sd_qd_cs)
        QWidget.setTabOrder(self.textinput_phonons_sd_qd_cs, self.textinput_phonons_sd_qd_size)
        QWidget.setTabOrder(self.textinput_phonons_sd_qd_size, self.button_add_electronic_state)
        QWidget.setTabOrder(self.button_add_electronic_state, self.text_output_program_qdacc_command)
        QWidget.setTabOrder(self.text_output_program_qdacc_command, self.text_output_program_main)
        QWidget.setTabOrder(self.text_output_program_main, self.slider_state_separator)
        QWidget.setTabOrder(self.slider_state_separator, self.slider_state_grouping)
        QWidget.setTabOrder(self.slider_state_grouping, self.input_initial_state)
        QWidget.setTabOrder(self.input_initial_state, self.input_phonons_adjust_radiativeloss)
        QWidget.setTabOrder(self.input_phonons_adjust_radiativeloss, self.input_phonons_adjust_pure_dephasing)
        QWidget.setTabOrder(self.input_phonons_adjust_pure_dephasing, self.input_phonons_adjust_renormalization)
        QWidget.setTabOrder(self.input_phonons_adjust_renormalization, self.input_interpolator_t)
        QWidget.setTabOrder(self.input_interpolator_t, self.textinput_time_tolerance)
        QWidget.setTabOrder(self.textinput_time_tolerance, self.textinput_phonons_nc)
        QWidget.setTabOrder(self.textinput_phonons_nc, self.button_time_config_grid)
        QWidget.setTabOrder(self.button_time_config_grid, self.textinput_time_timestep)
        QWidget.setTabOrder(self.textinput_time_timestep, self.button_time_config_tol)
        QWidget.setTabOrder(self.button_time_config_tol, self.textinput_time_endtime)
        QWidget.setTabOrder(self.textinput_time_endtime, self.input_interpolator_tau)
        QWidget.setTabOrder(self.input_interpolator_tau, self.textinput_time_startingtime)
        QWidget.setTabOrder(self.textinput_time_startingtime, self.textinput_phonons_tsteppath)
        QWidget.setTabOrder(self.textinput_phonons_tsteppath, self.textinput_time_gridresolution)
        QWidget.setTabOrder(self.textinput_time_gridresolution, self.input_rungekutta_order)
        QWidget.setTabOrder(self.input_rungekutta_order, self.text_output_list_of_custom_expvals)
        QWidget.setTabOrder(self.text_output_list_of_custom_expvals, self.input_logginglevel)
        QWidget.setTabOrder(self.input_logginglevel, self.input_dm_frame)
        QWidget.setTabOrder(self.input_dm_frame, self.input_add_output_greenf)
        QWidget.setTabOrder(self.input_add_output_greenf, self.input_add_output_rkerror)
        QWidget.setTabOrder(self.input_add_output_rkerror, self.input_add_output_phononcoeffs)
        QWidget.setTabOrder(self.input_add_output_phononcoeffs, self.input_add_output_phononj)
        QWidget.setTabOrder(self.input_add_output_phononj, self.button_add_custom_expval_matrix)
        QWidget.setTabOrder(self.button_add_custom_expval_matrix, self.input_add_output_detecotrtrafo)
        QWidget.setTabOrder(self.input_add_output_detecotrtrafo, self.input_add_output_chirp_fourier)
        QWidget.setTabOrder(self.input_add_output_chirp_fourier, self.input_add_output_eigenvalues)
        QWidget.setTabOrder(self.input_add_output_eigenvalues, self.input_add_output_tpm)
        QWidget.setTabOrder(self.input_add_output_tpm, self.input_add_output_operators)
        QWidget.setTabOrder(self.input_add_output_operators, self.textinput_cpucores)
        QWidget.setTabOrder(self.textinput_cpucores, self.button_remove_custom_expval_matrix)
        QWidget.setTabOrder(self.button_remove_custom_expval_matrix, self.input_add_output_pulse_fourier)
        QWidget.setTabOrder(self.input_add_output_pulse_fourier, self.input_add_output_concurrence_eigs)
        QWidget.setTabOrder(self.input_add_output_concurrence_eigs, self.input_add_output_vonneumannpath)
        QWidget.setTabOrder(self.input_add_output_vonneumannpath, self.input_dm_mode)
        QWidget.setTabOrder(self.input_dm_mode, self.input_add_output_photon_expv)
        QWidget.setTabOrder(self.input_add_output_photon_expv, self.input_path_to_qdacc)
        QWidget.setTabOrder(self.input_path_to_qdacc, self.button_change_rungstring_to_settingfile)
        QWidget.setTabOrder(self.button_change_rungstring_to_settingfile, self.textinput_file_destination)
        QWidget.setTabOrder(self.textinput_file_destination, self.textinput_file_qdacc)
        QWidget.setTabOrder(self.textinput_file_qdacc, self.input_destination)
        QWidget.setTabOrder(self.input_destination, self.input_escape_output_command)
        QWidget.setTabOrder(self.input_escape_output_command, self.button_empty_destination_folder)
        QWidget.setTabOrder(self.button_empty_destination_folder, self.button_open_destination_folder)
        QWidget.setTabOrder(self.button_open_destination_folder, self.button_generate_run)
        QWidget.setTabOrder(self.button_generate_run, self.button_generate_copy)
        QWidget.setTabOrder(self.button_generate_copy, self.button_run_program)
        QWidget.setTabOrder(self.button_run_program, self.button_run_external)
        QWidget.setTabOrder(self.button_run_external, self.input_plot_mode)
        QWidget.setTabOrder(self.input_plot_mode, self.button_plot_everything)
        QWidget.setTabOrder(self.button_plot_everything, self.textinput_path_to_settingfile)
        QWidget.setTabOrder(self.textinput_path_to_settingfile, self.button_set_setting_file_path)
        QWidget.setTabOrder(self.button_set_setting_file_path, self.checkbox_activate_scan_parameter_1)
        QWidget.setTabOrder(self.checkbox_activate_scan_parameter_1, self.textinput_scan_parameter_1_from)
        QWidget.setTabOrder(self.textinput_scan_parameter_1_from, self.textinput_scan_parameter_1_to)
        QWidget.setTabOrder(self.textinput_scan_parameter_1_to, self.textinput_scan_parameter_1_points)
        QWidget.setTabOrder(self.textinput_scan_parameter_1_points, self.checkbox_activate_scan_parameter_2)
        QWidget.setTabOrder(self.checkbox_activate_scan_parameter_2, self.textinput_scan_parameter_2_from)
        QWidget.setTabOrder(self.textinput_scan_parameter_2_from, self.textinput_scan_parameter_2_to)
        QWidget.setTabOrder(self.textinput_scan_parameter_2_to, self.textinput_scan_parameter_2_points)
        QWidget.setTabOrder(self.textinput_scan_parameter_2_points, self.text_output_program_qdacc_command_sweep_display)
        QWidget.setTabOrder(self.text_output_program_qdacc_command_sweep_display, self.text_output_program_qdacc_command_sweep)
        QWidget.setTabOrder(self.text_output_program_qdacc_command_sweep, self.combobox_p1_input)
        QWidget.setTabOrder(self.combobox_p1_input, self.combobox_p2_input)
        QWidget.setTabOrder(self.combobox_p2_input, self.textinput_scan_parameter_1_lambda)
        QWidget.setTabOrder(self.textinput_scan_parameter_1_lambda, self.textinput_scan_parameter_2_lambda)
        QWidget.setTabOrder(self.textinput_scan_parameter_2_lambda, self.button_add_optical_pulse)
        QWidget.setTabOrder(self.button_add_optical_pulse, self.textinput_phonons_temperature)
        QWidget.setTabOrder(self.textinput_phonons_temperature, self.textinput_phonons_iterator_stepsize)
        QWidget.setTabOrder(self.textinput_phonons_iterator_stepsize, self.button_add_electronic_shift)
        QWidget.setTabOrder(self.button_add_electronic_shift, self.button_modify_delete)
        QWidget.setTabOrder(self.button_modify_delete, self.button_add_cavity)
        QWidget.setTabOrder(self.button_add_cavity, self.input_phonons_approximation)
        QWidget.setTabOrder(self.input_phonons_approximation, self.button_modify_clear)
        QWidget.setTabOrder(self.button_modify_clear, self.textinput_rates_pure_dephasing)
        QWidget.setTabOrder(self.textinput_rates_pure_dephasing, self.textinput_phonons_sd_ohmamp)
        QWidget.setTabOrder(self.textinput_phonons_sd_ohmamp, self.input_draw_details)
        QWidget.setTabOrder(self.input_draw_details, self.button_modify_edit)
        QWidget.setTabOrder(self.button_modify_edit, self.textinput_rates_cavity_coupling)
        QWidget.setTabOrder(self.textinput_rates_cavity_coupling, self.textinput_rates_cavity_loss)
        QWidget.setTabOrder(self.textinput_rates_cavity_loss, self.textinput_rates_radiative_decay)
        QWidget.setTabOrder(self.textinput_rates_radiative_decay, self.button_optimizer_fitness_function)
        QWidget.setTabOrder(self.button_optimizer_fitness_function, self.output_howto)

        self.menubar.addAction(self.menu_main.menuAction())
        self.menubar.addAction(self.menu_tools.menuAction())
        self.menubar.addAction(self.menu_functions.menuAction())
        self.menubar.addAction(self.menu_developer_tools.menuAction())
        self.menu_main.addSeparator()

        self.retranslateUi(MainWindow)

        self.main_tab_widget.setCurrentIndex(0)
        self.input_phonons_approximation.setCurrentIndex(1)
        self.input_rungekutta_order.setCurrentIndex(0)
        self.statistics_tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"QDaCC Generator", None))
        self.actionLoad_QDaCC_Command.setText(QCoreApplication.translate("MainWindow", u"Import QDaCC Command", None))
        self.actionExport_QDaCC_Command.setText(QCoreApplication.translate("MainWindow", u"Export QDaCC Command", None))
        self.main_logo.setText("")
        self.main_descriptor.setText("")
        self.button_add_cavity.setText(QCoreApplication.translate("MainWindow", u"Cavity", None))
        self.button_add_electronic_shift.setText(QCoreApplication.translate("MainWindow", u"Chirp", None))
        self.button_add_optical_pulse.setText(QCoreApplication.translate("MainWindow", u"Pulse", None))
        self.button_add_electronic_state.setText(QCoreApplication.translate("MainWindow", u"State", None))
        self.input_initial_state.setText(QCoreApplication.translate("MainWindow", u"Initial State", None))
        self.textinput_initial_state.setText("")
#if QT_CONFIG(tooltip)
        self.slider_state_separator.setToolTip(QCoreApplication.translate("MainWindow", u"Adjust visible state separation", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.slider_state_x_seperation.setToolTip(QCoreApplication.translate("MainWindow", u"Adjust state grouping threshold", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.slider_state_grouping.setToolTip(QCoreApplication.translate("MainWindow", u"Adjust state grouping threshold", None))
#endif // QT_CONFIG(tooltip)
        self.button_modify_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.button_modify_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.button_modify_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
#if QT_CONFIG(statustip)
        self.input_draw_details.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_draw_details.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.tab_system), QCoreApplication.translate("MainWindow", u"System", None))
        self.textinput_rates_radiative_decay.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.textinput_rates_pure_dephasing.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Cavity Loss</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Cavity Coupling</span></p></body></html>", None))
        self.textinput_rates_cavity_loss.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Pure Dephasing</span></p></body></html>", None))
        self.textinput_rates_cavity_coupling.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Radiative Loss</span></p></body></html>", None))
        self.label_title_rates.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Rates</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Ohm</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Temperature</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Approximation</span></p></body></html>", None))
        self.input_phonons_approximation.setItemText(0, QCoreApplication.translate("MainWindow", u"Full", None))
        self.input_phonons_approximation.setItemText(1, QCoreApplication.translate("MainWindow", u"Matrixexponential", None))
        self.input_phonons_approximation.setItemText(2, QCoreApplication.translate("MainWindow", u"Omit Transformation", None))
        self.input_phonons_approximation.setItemText(3, QCoreApplication.translate("MainWindow", u"Analytical Rates", None))
        self.input_phonons_approximation.setItemText(4, QCoreApplication.translate("MainWindow", u"Hybrid", None))

        self.textinput_phonons_sd_ohmamp.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.textinput_phonons_temperature.setText(QCoreApplication.translate("MainWindow", u"No Phonons", None))
        self.label_title_phonons.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Environment (Phonons)</span></p></body></html>", None))
        self.label_title_phonons_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_title_phonons_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Phonon Integral</span></p></body></html>", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Integral Stepsize</span></p></body></html>", None))
        self.textinput_phonons_iterator_stepsize.setText(QCoreApplication.translate("MainWindow", u"auto", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Spectral Cutoff</span></p></body></html>", None))
        self.textinput_phonons_sd_wcutoff.setText(QCoreApplication.translate("MainWindow", u"1meV", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Spectral Delta</span></p></body></html>", None))
        self.textinput_phonons_sd_wdelta.setText(QCoreApplication.translate("MainWindow", u"0.01meV", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Time Cutoff</span></p></body></html>", None))
        self.textinput_phonons_sd_tcutoff.setText(QCoreApplication.translate("MainWindow", u"4ps", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Phonon Coupling</span></p></body></html>", None))
        self.textinput_phonons_sd_alpha.setText(QCoreApplication.translate("MainWindow", u"0.03E-24", None))
        self.label_title_adjust_rates.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Adjust</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.input_phonons_adjust_radiativeloss.setStatusTip(QCoreApplication.translate("MainWindow", u"Adjusts the radiative decay loss using the formula gamma_rad = gamma_rad*<B>", None))
#endif // QT_CONFIG(statustip)
        self.input_phonons_adjust_radiativeloss.setText(QCoreApplication.translate("MainWindow", u"Radiative Loss", None))
        self.label_title_adjust_rates_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Adjust</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.input_phonons_adjust_pure_dephasing.setStatusTip(QCoreApplication.translate("MainWindow", u"Adjusts the pure dephasing rate using the formula pure_dephasing = 1mueV/K * temperature. This effect is quite strong and should probably not be used.", None))
#endif // QT_CONFIG(statustip)
        self.input_phonons_adjust_pure_dephasing.setText(QCoreApplication.translate("MainWindow", u"Pure Dephasing", None))
        self.label_title_adjust_rates_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Adjust</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.input_phonons_adjust_renormalization.setToolTip(QCoreApplication.translate("MainWindow", u"Enables the renomalization of the polaron shifted energies and rates, e.g. using the <B> and <B>^2 scalings", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.input_phonons_adjust_renormalization.setStatusTip(QCoreApplication.translate("MainWindow", u"Enables the renomalization of the polaron shifted energies and rates, e.g. using the <B> and <B>^2 scalings", None))
#endif // QT_CONFIG(statustip)
        self.input_phonons_adjust_renormalization.setText(QCoreApplication.translate("MainWindow", u"Renormalization", None))
        self.label_title_phonons_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">PME Settings</span></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Electron Energy</span></p></body></html>", None))
        self.textinput_phonons_sd_qd_de.setText(QCoreApplication.translate("MainWindow", u"7eV", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Hole Energy</span></p></body></html>", None))
        self.textinput_phonons_sd_qd_dh.setText(QCoreApplication.translate("MainWindow", u"-3.5eV", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Material Density</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_rho.setStatusTip(QCoreApplication.translate("MainWindow", u"Unit is kg/m^3", None))
#endif // QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_rho.setText(QCoreApplication.translate("MainWindow", u"5370", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Speed of Sound</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_cs.setStatusTip(QCoreApplication.translate("MainWindow", u"Unit is m/s", None))
#endif // QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_cs.setText(QCoreApplication.translate("MainWindow", u"5110", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">E-H Ratio</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_aeah_ratio.setStatusTip(QCoreApplication.translate("MainWindow", u"a_e/a_h ratio", None))
#endif // QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_aeah_ratio.setText(QCoreApplication.translate("MainWindow", u"1.15", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">QD Size (m)</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_size.setStatusTip(QCoreApplication.translate("MainWindow", u"Typical Values lie around 3nm to 6nm", None))
#endif // QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_size.setText(QCoreApplication.translate("MainWindow", u"3e-9", None))
        self.label_title_phonons_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">QD Settings</span></p></body></html>", None))
        self.input_phonons_use_qd.setText(QCoreApplication.translate("MainWindow", u"Use QD Parameters Instead of PME Settings", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Spectral Density Plot</span></p></body></html>", None))
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.tab_environment), QCoreApplication.translate("MainWindow", u"Environment", None))
#if QT_CONFIG(tooltip)
        self.button_time_config_grid.setToolTip(QCoreApplication.translate("MainWindow", u"Configure a grid instead", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.button_time_config_grid.setStatusTip(QCoreApplication.translate("MainWindow", u"Configure a grid instead", None))
#endif // QT_CONFIG(statustip)
        self.button_time_config_grid.setText(QCoreApplication.translate("MainWindow", u"Gridresolution", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Time Step</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.button_time_config_tol.setToolTip(QCoreApplication.translate("MainWindow", u"Configure a grid instead", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.button_time_config_tol.setStatusTip(QCoreApplication.translate("MainWindow", u"Configure a grid instead", None))
#endif // QT_CONFIG(statustip)
        self.button_time_config_tol.setText(QCoreApplication.translate("MainWindow", u"Tolerance", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Starting Time</span></p></body></html>", None))
        self.textinput_time_timestep.setText(QCoreApplication.translate("MainWindow", u"auto", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">End Time</span></p></body></html>", None))
        self.textinput_time_endtime.setText(QCoreApplication.translate("MainWindow", u"auto", None))
        self.textinput_time_gridresolution.setText(QCoreApplication.translate("MainWindow", u"auto", None))
        self.textinput_time_gridresolution.setPlaceholderText(QCoreApplication.translate("MainWindow", u"None", None))
        self.textinput_time_startingtime.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.textinput_time_tolerance.setText(QCoreApplication.translate("MainWindow", u"1E-6", None))
        self.textinput_time_tolerance.setPlaceholderText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_title_time.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Time</span></p></body></html>", None))
        self.label_title_solver.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Solver</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Main Solver</span></p></body></html>", None))
        self.input_rungekutta_order.setItemText(0, QCoreApplication.translate("MainWindow", u"Variable Timestep Runge Kutta Dormand Prince", None))
        self.input_rungekutta_order.setItemText(1, QCoreApplication.translate("MainWindow", u"Fixed Timestep Runge-Kutta Order 4", None))
        self.input_rungekutta_order.setItemText(2, QCoreApplication.translate("MainWindow", u"Fixed Timestep Runge-Kutta Order 5", None))
        self.input_rungekutta_order.setItemText(3, QCoreApplication.translate("MainWindow", u"Path Integral (PSADM IQUAPI)", None))

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Interpolator</span></p></body></html>", None))
        self.input_interpolator_t.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.input_interpolator_t.setItemText(1, QCoreApplication.translate("MainWindow", u"Linear", None))
        self.input_interpolator_t.setItemText(2, QCoreApplication.translate("MainWindow", u"Cubic", None))
        self.input_interpolator_t.setItemText(3, QCoreApplication.translate("MainWindow", u"Monotone", None))

#if QT_CONFIG(statustip)
        self.input_interpolator_t.setStatusTip(QCoreApplication.translate("MainWindow", u"Main Direction Interpolator. If None, no interpolation will be used, meaning the main time output has non-equidistant elements", None))
#endif // QT_CONFIG(statustip)
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Grid Expander</span></p></body></html>", None))
        self.input_interpolator_tau.setItemText(0, QCoreApplication.translate("MainWindow", u"Linear", None))
        self.input_interpolator_tau.setItemText(1, QCoreApplication.translate("MainWindow", u"Monotone", None))

#if QT_CONFIG(statustip)
        self.input_interpolator_tau.setStatusTip(QCoreApplication.translate("MainWindow", u"Tau-Direction Interpolator which expands the time calculations onto an equidistant grid. Usually linear is sufficient.", None))
#endif // QT_CONFIG(statustip)
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">PI NC</span></p></body></html>", None))
        self.textinput_phonons_nc.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">PI Stepsize</span></p></body></html>", None))
        self.textinput_phonons_tsteppath.setText(QCoreApplication.translate("MainWindow", u"auto", None))
        self.label_title_predicted_timeline.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Predicted Timeline</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.button_timeline_force_calculate_time.setStatusTip(QCoreApplication.translate("MainWindow", u"Calculate a rough estimate of the temporal dynamics.", None))
#endif // QT_CONFIG(statustip)
        self.button_timeline_force_calculate_time.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.tab_timeline), QCoreApplication.translate("MainWindow", u"Timeline", None))
        self.label_title_set_spectrum.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Spectrum</span></p></body></html>", None))
        self.button_add_spectrum_mode.setText(QCoreApplication.translate("MainWindow", u"List of Modes", None))
        self.textinput_spectrum_modes.setText("")
        self.textinput_spectrum_modes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A=B,c", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Spectral Range</span></p></body></html>", None))
        self.textinput_spectrum_range.setText("")
        self.textinput_spectrum_range.setPlaceholderText(QCoreApplication.translate("MainWindow", u"2meV", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Spectral Center</span></p></body></html>", None))
        self.textinput_spectrum_center.setText("")
        self.textinput_spectrum_center.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1eV", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Resolution</span></p></body></html>", None))
        self.textinput_spectrum_res.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.textinput_spectrum_res.setPlaceholderText("")
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Correlation</span></p></body></html>", None))
        self.input_spectrum_order.setItemText(0, QCoreApplication.translate("MainWindow", u"G1", None))
        self.input_spectrum_order.setItemText(1, QCoreApplication.translate("MainWindow", u"G2", None))

        self.label_51.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Normalize</span></p></body></html>", None))
        self.input_spectrum_normalize.setText(QCoreApplication.translate("MainWindow", u"To 1", None))
        self.button_add_spectrum_to_output.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.button_remove_spectrum_from_output.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_title_predicted_spectral.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Predicted Spectral Properties</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.button_timeline_force_calculate_spectra.setStatusTip(QCoreApplication.translate("MainWindow", u"Calculate the predicted Spectra", None))
#endif // QT_CONFIG(statustip)
        self.button_timeline_force_calculate_spectra.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.statistics_tab_widget.setTabText(self.statistics_tab_widget.indexOf(self.subtab_spectrum), QCoreApplication.translate("MainWindow", u"Spectrum", None))
        self.label_title_set_indists.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Indistinguishabilities</span></p></body></html>", None))
        self.button_add_indist_mode.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.textinput_indist_modes.setText("")
        self.textinput_indist_modes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A=B, c", None))
        self.button_add_indist_to_output.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.button_remove_indist_from_output.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_title_set_concurrences.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Concurrences</span></p></body></html>", None))
        self.button_add_concurrence_mode_1.setText(QCoreApplication.translate("MainWindow", u"First Mode", None))
        self.textinput_concurrence_first.setText("")
        self.textinput_concurrence_first.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A=B+B=D", None))
        self.button_add_concurrence_mode_2.setText(QCoreApplication.translate("MainWindow", u"Second Mode", None))
        self.textinput_concurrence_second.setText("")
        self.textinput_concurrence_second.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A=C+C=D", None))
        self.button_add_concurrence_to_output.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.button_remove_concurrence_from_output.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_title_set_concurrences_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Concurrence Spectra</span></p></body></html>", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Center</span></p></body></html>", None))
        self.textinput_concurrence_spec_freq.setText("")
        self.textinput_concurrence_spec_freq.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Range</span></p></body></html>", None))
        self.textinput_concurrence_spec_range.setText("")
        self.textinput_concurrence_spec_range.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Resolution</span></p></body></html>", None))
        self.textinput_concurrence_spec_res.setText("")
        self.textinput_concurrence_spec_res.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.input_concurrence_add_spectra.setText(QCoreApplication.translate("MainWindow", u"Enable Spectrum Calculations for G2 concurrence functions", None))
        self.button_add_gfunc_mode.setText(QCoreApplication.translate("MainWindow", u"Modes", None))
        self.button_remove_gfunc_from_output.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Outputmethod</span></p></body></html>", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Order</span></p></body></html>", None))
        self.input_gfunc_integration.setItemText(0, QCoreApplication.translate("MainWindow", u"Integrated", None))
        self.input_gfunc_integration.setItemText(1, QCoreApplication.translate("MainWindow", u"Matrix", None))
        self.input_gfunc_integration.setItemText(2, QCoreApplication.translate("MainWindow", u"Both", None))

        self.textinput_correlation_modes.setText("")
        self.textinput_correlation_modes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A=B, c", None))
        self.input_gfunc_order.setItemText(0, QCoreApplication.translate("MainWindow", u"G1", None))
        self.input_gfunc_order.setItemText(1, QCoreApplication.translate("MainWindow", u"G2", None))

        self.button_add_gfunc_to_output.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_title_set_g1g2funcs.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">G1 and G2 Functions</span></p></body></html>", None))
        self.statistics_tab_widget.setTabText(self.statistics_tab_widget.indexOf(self.subtab_indist), QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.label_title_set_detector.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Temporal Measurement Window</span></p></body></html>", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Time Center</span></p></body></html>", None))
        self.textinput_detector_t0.setText("")
        self.textinput_detector_t0.setPlaceholderText(QCoreApplication.translate("MainWindow", u"start", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Width</span></p></body></html>", None))
        self.textinput_detector_t1.setText("")
        self.textinput_detector_t1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"end", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Falloff Power</span></p></body></html>", None))
        self.textinput_detector_tpower.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.textinput_detector_tpower.setPlaceholderText("")
        self.button_add_detector_time.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.button_remove_detector_time.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_title_set_detector_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Wigner Function</span></p></body></html>", None))
        self.button_add_wigner_mode.setText(QCoreApplication.translate("MainWindow", u"Modes", None))
        self.textinput_wigner_modes.setText("")
        self.textinput_wigner_modes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A=B,c", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">X</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.textinput_wigner_x.setStatusTip(QCoreApplication.translate("MainWindow", u"Alpha in -X:X range", None))
#endif // QT_CONFIG(statustip)
        self.textinput_wigner_x.setText("")
        self.textinput_wigner_x.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Y</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.textinput_wigner_y.setStatusTip(QCoreApplication.translate("MainWindow", u"Alpha in -Y:Y range", None))
#endif // QT_CONFIG(statustip)
        self.textinput_wigner_y.setText("")
        self.textinput_wigner_y.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Resolution</span></p></body></html>", None))
        self.textinput_wigner_resolution.setText("")
        self.textinput_wigner_resolution.setPlaceholderText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Skip</span></p></body></html>", None))
        self.textinput_wigner_skip.setText("")
        self.textinput_wigner_skip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button_add_wigner.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.button_remove_wigner.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_title_set_detector_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Spectral Measurement Window</span></p></body></html>", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Spectral Center</span></p></body></html>", None))
        self.textinput_detector_wcenter.setText("")
        self.textinput_detector_wcenter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"center", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Spectral Range</span></p></body></html>", None))
        self.textinput_detector_wrange.setText("")
        self.textinput_detector_wrange.setPlaceholderText(QCoreApplication.translate("MainWindow", u"range", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Fourier Points</span></p></body></html>", None))
        self.textinput_detector_wnum.setText("")
        self.textinput_detector_wnum.setPlaceholderText(QCoreApplication.translate("MainWindow", u"fourier points", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Falloff Power</span></p></body></html>", None))
        self.textinput_detector_wpower.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.textinput_detector_wpower.setPlaceholderText("")
        self.button_add_detector_spectral.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.button_remove_detector_spectral.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.statistics_tab_widget.setTabText(self.statistics_tab_widget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Special Functionality", None))
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.tab_statistics), QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Output Frame</span></p></body></html>", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Density Matrix</span></p></body></html>", None))
        self.input_dm_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"No Output", None))
        self.input_dm_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"Diagonal Elements", None))
        self.input_dm_mode.setItemText(2, QCoreApplication.translate("MainWindow", u"Full Matrix", None))

        self.label_64.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Frame</span></p></body></html>", None))
        self.input_dm_frame.setItemText(0, QCoreApplication.translate("MainWindow", u"Heisenberg", None))
        self.input_dm_frame.setItemText(1, QCoreApplication.translate("MainWindow", u"Schr\u00f6dinger", None))

        self.label_61.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">CPU Cores</span></p></body></html>", None))
        self.textinput_cpucores.setText(QCoreApplication.translate("MainWindow", u"all", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Logging Level</span></p></body></html>", None))
        self.input_logginglevel.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.input_logginglevel.setItemText(1, QCoreApplication.translate("MainWindow", u"Additional", None))
        self.input_logginglevel.setItemText(2, QCoreApplication.translate("MainWindow", u"Verbose", None))

        self.label_66.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Misc</span></p></body></html>", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Additional Outputs</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.input_add_output_eigenvalues.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_eigenvalues.setText(QCoreApplication.translate("MainWindow", u"Eigenvalues", None))
#if QT_CONFIG(statustip)
        self.input_add_output_operators.setStatusTip(QCoreApplication.translate("MainWindow", u"Note: Logging Level has to be at least L2", None))
#endif // QT_CONFIG(statustip)
        self.input_add_output_operators.setText(QCoreApplication.translate("MainWindow", u"Operator Matrices", None))
#if QT_CONFIG(statustip)
        self.input_add_output_rkerror.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_rkerror.setText(QCoreApplication.translate("MainWindow", u"Runge-Kutta Error", None))
#if QT_CONFIG(statustip)
        self.input_add_output_vonneumannpath.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_vonneumannpath.setText(QCoreApplication.translate("MainWindow", u"von Neumann Path", None))
#if QT_CONFIG(statustip)
        self.input_add_output_detecotrtrafo.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_detecotrtrafo.setText(QCoreApplication.translate("MainWindow", u"Detectorfunctions", None))
#if QT_CONFIG(statustip)
        self.input_add_output_chirp_fourier.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_chirp_fourier.setText(QCoreApplication.translate("MainWindow", u"Chirp Fourier", None))
#if QT_CONFIG(statustip)
        self.input_add_output_pulse_fourier.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_pulse_fourier.setText(QCoreApplication.translate("MainWindow", u"Pulse Fourier", None))
#if QT_CONFIG(statustip)
        self.input_add_output_phononj.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_phononj.setText(QCoreApplication.translate("MainWindow", u"Phonon Spectral J", None))
#if QT_CONFIG(statustip)
        self.input_add_output_greenf.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_greenf.setText(QCoreApplication.translate("MainWindow", u"Greenfunctions", None))
#if QT_CONFIG(statustip)
        self.input_add_output_phononcoeffs.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_phononcoeffs.setText(QCoreApplication.translate("MainWindow", u"Phononcoefficients", None))
#if QT_CONFIG(statustip)
        self.input_add_output_tpm.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_tpm.setText(QCoreApplication.translate("MainWindow", u"Two Photon Matrix", None))
#if QT_CONFIG(statustip)
        self.input_add_output_concurrence_eigs.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_concurrence_eigs.setText(QCoreApplication.translate("MainWindow", u"Concurrence EV", None))
#if QT_CONFIG(statustip)
        self.input_add_output_photon_expv.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_photon_expv.setText(QCoreApplication.translate("MainWindow", u"Full Photon EV", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Custom Expectation Values</span></p></body></html>", None))
        self.button_add_custom_expval_matrix.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.button_remove_custom_expval_matrix.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.tab_output), QCoreApplication.translate("MainWindow", u"Output", None))
        self.text_output_program_main.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.text_output_program_qdacc_command.setPlaceholderText(QCoreApplication.translate("MainWindow", u"./QDaCC.exe ...", None))
        self.button_generate_run.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.button_run_and_plot.setText(QCoreApplication.translate("MainWindow", u"Run and Plot", None))
        self.button_run_program.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.input_plot_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"Workspace Folder", None))
        self.input_plot_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"Animated Blochsphere", None))
        self.input_plot_mode.setItemText(2, QCoreApplication.translate("MainWindow", u"Animated Density Matrix", None))

#if QT_CONFIG(tooltip)
        self.button_run_external.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><a href=\"https://pc2.uni-paderborn.de/de/hpc-services/available-systems/noctua2\"><span style=\" font-size:12pt; font-weight:700; text-decoration: underline; color:#0000ff;\">Calculate QDaCC on the noctua2 HPC cluster</span></a></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">!! Currently not yet available !!</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_run_external.setText(QCoreApplication.translate("MainWindow", u"Run on Noctua", None))
        self.button_run_kill.setText(QCoreApplication.translate("MainWindow", u"Kill", None))
        self.button_generate_copy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.button_plot_everything.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.input_path_to_qdacc.setText(QCoreApplication.translate("MainWindow", u"QDaCC", None))
        self.textinput_file_qdacc.setText("")
        self.input_destination.setText(QCoreApplication.translate("MainWindow", u"Worskspace", None))
        self.textinput_file_destination.setText("")
        self.button_open_destination_folder.setText(QCoreApplication.translate("MainWindow", u"Open Destination Folder", None))
        self.button_empty_destination_folder.setText(QCoreApplication.translate("MainWindow", u"Empty Destination Folder", None))
        self.button_change_rungstring_to_settingfile.setText(QCoreApplication.translate("MainWindow", u"Toggle Runstring", None))
#if QT_CONFIG(statustip)
        self.input_escape_output_command.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_escape_output_command.setText(QCoreApplication.translate("MainWindow", u"Escape Output", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Progress</span></p></body></html>", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">CPU Usage</span></p></body></html>", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">RAM Usage</span></p></body></html>", None))
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.tab_generate), QCoreApplication.translate("MainWindow", u"Generate and Run", None))
        self.label_title_qdsystem_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Parameter x1</span></p></body></html>", None))
        self.checkbox_activate_scan_parameter_1.setText(QCoreApplication.translate("MainWindow", u"Activate", None))
        self.label_title_qdsystem_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">From</span></p></body></html>", None))
        self.label_title_qdsystem_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">To</span></p></body></html>", None))
        self.label_title_qdsystem_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\"># Points</span></p></body></html>", None))
        self.combobox_p1_input.setItemText(0, QCoreApplication.translate("MainWindow", u"P1(x1,...) =", None))
        self.combobox_p1_input.setItemText(1, QCoreApplication.translate("MainWindow", u"P12(x1,...) =", None))
        self.combobox_p1_input.setItemText(2, QCoreApplication.translate("MainWindow", u"P13(x1,...) =", None))
        self.combobox_p1_input.setItemText(3, QCoreApplication.translate("MainWindow", u"P14(x1,...) =", None))
        self.combobox_p1_input.setItemText(4, QCoreApplication.translate("MainWindow", u"P15(x1,...) =", None))

        self.textinput_scan_parameter_1_lambda.setText("")
        self.label_title_qdsystem_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Parameter x2</span></p></body></html>", None))
        self.checkbox_activate_scan_parameter_2.setText(QCoreApplication.translate("MainWindow", u"Activate", None))
        self.label_title_qdsystem_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">From</span></p></body></html>", None))
        self.label_title_qdsystem_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">To</span></p></body></html>", None))
        self.label_title_qdsystem_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\"># Points</span></p></body></html>", None))
        self.combobox_p2_input.setItemText(0, QCoreApplication.translate("MainWindow", u"P2(x2,...) =", None))
        self.combobox_p2_input.setItemText(1, QCoreApplication.translate("MainWindow", u"P22(x2,...) =", None))
        self.combobox_p2_input.setItemText(2, QCoreApplication.translate("MainWindow", u"P23(x2,...) =", None))
        self.combobox_p2_input.setItemText(3, QCoreApplication.translate("MainWindow", u"P24(x2,...) =", None))
        self.combobox_p2_input.setItemText(4, QCoreApplication.translate("MainWindow", u"P25(x2,...) =", None))

        self.textinput_scan_parameter_2_lambda.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">How to Use:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">- Activate one or both parameters</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" fon"
                        "t-weight:700;\">- Replace parameters in runstring with {P1} and {P2}, respectively</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">- Choose parameter range from-to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">- Choose number of points</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">-- Optional: Chose f(x)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">- Use the &quot;Generate Variables&quot; Button to generate and plot the Parameters</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px"
                        "; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">- Use the &quot;Generate Settingfile&quot; Button in the &quot;Generate and Run&quot; Tab to generate the settingfile</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Additional Parameters available (lower case = SI, upper case = number):</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">- g and G for Cavity-Coupling</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">- k and K for Cavity Losses</span></p>\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">- y and Y for Radiative Decay</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">- d and D for Pure Dephasing</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">- T for Temperature</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">- np.function for all Numpy Functions</span></p></body></html>", None))
        self.text_output_program_qdacc_command_sweep_display.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_output_program_qdacc_command_sweep_display.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Settingfile Output", None))
        self.button_set_setting_file_path.setText(QCoreApplication.translate("MainWindow", u"Settingfile", None))
        self.textinput_path_to_settingfile.setText("")
        self.label_title_qdsystem_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">QDaCC Runstring</span></p></body></html>", None))
        self.button_sweeper_plot.setText(QCoreApplication.translate("MainWindow", u"Generate Settingfile", None))
        self.button_sweeper_get_runstring.setText(QCoreApplication.translate("MainWindow", u"Get Current Runstring", None))
        self.text_output_program_qdacc_command_sweep.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_output_program_qdacc_command_sweep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"./QDaCC.exe ...", None))
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.tab_scanner), QCoreApplication.translate("MainWindow", u"Sweep and Scan", None))
        self.text_output_program_qdacc_command_sweep_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_output_program_qdacc_command_sweep_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"./QDaCC.exe ...", None))
        self.button_optimizer_get_runstring.setText(QCoreApplication.translate("MainWindow", u"Get Current Runstring", None))
        self.button_optimizer_optimize.setText(QCoreApplication.translate("MainWindow", u"Optimize", None))
        self.button_optimizer_runstring_to_main.setText(QCoreApplication.translate("MainWindow", u"Move Command to Main Window", None))
        self.text_output_program_qdacc_command_sweep_display_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_output_program_qdacc_command_sweep_display_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Optimizer Output", None))
        self.button_optimizer_files.setText(QCoreApplication.translate("MainWindow", u"Files", None))
        self.textinput_optimizer_files.setText("")
        self.button_optimizer_files_2.setText(QCoreApplication.translate("MainWindow", u"File Indices", None))
        self.textinput_optimizer_file_indices.setText("")
        self.label_title_qdsystem_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Legend</span></p></body></html>", None))
        self.textinput_optimizer_legend.setText("")
        self.label_title_qdsystem_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Initial Parameters</span></p></body></html>", None))
        self.textinput_optimizer_initial_parameters.setText("")
        self.label_title_qdsystem_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Parameters Bounds</span></p></body></html>", None))
        self.textinput_optimizer_parameter_bounds.setText("")
        self.label_title_qdsystem_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Parameter Names</span></p></body></html>", None))
        self.textinput_optimizer_parameter_names.setText("")
        self.button_optimizer_fitness_function.setText(QCoreApplication.translate("MainWindow", u"Fitness Function", None))
        self.textinput_optimizer_fitnessfunction.setText(QCoreApplication.translate("MainWindow", u"last(Y1)", None))
        self.label_title_qdsystem_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Format Function</span></p></body></html>", None))
        self.textinput_optimizer_formatfunction.setText(QCoreApplication.translate("MainWindow", u"basestring.format(*parameters)", None))
        self.label_title_qdsystem_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Tolerance</span></p></body></html>", None))
        self.textinput_optimizer_tol.setText(QCoreApplication.translate("MainWindow", u"1e-6", None))
        self.label_title_qdsystem_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Epsilon</span></p></body></html>", None))
        self.textinput_optimizer_eps.setText(QCoreApplication.translate("MainWindow", u"1e-6", None))
        self.label_title_qdsystem_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Maximum Iterations</span></p></body></html>", None))
        self.textinput_optimizer_maxit.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_title_qdsystem_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Optimizer</span></p></body></html>", None))
        self.textinput_optimizer_maxit_2.setText(QCoreApplication.translate("MainWindow", u"nelder-mead", None))
#if QT_CONFIG(tooltip)
        self.optimizer_call_plotscript.setToolTip(QCoreApplication.translate("MainWindow", u"Enabling Sweep or Scan Mode will call the plotscript after each iteration of the optimizer. This can be usefull if you want to optimize e.g. the endpoints of a simulation to fit a certain curve. Remember, numpy (np) and scipy(sp) can be used in the fitness function to enable fitting.", None))
#endif // QT_CONFIG(tooltip)
        self.optimizer_call_plotscript.setText(QCoreApplication.translate("MainWindow", u"Sweep or Scan Mode", None))
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.tab_optimizer), QCoreApplication.translate("MainWindow", u"Optimization", None))
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.tab_howto), QCoreApplication.translate("MainWindow", u"How-To", None))
        self.menu_main.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menu_functions.setTitle(QCoreApplication.translate("MainWindow", u"Functions", None))
        self.menu_developer_tools.setTitle(QCoreApplication.translate("MainWindow", u"Dev Tools", None))
        self.menu_tools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

