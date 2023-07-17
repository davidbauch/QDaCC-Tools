# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowDDPyFg.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
    QFrame, QGridLayout, QLabel, QLineEdit,
    QListView, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QTabWidget, QTextBrowser, QTextEdit,
    QWidget)

from .hoverbutton import HoverButton
from .plotwidget import PlotWidget
from .textbrowserexternal import TextBrowserExternal

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1458, 1072)
        MainWindow.setStyleSheet(u"")
        MainWindow.setIconSize(QSize(64, 64))
        self.actionLoad_QDaCC_Command = QAction(MainWindow)
        self.actionLoad_QDaCC_Command.setObjectName(u"actionLoad_QDaCC_Command")
        self.actionExport_QDaCC_Command = QAction(MainWindow)
        self.actionExport_QDaCC_Command.setObjectName(u"actionExport_QDaCC_Command")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_14 = QGridLayout(self.centralwidget)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab_system = QWidget()
        self.tab_system.setObjectName(u"tab_system")
        self.gridLayout_2 = QGridLayout(self.tab_system)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_title_qdsystem = QLabel(self.tab_system)
        self.label_title_qdsystem.setObjectName(u"label_title_qdsystem")
        self.label_title_qdsystem.setMinimumSize(QSize(0, 40))
        self.label_title_qdsystem.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem.setFrameShadow(QFrame.Plain)

        self.gridLayout_2.addWidget(self.label_title_qdsystem, 0, 4, 1, 1)

        self.label_5 = QLabel(self.tab_system)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 40))
        self.label_5.setMaximumSize(QSize(200, 40))

        self.gridLayout_2.addWidget(self.label_5, 1, 4, 1, 1)

        self.button_add_electronic_state = HoverButton(self.tab_system)
        self.button_add_electronic_state.setObjectName(u"button_add_electronic_state")
        self.button_add_electronic_state.setMinimumSize(QSize(0, 40))
        self.button_add_electronic_state.setMaximumSize(QSize(200, 40))

        self.gridLayout_2.addWidget(self.button_add_electronic_state, 2, 4, 1, 1)

        self.button_add_cavity = HoverButton(self.tab_system)
        self.button_add_cavity.setObjectName(u"button_add_cavity")
        self.button_add_cavity.setMinimumSize(QSize(0, 40))
        self.button_add_cavity.setMaximumSize(QSize(200, 40))

        self.gridLayout_2.addWidget(self.button_add_cavity, 3, 4, 1, 1)

        self.button_add_optical_pulse = HoverButton(self.tab_system)
        self.button_add_optical_pulse.setObjectName(u"button_add_optical_pulse")
        self.button_add_optical_pulse.setMinimumSize(QSize(0, 40))
        self.button_add_optical_pulse.setMaximumSize(QSize(200, 40))

        self.gridLayout_2.addWidget(self.button_add_optical_pulse, 4, 4, 1, 1)

        self.button_add_electronic_shift = HoverButton(self.tab_system)
        self.button_add_electronic_shift.setObjectName(u"button_add_electronic_shift")
        self.button_add_electronic_shift.setMinimumSize(QSize(0, 40))
        self.button_add_electronic_shift.setMaximumSize(QSize(200, 40))
        self.button_add_electronic_shift.setMouseTracking(True)

        self.gridLayout_2.addWidget(self.button_add_electronic_shift, 5, 4, 1, 1)

        self.list_components = QListView(self.tab_system)
        self.list_components.setObjectName(u"list_components")
        self.list_components.setMinimumSize(QSize(0, 40))
        self.list_components.setMaximumSize(QSize(200, 16777215))
        self.list_components.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list_components.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list_components.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list_components.setDefaultDropAction(Qt.IgnoreAction)
        self.list_components.setViewMode(QListView.ListMode)

        self.gridLayout_2.addWidget(self.list_components, 6, 4, 1, 1)

        self.button_modify_edit = HoverButton(self.tab_system)
        self.button_modify_edit.setObjectName(u"button_modify_edit")
        self.button_modify_edit.setMinimumSize(QSize(0, 40))
        self.button_modify_edit.setMaximumSize(QSize(200, 40))
        self.button_modify_edit.setFlat(False)

        self.gridLayout_2.addWidget(self.button_modify_edit, 7, 4, 1, 1)

        self.button_modify_delete = HoverButton(self.tab_system)
        self.button_modify_delete.setObjectName(u"button_modify_delete")
        self.button_modify_delete.setMinimumSize(QSize(0, 40))
        self.button_modify_delete.setMaximumSize(QSize(200, 40))
        self.button_modify_delete.setFlat(False)

        self.gridLayout_2.addWidget(self.button_modify_delete, 8, 4, 1, 1)

        self.button_modify_clear = HoverButton(self.tab_system)
        self.button_modify_clear.setObjectName(u"button_modify_clear")
        self.button_modify_clear.setMinimumSize(QSize(0, 40))
        self.button_modify_clear.setMaximumSize(QSize(200, 40))
        self.button_modify_clear.setFlat(False)

        self.gridLayout_2.addWidget(self.button_modify_clear, 9, 4, 1, 1)

        self.input_draw_details = QCheckBox(self.tab_system)
        self.input_draw_details.setObjectName(u"input_draw_details")
        self.input_draw_details.setMinimumSize(QSize(0, 40))
        self.input_draw_details.setMaximumSize(QSize(200, 40))
        self.input_draw_details.setChecked(False)

        self.gridLayout_2.addWidget(self.input_draw_details, 10, 4, 1, 1)

        self.slider_state_separator = QSlider(self.tab_system)
        self.slider_state_separator.setObjectName(u"slider_state_separator")
        self.slider_state_separator.setMinimumSize(QSize(0, 40))
        self.slider_state_separator.setMinimum(1)
        self.slider_state_separator.setMaximum(100)
        self.slider_state_separator.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.slider_state_separator, 11, 0, 1, 1)

        self.slider_state_grouping = QSlider(self.tab_system)
        self.slider_state_grouping.setObjectName(u"slider_state_grouping")
        self.slider_state_grouping.setMinimumSize(QSize(0, 40))
        self.slider_state_grouping.setMinimum(1)
        self.slider_state_grouping.setMaximum(100)
        self.slider_state_grouping.setValue(50)
        self.slider_state_grouping.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.slider_state_grouping, 11, 1, 1, 1)

        self.input_initial_state = HoverButton(self.tab_system)
        self.input_initial_state.setObjectName(u"input_initial_state")
        self.input_initial_state.setMinimumSize(QSize(0, 40))

        self.gridLayout_2.addWidget(self.input_initial_state, 11, 2, 1, 1)

        self.textinput_initial_state = QLineEdit(self.tab_system)
        self.textinput_initial_state.setObjectName(u"textinput_initial_state")
        self.textinput_initial_state.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.textinput_initial_state.setFont(font)
        self.textinput_initial_state.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")
        self.textinput_initial_state.setFrame(True)
        self.textinput_initial_state.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.textinput_initial_state, 11, 3, 1, 1)

        self.button_next_tab_system_to_config = QPushButton(self.tab_system)
        self.button_next_tab_system_to_config.setObjectName(u"button_next_tab_system_to_config")
        self.button_next_tab_system_to_config.setMinimumSize(QSize(0, 40))
        self.button_next_tab_system_to_config.setMaximumSize(QSize(200, 40))
        self.button_next_tab_system_to_config.setCheckable(False)

        self.gridLayout_2.addWidget(self.button_next_tab_system_to_config, 11, 4, 1, 1)

        self.label_output_system = QLabel(self.tab_system)
        self.label_output_system.setObjectName(u"label_output_system")
        self.label_output_system.setMinimumSize(QSize(0, 0))
        self.label_output_system.setAcceptDrops(True)
        self.label_output_system.setFrameShape(QFrame.NoFrame)
        self.label_output_system.setFrameShadow(QFrame.Plain)

        self.gridLayout_2.addWidget(self.label_output_system, 0, 0, 11, 4)

        self.tabWidget.addTab(self.tab_system, "")
        self.tab_environment = QWidget()
        self.tab_environment.setObjectName(u"tab_environment")
        self.gridLayout_3 = QGridLayout(self.tab_environment)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.textinput_phonons_sd_qd_de = QLineEdit(self.tab_environment)
        self.textinput_phonons_sd_qd_de.setObjectName(u"textinput_phonons_sd_qd_de")
        self.textinput_phonons_sd_qd_de.setEnabled(False)
        self.textinput_phonons_sd_qd_de.setMinimumSize(QSize(0, 40))
        self.textinput_phonons_sd_qd_de.setFont(font)
        self.textinput_phonons_sd_qd_de.setFrame(True)
        self.textinput_phonons_sd_qd_de.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_sd_qd_de, 16, 1, 1, 1)

        self.label_32 = QLabel(self.tab_environment)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_32, 16, 2, 1, 1)

        self.label_plot_spectral_density = PlotWidget(self.tab_environment)
        self.label_plot_spectral_density.setObjectName(u"label_plot_spectral_density")

        self.gridLayout_3.addWidget(self.label_plot_spectral_density, 15, 5, 4, 5)

        self.label_19 = QLabel(self.tab_environment)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_19, 4, 0, 1, 1)

        self.label_22 = QLabel(self.tab_environment)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_22, 3, 2, 1, 1)

        self.label_39 = QLabel(self.tab_environment)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_39, 14, 5, 1, 5)

        self.textinput_phonons_sd_tcutoff = QLineEdit(self.tab_environment)
        self.textinput_phonons_sd_tcutoff.setObjectName(u"textinput_phonons_sd_tcutoff")
        self.textinput_phonons_sd_tcutoff.setMinimumSize(QSize(0, 40))
        self.textinput_phonons_sd_tcutoff.setFont(font)
        self.textinput_phonons_sd_tcutoff.setFrame(True)
        self.textinput_phonons_sd_tcutoff.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_sd_tcutoff, 6, 6, 1, 1)

        self.label_29 = QLabel(self.tab_environment)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_29, 6, 5, 1, 1)

        self.label_20 = QLabel(self.tab_environment)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_20, 5, 0, 1, 1)

        self.textinput_rates_pure_dephasing = QLineEdit(self.tab_environment)
        self.textinput_rates_pure_dephasing.setObjectName(u"textinput_rates_pure_dephasing")
        self.textinput_rates_pure_dephasing.setMinimumSize(QSize(0, 40))
        self.textinput_rates_pure_dephasing.setFont(font)
        self.textinput_rates_pure_dephasing.setFrame(True)
        self.textinput_rates_pure_dephasing.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_rates_pure_dephasing, 6, 1, 1, 1)

        self.label_34 = QLabel(self.tab_environment)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_34, 17, 2, 1, 1)

        self.line_3 = QFrame(self.tab_environment)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(0, 40))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_3, 15, 4, 4, 1)

        self.textinput_phonons_iterator_stepsize = QLineEdit(self.tab_environment)
        self.textinput_phonons_iterator_stepsize.setObjectName(u"textinput_phonons_iterator_stepsize")
        self.textinput_phonons_iterator_stepsize.setMinimumSize(QSize(0, 40))
        self.textinput_phonons_iterator_stepsize.setFont(font)
        self.textinput_phonons_iterator_stepsize.setFrame(True)
        self.textinput_phonons_iterator_stepsize.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_iterator_stepsize, 3, 6, 1, 1)

        self.label_31 = QLabel(self.tab_environment)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_31, 16, 0, 1, 1)

        self.label_35 = QLabel(self.tab_environment)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_35, 18, 0, 1, 1)

        self.label_title_rates = QLabel(self.tab_environment)
        self.label_title_rates.setObjectName(u"label_title_rates")
        self.label_title_rates.setMinimumSize(QSize(0, 40))
        self.label_title_rates.setMaximumSize(QSize(16777215, 40))
        self.label_title_rates.setFrameShape(QFrame.NoFrame)
        self.label_title_rates.setFrameShadow(QFrame.Plain)

        self.gridLayout_3.addWidget(self.label_title_rates, 2, 0, 1, 2)

        self.label_18 = QLabel(self.tab_environment)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_18, 3, 0, 1, 1)

        self.line_2 = QFrame(self.tab_environment)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 40))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 13, 0, 1, 10)

        self.label_21 = QLabel(self.tab_environment)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_21, 6, 0, 1, 1)

        self.label_title_phonons_3 = QLabel(self.tab_environment)
        self.label_title_phonons_3.setObjectName(u"label_title_phonons_3")
        self.label_title_phonons_3.setMinimumSize(QSize(0, 40))
        self.label_title_phonons_3.setMaximumSize(QSize(16777215, 40))
        self.label_title_phonons_3.setFrameShape(QFrame.NoFrame)
        self.label_title_phonons_3.setFrameShadow(QFrame.Plain)

        self.gridLayout_3.addWidget(self.label_title_phonons_3, 2, 7, 1, 2)

        self.label_27 = QLabel(self.tab_environment)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_27, 4, 5, 1, 1)

        self.textinput_phonons_temperature = QLineEdit(self.tab_environment)
        self.textinput_phonons_temperature.setObjectName(u"textinput_phonons_temperature")
        self.textinput_phonons_temperature.setMinimumSize(QSize(0, 40))
        self.textinput_phonons_temperature.setFont(font)
        self.textinput_phonons_temperature.setFrame(True)
        self.textinput_phonons_temperature.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_temperature, 3, 3, 1, 1)

        self.textinput_phonons_sd_ohmamp = QLineEdit(self.tab_environment)
        self.textinput_phonons_sd_ohmamp.setObjectName(u"textinput_phonons_sd_ohmamp")
        self.textinput_phonons_sd_ohmamp.setMinimumSize(QSize(0, 40))
        self.textinput_phonons_sd_ohmamp.setFont(font)
        self.textinput_phonons_sd_ohmamp.setFrame(True)
        self.textinput_phonons_sd_ohmamp.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_sd_ohmamp, 4, 3, 1, 1)

        self.input_phonons_approximation = QComboBox(self.tab_environment)
        self.input_phonons_approximation.addItem("")
        self.input_phonons_approximation.addItem("")
        self.input_phonons_approximation.addItem("")
        self.input_phonons_approximation.addItem("")
        self.input_phonons_approximation.addItem("")
        self.input_phonons_approximation.setObjectName(u"input_phonons_approximation")
        self.input_phonons_approximation.setMinimumSize(QSize(0, 40))
        self.input_phonons_approximation.setFont(font)
        self.input_phonons_approximation.setFocusPolicy(Qt.WheelFocus)
        self.input_phonons_approximation.setFrame(True)

        self.gridLayout_3.addWidget(self.input_phonons_approximation, 5, 3, 1, 1)

        self.label_33 = QLabel(self.tab_environment)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_33, 17, 0, 1, 1)

        self.label_title_phonons_2 = QLabel(self.tab_environment)
        self.label_title_phonons_2.setObjectName(u"label_title_phonons_2")
        self.label_title_phonons_2.setMinimumSize(QSize(0, 40))
        self.label_title_phonons_2.setMaximumSize(QSize(16777215, 40))
        self.label_title_phonons_2.setFrameShape(QFrame.NoFrame)
        self.label_title_phonons_2.setFrameShadow(QFrame.Plain)

        self.gridLayout_3.addWidget(self.label_title_phonons_2, 2, 5, 1, 2)

        self.textinput_phonons_sd_qd_dh = QLineEdit(self.tab_environment)
        self.textinput_phonons_sd_qd_dh.setObjectName(u"textinput_phonons_sd_qd_dh")
        self.textinput_phonons_sd_qd_dh.setEnabled(False)
        self.textinput_phonons_sd_qd_dh.setMinimumSize(QSize(0, 40))
        self.textinput_phonons_sd_qd_dh.setFont(font)
        self.textinput_phonons_sd_qd_dh.setFrame(True)
        self.textinput_phonons_sd_qd_dh.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_sd_qd_dh, 16, 3, 1, 1)

        self.label_25 = QLabel(self.tab_environment)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_25, 15, 0, 1, 1)

        self.label_30 = QLabel(self.tab_environment)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_30, 4, 2, 1, 1)

        self.textinput_rates_radiative_decay = QLineEdit(self.tab_environment)
        self.textinput_rates_radiative_decay.setObjectName(u"textinput_rates_radiative_decay")
        self.textinput_rates_radiative_decay.setMinimumSize(QSize(0, 40))
        self.textinput_rates_radiative_decay.setFont(font)
        self.textinput_rates_radiative_decay.setFrame(True)
        self.textinput_rates_radiative_decay.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_rates_radiative_decay, 5, 1, 1, 1)

        self.textinput_phonons_sd_qd_size = QLineEdit(self.tab_environment)
        self.textinput_phonons_sd_qd_size.setObjectName(u"textinput_phonons_sd_qd_size")
        self.textinput_phonons_sd_qd_size.setEnabled(False)
        self.textinput_phonons_sd_qd_size.setMinimumSize(QSize(0, 40))
        self.textinput_phonons_sd_qd_size.setFont(font)
        self.textinput_phonons_sd_qd_size.setFrame(True)
        self.textinput_phonons_sd_qd_size.setCursorPosition(4)
        self.textinput_phonons_sd_qd_size.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_sd_qd_size, 18, 3, 1, 1)

        self.button_next_tab_config_to_timeline = QPushButton(self.tab_environment)
        self.button_next_tab_config_to_timeline.setObjectName(u"button_next_tab_config_to_timeline")
        self.button_next_tab_config_to_timeline.setMinimumSize(QSize(0, 40))
        self.button_next_tab_config_to_timeline.setMaximumSize(QSize(150, 16777215))
        self.button_next_tab_config_to_timeline.setCheckable(False)

        self.gridLayout_3.addWidget(self.button_next_tab_config_to_timeline, 19, 9, 1, 1)

        self.label_37 = QLabel(self.tab_environment)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_37, 3, 5, 1, 1)

        self.textinput_phonons_sd_qd_rho = QLineEdit(self.tab_environment)
        self.textinput_phonons_sd_qd_rho.setObjectName(u"textinput_phonons_sd_qd_rho")
        self.textinput_phonons_sd_qd_rho.setEnabled(False)
        self.textinput_phonons_sd_qd_rho.setMinimumSize(QSize(0, 40))
        self.textinput_phonons_sd_qd_rho.setFont(font)
        self.textinput_phonons_sd_qd_rho.setFrame(True)
        self.textinput_phonons_sd_qd_rho.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_sd_qd_rho, 17, 1, 1, 1)

        self.label_26 = QLabel(self.tab_environment)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_26, 3, 7, 1, 1)

        self.label_title_phonons_4 = QLabel(self.tab_environment)
        self.label_title_phonons_4.setObjectName(u"label_title_phonons_4")
        self.label_title_phonons_4.setMinimumSize(QSize(0, 40))
        self.label_title_phonons_4.setMaximumSize(QSize(16777215, 40))
        self.label_title_phonons_4.setFrameShape(QFrame.NoFrame)
        self.label_title_phonons_4.setFrameShadow(QFrame.Plain)

        self.gridLayout_3.addWidget(self.label_title_phonons_4, 14, 0, 1, 4)

        self.textinput_phonons_sd_alpha = QLineEdit(self.tab_environment)
        self.textinput_phonons_sd_alpha.setObjectName(u"textinput_phonons_sd_alpha")
        self.textinput_phonons_sd_alpha.setMinimumSize(QSize(0, 40))
        self.textinput_phonons_sd_alpha.setFont(font)
        self.textinput_phonons_sd_alpha.setFrame(True)
        self.textinput_phonons_sd_alpha.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_sd_alpha, 3, 8, 1, 1)

        self.label_36 = QLabel(self.tab_environment)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_36, 18, 2, 1, 1)

        self.textinput_phonons_sd_wcutoff = QLineEdit(self.tab_environment)
        self.textinput_phonons_sd_wcutoff.setObjectName(u"textinput_phonons_sd_wcutoff")
        self.textinput_phonons_sd_wcutoff.setMinimumSize(QSize(0, 40))
        self.textinput_phonons_sd_wcutoff.setFont(font)
        self.textinput_phonons_sd_wcutoff.setFrame(True)
        self.textinput_phonons_sd_wcutoff.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_sd_wcutoff, 4, 6, 1, 1)

        self.input_phonons_use_qd = QCheckBox(self.tab_environment)
        self.input_phonons_use_qd.setObjectName(u"input_phonons_use_qd")
        self.input_phonons_use_qd.setMinimumSize(QSize(0, 40))
        self.input_phonons_use_qd.setFont(font)

        self.gridLayout_3.addWidget(self.input_phonons_use_qd, 15, 1, 1, 3)

        self.label_title_phonons = QLabel(self.tab_environment)
        self.label_title_phonons.setObjectName(u"label_title_phonons")
        self.label_title_phonons.setMinimumSize(QSize(0, 40))
        self.label_title_phonons.setMaximumSize(QSize(16777215, 40))
        self.label_title_phonons.setFrameShape(QFrame.NoFrame)
        self.label_title_phonons.setFrameShadow(QFrame.Plain)

        self.gridLayout_3.addWidget(self.label_title_phonons, 2, 2, 1, 2)

        self.label_23 = QLabel(self.tab_environment)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_23, 5, 2, 1, 1)

        self.label_28 = QLabel(self.tab_environment)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_28, 5, 5, 1, 1)

        self.textinput_rates_cavity_loss = QLineEdit(self.tab_environment)
        self.textinput_rates_cavity_loss.setObjectName(u"textinput_rates_cavity_loss")
        self.textinput_rates_cavity_loss.setMinimumSize(QSize(0, 40))
        self.textinput_rates_cavity_loss.setFont(font)
        self.textinput_rates_cavity_loss.setFrame(True)
        self.textinput_rates_cavity_loss.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_rates_cavity_loss, 4, 1, 1, 1)

        self.textinput_phonons_sd_qd_cs = QLineEdit(self.tab_environment)
        self.textinput_phonons_sd_qd_cs.setObjectName(u"textinput_phonons_sd_qd_cs")
        self.textinput_phonons_sd_qd_cs.setEnabled(False)
        self.textinput_phonons_sd_qd_cs.setMinimumSize(QSize(0, 40))
        self.textinput_phonons_sd_qd_cs.setFont(font)
        self.textinput_phonons_sd_qd_cs.setFrame(True)
        self.textinput_phonons_sd_qd_cs.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_sd_qd_cs, 17, 3, 1, 1)

        self.textinput_phonons_sd_wdelta = QLineEdit(self.tab_environment)
        self.textinput_phonons_sd_wdelta.setObjectName(u"textinput_phonons_sd_wdelta")
        self.textinput_phonons_sd_wdelta.setMinimumSize(QSize(0, 40))
        self.textinput_phonons_sd_wdelta.setFont(font)
        self.textinput_phonons_sd_wdelta.setFrame(True)
        self.textinput_phonons_sd_wdelta.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_sd_wdelta, 5, 6, 1, 1)

        self.button_reset_phonon_qd = QPushButton(self.tab_environment)
        self.button_reset_phonon_qd.setObjectName(u"button_reset_phonon_qd")
        self.button_reset_phonon_qd.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.button_reset_phonon_qd, 19, 8, 1, 1)

        self.textinput_phonons_sd_qd_aeah_ratio = QLineEdit(self.tab_environment)
        self.textinput_phonons_sd_qd_aeah_ratio.setObjectName(u"textinput_phonons_sd_qd_aeah_ratio")
        self.textinput_phonons_sd_qd_aeah_ratio.setEnabled(False)
        self.textinput_phonons_sd_qd_aeah_ratio.setMinimumSize(QSize(0, 40))
        self.textinput_phonons_sd_qd_aeah_ratio.setFont(font)
        self.textinput_phonons_sd_qd_aeah_ratio.setFrame(True)
        self.textinput_phonons_sd_qd_aeah_ratio.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_sd_qd_aeah_ratio, 18, 1, 1, 1)

        self.textinput_rates_cavity_coupling = QLineEdit(self.tab_environment)
        self.textinput_rates_cavity_coupling.setObjectName(u"textinput_rates_cavity_coupling")
        self.textinput_rates_cavity_coupling.setMinimumSize(QSize(0, 40))
        self.textinput_rates_cavity_coupling.setFont(font)
        self.textinput_rates_cavity_coupling.setFrame(True)
        self.textinput_rates_cavity_coupling.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_rates_cavity_coupling, 3, 1, 1, 1)

        self.label_title_adjust_rates = QLabel(self.tab_environment)
        self.label_title_adjust_rates.setObjectName(u"label_title_adjust_rates")
        self.label_title_adjust_rates.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_title_adjust_rates, 4, 7, 1, 1)

        self.input_phonons_adjust_radiativeloss = QCheckBox(self.tab_environment)
        self.input_phonons_adjust_radiativeloss.setObjectName(u"input_phonons_adjust_radiativeloss")
        self.input_phonons_adjust_radiativeloss.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setBold(True)
        self.input_phonons_adjust_radiativeloss.setFont(font1)
        self.input_phonons_adjust_radiativeloss.setChecked(True)

        self.gridLayout_3.addWidget(self.input_phonons_adjust_radiativeloss, 4, 8, 1, 1)

        self.label_title_adjust_rates_2 = QLabel(self.tab_environment)
        self.label_title_adjust_rates_2.setObjectName(u"label_title_adjust_rates_2")
        self.label_title_adjust_rates_2.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_title_adjust_rates_2, 5, 7, 1, 1)

        self.label_title_adjust_rates_3 = QLabel(self.tab_environment)
        self.label_title_adjust_rates_3.setObjectName(u"label_title_adjust_rates_3")
        self.label_title_adjust_rates_3.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.label_title_adjust_rates_3, 6, 7, 1, 1)

        self.input_phonons_adjust_pure_dephasing = QCheckBox(self.tab_environment)
        self.input_phonons_adjust_pure_dephasing.setObjectName(u"input_phonons_adjust_pure_dephasing")
        self.input_phonons_adjust_pure_dephasing.setMinimumSize(QSize(0, 40))
        self.input_phonons_adjust_pure_dephasing.setFont(font1)

        self.gridLayout_3.addWidget(self.input_phonons_adjust_pure_dephasing, 5, 8, 1, 1)

        self.input_phonons_adjust_renormalization = QCheckBox(self.tab_environment)
        self.input_phonons_adjust_renormalization.setObjectName(u"input_phonons_adjust_renormalization")
        self.input_phonons_adjust_renormalization.setMinimumSize(QSize(0, 40))
        self.input_phonons_adjust_renormalization.setFont(font1)
        self.input_phonons_adjust_renormalization.setChecked(True)

        self.gridLayout_3.addWidget(self.input_phonons_adjust_renormalization, 6, 8, 1, 1)

        self.tabWidget.addTab(self.tab_environment, "")
        self.tab_timeline = QWidget()
        self.tab_timeline.setObjectName(u"tab_timeline")
        self.gridLayout_4 = QGridLayout(self.tab_timeline)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.input_interpolator_t = QComboBox(self.tab_timeline)
        self.input_interpolator_t.addItem("")
        self.input_interpolator_t.addItem("")
        self.input_interpolator_t.addItem("")
        self.input_interpolator_t.addItem("")
        self.input_interpolator_t.setObjectName(u"input_interpolator_t")
        self.input_interpolator_t.setMinimumSize(QSize(0, 40))
        self.input_interpolator_t.setFont(font)
        self.input_interpolator_t.setFocusPolicy(Qt.WheelFocus)
        self.input_interpolator_t.setFrame(True)

        self.gridLayout_4.addWidget(self.input_interpolator_t, 2, 6, 1, 1)

        self.textinput_time_tolerance = QLineEdit(self.tab_timeline)
        self.textinput_time_tolerance.setObjectName(u"textinput_time_tolerance")
        self.textinput_time_tolerance.setMinimumSize(QSize(0, 40))
        self.textinput_time_tolerance.setFont(font)
        self.textinput_time_tolerance.setFrame(True)
        self.textinput_time_tolerance.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.textinput_time_tolerance, 5, 1, 1, 1)

        self.label_12 = QLabel(self.tab_timeline)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 40))

        self.gridLayout_4.addWidget(self.label_12, 1, 5, 1, 1)

        self.textinput_phonons_nc = QLineEdit(self.tab_timeline)
        self.textinput_phonons_nc.setObjectName(u"textinput_phonons_nc")
        self.textinput_phonons_nc.setMinimumSize(QSize(0, 40))
        self.textinput_phonons_nc.setFont(font)
        self.textinput_phonons_nc.setFrame(True)
        self.textinput_phonons_nc.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.textinput_phonons_nc, 4, 6, 1, 1)

        self.button_time_config_grid = QPushButton(self.tab_timeline)
        self.button_time_config_grid.setObjectName(u"button_time_config_grid")
        self.button_time_config_grid.setMinimumSize(QSize(0, 40))
        self.button_time_config_grid.setFont(font1)

        self.gridLayout_4.addWidget(self.button_time_config_grid, 4, 0, 1, 1)

        self.textinput_time_timestep = QLineEdit(self.tab_timeline)
        self.textinput_time_timestep.setObjectName(u"textinput_time_timestep")
        self.textinput_time_timestep.setMinimumSize(QSize(0, 40))
        self.textinput_time_timestep.setFont(font)
        self.textinput_time_timestep.setFrame(True)
        self.textinput_time_timestep.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.textinput_time_timestep, 3, 1, 1, 1)

        self.button_time_config_tol = QPushButton(self.tab_timeline)
        self.button_time_config_tol.setObjectName(u"button_time_config_tol")
        self.button_time_config_tol.setMinimumSize(QSize(0, 40))
        self.button_time_config_tol.setFont(font1)

        self.gridLayout_4.addWidget(self.button_time_config_tol, 5, 0, 1, 1)

        self.label_plot_time_prediction = PlotWidget(self.tab_timeline)
        self.label_plot_time_prediction.setObjectName(u"label_plot_time_prediction")

        self.gridLayout_4.addWidget(self.label_plot_time_prediction, 14, 0, 1, 7)

        self.label_title_time = QLabel(self.tab_timeline)
        self.label_title_time.setObjectName(u"label_title_time")
        self.label_title_time.setMinimumSize(QSize(0, 40))
        self.label_title_time.setMaximumSize(QSize(16777215, 40))
        self.label_title_time.setFrameShape(QFrame.NoFrame)
        self.label_title_time.setFrameShadow(QFrame.Plain)

        self.gridLayout_4.addWidget(self.label_title_time, 0, 0, 1, 2)

        self.button_timeline_force_calculate = QPushButton(self.tab_timeline)
        self.button_timeline_force_calculate.setObjectName(u"button_timeline_force_calculate")
        self.button_timeline_force_calculate.setMinimumSize(QSize(0, 40))

        self.gridLayout_4.addWidget(self.button_timeline_force_calculate, 16, 1, 1, 1)

        self.textinput_time_endtime = QLineEdit(self.tab_timeline)
        self.textinput_time_endtime.setObjectName(u"textinput_time_endtime")
        self.textinput_time_endtime.setMinimumSize(QSize(0, 40))
        self.textinput_time_endtime.setFont(font)
        self.textinput_time_endtime.setFrame(True)
        self.textinput_time_endtime.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.textinput_time_endtime, 2, 1, 1, 1)

        self.input_timeline_enable_phonons = QCheckBox(self.tab_timeline)
        self.input_timeline_enable_phonons.setObjectName(u"input_timeline_enable_phonons")
        self.input_timeline_enable_phonons.setMinimumSize(QSize(0, 40))
        self.input_timeline_enable_phonons.setChecked(True)

        self.gridLayout_4.addWidget(self.input_timeline_enable_phonons, 16, 0, 1, 1)

        self.label_11 = QLabel(self.tab_timeline)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 40))

        self.gridLayout_4.addWidget(self.label_11, 3, 0, 1, 1)

        self.input_interpolator_tau = QComboBox(self.tab_timeline)
        self.input_interpolator_tau.addItem("")
        self.input_interpolator_tau.addItem("")
        self.input_interpolator_tau.setObjectName(u"input_interpolator_tau")
        self.input_interpolator_tau.setMinimumSize(QSize(0, 40))
        self.input_interpolator_tau.setFont(font)
        self.input_interpolator_tau.setFocusPolicy(Qt.WheelFocus)
        self.input_interpolator_tau.setFrame(True)

        self.gridLayout_4.addWidget(self.input_interpolator_tau, 3, 6, 1, 1)

        self.button_next_tab_timeline_to_spectrum = QPushButton(self.tab_timeline)
        self.button_next_tab_timeline_to_spectrum.setObjectName(u"button_next_tab_timeline_to_spectrum")
        self.button_next_tab_timeline_to_spectrum.setMinimumSize(QSize(0, 40))

        self.gridLayout_4.addWidget(self.button_next_tab_timeline_to_spectrum, 16, 6, 1, 1)

        self.textinput_time_startingtime = QLineEdit(self.tab_timeline)
        self.textinput_time_startingtime.setObjectName(u"textinput_time_startingtime")
        self.textinput_time_startingtime.setMinimumSize(QSize(0, 40))
        self.textinput_time_startingtime.setFont(font)
        self.textinput_time_startingtime.setFrame(True)
        self.textinput_time_startingtime.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.textinput_time_startingtime, 1, 1, 1, 1)

        self.label_title_solver = QLabel(self.tab_timeline)
        self.label_title_solver.setObjectName(u"label_title_solver")
        self.label_title_solver.setMinimumSize(QSize(0, 40))
        self.label_title_solver.setMaximumSize(QSize(16777215, 40))
        self.label_title_solver.setFrameShape(QFrame.NoFrame)
        self.label_title_solver.setFrameShadow(QFrame.Plain)

        self.gridLayout_4.addWidget(self.label_title_solver, 0, 5, 1, 2)

        self.textinput_phonons_tsteppath = QLineEdit(self.tab_timeline)
        self.textinput_phonons_tsteppath.setObjectName(u"textinput_phonons_tsteppath")
        self.textinput_phonons_tsteppath.setMinimumSize(QSize(0, 40))
        self.textinput_phonons_tsteppath.setFont(font)
        self.textinput_phonons_tsteppath.setFrame(True)
        self.textinput_phonons_tsteppath.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.textinput_phonons_tsteppath, 5, 6, 1, 1)

        self.label_10 = QLabel(self.tab_timeline)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 40))

        self.gridLayout_4.addWidget(self.label_10, 2, 0, 1, 1)

        self.textinput_time_gridresolution = QLineEdit(self.tab_timeline)
        self.textinput_time_gridresolution.setObjectName(u"textinput_time_gridresolution")
        self.textinput_time_gridresolution.setMinimumSize(QSize(0, 40))
        self.textinput_time_gridresolution.setFont(font)
        self.textinput_time_gridresolution.setFrame(True)
        self.textinput_time_gridresolution.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.textinput_time_gridresolution, 4, 1, 1, 1)

        self.label_9 = QLabel(self.tab_timeline)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 40))

        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_title_predicted_timeline = QLabel(self.tab_timeline)
        self.label_title_predicted_timeline.setObjectName(u"label_title_predicted_timeline")
        self.label_title_predicted_timeline.setMinimumSize(QSize(0, 40))
        self.label_title_predicted_timeline.setMaximumSize(QSize(16777215, 40))
        self.label_title_predicted_timeline.setFrameShape(QFrame.NoFrame)
        self.label_title_predicted_timeline.setFrameShadow(QFrame.Plain)

        self.gridLayout_4.addWidget(self.label_title_predicted_timeline, 13, 0, 1, 7)

        self.input_rungekutta_order = QComboBox(self.tab_timeline)
        self.input_rungekutta_order.addItem("")
        self.input_rungekutta_order.addItem("")
        self.input_rungekutta_order.addItem("")
        self.input_rungekutta_order.addItem("")
        self.input_rungekutta_order.setObjectName(u"input_rungekutta_order")
        self.input_rungekutta_order.setMinimumSize(QSize(0, 40))
        self.input_rungekutta_order.setFont(font)
        self.input_rungekutta_order.setFocusPolicy(Qt.WheelFocus)

        self.gridLayout_4.addWidget(self.input_rungekutta_order, 1, 6, 1, 1)

        self.label_15 = QLabel(self.tab_timeline)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 40))

        self.gridLayout_4.addWidget(self.label_15, 3, 5, 1, 1)

        self.label_41 = QLabel(self.tab_timeline)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(0, 40))

        self.gridLayout_4.addWidget(self.label_41, 5, 5, 1, 1)

        self.label_38 = QLabel(self.tab_timeline)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(0, 40))

        self.gridLayout_4.addWidget(self.label_38, 4, 5, 1, 1)

        self.label_14 = QLabel(self.tab_timeline)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 40))

        self.gridLayout_4.addWidget(self.label_14, 2, 5, 1, 1)

        self.line_14 = QFrame(self.tab_timeline)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setMinimumSize(QSize(0, 40))
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_14, 7, 0, 1, 7)

        self.line_15 = QFrame(self.tab_timeline)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setMinimumSize(QSize(0, 40))
        self.line_15.setFrameShape(QFrame.VLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_15, 0, 3, 6, 1)

        self.tabWidget.addTab(self.tab_timeline, "")
        self.tab_spectrum = QWidget()
        self.tab_spectrum.setObjectName(u"tab_spectrum")
        self.gridLayout_5 = QGridLayout(self.tab_spectrum)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.button_remove_spectrum_from_output = QPushButton(self.tab_spectrum)
        self.button_remove_spectrum_from_output.setObjectName(u"button_remove_spectrum_from_output")
        self.button_remove_spectrum_from_output.setMinimumSize(QSize(0, 40))
        self.button_remove_spectrum_from_output.setFont(font1)

        self.gridLayout_5.addWidget(self.button_remove_spectrum_from_output, 7, 2, 1, 2)

        self.input_timeline_enable_phonons_at_spectra = QCheckBox(self.tab_spectrum)
        self.input_timeline_enable_phonons_at_spectra.setObjectName(u"input_timeline_enable_phonons_at_spectra")
        self.input_timeline_enable_phonons_at_spectra.setMinimumSize(QSize(0, 40))
        self.input_timeline_enable_phonons_at_spectra.setChecked(True)

        self.gridLayout_5.addWidget(self.input_timeline_enable_phonons_at_spectra, 13, 0, 1, 1)

        self.label_49 = QLabel(self.tab_spectrum)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.label_49, 4, 0, 1, 1)

        self.input_spectrum_order = QComboBox(self.tab_spectrum)
        self.input_spectrum_order.addItem("")
        self.input_spectrum_order.addItem("")
        self.input_spectrum_order.setObjectName(u"input_spectrum_order")
        self.input_spectrum_order.setMinimumSize(QSize(0, 40))
        self.input_spectrum_order.setFont(font)

        self.gridLayout_5.addWidget(self.input_spectrum_order, 5, 1, 1, 3)

        self.label_48 = QLabel(self.tab_spectrum)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.label_48, 2, 0, 1, 1)

        self.label_47 = QLabel(self.tab_spectrum)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.label_47, 3, 0, 1, 1)

        self.button_next_tab_spectrum_to_indist = QPushButton(self.tab_spectrum)
        self.button_next_tab_spectrum_to_indist.setObjectName(u"button_next_tab_spectrum_to_indist")
        self.button_next_tab_spectrum_to_indist.setMinimumSize(QSize(0, 40))
        self.button_next_tab_spectrum_to_indist.setCheckable(False)

        self.gridLayout_5.addWidget(self.button_next_tab_spectrum_to_indist, 13, 11, 1, 1)

        self.button_add_spectrum_to_output = QPushButton(self.tab_spectrum)
        self.button_add_spectrum_to_output.setObjectName(u"button_add_spectrum_to_output")
        self.button_add_spectrum_to_output.setMinimumSize(QSize(0, 40))
        self.button_add_spectrum_to_output.setFont(font1)

        self.gridLayout_5.addWidget(self.button_add_spectrum_to_output, 7, 0, 1, 2)

        self.label_title_predicted_spectral = QLabel(self.tab_spectrum)
        self.label_title_predicted_spectral.setObjectName(u"label_title_predicted_spectral")
        self.label_title_predicted_spectral.setMinimumSize(QSize(0, 40))
        self.label_title_predicted_spectral.setMaximumSize(QSize(16777215, 40))
        self.label_title_predicted_spectral.setFrameShape(QFrame.NoFrame)
        self.label_title_predicted_spectral.setFrameShadow(QFrame.Plain)

        self.gridLayout_5.addWidget(self.label_title_predicted_spectral, 9, 0, 1, 12)

        self.textinput_spectrum_center = QLineEdit(self.tab_spectrum)
        self.textinput_spectrum_center.setObjectName(u"textinput_spectrum_center")
        self.textinput_spectrum_center.setMinimumSize(QSize(0, 40))
        self.textinput_spectrum_center.setFont(font)
        self.textinput_spectrum_center.setFrame(True)
        self.textinput_spectrum_center.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.textinput_spectrum_center, 3, 1, 1, 3)

        self.textinput_spectrum_modes = QLineEdit(self.tab_spectrum)
        self.textinput_spectrum_modes.setObjectName(u"textinput_spectrum_modes")
        self.textinput_spectrum_modes.setMinimumSize(QSize(0, 40))
        self.textinput_spectrum_modes.setFont(font)
        self.textinput_spectrum_modes.setFrame(True)
        self.textinput_spectrum_modes.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.textinput_spectrum_modes, 1, 1, 1, 3)

        self.textinput_spectrum_res = QLineEdit(self.tab_spectrum)
        self.textinput_spectrum_res.setObjectName(u"textinput_spectrum_res")
        self.textinput_spectrum_res.setMinimumSize(QSize(0, 40))
        self.textinput_spectrum_res.setFont(font)
        self.textinput_spectrum_res.setFrame(True)
        self.textinput_spectrum_res.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.textinput_spectrum_res, 4, 1, 1, 3)

        self.label_title_set_spectrum = QLabel(self.tab_spectrum)
        self.label_title_set_spectrum.setObjectName(u"label_title_set_spectrum")
        self.label_title_set_spectrum.setMinimumSize(QSize(0, 40))
        self.label_title_set_spectrum.setMaximumSize(QSize(16777215, 40))
        self.label_title_set_spectrum.setFrameShape(QFrame.NoFrame)
        self.label_title_set_spectrum.setFrameShadow(QFrame.Plain)

        self.gridLayout_5.addWidget(self.label_title_set_spectrum, 0, 0, 1, 12)

        self.text_output_list_of_spectra = QListView(self.tab_spectrum)
        self.text_output_list_of_spectra.setObjectName(u"text_output_list_of_spectra")
        self.text_output_list_of_spectra.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.text_output_list_of_spectra, 1, 4, 7, 8)

        self.label_51 = QLabel(self.tab_spectrum)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.label_51, 6, 0, 1, 1)

        self.input_spectrum_normalize = QCheckBox(self.tab_spectrum)
        self.input_spectrum_normalize.setObjectName(u"input_spectrum_normalize")
        self.input_spectrum_normalize.setMinimumSize(QSize(0, 40))
        self.input_spectrum_normalize.setFont(font)
        self.input_spectrum_normalize.setChecked(False)

        self.gridLayout_5.addWidget(self.input_spectrum_normalize, 6, 1, 1, 3)

        self.textinput_spectrum_range = QLineEdit(self.tab_spectrum)
        self.textinput_spectrum_range.setObjectName(u"textinput_spectrum_range")
        self.textinput_spectrum_range.setMinimumSize(QSize(0, 40))
        self.textinput_spectrum_range.setFont(font)
        self.textinput_spectrum_range.setFrame(True)
        self.textinput_spectrum_range.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.textinput_spectrum_range, 2, 1, 1, 3)

        self.button_timeline_force_calculate_spectra = QPushButton(self.tab_spectrum)
        self.button_timeline_force_calculate_spectra.setObjectName(u"button_timeline_force_calculate_spectra")
        self.button_timeline_force_calculate_spectra.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.button_timeline_force_calculate_spectra, 13, 10, 1, 1)

        self.label_plot_spectral_prediction = PlotWidget(self.tab_spectrum)
        self.label_plot_spectral_prediction.setObjectName(u"label_plot_spectral_prediction")

        self.gridLayout_5.addWidget(self.label_plot_spectral_prediction, 10, 0, 1, 12)

        self.label_50 = QLabel(self.tab_spectrum)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.label_50, 5, 0, 1, 1)

        self.line_13 = QFrame(self.tab_spectrum)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setMinimumSize(QSize(0, 40))
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_13, 8, 0, 1, 12)

        self.button_add_spectrum_mode = QPushButton(self.tab_spectrum)
        self.button_add_spectrum_mode.setObjectName(u"button_add_spectrum_mode")
        self.button_add_spectrum_mode.setMinimumSize(QSize(0, 40))
        self.button_add_spectrum_mode.setFont(font1)

        self.gridLayout_5.addWidget(self.button_add_spectrum_mode, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_spectrum, "")
        self.tab_indist = QWidget()
        self.tab_indist.setObjectName(u"tab_indist")
        self.gridLayout_7 = QGridLayout(self.tab_indist)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.text_output_list_of_indists = QListView(self.tab_indist)
        self.text_output_list_of_indists.setObjectName(u"text_output_list_of_indists")
        self.text_output_list_of_indists.setMinimumSize(QSize(0, 40))

        self.gridLayout_7.addWidget(self.text_output_list_of_indists, 2, 1, 1, 6)

        self.button_next_tab_indist_to_conc = QPushButton(self.tab_indist)
        self.button_next_tab_indist_to_conc.setObjectName(u"button_next_tab_indist_to_conc")
        self.button_next_tab_indist_to_conc.setMinimumSize(QSize(0, 40))
        self.button_next_tab_indist_to_conc.setCheckable(False)

        self.gridLayout_7.addWidget(self.button_next_tab_indist_to_conc, 3, 6, 1, 1)

        self.textinput_indist_modes = QLineEdit(self.tab_indist)
        self.textinput_indist_modes.setObjectName(u"textinput_indist_modes")
        self.textinput_indist_modes.setMinimumSize(QSize(0, 40))
        self.textinput_indist_modes.setFont(font)
        self.textinput_indist_modes.setFrame(True)
        self.textinput_indist_modes.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.textinput_indist_modes, 1, 2, 1, 1)

        self.label_title_set_indists = QLabel(self.tab_indist)
        self.label_title_set_indists.setObjectName(u"label_title_set_indists")
        self.label_title_set_indists.setMinimumSize(QSize(0, 40))
        self.label_title_set_indists.setFrameShape(QFrame.NoFrame)
        self.label_title_set_indists.setFrameShadow(QFrame.Plain)

        self.gridLayout_7.addWidget(self.label_title_set_indists, 0, 0, 1, 7)

        self.button_add_indist_to_output = QPushButton(self.tab_indist)
        self.button_add_indist_to_output.setObjectName(u"button_add_indist_to_output")
        self.button_add_indist_to_output.setMinimumSize(QSize(0, 40))
        self.button_add_indist_to_output.setFont(font1)

        self.gridLayout_7.addWidget(self.button_add_indist_to_output, 1, 3, 1, 1)

        self.button_remove_indist_from_output = QPushButton(self.tab_indist)
        self.button_remove_indist_from_output.setObjectName(u"button_remove_indist_from_output")
        self.button_remove_indist_from_output.setMinimumSize(QSize(0, 40))
        self.button_remove_indist_from_output.setFont(font1)

        self.gridLayout_7.addWidget(self.button_remove_indist_from_output, 1, 6, 1, 1)

        self.button_add_indist_mode = QPushButton(self.tab_indist)
        self.button_add_indist_mode.setObjectName(u"button_add_indist_mode")
        self.button_add_indist_mode.setMinimumSize(QSize(0, 40))
        self.button_add_indist_mode.setFont(font1)

        self.gridLayout_7.addWidget(self.button_add_indist_mode, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_indist, "")
        self.tab_concurrence = QWidget()
        self.tab_concurrence.setObjectName(u"tab_concurrence")
        self.gridLayout = QGridLayout(self.tab_concurrence)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_114 = QLabel(self.tab_concurrence)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setMinimumSize(QSize(0, 40))
        self.label_114.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.label_114, 11, 0, 1, 1)

        self.label_115 = QLabel(self.tab_concurrence)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setMinimumSize(QSize(0, 40))
        self.label_115.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.label_115, 12, 0, 1, 1)

        self.label_55 = QLabel(self.tab_concurrence)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(0, 40))
        self.label_55.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.label_55, 9, 0, 1, 1)

        self.label_113 = QLabel(self.tab_concurrence)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMinimumSize(QSize(0, 40))
        self.label_113.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.label_113, 10, 0, 1, 1)

        self.button_add_concurrence_to_output = QPushButton(self.tab_concurrence)
        self.button_add_concurrence_to_output.setObjectName(u"button_add_concurrence_to_output")
        self.button_add_concurrence_to_output.setMinimumSize(QSize(0, 40))
        self.button_add_concurrence_to_output.setFont(font1)

        self.gridLayout.addWidget(self.button_add_concurrence_to_output, 5, 0, 1, 2)

        self.button_remove_concurrence_from_output = QPushButton(self.tab_concurrence)
        self.button_remove_concurrence_from_output.setObjectName(u"button_remove_concurrence_from_output")
        self.button_remove_concurrence_from_output.setMinimumSize(QSize(0, 40))
        self.button_remove_concurrence_from_output.setFont(font1)

        self.gridLayout.addWidget(self.button_remove_concurrence_from_output, 5, 2, 1, 1)

        self.label_title_set_concurrences = QLabel(self.tab_concurrence)
        self.label_title_set_concurrences.setObjectName(u"label_title_set_concurrences")
        self.label_title_set_concurrences.setMinimumSize(QSize(0, 40))
        self.label_title_set_concurrences.setMaximumSize(QSize(16777215, 40))
        self.label_title_set_concurrences.setFrameShape(QFrame.NoFrame)
        self.label_title_set_concurrences.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.label_title_set_concurrences, 2, 0, 1, 3)

        self.textinput_concurrence_first = QLineEdit(self.tab_concurrence)
        self.textinput_concurrence_first.setObjectName(u"textinput_concurrence_first")
        self.textinput_concurrence_first.setMinimumSize(QSize(0, 40))
        self.textinput_concurrence_first.setFont(font)
        self.textinput_concurrence_first.setFrame(True)
        self.textinput_concurrence_first.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_concurrence_first, 3, 1, 1, 2)

        self.textinput_concurrence_second = QLineEdit(self.tab_concurrence)
        self.textinput_concurrence_second.setObjectName(u"textinput_concurrence_second")
        self.textinput_concurrence_second.setMinimumSize(QSize(0, 40))
        self.textinput_concurrence_second.setFont(font)
        self.textinput_concurrence_second.setFrame(True)
        self.textinput_concurrence_second.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_concurrence_second, 4, 1, 1, 2)

        self.text_output_list_of_concurrences = QListView(self.tab_concurrence)
        self.text_output_list_of_concurrences.setObjectName(u"text_output_list_of_concurrences")
        self.text_output_list_of_concurrences.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.text_output_list_of_concurrences, 6, 0, 1, 3)

        self.label_title_set_concurrences_2 = QLabel(self.tab_concurrence)
        self.label_title_set_concurrences_2.setObjectName(u"label_title_set_concurrences_2")
        self.label_title_set_concurrences_2.setMinimumSize(QSize(0, 40))
        self.label_title_set_concurrences_2.setMaximumSize(QSize(16777215, 40))
        self.label_title_set_concurrences_2.setFrameShape(QFrame.NoFrame)
        self.label_title_set_concurrences_2.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.label_title_set_concurrences_2, 8, 0, 1, 3)

        self.input_concurrence_add_spectra = QCheckBox(self.tab_concurrence)
        self.input_concurrence_add_spectra.setObjectName(u"input_concurrence_add_spectra")
        self.input_concurrence_add_spectra.setMinimumSize(QSize(0, 40))
        self.input_concurrence_add_spectra.setFont(font)
        self.input_concurrence_add_spectra.setChecked(False)

        self.gridLayout.addWidget(self.input_concurrence_add_spectra, 9, 1, 1, 2)

        self.textinput_concurrence_spec_freq = QLineEdit(self.tab_concurrence)
        self.textinput_concurrence_spec_freq.setObjectName(u"textinput_concurrence_spec_freq")
        self.textinput_concurrence_spec_freq.setEnabled(False)
        self.textinput_concurrence_spec_freq.setMinimumSize(QSize(0, 40))
        self.textinput_concurrence_spec_freq.setFont(font)
        self.textinput_concurrence_spec_freq.setFrame(True)
        self.textinput_concurrence_spec_freq.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_concurrence_spec_freq, 10, 1, 1, 2)

        self.textinput_concurrence_spec_range = QLineEdit(self.tab_concurrence)
        self.textinput_concurrence_spec_range.setObjectName(u"textinput_concurrence_spec_range")
        self.textinput_concurrence_spec_range.setEnabled(False)
        self.textinput_concurrence_spec_range.setMinimumSize(QSize(0, 40))
        self.textinput_concurrence_spec_range.setFont(font)
        self.textinput_concurrence_spec_range.setFrame(True)
        self.textinput_concurrence_spec_range.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_concurrence_spec_range, 11, 1, 1, 2)

        self.textinput_concurrence_spec_res = QLineEdit(self.tab_concurrence)
        self.textinput_concurrence_spec_res.setObjectName(u"textinput_concurrence_spec_res")
        self.textinput_concurrence_spec_res.setEnabled(False)
        self.textinput_concurrence_spec_res.setMinimumSize(QSize(0, 40))
        self.textinput_concurrence_spec_res.setFont(font)
        self.textinput_concurrence_spec_res.setFrame(True)
        self.textinput_concurrence_spec_res.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_concurrence_spec_res, 12, 1, 1, 2)

        self.button_next_tab_sconc_to_stats = QPushButton(self.tab_concurrence)
        self.button_next_tab_sconc_to_stats.setObjectName(u"button_next_tab_sconc_to_stats")
        self.button_next_tab_sconc_to_stats.setMinimumSize(QSize(0, 40))
        self.button_next_tab_sconc_to_stats.setMaximumSize(QSize(200, 16777215))
        self.button_next_tab_sconc_to_stats.setCheckable(False)

        self.gridLayout.addWidget(self.button_next_tab_sconc_to_stats, 13, 2, 1, 1)

        self.line_12 = QFrame(self.tab_concurrence)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setMinimumSize(QSize(0, 40))
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_12, 7, 0, 1, 3)

        self.button_add_concurrence_mode_1 = QPushButton(self.tab_concurrence)
        self.button_add_concurrence_mode_1.setObjectName(u"button_add_concurrence_mode_1")
        self.button_add_concurrence_mode_1.setMinimumSize(QSize(0, 40))
        self.button_add_concurrence_mode_1.setFont(font1)

        self.gridLayout.addWidget(self.button_add_concurrence_mode_1, 3, 0, 1, 1)

        self.button_add_concurrence_mode_2 = QPushButton(self.tab_concurrence)
        self.button_add_concurrence_mode_2.setObjectName(u"button_add_concurrence_mode_2")
        self.button_add_concurrence_mode_2.setMinimumSize(QSize(0, 40))
        self.button_add_concurrence_mode_2.setFont(font1)

        self.gridLayout.addWidget(self.button_add_concurrence_mode_2, 4, 0, 1, 1)

        self.tabWidget.addTab(self.tab_concurrence, "")
        self.tab_additional_stats = QWidget()
        self.tab_additional_stats.setObjectName(u"tab_additional_stats")
        self.gridLayout_8 = QGridLayout(self.tab_additional_stats)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_title_set_wigner_2 = QLabel(self.tab_additional_stats)
        self.label_title_set_wigner_2.setObjectName(u"label_title_set_wigner_2")
        self.label_title_set_wigner_2.setMinimumSize(QSize(0, 40))
        self.label_title_set_wigner_2.setMaximumSize(QSize(16777215, 40))
        self.label_title_set_wigner_2.setFrameShape(QFrame.NoFrame)
        self.label_title_set_wigner_2.setFrameShadow(QFrame.Plain)

        self.gridLayout_8.addWidget(self.label_title_set_wigner_2, 0, 0, 1, 2)

        self.textinput_correlation_modes = QLineEdit(self.tab_additional_stats)
        self.textinput_correlation_modes.setObjectName(u"textinput_correlation_modes")
        self.textinput_correlation_modes.setMinimumSize(QSize(0, 40))
        self.textinput_correlation_modes.setFont(font)
        self.textinput_correlation_modes.setFrame(True)
        self.textinput_correlation_modes.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.textinput_correlation_modes, 1, 1, 1, 1)

        self.text_output_list_of_gfuncs = QListView(self.tab_additional_stats)
        self.text_output_list_of_gfuncs.setObjectName(u"text_output_list_of_gfuncs")
        self.text_output_list_of_gfuncs.setMinimumSize(QSize(0, 40))

        self.gridLayout_8.addWidget(self.text_output_list_of_gfuncs, 1, 2, 3, 1)

        self.label_57 = QLabel(self.tab_additional_stats)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(0, 40))
        self.label_57.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_8.addWidget(self.label_57, 2, 0, 1, 1)

        self.input_gfunc_order = QComboBox(self.tab_additional_stats)
        self.input_gfunc_order.addItem("")
        self.input_gfunc_order.addItem("")
        self.input_gfunc_order.setObjectName(u"input_gfunc_order")
        self.input_gfunc_order.setMinimumSize(QSize(0, 40))
        self.input_gfunc_order.setFont(font)

        self.gridLayout_8.addWidget(self.input_gfunc_order, 2, 1, 1, 1)

        self.label_116 = QLabel(self.tab_additional_stats)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setMinimumSize(QSize(0, 40))
        self.label_116.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_8.addWidget(self.label_116, 3, 0, 1, 1)

        self.input_gfunc_integration = QComboBox(self.tab_additional_stats)
        self.input_gfunc_integration.addItem("")
        self.input_gfunc_integration.addItem("")
        self.input_gfunc_integration.addItem("")
        self.input_gfunc_integration.setObjectName(u"input_gfunc_integration")
        self.input_gfunc_integration.setMinimumSize(QSize(0, 40))
        self.input_gfunc_integration.setFont(font)

        self.gridLayout_8.addWidget(self.input_gfunc_integration, 3, 1, 1, 1)

        self.button_add_gfunc_to_output = QPushButton(self.tab_additional_stats)
        self.button_add_gfunc_to_output.setObjectName(u"button_add_gfunc_to_output")
        self.button_add_gfunc_to_output.setMinimumSize(QSize(0, 40))
        self.button_add_gfunc_to_output.setFont(font1)

        self.gridLayout_8.addWidget(self.button_add_gfunc_to_output, 4, 0, 1, 1)

        self.button_remove_gfunc_from_output = QPushButton(self.tab_additional_stats)
        self.button_remove_gfunc_from_output.setObjectName(u"button_remove_gfunc_from_output")
        self.button_remove_gfunc_from_output.setMinimumSize(QSize(0, 40))
        self.button_remove_gfunc_from_output.setFont(font1)

        self.gridLayout_8.addWidget(self.button_remove_gfunc_from_output, 4, 1, 1, 1)

        self.line_11 = QFrame(self.tab_additional_stats)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setMinimumSize(QSize(0, 40))
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout_8.addWidget(self.line_11, 5, 0, 1, 4)

        self.label_title_set_wigner = QLabel(self.tab_additional_stats)
        self.label_title_set_wigner.setObjectName(u"label_title_set_wigner")
        self.label_title_set_wigner.setMinimumSize(QSize(0, 40))
        self.label_title_set_wigner.setMaximumSize(QSize(16777215, 40))
        self.label_title_set_wigner.setFrameShape(QFrame.NoFrame)
        self.label_title_set_wigner.setFrameShadow(QFrame.Plain)

        self.gridLayout_8.addWidget(self.label_title_set_wigner, 6, 0, 1, 2)

        self.textinput_wigner_modes = QLineEdit(self.tab_additional_stats)
        self.textinput_wigner_modes.setObjectName(u"textinput_wigner_modes")
        self.textinput_wigner_modes.setMinimumSize(QSize(0, 40))
        self.textinput_wigner_modes.setFont(font)
        self.textinput_wigner_modes.setFrame(True)
        self.textinput_wigner_modes.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.textinput_wigner_modes, 7, 1, 1, 1)

        self.text_output_list_of_wigner_funcs = QListView(self.tab_additional_stats)
        self.text_output_list_of_wigner_funcs.setObjectName(u"text_output_list_of_wigner_funcs")
        self.text_output_list_of_wigner_funcs.setMinimumSize(QSize(600, 40))

        self.gridLayout_8.addWidget(self.text_output_list_of_wigner_funcs, 7, 2, 3, 2)

        self.label_123 = QLabel(self.tab_additional_stats)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setMinimumSize(QSize(0, 40))
        self.label_123.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_8.addWidget(self.label_123, 8, 0, 1, 1)

        self.textinput_wigner_x = QLineEdit(self.tab_additional_stats)
        self.textinput_wigner_x.setObjectName(u"textinput_wigner_x")
        self.textinput_wigner_x.setMinimumSize(QSize(0, 40))
        self.textinput_wigner_x.setFont(font)
        self.textinput_wigner_x.setFrame(True)
        self.textinput_wigner_x.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.textinput_wigner_x, 8, 1, 1, 1)

        self.label_124 = QLabel(self.tab_additional_stats)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setMinimumSize(QSize(0, 40))
        self.label_124.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_8.addWidget(self.label_124, 9, 0, 1, 1)

        self.textinput_wigner_y = QLineEdit(self.tab_additional_stats)
        self.textinput_wigner_y.setObjectName(u"textinput_wigner_y")
        self.textinput_wigner_y.setMinimumSize(QSize(0, 40))
        self.textinput_wigner_y.setFont(font)
        self.textinput_wigner_y.setFrame(True)
        self.textinput_wigner_y.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.textinput_wigner_y, 9, 1, 1, 1)

        self.label_125 = QLabel(self.tab_additional_stats)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setMinimumSize(QSize(0, 40))
        self.label_125.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_8.addWidget(self.label_125, 10, 0, 1, 1)

        self.textinput_wigner_resolution = QLineEdit(self.tab_additional_stats)
        self.textinput_wigner_resolution.setObjectName(u"textinput_wigner_resolution")
        self.textinput_wigner_resolution.setMinimumSize(QSize(0, 40))
        self.textinput_wigner_resolution.setFont(font)
        self.textinput_wigner_resolution.setFrame(True)
        self.textinput_wigner_resolution.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.textinput_wigner_resolution, 10, 1, 1, 1)

        self.label_126 = QLabel(self.tab_additional_stats)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setMinimumSize(QSize(0, 40))
        self.label_126.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_8.addWidget(self.label_126, 11, 0, 1, 1)

        self.textinput_wigner_skip = QLineEdit(self.tab_additional_stats)
        self.textinput_wigner_skip.setObjectName(u"textinput_wigner_skip")
        self.textinput_wigner_skip.setMinimumSize(QSize(0, 40))
        self.textinput_wigner_skip.setFont(font)
        self.textinput_wigner_skip.setFrame(True)
        self.textinput_wigner_skip.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.textinput_wigner_skip, 11, 1, 1, 1)

        self.button_add_wigner = QPushButton(self.tab_additional_stats)
        self.button_add_wigner.setObjectName(u"button_add_wigner")
        self.button_add_wigner.setMinimumSize(QSize(0, 40))
        self.button_add_wigner.setFont(font1)

        self.gridLayout_8.addWidget(self.button_add_wigner, 12, 0, 1, 1)

        self.button_remove_wigner = QPushButton(self.tab_additional_stats)
        self.button_remove_wigner.setObjectName(u"button_remove_wigner")
        self.button_remove_wigner.setMinimumSize(QSize(0, 40))
        self.button_remove_wigner.setFont(font1)

        self.gridLayout_8.addWidget(self.button_remove_wigner, 12, 1, 1, 1)

        self.button_next_tab_stats_to_detector = QPushButton(self.tab_additional_stats)
        self.button_next_tab_stats_to_detector.setObjectName(u"button_next_tab_stats_to_detector")
        self.button_next_tab_stats_to_detector.setMinimumSize(QSize(0, 40))
        self.button_next_tab_stats_to_detector.setCheckable(False)

        self.gridLayout_8.addWidget(self.button_next_tab_stats_to_detector, 12, 3, 1, 1)

        self.button_add_gfunc_mode = QPushButton(self.tab_additional_stats)
        self.button_add_gfunc_mode.setObjectName(u"button_add_gfunc_mode")
        self.button_add_gfunc_mode.setMinimumSize(QSize(0, 40))
        self.button_add_gfunc_mode.setFont(font1)

        self.gridLayout_8.addWidget(self.button_add_gfunc_mode, 1, 0, 1, 1)

        self.button_add_wigner_mode = QPushButton(self.tab_additional_stats)
        self.button_add_wigner_mode.setObjectName(u"button_add_wigner_mode")
        self.button_add_wigner_mode.setMinimumSize(QSize(0, 40))
        self.button_add_wigner_mode.setFont(font1)

        self.gridLayout_8.addWidget(self.button_add_wigner_mode, 7, 0, 1, 1)

        self.tabWidget.addTab(self.tab_additional_stats, "")
        self.tab_detector = QWidget()
        self.tab_detector.setObjectName(u"tab_detector")
        self.gridLayout_9 = QGridLayout(self.tab_detector)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.textinput_detector_t0 = QLineEdit(self.tab_detector)
        self.textinput_detector_t0.setObjectName(u"textinput_detector_t0")
        self.textinput_detector_t0.setMinimumSize(QSize(0, 40))
        self.textinput_detector_t0.setFont(font)
        self.textinput_detector_t0.setFrame(True)
        self.textinput_detector_t0.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.textinput_detector_t0, 1, 1, 1, 1)

        self.label_128 = QLabel(self.tab_detector)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setMinimumSize(QSize(0, 40))
        self.label_128.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_9.addWidget(self.label_128, 2, 0, 1, 1)

        self.textinput_detector_tpower = QLineEdit(self.tab_detector)
        self.textinput_detector_tpower.setObjectName(u"textinput_detector_tpower")
        self.textinput_detector_tpower.setMinimumSize(QSize(0, 40))
        self.textinput_detector_tpower.setFont(font)
        self.textinput_detector_tpower.setFrame(True)
        self.textinput_detector_tpower.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.textinput_detector_tpower, 3, 1, 1, 1)

        self.label_title_set_detector_2 = QLabel(self.tab_detector)
        self.label_title_set_detector_2.setObjectName(u"label_title_set_detector_2")
        self.label_title_set_detector_2.setMinimumSize(QSize(0, 40))
        self.label_title_set_detector_2.setMaximumSize(QSize(16777215, 40))
        self.label_title_set_detector_2.setFrameShape(QFrame.NoFrame)
        self.label_title_set_detector_2.setFrameShadow(QFrame.Plain)

        self.gridLayout_9.addWidget(self.label_title_set_detector_2, 6, 0, 1, 10)

        self.text_output_list_of_detector_spec = QListView(self.tab_detector)
        self.text_output_list_of_detector_spec.setObjectName(u"text_output_list_of_detector_spec")
        self.text_output_list_of_detector_spec.setMinimumSize(QSize(499, 40))

        self.gridLayout_9.addWidget(self.text_output_list_of_detector_spec, 7, 2, 5, 8)

        self.button_add_detector_time = QPushButton(self.tab_detector)
        self.button_add_detector_time.setObjectName(u"button_add_detector_time")
        self.button_add_detector_time.setMinimumSize(QSize(0, 40))
        self.button_add_detector_time.setFont(font1)

        self.gridLayout_9.addWidget(self.button_add_detector_time, 4, 0, 1, 1)

        self.label_title_set_detector = QLabel(self.tab_detector)
        self.label_title_set_detector.setObjectName(u"label_title_set_detector")
        self.label_title_set_detector.setMinimumSize(QSize(0, 40))
        self.label_title_set_detector.setMaximumSize(QSize(16777215, 40))
        self.label_title_set_detector.setFrameShape(QFrame.NoFrame)
        self.label_title_set_detector.setFrameShadow(QFrame.Plain)

        self.gridLayout_9.addWidget(self.label_title_set_detector, 0, 0, 1, 10)

        self.button_next_tab_detector_to_generate = QPushButton(self.tab_detector)
        self.button_next_tab_detector_to_generate.setObjectName(u"button_next_tab_detector_to_generate")
        self.button_next_tab_detector_to_generate.setMinimumSize(QSize(0, 40))
        self.button_next_tab_detector_to_generate.setCheckable(False)

        self.gridLayout_9.addWidget(self.button_next_tab_detector_to_generate, 12, 9, 1, 1)

        self.label_117 = QLabel(self.tab_detector)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setMinimumSize(QSize(0, 40))
        self.label_117.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_9.addWidget(self.label_117, 1, 0, 1, 1)

        self.button_remove_detector_time = QPushButton(self.tab_detector)
        self.button_remove_detector_time.setObjectName(u"button_remove_detector_time")
        self.button_remove_detector_time.setMinimumSize(QSize(0, 40))
        self.button_remove_detector_time.setFont(font1)

        self.gridLayout_9.addWidget(self.button_remove_detector_time, 4, 1, 1, 1)

        self.label_118 = QLabel(self.tab_detector)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMinimumSize(QSize(0, 40))
        self.label_118.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_9.addWidget(self.label_118, 3, 0, 1, 1)

        self.textinput_detector_t1 = QLineEdit(self.tab_detector)
        self.textinput_detector_t1.setObjectName(u"textinput_detector_t1")
        self.textinput_detector_t1.setMinimumSize(QSize(0, 40))
        self.textinput_detector_t1.setFont(font)
        self.textinput_detector_t1.setFrame(True)
        self.textinput_detector_t1.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.textinput_detector_t1, 2, 1, 1, 1)

        self.textinput_detector_wcenter = QLineEdit(self.tab_detector)
        self.textinput_detector_wcenter.setObjectName(u"textinput_detector_wcenter")
        self.textinput_detector_wcenter.setMinimumSize(QSize(0, 40))
        self.textinput_detector_wcenter.setFont(font)
        self.textinput_detector_wcenter.setFrame(True)
        self.textinput_detector_wcenter.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.textinput_detector_wcenter, 7, 1, 1, 1)

        self.textinput_detector_wrange = QLineEdit(self.tab_detector)
        self.textinput_detector_wrange.setObjectName(u"textinput_detector_wrange")
        self.textinput_detector_wrange.setMinimumSize(QSize(0, 40))
        self.textinput_detector_wrange.setFont(font)
        self.textinput_detector_wrange.setFrame(True)
        self.textinput_detector_wrange.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.textinput_detector_wrange, 8, 1, 1, 1)

        self.label_119 = QLabel(self.tab_detector)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setMinimumSize(QSize(0, 40))

        self.gridLayout_9.addWidget(self.label_119, 8, 0, 1, 1)

        self.label_121 = QLabel(self.tab_detector)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setMinimumSize(QSize(0, 40))

        self.gridLayout_9.addWidget(self.label_121, 7, 0, 1, 1)

        self.label_127 = QLabel(self.tab_detector)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setMinimumSize(QSize(0, 40))

        self.gridLayout_9.addWidget(self.label_127, 9, 0, 1, 1)

        self.textinput_detector_wnum = QLineEdit(self.tab_detector)
        self.textinput_detector_wnum.setObjectName(u"textinput_detector_wnum")
        self.textinput_detector_wnum.setMinimumSize(QSize(0, 40))
        self.textinput_detector_wnum.setFont(font)
        self.textinput_detector_wnum.setFrame(True)
        self.textinput_detector_wnum.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.textinput_detector_wnum, 9, 1, 1, 1)

        self.label_120 = QLabel(self.tab_detector)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setMinimumSize(QSize(0, 40))

        self.gridLayout_9.addWidget(self.label_120, 10, 0, 1, 1)

        self.textinput_detector_wpower = QLineEdit(self.tab_detector)
        self.textinput_detector_wpower.setObjectName(u"textinput_detector_wpower")
        self.textinput_detector_wpower.setMinimumSize(QSize(0, 40))
        self.textinput_detector_wpower.setFont(font)
        self.textinput_detector_wpower.setFrame(True)
        self.textinput_detector_wpower.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.textinput_detector_wpower, 10, 1, 1, 1)

        self.button_add_detector_spectral = QPushButton(self.tab_detector)
        self.button_add_detector_spectral.setObjectName(u"button_add_detector_spectral")
        self.button_add_detector_spectral.setMinimumSize(QSize(0, 40))
        self.button_add_detector_spectral.setFont(font1)

        self.gridLayout_9.addWidget(self.button_add_detector_spectral, 11, 0, 1, 1)

        self.button_remove_detector_spectral = QPushButton(self.tab_detector)
        self.button_remove_detector_spectral.setObjectName(u"button_remove_detector_spectral")
        self.button_remove_detector_spectral.setMinimumSize(QSize(0, 40))
        self.button_remove_detector_spectral.setFont(font1)

        self.gridLayout_9.addWidget(self.button_remove_detector_spectral, 11, 1, 1, 1)

        self.text_output_list_of_detector_time = QListView(self.tab_detector)
        self.text_output_list_of_detector_time.setObjectName(u"text_output_list_of_detector_time")
        self.text_output_list_of_detector_time.setMinimumSize(QSize(499, 40))

        self.gridLayout_9.addWidget(self.text_output_list_of_detector_time, 1, 2, 4, 8)

        self.tabWidget.addTab(self.tab_detector, "")
        self.tab_output = QWidget()
        self.tab_output.setObjectName(u"tab_output")
        self.gridLayout_10 = QGridLayout(self.tab_output)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.text_output_list_of_custom_expvals = QListView(self.tab_output)
        self.text_output_list_of_custom_expvals.setObjectName(u"text_output_list_of_custom_expvals")

        self.gridLayout_10.addWidget(self.text_output_list_of_custom_expvals, 10, 3, 2, 5)

        self.input_logginglevel = QComboBox(self.tab_output)
        self.input_logginglevel.addItem("")
        self.input_logginglevel.addItem("")
        self.input_logginglevel.addItem("")
        self.input_logginglevel.setObjectName(u"input_logginglevel")
        self.input_logginglevel.setMinimumSize(QSize(0, 40))
        self.input_logginglevel.setFont(font)
        self.input_logginglevel.setFocusPolicy(Qt.WheelFocus)
        self.input_logginglevel.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")

        self.gridLayout_10.addWidget(self.input_logginglevel, 0, 2, 1, 6)

        self.input_dm_frame = QComboBox(self.tab_output)
        self.input_dm_frame.addItem("")
        self.input_dm_frame.addItem("")
        self.input_dm_frame.setObjectName(u"input_dm_frame")
        self.input_dm_frame.setMinimumSize(QSize(0, 40))
        self.input_dm_frame.setFont(font)
        self.input_dm_frame.setFocusPolicy(Qt.WheelFocus)
        self.input_dm_frame.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-top-right-radius: 0px; border-bottom-left-radius: 0px; border-top-width: 0px;")
        self.input_dm_frame.setFrame(True)

        self.gridLayout_10.addWidget(self.input_dm_frame, 2, 2, 1, 6)

        self.label_64 = QLabel(self.tab_output)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(0, 0))
        self.label_64.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_10.addWidget(self.label_64, 2, 0, 1, 2)

        self.label_65 = QLabel(self.tab_output)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(0, 0))
        self.label_65.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_10.addWidget(self.label_65, 9, 0, 1, 7)

        self.input_add_output_greenf = QCheckBox(self.tab_output)
        self.input_add_output_greenf.setObjectName(u"input_add_output_greenf")
        self.input_add_output_greenf.setMinimumSize(QSize(0, 0))
        self.input_add_output_greenf.setFont(font1)
        self.input_add_output_greenf.setChecked(False)

        self.gridLayout_10.addWidget(self.input_add_output_greenf, 6, 2, 1, 2)

        self.input_add_output_rkerror = QCheckBox(self.tab_output)
        self.input_add_output_rkerror.setObjectName(u"input_add_output_rkerror")
        self.input_add_output_rkerror.setMinimumSize(QSize(0, 0))
        self.input_add_output_rkerror.setFont(font1)
        self.input_add_output_rkerror.setChecked(False)

        self.gridLayout_10.addWidget(self.input_add_output_rkerror, 4, 6, 1, 1)

        self.input_add_output_phononcoeffs = QCheckBox(self.tab_output)
        self.input_add_output_phononcoeffs.setObjectName(u"input_add_output_phononcoeffs")
        self.input_add_output_phononcoeffs.setMinimumSize(QSize(0, 0))
        self.input_add_output_phononcoeffs.setFont(font1)
        self.input_add_output_phononcoeffs.setChecked(False)

        self.gridLayout_10.addWidget(self.input_add_output_phononcoeffs, 6, 4, 1, 2)

        self.input_add_output_phononj = QCheckBox(self.tab_output)
        self.input_add_output_phononj.setObjectName(u"input_add_output_phononj")
        self.input_add_output_phononj.setMinimumSize(QSize(0, 0))
        self.input_add_output_phononj.setFont(font1)
        self.input_add_output_phononj.setChecked(False)

        self.gridLayout_10.addWidget(self.input_add_output_phononj, 5, 7, 1, 1)

        self.button_add_custom_expval_matrix = QPushButton(self.tab_output)
        self.button_add_custom_expval_matrix.setObjectName(u"button_add_custom_expval_matrix")
        self.button_add_custom_expval_matrix.setMinimumSize(QSize(0, 40))
        self.button_add_custom_expval_matrix.setFont(font1)

        self.gridLayout_10.addWidget(self.button_add_custom_expval_matrix, 10, 0, 1, 3)

        self.input_add_output_detecotrtrafo = QCheckBox(self.tab_output)
        self.input_add_output_detecotrtrafo.setObjectName(u"input_add_output_detecotrtrafo")
        self.input_add_output_detecotrtrafo.setMinimumSize(QSize(0, 0))
        self.input_add_output_detecotrtrafo.setFont(font1)
        self.input_add_output_detecotrtrafo.setChecked(False)

        self.gridLayout_10.addWidget(self.input_add_output_detecotrtrafo, 5, 2, 1, 2)

        self.input_add_output_chirp_fourier = QCheckBox(self.tab_output)
        self.input_add_output_chirp_fourier.setObjectName(u"input_add_output_chirp_fourier")
        self.input_add_output_chirp_fourier.setMinimumSize(QSize(0, 0))
        self.input_add_output_chirp_fourier.setFont(font1)
        self.input_add_output_chirp_fourier.setChecked(False)

        self.gridLayout_10.addWidget(self.input_add_output_chirp_fourier, 5, 4, 1, 2)

        self.input_add_output_eigenvalues = QCheckBox(self.tab_output)
        self.input_add_output_eigenvalues.setObjectName(u"input_add_output_eigenvalues")
        self.input_add_output_eigenvalues.setMinimumSize(QSize(0, 0))
        self.input_add_output_eigenvalues.setFont(font1)
        self.input_add_output_eigenvalues.setChecked(False)

        self.gridLayout_10.addWidget(self.input_add_output_eigenvalues, 4, 2, 1, 2)

        self.input_add_output_tpm = QCheckBox(self.tab_output)
        self.input_add_output_tpm.setObjectName(u"input_add_output_tpm")
        self.input_add_output_tpm.setMinimumSize(QSize(0, 0))
        self.input_add_output_tpm.setFont(font1)
        self.input_add_output_tpm.setChecked(False)

        self.gridLayout_10.addWidget(self.input_add_output_tpm, 6, 6, 1, 1)

        self.label_63 = QLabel(self.tab_output)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(0, 0))
        self.label_63.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_10.addWidget(self.label_63, 1, 0, 1, 2)

        self.input_add_output_operators = QCheckBox(self.tab_output)
        self.input_add_output_operators.setObjectName(u"input_add_output_operators")
        self.input_add_output_operators.setMinimumSize(QSize(0, 0))
        self.input_add_output_operators.setFont(font1)
        self.input_add_output_operators.setChecked(False)

        self.gridLayout_10.addWidget(self.input_add_output_operators, 4, 4, 1, 2)

        self.label_62 = QLabel(self.tab_output)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(0, 0))
        self.label_62.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_10.addWidget(self.label_62, 0, 0, 1, 2)

        self.label_61 = QLabel(self.tab_output)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(0, 0))
        self.label_61.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_10.addWidget(self.label_61, 3, 0, 1, 2)

        self.textinput_cpucores = QLineEdit(self.tab_output)
        self.textinput_cpucores.setObjectName(u"textinput_cpucores")
        self.textinput_cpucores.setMinimumSize(QSize(0, 40))
        self.textinput_cpucores.setFont(font)
        self.textinput_cpucores.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")
        self.textinput_cpucores.setFrame(True)
        self.textinput_cpucores.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.textinput_cpucores, 3, 2, 1, 6)

        self.button_remove_custom_expval_matrix = QPushButton(self.tab_output)
        self.button_remove_custom_expval_matrix.setObjectName(u"button_remove_custom_expval_matrix")
        self.button_remove_custom_expval_matrix.setMinimumSize(QSize(0, 40))
        self.button_remove_custom_expval_matrix.setFont(font1)

        self.gridLayout_10.addWidget(self.button_remove_custom_expval_matrix, 11, 0, 1, 3)

        self.input_add_output_pulse_fourier = QCheckBox(self.tab_output)
        self.input_add_output_pulse_fourier.setObjectName(u"input_add_output_pulse_fourier")
        self.input_add_output_pulse_fourier.setMinimumSize(QSize(0, 0))
        self.input_add_output_pulse_fourier.setFont(font1)
        self.input_add_output_pulse_fourier.setChecked(False)

        self.gridLayout_10.addWidget(self.input_add_output_pulse_fourier, 5, 6, 1, 1)

        self.input_add_output_concurrence_eigs = QCheckBox(self.tab_output)
        self.input_add_output_concurrence_eigs.setObjectName(u"input_add_output_concurrence_eigs")
        self.input_add_output_concurrence_eigs.setMinimumSize(QSize(0, 0))
        self.input_add_output_concurrence_eigs.setFont(font1)
        self.input_add_output_concurrence_eigs.setChecked(False)

        self.gridLayout_10.addWidget(self.input_add_output_concurrence_eigs, 6, 7, 1, 1)

        self.label_60 = QLabel(self.tab_output)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(0, 0))

        self.gridLayout_10.addWidget(self.label_60, 4, 0, 1, 2)

        self.input_add_output_vonneumannpath = QCheckBox(self.tab_output)
        self.input_add_output_vonneumannpath.setObjectName(u"input_add_output_vonneumannpath")
        self.input_add_output_vonneumannpath.setMinimumSize(QSize(0, 0))
        self.input_add_output_vonneumannpath.setFont(font1)
        self.input_add_output_vonneumannpath.setChecked(False)

        self.gridLayout_10.addWidget(self.input_add_output_vonneumannpath, 4, 7, 1, 1)

        self.input_dm_mode = QComboBox(self.tab_output)
        self.input_dm_mode.addItem("")
        self.input_dm_mode.addItem("")
        self.input_dm_mode.addItem("")
        self.input_dm_mode.setObjectName(u"input_dm_mode")
        self.input_dm_mode.setMinimumSize(QSize(0, 40))
        self.input_dm_mode.setFont(font)
        self.input_dm_mode.setFocusPolicy(Qt.WheelFocus)
        self.input_dm_mode.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-right-radius: 0px; border-bottom-left-radius: 0px;")
        self.input_dm_mode.setFrame(True)

        self.gridLayout_10.addWidget(self.input_dm_mode, 1, 2, 1, 6)

        self.input_add_output_photon_expv = QCheckBox(self.tab_output)
        self.input_add_output_photon_expv.setObjectName(u"input_add_output_photon_expv")
        self.input_add_output_photon_expv.setMinimumSize(QSize(0, 0))
        self.input_add_output_photon_expv.setFont(font1)
        self.input_add_output_photon_expv.setChecked(False)

        self.gridLayout_10.addWidget(self.input_add_output_photon_expv, 7, 2, 1, 1)

        self.tabWidget.addTab(self.tab_output, "")
        self.tab_generate = QWidget()
        self.tab_generate.setObjectName(u"tab_generate")
        self.gridLayout_12 = QGridLayout(self.tab_generate)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.input_path_to_qdacc = HoverButton(self.tab_generate)
        self.input_path_to_qdacc.setObjectName(u"input_path_to_qdacc")
        self.input_path_to_qdacc.setMinimumSize(QSize(0, 40))

        self.gridLayout_12.addWidget(self.input_path_to_qdacc, 11, 1, 1, 1)

        self.progressBar = QProgressBar(self.tab_generate)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout_12.addWidget(self.progressBar, 10, 1, 1, 2)

        self.label_58 = QLabel(self.tab_generate)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(0, 0))
        self.label_58.setFrameShape(QFrame.NoFrame)
        self.label_58.setFrameShadow(QFrame.Plain)

        self.gridLayout_12.addWidget(self.label_58, 0, 0, 1, 8)

        self.button_change_rungstring_to_settingfile = HoverButton(self.tab_generate)
        self.button_change_rungstring_to_settingfile.setObjectName(u"button_change_rungstring_to_settingfile")
        self.button_change_rungstring_to_settingfile.setMinimumSize(QSize(0, 40))

        self.gridLayout_12.addWidget(self.button_change_rungstring_to_settingfile, 17, 4, 1, 2)

        self.textinput_file_destination = QLineEdit(self.tab_generate)
        self.textinput_file_destination.setObjectName(u"textinput_file_destination")
        self.textinput_file_destination.setMinimumSize(QSize(0, 40))
        self.textinput_file_destination.setFont(font)
        self.textinput_file_destination.setFrame(True)
        self.textinput_file_destination.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.textinput_file_destination, 12, 2, 1, 1)

        self.text_output_program_qdacc_command = QTextBrowser(self.tab_generate)
        self.text_output_program_qdacc_command.setObjectName(u"text_output_program_qdacc_command")
        self.text_output_program_qdacc_command.setMinimumSize(QSize(600, 0))
        self.text_output_program_qdacc_command.setFrameShape(QFrame.NoFrame)
        self.text_output_program_qdacc_command.setReadOnly(False)

        self.gridLayout_12.addWidget(self.text_output_program_qdacc_command, 1, 4, 1, 4)

        self.line_4 = QFrame(self.tab_generate)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_12.addWidget(self.line_4, 1, 3, 17, 1)

        self.textinput_file_qdacc = QLineEdit(self.tab_generate)
        self.textinput_file_qdacc.setObjectName(u"textinput_file_qdacc")
        self.textinput_file_qdacc.setMinimumSize(QSize(0, 40))
        self.textinput_file_qdacc.setFont(font)
        self.textinput_file_qdacc.setFrame(True)
        self.textinput_file_qdacc.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.textinput_file_qdacc, 11, 2, 1, 1)

        self.input_destination = HoverButton(self.tab_generate)
        self.input_destination.setObjectName(u"input_destination")
        self.input_destination.setMinimumSize(QSize(0, 40))

        self.gridLayout_12.addWidget(self.input_destination, 12, 1, 1, 1)

        self.input_escape_output_command = QCheckBox(self.tab_generate)
        self.input_escape_output_command.setObjectName(u"input_escape_output_command")
        self.input_escape_output_command.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.input_escape_output_command.setFont(font2)
        self.input_escape_output_command.setChecked(False)

        self.gridLayout_12.addWidget(self.input_escape_output_command, 17, 6, 1, 2)

        self.button_empty_destination_folder = HoverButton(self.tab_generate)
        self.button_empty_destination_folder.setObjectName(u"button_empty_destination_folder")
        self.button_empty_destination_folder.setMinimumSize(QSize(0, 40))

        self.gridLayout_12.addWidget(self.button_empty_destination_folder, 17, 2, 1, 1)

        self.button_open_destination_folder = HoverButton(self.tab_generate)
        self.button_open_destination_folder.setObjectName(u"button_open_destination_folder")
        self.button_open_destination_folder.setMinimumSize(QSize(0, 40))

        self.gridLayout_12.addWidget(self.button_open_destination_folder, 17, 1, 1, 1)

        self.text_output_program_main = TextBrowserExternal(self.tab_generate)
        self.text_output_program_main.setObjectName(u"text_output_program_main")
        self.text_output_program_main.setMinimumSize(QSize(600, 0))
        self.text_output_program_main.setFrameShape(QFrame.NoFrame)
        self.text_output_program_main.setLineWrapMode(QTextEdit.NoWrap)
        self.text_output_program_main.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.text_output_program_main.setOpenExternalLinks(True)
        self.text_output_program_main.setOpenLinks(True)

        self.gridLayout_12.addWidget(self.text_output_program_main, 1, 0, 3, 3)

        self.button_generate_run = QPushButton(self.tab_generate)
        self.button_generate_run.setObjectName(u"button_generate_run")
        self.button_generate_run.setEnabled(True)
        self.button_generate_run.setMinimumSize(QSize(0, 40))
        self.button_generate_run.setFont(font1)
        self.button_generate_run.setStyleSheet(u"QPushButton {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #f4771e, stop:0.91 #4f2609); color: #ffffff;}\n"
"QPushButton::hover {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #f7954f, stop:0.91 #4f2609); color: #ffffff;}")
        self.button_generate_run.setCheckable(False)
        self.button_generate_run.setChecked(False)

        self.gridLayout_12.addWidget(self.button_generate_run, 4, 4, 1, 2)

        self.button_generate_copy = QPushButton(self.tab_generate)
        self.button_generate_copy.setObjectName(u"button_generate_copy")
        self.button_generate_copy.setEnabled(True)
        self.button_generate_copy.setMinimumSize(QSize(0, 40))
        self.button_generate_copy.setFont(font1)
        self.button_generate_copy.setStyleSheet(u"QPushButton {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #f4771e, stop:0.91 #4f2609); color: #ffffff;}\n"
"QPushButton::hover {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #f7954f, stop:0.91 #4f2609); color: #ffffff;}")
        self.button_generate_copy.setCheckable(False)
        self.button_generate_copy.setChecked(False)

        self.gridLayout_12.addWidget(self.button_generate_copy, 4, 6, 1, 2)

        self.button_run_kill = QPushButton(self.tab_generate)
        self.button_run_kill.setObjectName(u"button_run_kill")
        self.button_run_kill.setEnabled(True)
        self.button_run_kill.setMinimumSize(QSize(0, 40))
        self.button_run_kill.setFont(font1)
        self.button_run_kill.setStyleSheet(u"QPushButton {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #f4331e, stop:0.91 #450f0a); color: #ffffff;}\n"
"QPushButton::hover {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #a62214, stop:0.91 #450f0a); color: #ffffff;}")
        self.button_run_kill.setCheckable(False)
        self.button_run_kill.setChecked(False)

        self.gridLayout_12.addWidget(self.button_run_kill, 10, 6, 1, 2)

        self.button_run_program = QPushButton(self.tab_generate)
        self.button_run_program.setObjectName(u"button_run_program")
        self.button_run_program.setEnabled(True)
        self.button_run_program.setMinimumSize(QSize(0, 40))
        self.button_run_program.setFont(font1)
        self.button_run_program.setStyleSheet(u"QPushButton {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #288c14, stop:0.91 #0d3006); color: #ffffff;}\n"
"QPushButton::hover {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #55ba41, stop:0.91 #0d3006); color: #ffffff;}")
        self.button_run_program.setIconSize(QSize(32, 32))
        self.button_run_program.setCheckable(False)
        self.button_run_program.setChecked(False)

        self.gridLayout_12.addWidget(self.button_run_program, 10, 4, 1, 2)

        self.input_plot_mode = QComboBox(self.tab_generate)
        self.input_plot_mode.addItem("")
        self.input_plot_mode.addItem("")
        self.input_plot_mode.addItem("")
        self.input_plot_mode.setObjectName(u"input_plot_mode")
        self.input_plot_mode.setMinimumSize(QSize(0, 40))
        self.input_plot_mode.setStyleSheet(u"QComboBox {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #3f1d5c, stop:0.91 #1c0d29); color: #ffffff;}\n"
"QComboBox::hover {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #582980, stop:0.91 #1c0d29); color: #ffffff;}")
        self.input_plot_mode.setFrame(False)

        self.gridLayout_12.addWidget(self.input_plot_mode, 12, 6, 1, 2)

        self.button_plot_everything = QPushButton(self.tab_generate)
        self.button_plot_everything.setObjectName(u"button_plot_everything")
        self.button_plot_everything.setMinimumSize(QSize(0, 40))
        self.button_plot_everything.setStyleSheet(u"QPushButton {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #3f1d5c, stop:0.91 #1c0d29); color: #ffffff;}\n"
"QPushButton::hover {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #582980, stop:0.91 #1c0d29); color: #ffffff;}")
        self.button_plot_everything.setIconSize(QSize(32, 32))

        self.gridLayout_12.addWidget(self.button_plot_everything, 12, 4, 1, 2)

        self.button_run_external = QPushButton(self.tab_generate)
        self.button_run_external.setObjectName(u"button_run_external")
        self.button_run_external.setEnabled(True)
        self.button_run_external.setMinimumSize(QSize(0, 40))
        self.button_run_external.setFont(font1)
        self.button_run_external.setStyleSheet(u"QPushButton {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #1e6cf4, stop:0.91 #133e8d); color: #ffffff;}\n"
"QPushButton::hover {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #5d94f5, stop:0.91 #133e8d); color: #ffffff;}")
        self.button_run_external.setCheckable(False)
        self.button_run_external.setChecked(False)

        self.gridLayout_12.addWidget(self.button_run_external, 11, 6, 1, 2)

        self.button_run_and_plot = QPushButton(self.tab_generate)
        self.button_run_and_plot.setObjectName(u"button_run_and_plot")
        self.button_run_and_plot.setEnabled(True)
        self.button_run_and_plot.setMinimumSize(QSize(0, 40))
        self.button_run_and_plot.setFont(font1)
        self.button_run_and_plot.setStyleSheet(u"QPushButton {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #1e6cf4, stop:0.91 #133e8d); color: #ffffff;}\n"
"QPushButton::hover {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #5d94f5, stop:0.91 #133e8d); color: #ffffff;}")
        self.button_run_and_plot.setCheckable(False)
        self.button_run_and_plot.setChecked(False)

        self.gridLayout_12.addWidget(self.button_run_and_plot, 11, 4, 1, 2)

        self.tabWidget.addTab(self.tab_generate, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_6 = QGridLayout(self.tab_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_title_qdsystem_5 = QLabel(self.tab_5)
        self.label_title_qdsystem_5.setObjectName(u"label_title_qdsystem_5")
        self.label_title_qdsystem_5.setMinimumSize(QSize(0, 40))
        self.label_title_qdsystem_5.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_5.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_5.setFrameShadow(QFrame.Plain)

        self.gridLayout_6.addWidget(self.label_title_qdsystem_5, 3, 2, 1, 1)

        self.textinput_path_to_settingfile = QLineEdit(self.tab_5)
        self.textinput_path_to_settingfile.setObjectName(u"textinput_path_to_settingfile")
        self.textinput_path_to_settingfile.setMinimumSize(QSize(0, 40))
        self.textinput_path_to_settingfile.setFont(font)
        self.textinput_path_to_settingfile.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")
        self.textinput_path_to_settingfile.setFrame(True)
        self.textinput_path_to_settingfile.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.textinput_path_to_settingfile, 13, 1, 1, 1)

        self.label_title_qdsystem_9 = QLabel(self.tab_5)
        self.label_title_qdsystem_9.setObjectName(u"label_title_qdsystem_9")
        self.label_title_qdsystem_9.setMinimumSize(QSize(0, 40))
        self.label_title_qdsystem_9.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_9.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_9.setFrameShadow(QFrame.Plain)

        self.gridLayout_6.addWidget(self.label_title_qdsystem_9, 8, 2, 1, 1)

        self.label_title_qdsystem_13 = QLabel(self.tab_5)
        self.label_title_qdsystem_13.setObjectName(u"label_title_qdsystem_13")
        self.label_title_qdsystem_13.setMinimumSize(QSize(0, 40))
        self.label_title_qdsystem_13.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_13.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_13.setFrameShadow(QFrame.Plain)

        self.gridLayout_6.addWidget(self.label_title_qdsystem_13, 10, 2, 1, 1)

        self.button_sweeper_get_runstring = HoverButton(self.tab_5)
        self.button_sweeper_get_runstring.setObjectName(u"button_sweeper_get_runstring")
        self.button_sweeper_get_runstring.setMinimumSize(QSize(0, 40))

        self.gridLayout_6.addWidget(self.button_sweeper_get_runstring, 12, 0, 1, 2)

        self.label_title_qdsystem_2 = QLabel(self.tab_5)
        self.label_title_qdsystem_2.setObjectName(u"label_title_qdsystem_2")
        self.label_title_qdsystem_2.setMinimumSize(QSize(0, 40))
        self.label_title_qdsystem_2.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_2.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_2.setFrameShadow(QFrame.Plain)

        self.gridLayout_6.addWidget(self.label_title_qdsystem_2, 1, 2, 1, 1)

        self.label_title_qdsystem_10 = QLabel(self.tab_5)
        self.label_title_qdsystem_10.setObjectName(u"label_title_qdsystem_10")
        self.label_title_qdsystem_10.setMinimumSize(QSize(0, 40))
        self.label_title_qdsystem_10.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_10.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_10.setFrameShadow(QFrame.Plain)

        self.gridLayout_6.addWidget(self.label_title_qdsystem_10, 9, 2, 1, 1)

        self.label_3 = QLabel(self.tab_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 40))

        self.gridLayout_6.addWidget(self.label_3, 15, 0, 1, 2)

        self.plot_sweep_parameter_first = PlotWidget(self.tab_5)
        self.plot_sweep_parameter_first.setObjectName(u"plot_sweep_parameter_first")
        self.plot_sweep_parameter_first.setMinimumSize(QSize(400, 150))

        self.gridLayout_6.addWidget(self.plot_sweep_parameter_first, 12, 2, 4, 2)

        self.line = QFrame(self.tab_5)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 40))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line, 6, 2, 1, 3)

        self.label_title_qdsystem_4 = QLabel(self.tab_5)
        self.label_title_qdsystem_4.setObjectName(u"label_title_qdsystem_4")
        self.label_title_qdsystem_4.setMinimumSize(QSize(0, 40))
        self.label_title_qdsystem_4.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_4.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_4.setFrameShadow(QFrame.Plain)

        self.gridLayout_6.addWidget(self.label_title_qdsystem_4, 2, 2, 1, 1)

        self.label_title_qdsystem_8 = QLabel(self.tab_5)
        self.label_title_qdsystem_8.setObjectName(u"label_title_qdsystem_8")
        self.label_title_qdsystem_8.setMinimumSize(QSize(0, 40))
        self.label_title_qdsystem_8.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_8.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_8.setFrameShadow(QFrame.Plain)

        self.gridLayout_6.addWidget(self.label_title_qdsystem_8, 7, 2, 1, 1)

        self.button_sweeper_plot = QPushButton(self.tab_5)
        self.button_sweeper_plot.setObjectName(u"button_sweeper_plot")
        self.button_sweeper_plot.setMinimumSize(QSize(0, 40))
        self.button_sweeper_plot.setStyleSheet(u"QPushButton {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #f4771e, stop:0.91 #4f2609); color: #ffffff;}\n"
"QPushButton::hover {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #f7954f, stop:0.91 #4f2609); color: #ffffff;}")

        self.gridLayout_6.addWidget(self.button_sweeper_plot, 14, 0, 1, 2)

        self.label_title_qdsystem_3 = QLabel(self.tab_5)
        self.label_title_qdsystem_3.setObjectName(u"label_title_qdsystem_3")
        self.label_title_qdsystem_3.setMinimumSize(QSize(0, 40))
        self.label_title_qdsystem_3.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_3.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_3.setFrameShadow(QFrame.Plain)

        self.gridLayout_6.addWidget(self.label_title_qdsystem_3, 0, 0, 1, 2)

        self.label_title_qdsystem_12 = QLabel(self.tab_5)
        self.label_title_qdsystem_12.setObjectName(u"label_title_qdsystem_12")
        self.label_title_qdsystem_12.setMinimumSize(QSize(0, 40))
        self.label_title_qdsystem_12.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_12.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_12.setFrameShadow(QFrame.Plain)

        self.gridLayout_6.addWidget(self.label_title_qdsystem_12, 4, 2, 1, 1)

        self.button_set_setting_file_path = HoverButton(self.tab_5)
        self.button_set_setting_file_path.setObjectName(u"button_set_setting_file_path")
        self.button_set_setting_file_path.setMinimumSize(QSize(0, 40))

        self.gridLayout_6.addWidget(self.button_set_setting_file_path, 13, 0, 1, 1)

        self.plot_sweep_parameter_second = PlotWidget(self.tab_5)
        self.plot_sweep_parameter_second.setObjectName(u"plot_sweep_parameter_second")
        self.plot_sweep_parameter_second.setMinimumSize(QSize(400, 150))

        self.gridLayout_6.addWidget(self.plot_sweep_parameter_second, 12, 4, 4, 1)

        self.label_title_qdsystem_7 = QLabel(self.tab_5)
        self.label_title_qdsystem_7.setObjectName(u"label_title_qdsystem_7")
        self.label_title_qdsystem_7.setMinimumSize(QSize(0, 40))
        self.label_title_qdsystem_7.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_7.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_7.setFrameShadow(QFrame.Plain)

        self.gridLayout_6.addWidget(self.label_title_qdsystem_7, 0, 2, 1, 3)

        self.checkbox_activate_scan_parameter_1 = QCheckBox(self.tab_5)
        self.checkbox_activate_scan_parameter_1.setObjectName(u"checkbox_activate_scan_parameter_1")
        self.checkbox_activate_scan_parameter_1.setMinimumSize(QSize(0, 40))

        self.gridLayout_6.addWidget(self.checkbox_activate_scan_parameter_1, 1, 3, 1, 2)

        self.textinput_scan_parameter_1_from = QLineEdit(self.tab_5)
        self.textinput_scan_parameter_1_from.setObjectName(u"textinput_scan_parameter_1_from")
        self.textinput_scan_parameter_1_from.setMinimumSize(QSize(0, 40))

        self.gridLayout_6.addWidget(self.textinput_scan_parameter_1_from, 2, 3, 1, 2)

        self.textinput_scan_parameter_1_to = QLineEdit(self.tab_5)
        self.textinput_scan_parameter_1_to.setObjectName(u"textinput_scan_parameter_1_to")
        self.textinput_scan_parameter_1_to.setMinimumSize(QSize(0, 40))

        self.gridLayout_6.addWidget(self.textinput_scan_parameter_1_to, 3, 3, 1, 2)

        self.textinput_scan_parameter_1_points = QLineEdit(self.tab_5)
        self.textinput_scan_parameter_1_points.setObjectName(u"textinput_scan_parameter_1_points")
        self.textinput_scan_parameter_1_points.setMinimumSize(QSize(0, 40))

        self.gridLayout_6.addWidget(self.textinput_scan_parameter_1_points, 4, 3, 1, 2)

        self.checkbox_activate_scan_parameter_2 = QCheckBox(self.tab_5)
        self.checkbox_activate_scan_parameter_2.setObjectName(u"checkbox_activate_scan_parameter_2")
        self.checkbox_activate_scan_parameter_2.setMinimumSize(QSize(0, 40))

        self.gridLayout_6.addWidget(self.checkbox_activate_scan_parameter_2, 7, 3, 1, 2)

        self.textinput_scan_parameter_2_from = QLineEdit(self.tab_5)
        self.textinput_scan_parameter_2_from.setObjectName(u"textinput_scan_parameter_2_from")
        self.textinput_scan_parameter_2_from.setMinimumSize(QSize(0, 40))

        self.gridLayout_6.addWidget(self.textinput_scan_parameter_2_from, 8, 3, 1, 2)

        self.textinput_scan_parameter_2_to = QLineEdit(self.tab_5)
        self.textinput_scan_parameter_2_to.setObjectName(u"textinput_scan_parameter_2_to")
        self.textinput_scan_parameter_2_to.setMinimumSize(QSize(0, 40))
        self.textinput_scan_parameter_2_to.setStyleSheet(u"b")

        self.gridLayout_6.addWidget(self.textinput_scan_parameter_2_to, 9, 3, 1, 2)

        self.textinput_scan_parameter_2_points = QLineEdit(self.tab_5)
        self.textinput_scan_parameter_2_points.setObjectName(u"textinput_scan_parameter_2_points")
        self.textinput_scan_parameter_2_points.setMinimumSize(QSize(0, 40))
        self.textinput_scan_parameter_2_points.setStyleSheet(u"b")

        self.gridLayout_6.addWidget(self.textinput_scan_parameter_2_points, 10, 3, 1, 2)

        self.text_output_program_qdacc_command_sweep_display = QTextBrowser(self.tab_5)
        self.text_output_program_qdacc_command_sweep_display.setObjectName(u"text_output_program_qdacc_command_sweep_display")
        self.text_output_program_qdacc_command_sweep_display.setMinimumSize(QSize(599, 40))
        self.text_output_program_qdacc_command_sweep_display.setFrameShape(QFrame.NoFrame)
        self.text_output_program_qdacc_command_sweep_display.setLineWrapMode(QTextEdit.NoWrap)
        self.text_output_program_qdacc_command_sweep_display.setReadOnly(True)

        self.gridLayout_6.addWidget(self.text_output_program_qdacc_command_sweep_display, 6, 0, 6, 2)

        self.text_output_program_qdacc_command_sweep = QTextBrowser(self.tab_5)
        self.text_output_program_qdacc_command_sweep.setObjectName(u"text_output_program_qdacc_command_sweep")
        self.text_output_program_qdacc_command_sweep.setMinimumSize(QSize(599, 40))
        self.text_output_program_qdacc_command_sweep.setFrameShape(QFrame.NoFrame)
        self.text_output_program_qdacc_command_sweep.setReadOnly(False)

        self.gridLayout_6.addWidget(self.text_output_program_qdacc_command_sweep, 1, 0, 5, 2)

        self.combobox_p1_input = QComboBox(self.tab_5)
        self.combobox_p1_input.addItem("")
        self.combobox_p1_input.addItem("")
        self.combobox_p1_input.addItem("")
        self.combobox_p1_input.addItem("")
        self.combobox_p1_input.addItem("")
        self.combobox_p1_input.setObjectName(u"combobox_p1_input")
        self.combobox_p1_input.setMinimumSize(QSize(0, 40))

        self.gridLayout_6.addWidget(self.combobox_p1_input, 5, 2, 1, 1)

        self.combobox_p2_input = QComboBox(self.tab_5)
        self.combobox_p2_input.addItem("")
        self.combobox_p2_input.addItem("")
        self.combobox_p2_input.addItem("")
        self.combobox_p2_input.addItem("")
        self.combobox_p2_input.addItem("")
        self.combobox_p2_input.setObjectName(u"combobox_p2_input")
        self.combobox_p2_input.setMinimumSize(QSize(0, 40))

        self.gridLayout_6.addWidget(self.combobox_p2_input, 11, 2, 1, 1)

        self.textinput_scan_parameter_1_lambda = QLineEdit(self.tab_5)
        self.textinput_scan_parameter_1_lambda.setObjectName(u"textinput_scan_parameter_1_lambda")
        self.textinput_scan_parameter_1_lambda.setMinimumSize(QSize(0, 40))

        self.gridLayout_6.addWidget(self.textinput_scan_parameter_1_lambda, 5, 3, 1, 2)

        self.textinput_scan_parameter_2_lambda = QLineEdit(self.tab_5)
        self.textinput_scan_parameter_2_lambda.setObjectName(u"textinput_scan_parameter_2_lambda")
        self.textinput_scan_parameter_2_lambda.setMinimumSize(QSize(0, 40))
        self.textinput_scan_parameter_2_lambda.setStyleSheet(u"b")

        self.gridLayout_6.addWidget(self.textinput_scan_parameter_2_lambda, 11, 3, 1, 2)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_11 = QGridLayout(self.tab_8)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.button_optimizer_files = HoverButton(self.tab_8)
        self.button_optimizer_files.setObjectName(u"button_optimizer_files")
        self.button_optimizer_files.setMinimumSize(QSize(0, 40))

        self.gridLayout_11.addWidget(self.button_optimizer_files, 1, 2, 1, 1)

        self.text_output_program_qdacc_command_sweep_display_2 = QTextBrowser(self.tab_8)
        self.text_output_program_qdacc_command_sweep_display_2.setObjectName(u"text_output_program_qdacc_command_sweep_display_2")
        self.text_output_program_qdacc_command_sweep_display_2.setMinimumSize(QSize(599, 200))
        self.text_output_program_qdacc_command_sweep_display_2.setFrameShape(QFrame.NoFrame)
        self.text_output_program_qdacc_command_sweep_display_2.setLineWrapMode(QTextEdit.NoWrap)
        self.text_output_program_qdacc_command_sweep_display_2.setReadOnly(True)

        self.gridLayout_11.addWidget(self.text_output_program_qdacc_command_sweep_display_2, 0, 2, 1, 7)

        self.label_title_qdsystem_22 = QLabel(self.tab_8)
        self.label_title_qdsystem_22.setObjectName(u"label_title_qdsystem_22")
        self.label_title_qdsystem_22.setMinimumSize(QSize(0, 40))
        self.label_title_qdsystem_22.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_22.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_22.setFrameShadow(QFrame.Plain)

        self.gridLayout_11.addWidget(self.label_title_qdsystem_22, 13, 2, 1, 1)

        self.label_title_qdsystem_17 = QLabel(self.tab_8)
        self.label_title_qdsystem_17.setObjectName(u"label_title_qdsystem_17")
        self.label_title_qdsystem_17.setMinimumSize(QSize(0, 40))
        self.label_title_qdsystem_17.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_17.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_17.setFrameShadow(QFrame.Plain)

        self.gridLayout_11.addWidget(self.label_title_qdsystem_17, 8, 2, 1, 1)

        self.label_title_qdsystem_6 = QLabel(self.tab_8)
        self.label_title_qdsystem_6.setObjectName(u"label_title_qdsystem_6")
        self.label_title_qdsystem_6.setMinimumSize(QSize(0, 40))
        self.label_title_qdsystem_6.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_6.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_6.setFrameShadow(QFrame.Plain)

        self.gridLayout_11.addWidget(self.label_title_qdsystem_6, 5, 2, 1, 1)

        self.label_plot_optimizer_1 = PlotWidget(self.tab_8)
        self.label_plot_optimizer_1.setObjectName(u"label_plot_optimizer_1")
        self.label_plot_optimizer_1.setMinimumSize(QSize(300, 200))
        self.label_plot_optimizer_1.setStyleSheet(u"background-color: b")

        self.gridLayout_11.addWidget(self.label_plot_optimizer_1, 10, 0, 9, 1)

        self.button_optimizer_optimize = QPushButton(self.tab_8)
        self.button_optimizer_optimize.setObjectName(u"button_optimizer_optimize")
        self.button_optimizer_optimize.setMinimumSize(QSize(0, 40))
        self.button_optimizer_optimize.setStyleSheet(u"QPushButton {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #288c14, stop:0.91 #0d3006); color: #ffffff;}\n"
"QPushButton::hover {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #55ba41, stop:0.91 #0d3006); color: #ffffff;}")

        self.gridLayout_11.addWidget(self.button_optimizer_optimize, 8, 0, 1, 2)

        self.button_optimizer_get_runstring = HoverButton(self.tab_8)
        self.button_optimizer_get_runstring.setObjectName(u"button_optimizer_get_runstring")
        self.button_optimizer_get_runstring.setMinimumSize(QSize(0, 40))

        self.gridLayout_11.addWidget(self.button_optimizer_get_runstring, 5, 0, 1, 2)

        self.button_optimizer_fitness_function = HoverButton(self.tab_8)
        self.button_optimizer_fitness_function.setObjectName(u"button_optimizer_fitness_function")
        self.button_optimizer_fitness_function.setMinimumSize(QSize(0, 40))

        self.gridLayout_11.addWidget(self.button_optimizer_fitness_function, 9, 2, 1, 1)

        self.button_optimizer_runstring_to_main = HoverButton(self.tab_8)
        self.button_optimizer_runstring_to_main.setObjectName(u"button_optimizer_runstring_to_main")
        self.button_optimizer_runstring_to_main.setMinimumSize(QSize(0, 40))

        self.gridLayout_11.addWidget(self.button_optimizer_runstring_to_main, 9, 0, 1, 2)

        self.button_optimizer_files_2 = HoverButton(self.tab_8)
        self.button_optimizer_files_2.setObjectName(u"button_optimizer_files_2")
        self.button_optimizer_files_2.setMinimumSize(QSize(0, 40))

        self.gridLayout_11.addWidget(self.button_optimizer_files_2, 2, 2, 1, 1)

        self.label_title_qdsystem_14 = QLabel(self.tab_8)
        self.label_title_qdsystem_14.setObjectName(u"label_title_qdsystem_14")
        self.label_title_qdsystem_14.setMinimumSize(QSize(0, 40))
        self.label_title_qdsystem_14.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_14.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_14.setFrameShadow(QFrame.Plain)

        self.gridLayout_11.addWidget(self.label_title_qdsystem_14, 4, 2, 1, 1)

        self.label_plot_optimizer_3 = PlotWidget(self.tab_8)
        self.label_plot_optimizer_3.setObjectName(u"label_plot_optimizer_3")
        self.label_plot_optimizer_3.setMinimumSize(QSize(0, 200))
        self.label_plot_optimizer_3.setStyleSheet(u"background-color: b")

        self.gridLayout_11.addWidget(self.label_plot_optimizer_3, 18, 1, 1, 1)

        self.label_title_qdsystem_21 = QLabel(self.tab_8)
        self.label_title_qdsystem_21.setObjectName(u"label_title_qdsystem_21")
        self.label_title_qdsystem_21.setMinimumSize(QSize(0, 40))
        self.label_title_qdsystem_21.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_21.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_21.setFrameShadow(QFrame.Plain)

        self.gridLayout_11.addWidget(self.label_title_qdsystem_21, 12, 2, 1, 1)

        self.label_title_qdsystem_16 = QLabel(self.tab_8)
        self.label_title_qdsystem_16.setObjectName(u"label_title_qdsystem_16")
        self.label_title_qdsystem_16.setMinimumSize(QSize(0, 40))
        self.label_title_qdsystem_16.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_16.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_16.setFrameShadow(QFrame.Plain)

        self.gridLayout_11.addWidget(self.label_title_qdsystem_16, 3, 2, 1, 1)

        self.label_title_qdsystem_19 = QLabel(self.tab_8)
        self.label_title_qdsystem_19.setObjectName(u"label_title_qdsystem_19")
        self.label_title_qdsystem_19.setMinimumSize(QSize(0, 40))
        self.label_title_qdsystem_19.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_19.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_19.setFrameShadow(QFrame.Plain)

        self.gridLayout_11.addWidget(self.label_title_qdsystem_19, 10, 2, 1, 1)

        self.text_output_program_qdacc_command_sweep_2 = QTextBrowser(self.tab_8)
        self.text_output_program_qdacc_command_sweep_2.setObjectName(u"text_output_program_qdacc_command_sweep_2")
        self.text_output_program_qdacc_command_sweep_2.setMinimumSize(QSize(599, 200))
        self.text_output_program_qdacc_command_sweep_2.setFrameShape(QFrame.NoFrame)
        self.text_output_program_qdacc_command_sweep_2.setReadOnly(False)

        self.gridLayout_11.addWidget(self.text_output_program_qdacc_command_sweep_2, 0, 0, 5, 2)

        self.label_title_qdsystem_20 = QLabel(self.tab_8)
        self.label_title_qdsystem_20.setObjectName(u"label_title_qdsystem_20")
        self.label_title_qdsystem_20.setMinimumSize(QSize(0, 40))
        self.label_title_qdsystem_20.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem_20.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem_20.setFrameShadow(QFrame.Plain)

        self.gridLayout_11.addWidget(self.label_title_qdsystem_20, 11, 2, 1, 1)

        self.label_plot_optimizer_2 = PlotWidget(self.tab_8)
        self.label_plot_optimizer_2.setObjectName(u"label_plot_optimizer_2")
        self.label_plot_optimizer_2.setMinimumSize(QSize(0, 200))
        self.label_plot_optimizer_2.setStyleSheet(u"background-color: b")

        self.gridLayout_11.addWidget(self.label_plot_optimizer_2, 10, 1, 5, 1)

        self.textinput_optimizer_files = QLineEdit(self.tab_8)
        self.textinput_optimizer_files.setObjectName(u"textinput_optimizer_files")
        self.textinput_optimizer_files.setMinimumSize(QSize(0, 40))

        self.gridLayout_11.addWidget(self.textinput_optimizer_files, 1, 3, 1, 6)

        self.textinput_optimizer_file_indices = QLineEdit(self.tab_8)
        self.textinput_optimizer_file_indices.setObjectName(u"textinput_optimizer_file_indices")
        self.textinput_optimizer_file_indices.setMinimumSize(QSize(0, 40))

        self.gridLayout_11.addWidget(self.textinput_optimizer_file_indices, 2, 3, 1, 6)

        self.textinput_optimizer_legend = QLineEdit(self.tab_8)
        self.textinput_optimizer_legend.setObjectName(u"textinput_optimizer_legend")
        self.textinput_optimizer_legend.setMinimumSize(QSize(0, 40))

        self.gridLayout_11.addWidget(self.textinput_optimizer_legend, 3, 3, 1, 6)

        self.textinput_optimizer_initial_parameters = QLineEdit(self.tab_8)
        self.textinput_optimizer_initial_parameters.setObjectName(u"textinput_optimizer_initial_parameters")
        self.textinput_optimizer_initial_parameters.setMinimumSize(QSize(0, 40))

        self.gridLayout_11.addWidget(self.textinput_optimizer_initial_parameters, 4, 3, 1, 6)

        self.textinput_optimizer_parameter_bounds = QLineEdit(self.tab_8)
        self.textinput_optimizer_parameter_bounds.setObjectName(u"textinput_optimizer_parameter_bounds")
        self.textinput_optimizer_parameter_bounds.setMinimumSize(QSize(0, 40))

        self.gridLayout_11.addWidget(self.textinput_optimizer_parameter_bounds, 5, 3, 1, 6)

        self.textinput_optimizer_parameter_names = QLineEdit(self.tab_8)
        self.textinput_optimizer_parameter_names.setObjectName(u"textinput_optimizer_parameter_names")
        self.textinput_optimizer_parameter_names.setMinimumSize(QSize(0, 40))

        self.gridLayout_11.addWidget(self.textinput_optimizer_parameter_names, 8, 3, 1, 6)

        self.textinput_optimizer_fitnessfunction = QLineEdit(self.tab_8)
        self.textinput_optimizer_fitnessfunction.setObjectName(u"textinput_optimizer_fitnessfunction")
        self.textinput_optimizer_fitnessfunction.setMinimumSize(QSize(0, 40))

        self.gridLayout_11.addWidget(self.textinput_optimizer_fitnessfunction, 9, 3, 1, 6)

        self.textinput_optimizer_formatfunction = QLineEdit(self.tab_8)
        self.textinput_optimizer_formatfunction.setObjectName(u"textinput_optimizer_formatfunction")
        self.textinput_optimizer_formatfunction.setMinimumSize(QSize(0, 40))

        self.gridLayout_11.addWidget(self.textinput_optimizer_formatfunction, 10, 3, 1, 6)

        self.textinput_optimizer_tol = QLineEdit(self.tab_8)
        self.textinput_optimizer_tol.setObjectName(u"textinput_optimizer_tol")
        self.textinput_optimizer_tol.setMinimumSize(QSize(0, 40))

        self.gridLayout_11.addWidget(self.textinput_optimizer_tol, 11, 3, 1, 6)

        self.textinput_optimizer_eps = QLineEdit(self.tab_8)
        self.textinput_optimizer_eps.setObjectName(u"textinput_optimizer_eps")
        self.textinput_optimizer_eps.setMinimumSize(QSize(0, 40))

        self.gridLayout_11.addWidget(self.textinput_optimizer_eps, 12, 3, 1, 6)

        self.textinput_optimizer_maxit = QLineEdit(self.tab_8)
        self.textinput_optimizer_maxit.setObjectName(u"textinput_optimizer_maxit")
        self.textinput_optimizer_maxit.setMinimumSize(QSize(0, 40))

        self.gridLayout_11.addWidget(self.textinput_optimizer_maxit, 13, 3, 1, 6)

        self.optimizer_call_plotscript = QCheckBox(self.tab_8)
        self.optimizer_call_plotscript.setObjectName(u"optimizer_call_plotscript")
        self.optimizer_call_plotscript.setMinimumSize(QSize(0, 40))

        self.gridLayout_11.addWidget(self.optimizer_call_plotscript, 14, 2, 1, 7)

        self.tabWidget.addTab(self.tab_8, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_13 = QGridLayout(self.tab)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.output_howto = QTextBrowser(self.tab)
        self.output_howto.setObjectName(u"output_howto")
        self.output_howto.setOpenLinks(False)

        self.gridLayout_13.addWidget(self.output_howto, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_14.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1458, 22))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuMenu.setGeometry(QRect(269, 131, 135, 59))
        self.menuFunctions = QMenu(self.menubar)
        self.menuFunctions.setObjectName(u"menuFunctions")
        self.menuDeveloper_Tools = QMenu(self.menubar)
        self.menuDeveloper_Tools.setObjectName(u"menuDeveloper_Tools")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
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
        QWidget.setTabOrder(self.textinput_phonons_sd_qd_size, self.button_next_tab_config_to_timeline)
        QWidget.setTabOrder(self.button_next_tab_config_to_timeline, self.button_next_tab_timeline_to_spectrum)
        QWidget.setTabOrder(self.button_next_tab_timeline_to_spectrum, self.textinput_spectrum_modes)
        QWidget.setTabOrder(self.textinput_spectrum_modes, self.textinput_spectrum_range)
        QWidget.setTabOrder(self.textinput_spectrum_range, self.textinput_spectrum_center)
        QWidget.setTabOrder(self.textinput_spectrum_center, self.textinput_spectrum_res)
        QWidget.setTabOrder(self.textinput_spectrum_res, self.input_spectrum_order)
        QWidget.setTabOrder(self.input_spectrum_order, self.input_spectrum_normalize)
        QWidget.setTabOrder(self.input_spectrum_normalize, self.button_add_spectrum_to_output)
        QWidget.setTabOrder(self.button_add_spectrum_to_output, self.button_next_tab_spectrum_to_indist)
        QWidget.setTabOrder(self.button_next_tab_spectrum_to_indist, self.textinput_indist_modes)
        QWidget.setTabOrder(self.textinput_indist_modes, self.button_next_tab_indist_to_conc)
        QWidget.setTabOrder(self.button_next_tab_indist_to_conc, self.textinput_concurrence_first)
        QWidget.setTabOrder(self.textinput_concurrence_first, self.textinput_concurrence_second)
        QWidget.setTabOrder(self.textinput_concurrence_second, self.button_add_concurrence_to_output)
        QWidget.setTabOrder(self.button_add_concurrence_to_output, self.button_next_tab_sconc_to_stats)
        QWidget.setTabOrder(self.button_next_tab_sconc_to_stats, self.textinput_detector_t0)
        QWidget.setTabOrder(self.textinput_detector_t0, self.textinput_detector_t1)
        QWidget.setTabOrder(self.textinput_detector_t1, self.textinput_detector_tpower)
        QWidget.setTabOrder(self.textinput_detector_tpower, self.input_timeline_enable_phonons_at_spectra)
        QWidget.setTabOrder(self.input_timeline_enable_phonons_at_spectra, self.button_add_detector_time)
        QWidget.setTabOrder(self.button_add_detector_time, self.button_next_tab_detector_to_generate)
        QWidget.setTabOrder(self.button_next_tab_detector_to_generate, self.button_next_tab_stats_to_detector)
        QWidget.setTabOrder(self.button_next_tab_stats_to_detector, self.text_output_list_of_wigner_funcs)
        QWidget.setTabOrder(self.text_output_list_of_wigner_funcs, self.button_add_electronic_state)
        QWidget.setTabOrder(self.button_add_electronic_state, self.text_output_list_of_spectra)
        QWidget.setTabOrder(self.text_output_list_of_spectra, self.text_output_list_of_indists)
        QWidget.setTabOrder(self.text_output_list_of_indists, self.button_timeline_force_calculate)
        QWidget.setTabOrder(self.button_timeline_force_calculate, self.button_timeline_force_calculate_spectra)
        QWidget.setTabOrder(self.button_timeline_force_calculate_spectra, self.text_output_list_of_detector_spec)
        QWidget.setTabOrder(self.text_output_list_of_detector_spec, self.input_timeline_enable_phonons)
        QWidget.setTabOrder(self.input_timeline_enable_phonons, self.button_remove_spectrum_from_output)
        QWidget.setTabOrder(self.button_remove_spectrum_from_output, self.text_output_list_of_detector_time)
        QWidget.setTabOrder(self.text_output_list_of_detector_time, self.textinput_concurrence_spec_range)
        QWidget.setTabOrder(self.textinput_concurrence_spec_range, self.text_output_program_qdacc_command)
        QWidget.setTabOrder(self.text_output_program_qdacc_command, self.textinput_concurrence_spec_freq)
        QWidget.setTabOrder(self.textinput_concurrence_spec_freq, self.text_output_program_main)
        QWidget.setTabOrder(self.text_output_program_main, self.input_concurrence_add_spectra)
        QWidget.setTabOrder(self.input_concurrence_add_spectra, self.textinput_concurrence_spec_res)
        QWidget.setTabOrder(self.textinput_concurrence_spec_res, self.text_output_list_of_concurrences)
        QWidget.setTabOrder(self.text_output_list_of_concurrences, self.button_reset_phonon_qd)
        QWidget.setTabOrder(self.button_reset_phonon_qd, self.list_components)
        QWidget.setTabOrder(self.list_components, self.button_remove_concurrence_from_output)
        QWidget.setTabOrder(self.button_remove_concurrence_from_output, self.slider_state_separator)
        QWidget.setTabOrder(self.slider_state_separator, self.slider_state_grouping)
        QWidget.setTabOrder(self.slider_state_grouping, self.input_initial_state)
        QWidget.setTabOrder(self.input_initial_state, self.textinput_initial_state)
        QWidget.setTabOrder(self.textinput_initial_state, self.input_phonons_adjust_radiativeloss)
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
        QWidget.setTabOrder(self.input_rungekutta_order, self.button_add_spectrum_mode)
        QWidget.setTabOrder(self.button_add_spectrum_mode, self.button_add_indist_to_output)
        QWidget.setTabOrder(self.button_add_indist_to_output, self.button_remove_indist_from_output)
        QWidget.setTabOrder(self.button_remove_indist_from_output, self.button_add_indist_mode)
        QWidget.setTabOrder(self.button_add_indist_mode, self.button_add_concurrence_mode_1)
        QWidget.setTabOrder(self.button_add_concurrence_mode_1, self.button_add_concurrence_mode_2)
        QWidget.setTabOrder(self.button_add_concurrence_mode_2, self.textinput_correlation_modes)
        QWidget.setTabOrder(self.textinput_correlation_modes, self.text_output_list_of_gfuncs)
        QWidget.setTabOrder(self.text_output_list_of_gfuncs, self.input_gfunc_order)
        QWidget.setTabOrder(self.input_gfunc_order, self.input_gfunc_integration)
        QWidget.setTabOrder(self.input_gfunc_integration, self.button_add_gfunc_to_output)
        QWidget.setTabOrder(self.button_add_gfunc_to_output, self.button_remove_gfunc_from_output)
        QWidget.setTabOrder(self.button_remove_gfunc_from_output, self.textinput_wigner_modes)
        QWidget.setTabOrder(self.textinput_wigner_modes, self.textinput_wigner_x)
        QWidget.setTabOrder(self.textinput_wigner_x, self.textinput_wigner_y)
        QWidget.setTabOrder(self.textinput_wigner_y, self.textinput_wigner_resolution)
        QWidget.setTabOrder(self.textinput_wigner_resolution, self.textinput_wigner_skip)
        QWidget.setTabOrder(self.textinput_wigner_skip, self.button_add_wigner)
        QWidget.setTabOrder(self.button_add_wigner, self.button_remove_wigner)
        QWidget.setTabOrder(self.button_remove_wigner, self.button_add_gfunc_mode)
        QWidget.setTabOrder(self.button_add_gfunc_mode, self.button_add_wigner_mode)
        QWidget.setTabOrder(self.button_add_wigner_mode, self.button_remove_detector_time)
        QWidget.setTabOrder(self.button_remove_detector_time, self.textinput_detector_wcenter)
        QWidget.setTabOrder(self.textinput_detector_wcenter, self.textinput_detector_wrange)
        QWidget.setTabOrder(self.textinput_detector_wrange, self.textinput_detector_wnum)
        QWidget.setTabOrder(self.textinput_detector_wnum, self.textinput_detector_wpower)
        QWidget.setTabOrder(self.textinput_detector_wpower, self.button_add_detector_spectral)
        QWidget.setTabOrder(self.button_add_detector_spectral, self.button_remove_detector_spectral)
        QWidget.setTabOrder(self.button_remove_detector_spectral, self.text_output_list_of_custom_expvals)
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
        QWidget.setTabOrder(self.button_generate_copy, self.button_run_kill)
        QWidget.setTabOrder(self.button_run_kill, self.button_run_program)
        QWidget.setTabOrder(self.button_run_program, self.button_run_external)
        QWidget.setTabOrder(self.button_run_external, self.input_plot_mode)
        QWidget.setTabOrder(self.input_plot_mode, self.button_plot_everything)
        QWidget.setTabOrder(self.button_plot_everything, self.textinput_path_to_settingfile)
        QWidget.setTabOrder(self.textinput_path_to_settingfile, self.button_sweeper_get_runstring)
        QWidget.setTabOrder(self.button_sweeper_get_runstring, self.button_sweeper_plot)
        QWidget.setTabOrder(self.button_sweeper_plot, self.button_set_setting_file_path)
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
        QWidget.setTabOrder(self.button_add_electronic_shift, self.button_next_tab_system_to_config)
        QWidget.setTabOrder(self.button_next_tab_system_to_config, self.button_modify_delete)
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

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuFunctions.menuAction())
        self.menubar.addAction(self.menuDeveloper_Tools.menuAction())
        self.menuMenu.addSeparator()

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.input_phonons_approximation.setCurrentIndex(1)
        self.input_rungekutta_order.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"QDaCC Generator", None))
        self.actionLoad_QDaCC_Command.setText(QCoreApplication.translate("MainWindow", u"Import QDaCC Command", None))
        self.actionExport_QDaCC_Command.setText(QCoreApplication.translate("MainWindow", u"Export QDaCC Command", None))
        self.label_title_qdsystem.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">QD System</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Add...</span></p></body></html>", None))
        self.button_add_electronic_state.setText(QCoreApplication.translate("MainWindow", u"State", None))
        self.button_add_cavity.setText(QCoreApplication.translate("MainWindow", u"Cavity", None))
        self.button_add_optical_pulse.setText(QCoreApplication.translate("MainWindow", u"Pulse", None))
        self.button_add_electronic_shift.setText(QCoreApplication.translate("MainWindow", u"Chirp", None))
        self.button_modify_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.button_modify_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.button_modify_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
#if QT_CONFIG(statustip)
        self.input_draw_details.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_draw_details.setText(QCoreApplication.translate("MainWindow", u"Details", None))
#if QT_CONFIG(tooltip)
        self.slider_state_separator.setToolTip(QCoreApplication.translate("MainWindow", u"Adjust visible state separation", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.slider_state_grouping.setToolTip(QCoreApplication.translate("MainWindow", u"Adjust state grouping threshold", None))
#endif // QT_CONFIG(tooltip)
        self.input_initial_state.setText(QCoreApplication.translate("MainWindow", u"Initial State", None))
        self.textinput_initial_state.setText("")
        self.button_next_tab_system_to_config.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_output_system.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_system), QCoreApplication.translate("MainWindow", u"System", None))
        self.textinput_phonons_sd_qd_de.setText(QCoreApplication.translate("MainWindow", u"7eV", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Hole Energy</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Cavity Loss</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Temperature</span></p></body></html>", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Spectral Density Plot</span></p></body></html>", None))
        self.textinput_phonons_sd_tcutoff.setText(QCoreApplication.translate("MainWindow", u"4ps", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Time Cutoff</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Radiative Loss</span></p></body></html>", None))
        self.textinput_rates_pure_dephasing.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Speed of Sound</span></p></body></html>", None))
        self.textinput_phonons_iterator_stepsize.setText(QCoreApplication.translate("MainWindow", u"auto", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Electron Energy</span></p></body></html>", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">E-H Ratio</span></p></body></html>", None))
        self.label_title_rates.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Rates</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Cavity Coupling</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Pure Dephasing</span></p></body></html>", None))
        self.label_title_phonons_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">PME Settings</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Spectral Cutoff</span></p></body></html>", None))
        self.textinput_phonons_temperature.setText(QCoreApplication.translate("MainWindow", u"No Phonons", None))
        self.textinput_phonons_sd_ohmamp.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.input_phonons_approximation.setItemText(0, QCoreApplication.translate("MainWindow", u"Full", None))
        self.input_phonons_approximation.setItemText(1, QCoreApplication.translate("MainWindow", u"Matrixexponential", None))
        self.input_phonons_approximation.setItemText(2, QCoreApplication.translate("MainWindow", u"Omit Transformation", None))
        self.input_phonons_approximation.setItemText(3, QCoreApplication.translate("MainWindow", u"Analytical Rates", None))
        self.input_phonons_approximation.setItemText(4, QCoreApplication.translate("MainWindow", u"Hybrid", None))

        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Material Density</span></p></body></html>", None))
        self.label_title_phonons_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Phonon Integral</span></p></body></html>", None))
        self.textinput_phonons_sd_qd_dh.setText(QCoreApplication.translate("MainWindow", u"-3.5eV", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Quantum Dot</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Ohm</span></p></body></html>", None))
        self.textinput_rates_radiative_decay.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_size.setStatusTip(QCoreApplication.translate("MainWindow", u"Typical Values lie around 3nm to 6nm", None))
#endif // QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_size.setText(QCoreApplication.translate("MainWindow", u"3e-9", None))
        self.button_next_tab_config_to_timeline.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Integral Stepsize</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_rho.setStatusTip(QCoreApplication.translate("MainWindow", u"Unit is kg/m^3", None))
#endif // QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_rho.setText(QCoreApplication.translate("MainWindow", u"5370", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Phonon Coupling</span></p></body></html>", None))
        self.label_title_phonons_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">QD Settings</span></p></body></html>", None))
        self.textinput_phonons_sd_alpha.setText(QCoreApplication.translate("MainWindow", u"0.03E-24", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">QD Size (m)</span></p></body></html>", None))
        self.textinput_phonons_sd_wcutoff.setText(QCoreApplication.translate("MainWindow", u"1meV", None))
        self.input_phonons_use_qd.setText(QCoreApplication.translate("MainWindow", u"Use QD Parameters Instead of PME Settings", None))
        self.label_title_phonons.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Environment (Phonons)</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Approximation</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Spectral Delta</span></p></body></html>", None))
        self.textinput_rates_cavity_loss.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_cs.setStatusTip(QCoreApplication.translate("MainWindow", u"Unit is m/s", None))
#endif // QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_cs.setText(QCoreApplication.translate("MainWindow", u"5110", None))
        self.textinput_phonons_sd_wdelta.setText(QCoreApplication.translate("MainWindow", u"0.01meV", None))
        self.button_reset_phonon_qd.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
#if QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_aeah_ratio.setStatusTip(QCoreApplication.translate("MainWindow", u"a_e/a_h ratio", None))
#endif // QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_aeah_ratio.setText(QCoreApplication.translate("MainWindow", u"1.15", None))
        self.textinput_rates_cavity_coupling.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_title_adjust_rates.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Adjust</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.input_phonons_adjust_radiativeloss.setStatusTip(QCoreApplication.translate("MainWindow", u"Adjusts the radiative decay loss using the formula gamma_rad = gamma_rad*<B>", None))
#endif // QT_CONFIG(statustip)
        self.input_phonons_adjust_radiativeloss.setText(QCoreApplication.translate("MainWindow", u"Radiative Loss", None))
        self.label_title_adjust_rates_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Adjust</span></p></body></html>", None))
        self.label_title_adjust_rates_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Adjust</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.input_phonons_adjust_pure_dephasing.setStatusTip(QCoreApplication.translate("MainWindow", u"Adjusts the pure dephasing rate using the formula pure_dephasing = 1mueV/K * temperature. This effect is quite strong and should probably not be used.", None))
#endif // QT_CONFIG(statustip)
        self.input_phonons_adjust_pure_dephasing.setText(QCoreApplication.translate("MainWindow", u"Pure Dephasing", None))
#if QT_CONFIG(tooltip)
        self.input_phonons_adjust_renormalization.setToolTip(QCoreApplication.translate("MainWindow", u"Enables the renomalization of the polaron shifted energies and rates, e.g. using the <B> and <B>^2 scalings", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.input_phonons_adjust_renormalization.setStatusTip(QCoreApplication.translate("MainWindow", u"Enables the renomalization of the polaron shifted energies and rates, e.g. using the <B> and <B>^2 scalings", None))
#endif // QT_CONFIG(statustip)
        self.input_phonons_adjust_renormalization.setText(QCoreApplication.translate("MainWindow", u"Renormalization", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_environment), QCoreApplication.translate("MainWindow", u"Environment", None))
        self.input_interpolator_t.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.input_interpolator_t.setItemText(1, QCoreApplication.translate("MainWindow", u"Linear", None))
        self.input_interpolator_t.setItemText(2, QCoreApplication.translate("MainWindow", u"Cubic", None))
        self.input_interpolator_t.setItemText(3, QCoreApplication.translate("MainWindow", u"Monotone", None))

#if QT_CONFIG(statustip)
        self.input_interpolator_t.setStatusTip(QCoreApplication.translate("MainWindow", u"Main Direction Interpolator. If None, no interpolation will be used, meaning the main time output has non-equidistant elements", None))
#endif // QT_CONFIG(statustip)
        self.textinput_time_tolerance.setText(QCoreApplication.translate("MainWindow", u"1E-6", None))
        self.textinput_time_tolerance.setPlaceholderText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Main Solver</span></p></body></html>", None))
        self.textinput_phonons_nc.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(tooltip)
        self.button_time_config_grid.setToolTip(QCoreApplication.translate("MainWindow", u"Configure a grid instead", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.button_time_config_grid.setStatusTip(QCoreApplication.translate("MainWindow", u"Configure a grid instead", None))
#endif // QT_CONFIG(statustip)
        self.button_time_config_grid.setText(QCoreApplication.translate("MainWindow", u"Gridresolution", None))
        self.textinput_time_timestep.setText(QCoreApplication.translate("MainWindow", u"auto", None))
#if QT_CONFIG(tooltip)
        self.button_time_config_tol.setToolTip(QCoreApplication.translate("MainWindow", u"Configure a grid instead", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.button_time_config_tol.setStatusTip(QCoreApplication.translate("MainWindow", u"Configure a grid instead", None))
#endif // QT_CONFIG(statustip)
        self.button_time_config_tol.setText(QCoreApplication.translate("MainWindow", u"Tolerance", None))
        self.label_title_time.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Time</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.button_timeline_force_calculate.setStatusTip(QCoreApplication.translate("MainWindow", u"Calculate the actual temporal evolution. This disables the phonon interactions, such that calculations are fast.", None))
#endif // QT_CONFIG(statustip)
        self.button_timeline_force_calculate.setText(QCoreApplication.translate("MainWindow", u"Calculate Time", None))
        self.textinput_time_endtime.setText(QCoreApplication.translate("MainWindow", u"auto", None))
#if QT_CONFIG(statustip)
        self.input_timeline_enable_phonons.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_timeline_enable_phonons.setText(QCoreApplication.translate("MainWindow", u"Disable Phonons", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Time Step</span></p></body></html>", None))
        self.input_interpolator_tau.setItemText(0, QCoreApplication.translate("MainWindow", u"Linear", None))
        self.input_interpolator_tau.setItemText(1, QCoreApplication.translate("MainWindow", u"Monotone", None))

#if QT_CONFIG(statustip)
        self.input_interpolator_tau.setStatusTip(QCoreApplication.translate("MainWindow", u"Tau-Direction Interpolator which expands the time calculations onto an equidistant grid. Usually linear is sufficient.", None))
#endif // QT_CONFIG(statustip)
        self.button_next_tab_timeline_to_spectrum.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.textinput_time_startingtime.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_title_solver.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Solver</span></p></body></html>", None))
        self.textinput_phonons_tsteppath.setText(QCoreApplication.translate("MainWindow", u"auto", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">End Time</span></p></body></html>", None))
        self.textinput_time_gridresolution.setText(QCoreApplication.translate("MainWindow", u"auto", None))
        self.textinput_time_gridresolution.setPlaceholderText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Starting Time</span></p></body></html>", None))
        self.label_title_predicted_timeline.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Predicted Timeline</span></p></body></html>", None))
        self.input_rungekutta_order.setItemText(0, QCoreApplication.translate("MainWindow", u"Variable Timestep Runge Kutta Dormand Prince", None))
        self.input_rungekutta_order.setItemText(1, QCoreApplication.translate("MainWindow", u"Fixed Timestep Runge-Kutta Order 4", None))
        self.input_rungekutta_order.setItemText(2, QCoreApplication.translate("MainWindow", u"Fixed Timestep Runge-Kutta Order 5", None))
        self.input_rungekutta_order.setItemText(3, QCoreApplication.translate("MainWindow", u"Path Integral (PSADM IQUAPI)", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Grid Expander</span></p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">PI Stepsize</span></p></body></html>", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">PI NC</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Interpolator</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_timeline), QCoreApplication.translate("MainWindow", u"Timeline", None))
        self.button_remove_spectrum_from_output.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
#if QT_CONFIG(statustip)
        self.input_timeline_enable_phonons_at_spectra.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_timeline_enable_phonons_at_spectra.setText(QCoreApplication.translate("MainWindow", u"Disable Phonons", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Resolution</span></p></body></html>", None))
        self.input_spectrum_order.setItemText(0, QCoreApplication.translate("MainWindow", u"G1", None))
        self.input_spectrum_order.setItemText(1, QCoreApplication.translate("MainWindow", u"G2", None))

        self.label_48.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Spectral Range</span></p></body></html>", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Spectral Center</span></p></body></html>", None))
        self.button_next_tab_spectrum_to_indist.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.button_add_spectrum_to_output.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_title_predicted_spectral.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Predicted Spectral Properties</span></p></body></html>", None))
        self.textinput_spectrum_center.setText("")
        self.textinput_spectrum_center.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1eV", None))
        self.textinput_spectrum_modes.setText("")
        self.textinput_spectrum_modes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A=B,c", None))
        self.textinput_spectrum_res.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.textinput_spectrum_res.setPlaceholderText("")
        self.label_title_set_spectrum.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Spectrum</span></p></body></html>", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Normalize</span></p></body></html>", None))
        self.input_spectrum_normalize.setText(QCoreApplication.translate("MainWindow", u"To 1", None))
        self.textinput_spectrum_range.setText("")
        self.textinput_spectrum_range.setPlaceholderText(QCoreApplication.translate("MainWindow", u"2meV", None))
#if QT_CONFIG(statustip)
        self.button_timeline_force_calculate_spectra.setStatusTip(QCoreApplication.translate("MainWindow", u"Calculate the actual spectral properties using a small spectral window. This disables the phonon interactions, such that calculations are fast.", None))
#endif // QT_CONFIG(statustip)
        self.button_timeline_force_calculate_spectra.setText(QCoreApplication.translate("MainWindow", u"Calculate Spectra", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Correlation</span></p></body></html>", None))
        self.button_add_spectrum_mode.setText(QCoreApplication.translate("MainWindow", u"List of Modes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_spectrum), QCoreApplication.translate("MainWindow", u"Spectrum", None))
        self.button_next_tab_indist_to_conc.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.textinput_indist_modes.setText("")
        self.textinput_indist_modes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A=B, c", None))
        self.label_title_set_indists.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Indistinguishabilities</span></p></body></html>", None))
        self.button_add_indist_to_output.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.button_remove_indist_from_output.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.button_add_indist_mode.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_indist), QCoreApplication.translate("MainWindow", u"Indistinguishability", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Range</span></p></body></html>", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Resolution</span></p></body></html>", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">G2 Spectra</span></p></body></html>", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Center</span></p></body></html>", None))
        self.button_add_concurrence_to_output.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.button_remove_concurrence_from_output.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_title_set_concurrences.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Concurrences</span></p></body></html>", None))
        self.textinput_concurrence_first.setText("")
        self.textinput_concurrence_first.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A=B+B=D", None))
        self.textinput_concurrence_second.setText("")
        self.textinput_concurrence_second.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A=C+C=D", None))
        self.label_title_set_concurrences_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Spectral Properties</span></p></body></html>", None))
        self.input_concurrence_add_spectra.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.textinput_concurrence_spec_freq.setText("")
        self.textinput_concurrence_spec_freq.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.textinput_concurrence_spec_range.setText("")
        self.textinput_concurrence_spec_range.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.textinput_concurrence_spec_res.setText("")
        self.textinput_concurrence_spec_res.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button_next_tab_sconc_to_stats.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.button_add_concurrence_mode_1.setText(QCoreApplication.translate("MainWindow", u"First Mode", None))
        self.button_add_concurrence_mode_2.setText(QCoreApplication.translate("MainWindow", u"Second Mode", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_concurrence), QCoreApplication.translate("MainWindow", u"Concurrence", None))
        self.label_title_set_wigner_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">G</span><span style=\" font-size:14pt; vertical-align:super;\">1</span><span style=\" font-size:14pt;\"> and G</span><span style=\" font-size:14pt; vertical-align:super;\">2</span><span style=\" font-size:14pt;\"> Correlation Function</span></p></body></html>", None))
        self.textinput_correlation_modes.setText("")
        self.textinput_correlation_modes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A=B, c", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Order</span></p></body></html>", None))
        self.input_gfunc_order.setItemText(0, QCoreApplication.translate("MainWindow", u"G1", None))
        self.input_gfunc_order.setItemText(1, QCoreApplication.translate("MainWindow", u"G2", None))

        self.label_116.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Outputmethod</span></p></body></html>", None))
        self.input_gfunc_integration.setItemText(0, QCoreApplication.translate("MainWindow", u"Integrated", None))
        self.input_gfunc_integration.setItemText(1, QCoreApplication.translate("MainWindow", u"Matrix", None))
        self.input_gfunc_integration.setItemText(2, QCoreApplication.translate("MainWindow", u"Both", None))

        self.button_add_gfunc_to_output.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.button_remove_gfunc_from_output.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_title_set_wigner.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Wigner Function</span></p></body></html>", None))
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
        self.button_next_tab_stats_to_detector.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.button_add_gfunc_mode.setText(QCoreApplication.translate("MainWindow", u"Modes", None))
        self.button_add_wigner_mode.setText(QCoreApplication.translate("MainWindow", u"Modes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_additional_stats), QCoreApplication.translate("MainWindow", u"Additional Statistics", None))
        self.textinput_detector_t0.setText("")
        self.textinput_detector_t0.setPlaceholderText(QCoreApplication.translate("MainWindow", u"start", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Width</span></p></body></html>", None))
        self.textinput_detector_tpower.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.textinput_detector_tpower.setPlaceholderText("")
        self.label_title_set_detector_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Spectral Measurement Window</span></p></body></html>", None))
        self.button_add_detector_time.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_title_set_detector.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Temporal Measurement Window</span></p></body></html>", None))
        self.button_next_tab_detector_to_generate.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Time Center</span></p></body></html>", None))
        self.button_remove_detector_time.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Falloff Power</span></p></body></html>", None))
        self.textinput_detector_t1.setText("")
        self.textinput_detector_t1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"end", None))
        self.textinput_detector_wcenter.setText("")
        self.textinput_detector_wcenter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"center", None))
        self.textinput_detector_wrange.setText("")
        self.textinput_detector_wrange.setPlaceholderText(QCoreApplication.translate("MainWindow", u"range", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Spectral Range</span></p></body></html>", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Spectral Center</span></p></body></html>", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Fourier Points</span></p></body></html>", None))
        self.textinput_detector_wnum.setText("")
        self.textinput_detector_wnum.setPlaceholderText(QCoreApplication.translate("MainWindow", u"fourier points", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Falloff Power</span></p></body></html>", None))
        self.textinput_detector_wpower.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.textinput_detector_wpower.setPlaceholderText("")
        self.button_add_detector_spectral.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.button_remove_detector_spectral.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_detector), QCoreApplication.translate("MainWindow", u"Detector", None))
        self.input_logginglevel.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.input_logginglevel.setItemText(1, QCoreApplication.translate("MainWindow", u"Additional", None))
        self.input_logginglevel.setItemText(2, QCoreApplication.translate("MainWindow", u"Verbose", None))

        self.input_dm_frame.setItemText(0, QCoreApplication.translate("MainWindow", u"Heisenberg", None))
        self.input_dm_frame.setItemText(1, QCoreApplication.translate("MainWindow", u"Schr\u00f6dinger", None))

        self.label_64.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Frame</span></p></body></html>", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Custom Expectation Values</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.input_add_output_greenf.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_greenf.setText(QCoreApplication.translate("MainWindow", u"Greenfunctions", None))
#if QT_CONFIG(statustip)
        self.input_add_output_rkerror.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_rkerror.setText(QCoreApplication.translate("MainWindow", u"Runge-Kutta Error", None))
#if QT_CONFIG(statustip)
        self.input_add_output_phononcoeffs.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_phononcoeffs.setText(QCoreApplication.translate("MainWindow", u"Phononcoefficients", None))
#if QT_CONFIG(statustip)
        self.input_add_output_phononj.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_phononj.setText(QCoreApplication.translate("MainWindow", u"Phonon Spectral J", None))
        self.button_add_custom_expval_matrix.setText(QCoreApplication.translate("MainWindow", u"Add", None))
#if QT_CONFIG(statustip)
        self.input_add_output_detecotrtrafo.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_detecotrtrafo.setText(QCoreApplication.translate("MainWindow", u"Detectorfunctions", None))
#if QT_CONFIG(statustip)
        self.input_add_output_chirp_fourier.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_chirp_fourier.setText(QCoreApplication.translate("MainWindow", u"Chirp Fourier", None))
#if QT_CONFIG(statustip)
        self.input_add_output_eigenvalues.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_eigenvalues.setText(QCoreApplication.translate("MainWindow", u"Eigenvalues", None))
#if QT_CONFIG(statustip)
        self.input_add_output_tpm.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_tpm.setText(QCoreApplication.translate("MainWindow", u"Two Photon Matrix", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Density Matrix</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.input_add_output_operators.setStatusTip(QCoreApplication.translate("MainWindow", u"Note: Logging Level has to be at least L2", None))
#endif // QT_CONFIG(statustip)
        self.input_add_output_operators.setText(QCoreApplication.translate("MainWindow", u"Operator Matrices", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Logging Level</span></p></body></html>", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">CPU Cores</span></p></body></html>", None))
        self.textinput_cpucores.setText(QCoreApplication.translate("MainWindow", u"all", None))
        self.button_remove_custom_expval_matrix.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
#if QT_CONFIG(statustip)
        self.input_add_output_pulse_fourier.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_pulse_fourier.setText(QCoreApplication.translate("MainWindow", u"Pulse Fourier", None))
#if QT_CONFIG(statustip)
        self.input_add_output_concurrence_eigs.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_concurrence_eigs.setText(QCoreApplication.translate("MainWindow", u"Concurrence EV", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Output</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.input_add_output_vonneumannpath.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_vonneumannpath.setText(QCoreApplication.translate("MainWindow", u"von Neumann Path", None))
        self.input_dm_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"No Output", None))
        self.input_dm_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"Diagonal Elements", None))
        self.input_dm_mode.setItemText(2, QCoreApplication.translate("MainWindow", u"Full Matrix", None))

#if QT_CONFIG(statustip)
        self.input_add_output_photon_expv.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_photon_expv.setText(QCoreApplication.translate("MainWindow", u"Full Photon EV", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_output), QCoreApplication.translate("MainWindow", u"Output", None))
        self.input_path_to_qdacc.setText(QCoreApplication.translate("MainWindow", u"QDaCC", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Generate QDaCC Command and Run</span></p></body></html>", None))
        self.button_change_rungstring_to_settingfile.setText(QCoreApplication.translate("MainWindow", u"Toggle Runstring", None))
        self.textinput_file_destination.setText("")
        self.text_output_program_qdacc_command.setPlaceholderText(QCoreApplication.translate("MainWindow", u"./QDaCC.exe ...", None))
        self.textinput_file_qdacc.setText("")
        self.input_destination.setText(QCoreApplication.translate("MainWindow", u"Worskspace", None))
#if QT_CONFIG(statustip)
        self.input_escape_output_command.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_escape_output_command.setText(QCoreApplication.translate("MainWindow", u"Escape Output", None))
        self.button_empty_destination_folder.setText(QCoreApplication.translate("MainWindow", u"Empty Destination Folder", None))
        self.button_open_destination_folder.setText(QCoreApplication.translate("MainWindow", u"Open Destination Folder", None))
        self.text_output_program_main.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.button_generate_run.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.button_generate_copy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.button_run_kill.setText(QCoreApplication.translate("MainWindow", u"Kill", None))
        self.button_run_program.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.input_plot_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"Workspace Folder", None))
        self.input_plot_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"Animated Blochsphere", None))
        self.input_plot_mode.setItemText(2, QCoreApplication.translate("MainWindow", u"Animated Density Matrix", None))

        self.button_plot_everything.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.button_run_external.setText(QCoreApplication.translate("MainWindow", u"Run on Noctua", None))
        self.button_run_and_plot.setText(QCoreApplication.translate("MainWindow", u"Run And Plot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_generate), QCoreApplication.translate("MainWindow", u"Generate and Run", None))
        self.label_title_qdsystem_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">To</span></p></body></html>", None))
        self.textinput_path_to_settingfile.setText("")
        self.label_title_qdsystem_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">From</span></p></body></html>", None))
        self.label_title_qdsystem_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\"># Points</span></p></body></html>", None))
        self.button_sweeper_get_runstring.setText(QCoreApplication.translate("MainWindow", u"Get Current Runstring", None))
        self.label_title_qdsystem_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Parameter x1</span></p></body></html>", None))
        self.label_title_qdsystem_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">To</span></p></body></html>", None))
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
        self.label_title_qdsystem_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">From</span></p></body></html>", None))
        self.label_title_qdsystem_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Parameter x2</span></p></body></html>", None))
        self.button_sweeper_plot.setText(QCoreApplication.translate("MainWindow", u"Generate Settingfile", None))
        self.label_title_qdsystem_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">QDaCC Runstring</span></p></body></html>", None))
        self.label_title_qdsystem_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\"># Points</span></p></body></html>", None))
        self.button_set_setting_file_path.setText(QCoreApplication.translate("MainWindow", u"Settingfile", None))
        self.label_title_qdsystem_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Parameter Scanner</span></p></body></html>", None))
        self.checkbox_activate_scan_parameter_1.setText(QCoreApplication.translate("MainWindow", u"Activate", None))
        self.checkbox_activate_scan_parameter_2.setText(QCoreApplication.translate("MainWindow", u"Activate", None))
        self.text_output_program_qdacc_command_sweep_display.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_output_program_qdacc_command_sweep_display.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Settingfile Output", None))
        self.text_output_program_qdacc_command_sweep.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_output_program_qdacc_command_sweep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"./QDaCC.exe ...", None))
        self.combobox_p1_input.setItemText(0, QCoreApplication.translate("MainWindow", u"P1(x1,...) =", None))
        self.combobox_p1_input.setItemText(1, QCoreApplication.translate("MainWindow", u"P12(x1,...) =", None))
        self.combobox_p1_input.setItemText(2, QCoreApplication.translate("MainWindow", u"P13(x1,...) =", None))
        self.combobox_p1_input.setItemText(3, QCoreApplication.translate("MainWindow", u"P14(x1,...) =", None))
        self.combobox_p1_input.setItemText(4, QCoreApplication.translate("MainWindow", u"P15(x1,...) =", None))

        self.combobox_p2_input.setItemText(0, QCoreApplication.translate("MainWindow", u"P2(x2,...) =", None))
        self.combobox_p2_input.setItemText(1, QCoreApplication.translate("MainWindow", u"P22(x2,...) =", None))
        self.combobox_p2_input.setItemText(2, QCoreApplication.translate("MainWindow", u"P23(x2,...) =", None))
        self.combobox_p2_input.setItemText(3, QCoreApplication.translate("MainWindow", u"P24(x2,...) =", None))
        self.combobox_p2_input.setItemText(4, QCoreApplication.translate("MainWindow", u"P25(x2,...) =", None))

        self.textinput_scan_parameter_1_lambda.setText("")
        self.textinput_scan_parameter_2_lambda.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Sweep and Scan", None))
        self.button_optimizer_files.setText(QCoreApplication.translate("MainWindow", u"Files", None))
        self.text_output_program_qdacc_command_sweep_display_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_output_program_qdacc_command_sweep_display_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Optimizer Output", None))
        self.label_title_qdsystem_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Maximum Iterations</span></p></body></html>", None))
        self.label_title_qdsystem_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Parameter Names</span></p></body></html>", None))
        self.label_title_qdsystem_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Parameters Bounds</span></p></body></html>", None))
        self.button_optimizer_optimize.setText(QCoreApplication.translate("MainWindow", u"Optimize", None))
        self.button_optimizer_get_runstring.setText(QCoreApplication.translate("MainWindow", u"Get Current Runstring", None))
        self.button_optimizer_fitness_function.setText(QCoreApplication.translate("MainWindow", u"Fitness Function", None))
        self.button_optimizer_runstring_to_main.setText(QCoreApplication.translate("MainWindow", u"Move Command to Main Window", None))
        self.button_optimizer_files_2.setText(QCoreApplication.translate("MainWindow", u"File Indices", None))
        self.label_title_qdsystem_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Initial Parameters</span></p></body></html>", None))
        self.label_title_qdsystem_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Epsilon</span></p></body></html>", None))
        self.label_title_qdsystem_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Legend</span></p></body></html>", None))
        self.label_title_qdsystem_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Format Function</span></p></body></html>", None))
        self.text_output_program_qdacc_command_sweep_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_output_program_qdacc_command_sweep_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"./QDaCC.exe ...", None))
        self.label_title_qdsystem_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Tolerance</span></p></body></html>", None))
        self.textinput_optimizer_files.setText("")
        self.textinput_optimizer_file_indices.setText("")
        self.textinput_optimizer_legend.setText("")
        self.textinput_optimizer_initial_parameters.setText("")
        self.textinput_optimizer_parameter_bounds.setText("")
        self.textinput_optimizer_parameter_names.setText("")
        self.textinput_optimizer_fitnessfunction.setText(QCoreApplication.translate("MainWindow", u"last(Y1)", None))
        self.textinput_optimizer_formatfunction.setText(QCoreApplication.translate("MainWindow", u"basestring.format(*parameters)", None))
        self.textinput_optimizer_tol.setText(QCoreApplication.translate("MainWindow", u"1e-6", None))
        self.textinput_optimizer_eps.setText(QCoreApplication.translate("MainWindow", u"1e-6", None))
        self.textinput_optimizer_maxit.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.optimizer_call_plotscript.setText(QCoreApplication.translate("MainWindow", u"Sweep or Scan Mode", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Optimization", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"How-To", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuFunctions.setTitle(QCoreApplication.translate("MainWindow", u"Functions", None))
        self.menuDeveloper_Tools.setTitle(QCoreApplication.translate("MainWindow", u"Dev Tools", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

