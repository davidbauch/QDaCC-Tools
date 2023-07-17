import sys, os
from PySide6.QtWidgets import QWidget,QMainWindow, QApplication,QLabel, QLineEdit,QTextEdit, QGridLayout, QTextBrowser, QTabWidget, QBoxLayout, QPushButton, QDialog, QFormLayout, QMessageBox, QFileDialog, QInputDialog, QToolTip, QMenu, QCheckBox, QProgressBar
from PySide6.QtGui import QIcon, QAction, QPainter, QColor, QPixmap,QFont, QPen, QPainterPath, QStandardItemModel, QStandardItem, QGuiApplication, QDesktopServices, QTextCursor, QMovie
from PySide6.QtCore import Qt,QRect,QPropertyAnimation,QThread,Signal,QObject, QUrl, QTimer, QSize

import sys, os
#from hoverbutton import HoverButton
from gui.ui_main_window import Ui_MainWindow
from gui.unit_seperator import get_unit, get_unit_scaling, get_unit_value,get_uv_scaled
from gui.gui_add_electronic import DialogAddElectronic
from gui.gui_add_cavity import DialogAddCavity
from gui.gui_add_pulse import DialogAddPulse
from gui.gui_add_chirp import DialogAddChirp
from gui.gui_add_fitness_function import DialogAddFitness
from gui.gui_parse_components import component_parser
from gui.gui_time_grid_or_tolerance import DialogAddGridOrTolerance
import numpy as np
import scipy as sp
from gui.parse_ansi import replace_ansi_escape_sequences
from collections import defaultdict
from subprocess import Popen, PIPE
import markdown
from time import time
from gui.gui_filter_components import component_filter
from gui.dialogs import getGeneralItems, getCheckedItems
from gui.worker import QDaCCMainWoker, QDaCCSettingGenerator, QDaCCOptimizer

# todo: alles in funktionen umwälzen die über kontextmenü callbar sind
# save/loading.

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.retranslateUi(self)
        self.filepath = os.path.dirname(os.path.realpath(__file__))

        # Set Stylesheet from file
        with open(os.path.join(self.filepath,"style.qss"),"r") as f:
            self.setStyleSheet(f.read())
            
        # Config
        self.colors = {"Background" : "#DDDDDD", 
        "State" : "#88282A3A",
        "StateName" : "#FFFFFF",
        "Transition" : "#88282A3A",
        "Cavity" : ("#aaf4501e", "#aaf4501e"),
        "Neutral" : "#000000",
        "Red" : "#FF0000",
        }
        self.resources = {
            "Icon" : os.path.join(self.filepath,"gui/resources/test.png"),
            "Logo" : os.path.join(self.filepath,"gui/resources/logo.png"),
            "Tree" : os.path.join(self.filepath,"gui/resources/add_random.png"),
            "Arrow_Down_Save" : os.path.join(self.filepath,"gui/resources/arrow_down_save.png"),
            "Arrow_Up_Load" : os.path.join(self.filepath,"gui/resources/arrow_up_load.png"),
            "Save" : os.path.join(self.filepath,"gui/resources/save.png"),
            "Rings" : os.path.join(self.filepath,"gui/resources/rings.png"),
            "Gear" : os.path.join(self.filepath,"gui/resources/gear.png"),
            "OnOff" : os.path.join(self.filepath,"gui/resources/onoff.png"),
            "marrow_right" : os.path.join(self.filepath,"gui/resources/marrow_right.png"),
            "marrow_left" : os.path.join(self.filepath,"gui/resources/marrow_left.png"),
            "graph1" : os.path.join(self.filepath,"gui/resources/graph1.png"),
            "graph2" : os.path.join(self.filepath,"gui/resources/graph2.png"),
            "loading" : os.path.join(self.filepath,"gui/resources/loading_6.gif"),
        }

        self.loading_animation = QMovie(self.resources["loading"])
        self.thread_timer = defaultdict(self.generateQAnimationTimer)
        self.loading_animation_fps = 1000/360
        self.button_run_program.setIconSize(QSize(120,28))
        self.button_plot_everything.setIconSize(QSize(120,28))
        self.button_sweeper_plot.setIconSize(QSize(120,28))
        self.button_optimizer_optimize.setIconSize(QSize(120,28))

        # Thread Dummies
        self.thread = None
        self.optimizer_thread = None
        self.plot_thread = None

        self.plot_system_details = False
        # System Components that contribute to the execution string
        self.system_components = defaultdict(lambda: {})
        self.system_components_fields = {}
        # Hoverable Widgets
        self.system_widgets = {}

        # Clipboard
        self.clipboard = QGuiApplication.clipboard()

        # Cache sizes:
        self.fixed_energy_w, self.fixed_energy_h = None, None

        # Cache Variable for plotting lines
        self.label_plot_spectral_density_cache = []

        # Add functionality to buttons
        self.connect_functionality()

        # Set Name
        self.window_title_unsaved = "[unsaved changes]"
        self.is_currently_unsaved = False
        self.connectObjectsToEdited()
        self.current_qdacc_file_path = f"untitled.qdacc {self.window_title_unsaved}"
        self.refreshWindowTitle()
        # Set .svg logo
        self.setWindowIcon(QIcon(self.resources["Logo"]))

        self.show()
        self.connect_config_to_fields()
        self.set_components_from_fields()
        
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.set_components_from_fields()
        self.update_component_list()
        self.drawSystem()


    def connectObjectsToEdited(self):
        def func():
            self.is_currently_unsaved = True
            self.refreshWindowTitle()
        for name, obj in self.__dict__.items():
            if isinstance(obj, QPushButton):
                obj.clicked.connect(func)
            elif isinstance(obj, (QTextEdit, QLineEdit)):
                obj.textChanged.connect(func)
            elif isinstance(obj, QCheckBox):
                obj.stateChanged.connect(func)

    def generateQAnimationTimer(self):
        timer = QTimer(self)
        timer.timeout.connect(lambda: self.loading_animation.jumpToNextFrame())
        timer.start()
        return timer

    def refreshWindowTitle(self, name = None):
        if name is not None:
            self.current_qdacc_file_path = name
        display_name = os.path.basename(self.current_qdacc_file_path)
        unsaved = f" {self.window_title_unsaved}" if self.is_currently_unsaved else ""
        self.setWindowTitle(f"QDaCC - {display_name}{unsaved}")
    
    def getWindowTitle(self):
        return self.windowTitle().replace("QDaCC - ","")

    def save_to_qdacc_file(self, filepath = "settings.qdacc"):
        from pickle import dump, HIGHEST_PROTOCOL
        print(f"Saving to {filepath}")
        self.set_components_from_fields()
        self.refreshWindowTitle(filepath)
        with open(filepath, "wb") as f:
            print(f"Current Dict: {dict(self.system_components)}")
            dump(dict(self.system_components), f, protocol=HIGHEST_PROTOCOL)
        self.is_currently_unsaved = False
        self.refreshWindowTitle()

    def load_from_qdacc_file(self, filepath = "settings.qdacc", key: str | None = None):
        from pickle import load
        print(f"Loading from {filepath}")
        with open(filepath, "rb") as f:
            loaded = load(f)
            if key:
                self.system_components[key] = loaded[key] 
            else:
                self.refreshWindowTitle(filepath)
                self.system_components.update(loaded)
            print(f"Current Dict: {dict(self.system_components)}")
        self.set_fields_from_components()
        self.is_currently_unsaved = False
        self.refreshWindowTitle()

    def connect_functionality(self):
        # "Next" Buttons
        for button in [self.button_next_tab_system_to_config, self.button_next_tab_config_to_timeline, self.button_next_tab_timeline_to_spectrum, self.button_next_tab_spectrum_to_indist, self.button_next_tab_indist_to_conc, self.button_next_tab_sconc_to_stats, self.button_next_tab_stats_to_detector, self.button_next_tab_detector_to_generate]:
            button.clicked.connect( lambda: self.tabWidget.setCurrentIndex( self.tabWidget.currentIndex() + 1 ) )
        # Add Stuff Dialog
        self.button_add_electronic_state.clicked.connect(lambda: DialogAddElectronic(main_window=self, style_sheet=self.styleSheet()))
        self.button_add_cavity.clicked.connect(lambda: DialogAddCavity(main_window=self, style_sheet=self.styleSheet()))
        self.button_add_optical_pulse.clicked.connect(lambda: DialogAddPulse(main_window=self, style_sheet=self.styleSheet()))
        self.button_add_electronic_shift.clicked.connect(lambda: DialogAddChirp(main_window=self, style_sheet=self.styleSheet()))
        # Modify Stuff
        self.button_modify_clear.clicked.connect(self.clearSystem)
        
        # Set how to as the markdown readme file
        html = markdown.markdown(open(os.path.join(self.filepath,"../README.md")).read(),extensions=['markdown.extensions.fenced_code']) #.replace('<img src="','<img src="../')
        rep = os.path.join(self.filepath,"../")
        html = html.replace('<img src="',f'<img style="max-width:100%" src="{rep}')
        html = html.replace(".svg",".png")
        html = html.replace('px"','"')
        self.output_howto.setHtml(html)

        def modify():
            self.plot_system_details = self.input_draw_details.isChecked()
            self.drawSystem()
        self.input_draw_details.clicked.connect(modify)

        def delete_input():
            current = self.list_components.currentIndex().data()
            if current is None or current == "None":
                return
            name, category = current.split(" - ")
            self.system_components[category].pop(name)
            print(f"Dropped {name} from {category}")
            self.drawSystem()
            self.update_component_list()
        self.button_modify_delete.clicked.connect(delete_input)

        def edit_input():
            current = self.list_components.currentIndex().data()
            print(current)
            if current is None or current == "None":
                return
            name, category = current.split(" - ")
            if category == "EnergyLevels":
                DialogAddElectronic(main_window=self, load_existing=name, style_sheet=self.styleSheet())
            elif category == "CavityLevels":
                DialogAddCavity(main_window=self, load_existing=name, style_sheet=self.styleSheet())
            elif category == "Pulse":
                DialogAddPulse(main_window=self, load_existing=name, style_sheet=self.styleSheet())
            elif category == "Chirp" or category == "Shift":
                DialogAddChirp(main_window=self, load_existing=name, style_sheet=self.styleSheet())
        self.button_modify_edit.clicked.connect(edit_input)
        self.list_components.doubleClicked.connect(edit_input)

        # Config Inputs
        self.button_time_config_tol.clicked.connect(lambda: DialogAddGridOrTolerance(main_window=self,name="Tolerances", style_sheet=self.styleSheet()))
        self.button_time_config_grid.clicked.connect(lambda: DialogAddGridOrTolerance(main_window=self,name="Grid", style_sheet=self.styleSheet()))

        self.button_open_destination_folder.clicked.connect(lambda: QDesktopServices.openUrl(QUrl.fromLocalFile(self.textinput_file_destination.text())))
        
        # Empty Target Folder
        def empty_target_folder():
            dest = self.textinput_file_destination.text()
            files = [f for f in os.listdir(dest) if f.endswith(".txt") or f.endswith(".png") or f.endswith(".log") or f.endswith(".pdf")]
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Clear Destination Folder?")
            msg.setInformativeText(f"Are you sure you want to clear the contents of '{dest}'? Only .txt, .pdf, .png and .log files are deleted. There are {len(files)} files to delete.")
            msg.setWindowTitle("Clear Destination Folder?")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Cancel)
            msg.setStyleSheet(self.styleSheet())
            retval = msg.exec()
            if retval == QMessageBox.Ok:
                for file in files:
                    try:
                        path = os.path.join(dest,file)
                        print(f"Deleting {path}")
                        os.remove(path)
                    except Exception as e:
                        print(f"Failed to delete {file}: {e}")

        self.button_empty_destination_folder.clicked.connect(empty_target_folder)

        # Loading / Saving
        def export_command(name = None):
            if name is None:
                dlg = QFileDialog()
                dlg.setFileMode(QFileDialog.AnyFile)
                dlg.setAcceptMode(QFileDialog.AcceptSave)
                dlg.setNameFilters(["*.qdacc", "*.log"])
                if dlg.exec():
                    filename = dlg.selectedFiles()[0]
                else:
                    self.sendErrorMessage("No File Selected", "No file has been selected. Please use 'Export QDaCC Command' to save a new file.")
                    return
            else:
                filename = name
            if filename.endswith(self.window_title_unsaved):
                filename = filename[:-1]
            print(f"Exporting to {filename}")
            self.save_to_qdacc_file(filepath = filename)

        def import_command(key: str | None = None):
            dlg = QFileDialog()
            dlg.setFileMode(QFileDialog.AnyFile)
            dlg.setAcceptMode(QFileDialog.AcceptOpen)
            dlg.setNameFilters(["*.qdacc", "*.log"])
            if dlg.exec():
                filenames = dlg.selectedFiles()
                self.load_from_qdacc_file(filepath = filenames[0], key=key )
                self.drawSystem()
                self.update_component_list()
        
        def export_save_existing():
            filename = self.current_qdacc_file_path
            if filename is None:
                self.sendErrorMessage("No File Loaded", "No file has been loaded. Please use 'Export QDaCC Command' to save a new file.")
                return
            # Get "OK" Dialog
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Overwrite Existing File?")
            msg.setInformativeText(f"Are you sure you want to overwrite the existing file '{filename}'?")
            msg.setWindowTitle("Overwrite File?")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Cancel)
            msg.setStyleSheet(self.styleSheet())
            retval = msg.exec()
            if retval == QMessageBox.Ok:
                export_command(name = filename)

        # File Path
        def set_file_path():
            dlg = QFileDialog()
            dlg.setFileMode(QFileDialog.Directory)
            if dlg.exec():
                filename = dlg.selectedFiles()[0]
                if not filename.endswith("/"):
                    filename += "/"
                self.textinput_file_destination.setText(filename)
        def set_qdacc_filepath():
            dlg = QFileDialog()
            dlg.setFileMode(QFileDialog.AnyFile)
            dlg.setAcceptMode(QFileDialog.AcceptOpen)
            dlg.setNameFilters(["*.exe", "*.out", "*.*"])
            if dlg.exec():
                filenames = dlg.selectedFiles()
                #path = os.path.relpath(filenames[0], os.getcwd())
                self.textinput_file_qdacc.setText(filenames[0])
        self.input_destination.clicked.connect(set_file_path) 
        self.input_path_to_qdacc.clicked.connect(set_qdacc_filepath) 
        
        # Save Settings
        def set_settingfile_path():
            dlg = QFileDialog()
            dlg.setFileMode(QFileDialog.AnyFile)
            dlg.setAcceptMode(QFileDialog.AcceptSave)
            dlg.setNameFilters(["*.txt", "*.*"])
            if dlg.exec():
                filename = dlg.selectedFiles()[0]
                self.textinput_path_to_settingfile.setText(filename)
        self.button_set_setting_file_path.clicked.connect(set_settingfile_path)
        
        def save_to_setting_file(filepath, project_name):
            one = self.checkbox_activate_scan_parameter_1.isChecked()
            dual = self.checkbox_activate_scan_parameter_2.isChecked()
            runstring = self.text_output_program_qdacc_command_sweep.toPlainText()
            
            qdacc_path_str = self.textinput_file_qdacc.text()
            qdacc_path = qdacc_path_str.split("/")
            qdacc_executable = qdacc_path[-1]
            cwd = qdacc_path_str.replace(qdacc_executable, "")
            self.settings_thread = QDaCCSettingGenerator(parent=self, mgx = self.mgx, mgy = self.mgy, values = self.scan_sweep_values, file = filepath, name = project_name, converter = self.commandToCLAList, runstring = runstring, one = one, two = dual)
    
            self.settings_thread.pipeUpdatesTo(lambda text: self.updateTextBrowser(self.text_output_program_main, text), lambda text: self.updateProgressBar(self.progressBar,text)) 
            self.settings_thread.pipeUpdatesTo(lambda text: self.updateTextBrowser(self.text_output_program_qdacc_command_sweep_display, text), None) 
            self.settings_thread.connectStarted(lambda: self.enableRunningButtonAnimation(self.button_sweeper_plot, [self.button_run_program, self.button_plot_everything]))
            self.settings_thread.connectFinished(lambda: self.disableRunningButtonAnimation(self.button_sweeper_plot, "Generate Settingfile", [self.button_run_program, self.button_plot_everything]))

            self.settings_thread.start()
        
        def save_settings_file():
            filepath = self.textinput_path_to_settingfile.text()
            if filepath == "":
                return
            project_name, ok = QInputDialog.getText(self, "Save Settings", "Project Name", QLineEdit.Normal, filepath.split("/")[-1].replace(".txt", "").replace("settings_",""))
            self.text_output_program_main.append(f"Saving Settingfile to {filepath}")
            if not ok or not len(project_name):
                self.sendErrorMessage("No Name given")
                return
            save_to_setting_file(filepath, project_name)
        self.save_settings_file = save_settings_file

        def toggle_runstring_full_settingfile():
            current_text = self.text_output_program_qdacc_command.toPlainText()
            print(current_text)
            if "--file" in current_text:
                generate_command()
            else:   
                runstr = f"[QDaCC] --file [SETTINGFILE] [FILEPATH]"
                self.text_output_program_qdacc_command.setPlainText(runstr)
        self.button_change_rungstring_to_settingfile.clicked.connect(toggle_runstring_full_settingfile)

        def pick_from_list_of_available_states():
            items = self.generate_list_of_available_total_states()
            print(items)
            item, ok = QInputDialog.getItem(self, "Select Input State", "Valid States", items, 0, False)
            if ok and item:
                self.textinput_initial_state.setText(item)
        self.input_initial_state.clicked.connect(pick_from_list_of_available_states)

        # Dynamic change phonons
        def toggle_phonon_inputs():
            enable = self.input_phonons_use_qd.isChecked()
            for a in [self.textinput_phonons_sd_qd_de,self.textinput_phonons_sd_qd_dh,self.textinput_phonons_sd_qd_rho,self.textinput_phonons_sd_qd_cs,self.textinput_phonons_sd_qd_aeah_ratio,self.textinput_phonons_sd_qd_size]:
                a.setEnabled(enable)
            self.textinput_phonons_sd_alpha.setEnabled(not enable)
        self.input_phonons_use_qd.stateChanged.connect(toggle_phonon_inputs)

        # Set ListView Models
        self.list_components.setModel(QStandardItemModel())
        self.text_output_list_of_spectra.setModel(QStandardItemModel())

        # Add/Remove Spectrum Buttons
        def spectrum_add():
            spec_modes = self.textinput_spectrum_modes.text().split(",")
            spec_range = self.textinput_spectrum_range.text()
            spec_center = self.textinput_spectrum_center.text()
            spec_res = self.textinput_spectrum_res.text()
            spec_order = self.input_spectrum_order.currentIndex()
            spec_norm = self.input_spectrum_normalize.isChecked()
            name = f"{''.join(spec_modes)}{spec_range}{spec_center}{spec_res}{spec_order}{spec_norm}"
            self.add_component( "Spectrum", {"Name" : name, "Modes" : spec_modes, "Range" : spec_range, "Center" : spec_center, "Res" : spec_res, "Order" : spec_order, "Norm": spec_norm} )
            #self.text_output_list_of_spectra.model().appendRow(QStandardItem(f"For modes {','.join(spec_modes)} at center {spec_center} with resolution {spec_res} and range {spec_range}. Identifier: {name}"))
            self.update_component_list()
        def spectrum_remove():
            index = self.text_output_list_of_spectra.currentIndex().row()
            name = self.text_output_list_of_spectra.model().item(index).toolTip()
            self.system_components["Spectrum"].pop(name)
            self.update_component_list()
            #self.text_output_list_of_spectra.model().removeRow(self.text_output_list_of_spectra.currentIndex().row().row())
        def spectrum_active_change():
            try:
                index = self.text_output_list_of_spectra.currentIndex().row()
                name = self.text_output_list_of_spectra.model().item(index).toolTip()
            except:
                return
            struct = self.system_components["Spectrum"][name]
            for text, field in zip( [",".join(struct["Modes"]), struct["Range"], struct["Center"], struct["Res"]], [self.textinput_spectrum_modes, self.textinput_spectrum_range, self.textinput_spectrum_center, self.textinput_spectrum_res] ):
                field.setText(text)
            self.input_spectrum_order.setCurrentIndex(struct["Order"])
            self.input_spectrum_normalize.setChecked(struct["Norm"])
        def spectrum_predict_plot():
            # alle cavs. und transitions durchgehen
            # alle energien rausschreiben
            # für jede cav lorentzpeak
            # für jede transition lorentzpeak
            from matplotlib.lines import Line2D
            def normalize(y):
                return (y-np.min(y))/(np.max(y)-np.min(y))
            def lorentzian(x, a, x0):
                return normalize(1 / ((x-x0)**2 + a**2) / np.pi)
            energies_cavity = [ get_uv_scaled(struct["Energy"]) for struct in self.system_components["CavityLevels"].values() ]
            #transition = list(set([ abs(get_uv_scaled(struct["Energy"]) - get_uv_scaled(other["Energy"])) for struct in self.system_components["EnergyLevels"].values() for other in self.system_components["EnergyLevels"].values() ]))
            transition = list(set([ abs(get_uv_scaled(struct["Energy"]) - get_uv_scaled(self.system_components["EnergyLevels"][other]["Energy"])) for struct in self.system_components["EnergyLevels"].values() for other in struct["CoupledTo"] ]))
            self.label_plot_spectral_prediction.canvas.axes.clear()
            mmax = np.max(energies_cavity + transition)
            mmin = np.min(energies_cavity + transition)
            mean = np.median(energies_cavity + transition)/5000
            x = np.linspace( mmin-4*mean,mmax+4*mean, 10000)
            cavity_kappa = get_uv_scaled(self.textinput_rates_cavity_loss.text())
            cavity_g = get_uv_scaled(self.textinput_rates_cavity_coupling.text())
            electronic_gamma = get_uv_scaled(self.textinput_rates_radiative_decay.text())+get_uv_scaled(self.textinput_rates_pure_dephasing.text())
            ev_scaling = 1/get_unit_scaling("eV")
            if len(energies_cavity):
                self.label_plot_spectral_prediction.canvas.axes.plot(x*ev_scaling, normalize(sum([lorentzian(x-cavity_g, cavity_kappa, cav)+lorentzian(x+cavity_g, cavity_kappa, cav) for cav in energies_cavity])), color="blue")
            if len(transition):
                self.label_plot_spectral_prediction.canvas.axes.plot(x*ev_scaling, normalize(sum([lorentzian(x, electronic_gamma, tra) for tra in transition])), color="red")
            lines = [Line2D([0], [0], color="blue"), Line2D([0], [0], color="red")]
            self.label_plot_spectral_prediction.canvas.axes.legend(lines,["Cavity", "Transition"])
            self.label_plot_spectral_prediction.canvas.draw()
        
        self.text_output_list_of_spectra.selectionModel().selectionChanged.connect(spectrum_active_change)
        self.button_add_spectrum_to_output.clicked.connect(spectrum_add)
        self.button_remove_spectrum_from_output.clicked.connect(spectrum_remove)

        # Spectrum Mode Button
        self.button_add_spectrum_mode.clicked.connect(lambda: self.textinput_spectrum_modes.setText( self.getListOfTransitions() ))

        # Indist
        self.text_output_list_of_indists.setModel(QStandardItemModel())
        def indist_add():
            indist_modes = self.textinput_indist_modes.text().split(",")
            if not len(indist_modes):
                return
            for mode in indist_modes:
                if not len(mode):
                    continue
                self.add_component( "Indistinguishability", {"Name" : mode, "Mode" : mode} )
            self.update_component_list()
        def indist_remove():
            index = self.text_output_list_of_indists.currentIndex().row()
            name = self.text_output_list_of_indists.model().item(index).toolTip()
            if name is None or not len(name):
                return
            if name not in self.system_components["Indistinguishability"]:
                return
            self.system_components["Indistinguishability"].pop(name)
            self.update_component_list()
        self.button_add_indist_to_output.clicked.connect(indist_add)
        self.button_remove_indist_from_output.clicked.connect(indist_remove)

        self.button_add_indist_mode.clicked.connect(lambda: self.textinput_indist_modes.setText( self.getListOfTransitions() ))

        # Concurrence
        self.text_output_list_of_concurrences.setModel(QStandardItemModel())
        def concurrence_add():
            concurrence_mode_1 = self.textinput_concurrence_first.text()
            concurrence_mode_2 = self.textinput_concurrence_second.text()
            if not len(concurrence_mode_1) or not len(concurrence_mode_2):
                return
            self.add_component( "Concurrence", {"Name" : concurrence_mode_1+concurrence_mode_2, "Mode" : concurrence_mode_1+"+"+concurrence_mode_2} )
            self.update_component_list()
        def concurrence_remove():
            index = self.text_output_list_of_concurrences.currentIndex().row()
            name = self.text_output_list_of_concurrences.model().item(index).toolTip()
            if name is None or not len(name):
                return
            if name not in self.system_components["Concurrence"]:
                return
            self.system_components["Concurrence"].pop(name)
            self.update_component_list()
        def toggle_concurrence_spectrum():
            enable = self.input_concurrence_add_spectra.isChecked()
            for a in [self.textinput_concurrence_spec_freq,self.textinput_concurrence_spec_range,self.textinput_concurrence_spec_res]:
                a.setEnabled(enable)
        self.input_concurrence_add_spectra.stateChanged.connect(toggle_concurrence_spectrum)
        self.button_add_concurrence_to_output.clicked.connect(concurrence_add)
        self.button_remove_concurrence_from_output.clicked.connect(concurrence_remove)

        self.button_add_concurrence_mode_1.clicked.connect(lambda: self.textinput_concurrence_first.setText( self.getListOfTransitions() ))
        self.button_add_concurrence_mode_2.clicked.connect(lambda: self.textinput_concurrence_second.setText( self.getListOfTransitions() ))

        # G1 and G2
        self.text_output_list_of_gfuncs.setModel(QStandardItemModel())
        def gfunc_add():
            modes = self.textinput_correlation_modes.text().split(",")
            order = self.input_gfunc_order.currentIndex()
            method = self.input_gfunc_integration.currentIndex()
            if not len(modes):
                return
            for mode in modes:
                if not len(mode):
                    continue
                name = mode+str(order)+str(method)
                self.add_component( "G1G2", {"Name" : name, "Mode" : mode, "Order" : order, "Method" : method} )
            self.update_component_list()
        def gfunc_remove():
            index = self.text_output_list_of_gfuncs.currentIndex().row()
            name = self.text_output_list_of_gfuncs.model().item(index).toolTip()
            if name is None or not len(name):
                return
            if name not in self.system_components["G1G2"]:
                return
            self.system_components["G1G2"].pop(name)
            self.update_component_list()
        self.button_add_gfunc_to_output.clicked.connect(gfunc_add)
        self.button_remove_gfunc_from_output.clicked.connect(gfunc_remove)

        self.button_add_gfunc_mode.clicked.connect(lambda: self.textinput_correlation_modes.setText( self.getListOfTransitions() ))

        # Detector
        self.text_output_list_of_detector_time.setModel(QStandardItemModel())
        def detector_time_add():
            t0 = self.textinput_detector_t0.text()
            t1 = self.textinput_detector_t1.text()
            power = self.textinput_detector_tpower.text()
            if not len(t0) or not len(t1) or not len(power):
                return
            name = t0+t1+power
            self.add_component( "DetectorTime", {"Name" : name, "t0" : t0, "t1" : t1, "Power" : power} )
            self.update_component_list()
        def detector_time_remove():
            index = self.text_output_list_of_detector_time.currentIndex().row()
            name = self.text_output_list_of_detector_time.model().item(index).toolTip()
            if name is None or not len(name):
                return
            if name not in self.system_components["DetectorTime"]:
                return
            self.system_components["DetectorTime"].pop(name)
            self.update_component_list()
        self.text_output_list_of_detector_spec.setModel(QStandardItemModel())
        def detector_spec_add():
            w0 = self.textinput_detector_wcenter.text()
            w1 = self.textinput_detector_wrange.text()
            res = self.textinput_detector_wnum.text()
            power = self.textinput_detector_wpower.text()
            if not len(w0) or not len(w1) or not len(res) or not len(power):
                return
            name = w0+w1+res+power
            self.add_component( "DetectorSpectrum", {"Name" : name, "w0" : w0, "w1" : w1, "Points" : res, "Power" : power} )
            self.update_component_list()
        def detector_spec_remove():
            index = self.text_output_list_of_detector_spec.currentIndex().row()
            name = self.text_output_list_of_detector_spec.model().item(index).toolTip()
            if name is None or not len(name):
                return
            if name not in self.system_components["DetectorSpectrum"]:
                return
            self.system_components["DetectorSpectrum"].pop(name)
            self.update_component_list()
        self.button_add_detector_time.clicked.connect(detector_time_add)
        self.button_add_detector_spectral.clicked.connect(detector_spec_add)
        self.button_remove_detector_time.clicked.connect(detector_time_remove)
        self.button_remove_detector_spectral.clicked.connect(detector_spec_remove)
        

        # Wigner Function
        self.text_output_list_of_wigner_funcs.setModel(QStandardItemModel())
        def wigner_func_add():
            modes = self.textinput_wigner_modes.text().split(",")
            xmax = self.textinput_wigner_x.text()
            ymax = self.textinput_wigner_y.text()
            res = self.textinput_wigner_resolution.text()
            skip = self.textinput_wigner_skip.text()
            if not len(modes):
                return
            for mode in modes:
                if not len(mode):
                    continue
                name = mode+xmax+ymax+res+skip
                self.add_component( "Wigner", {"Name" : name, "Mode" : mode, "XMax" : xmax, "YMax" : ymax, "Resolution" : res, "Skip" : skip} )
            self.update_component_list()
        def wigner_func_remove():
            index = self.text_output_list_of_wigner_funcs.currentIndex().row()
            name = self.text_output_list_of_wigner_funcs.model().item(index).toolTip()
            if name is None or not len(name):
                return
            if name not in self.system_components["Wigner"]:
                return
            self.system_components["Wigner"].pop(name)
            self.update_component_list()
        self.button_add_wigner.clicked.connect(wigner_func_add)
        self.button_remove_wigner.clicked.connect(wigner_func_remove)

        # Phonon Spectral functions
        def phonon_spectral_function(multi: bool = False):
            phonon_ohm = get_uv_scaled(self.textinput_phonons_sd_ohmamp.text())
            phonon_cutoff = get_uv_scaled(self.textinput_phonons_sd_wcutoff.text())
            x = np.linspace(0, 6*phonon_cutoff, 1000)
            if multi:
                phonon_rho = get_uv_scaled(self.textinput_phonons_sd_qd_rho.text())
                phonon_de = get_uv_scaled(self.textinput_phonons_sd_qd_de.text())
                phonon_dh = get_uv_scaled(self.textinput_phonons_sd_qd_dh.text())
                phonon_cs = get_uv_scaled(self.textinput_phonons_sd_qd_cs.text())
                phonon_ahr = get_uv_scaled(self.textinput_phonons_sd_qd_aeah_ratio.text())
                phonon_s = get_uv_scaled(self.textinput_phonons_sd_qd_size.text())
                ac_over_cs = phonon_s**2/(4*phonon_cs**2)
                hbar = get_unit_scaling("hbar")
                y = hbar*x**phonon_ohm / (4*np.pi**2*phonon_rho*phonon_cs**5)*( phonon_de*np.exp(-x**2*ac_over_cs) - phonon_dh*np.exp(-x**2*ac_over_cs/phonon_ahr**2) )**2
            else:
                phonon_alpha = get_uv_scaled(self.textinput_phonons_sd_alpha.text())
                y = phonon_alpha * x**phonon_ohm * np.exp(-x**2/phonon_cutoff**2/2)
            return x,y
        def plot_phonon_spectral_function():
            self.label_plot_spectral_density.canvas.axes.clear()
            if self.input_phonons_use_qd.isChecked():
                x,y = phonon_spectral_function(True)
                c = "C1"
            else:
                x,y = phonon_spectral_function()
                c = "C0"
            self.label_plot_spectral_density_cache.append((x,y,c))
            self.label_plot_spectral_density.canvas.axes.plot(x,y, color=c)
            for i,(x,y,c) in enumerate(self.label_plot_spectral_density_cache):
                self.label_plot_spectral_density.canvas.axes.plot(x,y, color=c, alpha = 1-0.9*i/len(self.label_plot_spectral_density_cache), linestyle="dotted")
            if len(self.label_plot_spectral_density_cache) > 10:
                self.label_plot_spectral_density_cache.pop(0)
            # legend
            self.label_plot_spectral_density.canvas.axes.legend(["Simple", "QD Params"])
            self.label_plot_spectral_density.canvas.draw()

        for field in [self.textinput_phonons_iterator_stepsize, self.textinput_phonons_sd_wcutoff, self.textinput_phonons_sd_wdelta, self.textinput_phonons_sd_tcutoff, self.textinput_phonons_sd_ohmamp, self.textinput_phonons_sd_alpha,
                      self.textinput_phonons_sd_qd_de, self.textinput_phonons_sd_qd_rho, self.textinput_phonons_sd_qd_aeah_ratio, self.textinput_phonons_sd_qd_dh, self.textinput_phonons_sd_qd_cs, self.textinput_phonons_sd_qd_size]:
            field.editingFinished.connect(plot_phonon_spectral_function)
        
        # TODO: statt dem hier N TLS einfügen, dann aus den TLS die transitions berechnen, und daraus den Tensor.
        # Experimental: Add N coupled TLS
        def get_N_level_couplings(cl: str, prefix: str, energy):
            coupled_to = []
            for i in range(len(cl)):
                if cl[i] != "1":
                    state = f"{cl[:i] + '1' + cl[i+1:]}"
                    coupled_to.append( state ) 
            # Add state to system
            self.addEnergyLevel({"Name": f"{prefix}{cl}","Energy": energy(),"CoupledTo": tuple([f"{prefix}{ct}" for ct in coupled_to]),"DecayScaling" : "1" if "1" in cl else "0","DephasingScaling": "1","PhononScaling": "1" if "1" in cl else "0"} )
            return coupled_to
        def add_N_levels(nTLS: int = 2, energy: float = 1.0, sd = 1E-3, unit: str = "eV", prefix: str = "X"):
            states = ["0"*nTLS]
            current_deph = 0
            while len(states):
                if energy is not None:                    
                    # random value between -sd and +sd
                    senergy = lambda current_deph=current_deph: f"{current_deph * (energy + (np.random.rand() - 0.5) * sd)}{unit}"
                else:
                    en = QInputDialog.getDouble(self, 'Energy', f'Energy for State {current_deph} in eV', 1, 0, 1000, 10)[0]
                    senergy = lambda current_deph=current_deph: f"{en}{unit}"
                states = [get_N_level_couplings(state, prefix, senergy) for state in states]
                states = [item for sebstates in states for item in sebstates]
                states = list(set(states))
                current_deph += 1
                print(current_deph)
            len(states)
        def dialog_add_N_levels():
            nTLS, ok = QInputDialog.getInt(self, "Add N TLS", "Number of TLS", 2, 1, 30, 1)
            if ok:
                energy, ok2 = QInputDialog.getDouble(self, "Energy", "Singe State Energy in eV", 1, 0, 1000, 1)
            if ok and ok2:
                stv, ok3 = QInputDialog.getDouble(self, "Energy Uncertainty", "Energy Uncertainty in mueV", 0, 0, 100000,1)
            if ok and ok2 and ok3:
                add_N_levels(nTLS, energy, stv*1E-6)

        def abbreviate_names():
            from string import ascii_uppercase as replace # This is the list of letters to use
            replace_rules = {} # This will be a dict of {old_name: new_name}
            super_index = 0 # This will ensure Letters A-Z, then A0, B0, ... A1, B1, ... is used.
            # Build Replace Dict
            for i,state in enumerate(self.system_components["EnergyLevels"].values()):
                replace_rules[state["Name"]] = f"{replace[i%len(replace)]}{super_index-1 if super_index > 0 else ''}"
                if i%len(replace) == 0 and i > 0:
                    super_index += 1
            print(f"Replace Rulse are {replace_rules}")
            # Replace All Transitions in Cavities, Pulses, Chirps and Levels
            for level in self.system_components["EnergyLevels"].values():
                level["Name"] = replace_rules[level["Name"]]
                level["CoupledTo"] = tuple([replace_rules[ct] for ct in level["CoupledTo"]])
            # Rename Keys
            self.system_components["EnergyLevels"] = { content["Name"] : content for name,content in self.system_components["EnergyLevels"].items() }
            for cavity in self.system_components["CavityLevels"].values():
                cavity["CoupledTo"] = tuple("=".join([replace_rules[a] for a in transition.split("=")]) if "=" in transition else transition for transition in cavity["CoupledTo"])
            # Rename Keys
            self.system_components["CavityLevels"] = { content["Name"] : content for name,content in self.system_components["CavityLevels"].items() }
            for shift in self.system_components["Shift"].values():
                shift["CoupledTo"] = tuple([replace_rules[ct] for ct in shift["CoupledTo"]])
            # Rename Keys
            self.system_components["Shift"] = { content["Name"] : content for name,content in self.system_components["Shift"].items() }
            for pulse in self.system_components["Pulse"].values():
                pulse["CoupledTo"] = tuple("=".join([replace_rules[a] for a in transition.split("=")]) if "=" in transition else transition for transition in pulse["CoupledTo"])
            # Rename Keys
            self.system_components["Pulse"] = { content["Name"] : content for name,content in self.system_components["Pulse"].items() }

            self.set_fields_from_components()
            self.update_component_list()
            self.drawSystem()


        def print_all_transitions():
            print(",".join(self.generate_list_of_available_electronic_transitions()))
        

        def clipboard_copy_transition_list():
            self.clipboard.setText(",".join(self.generate_list_of_available_electronic_transitions()))
        def clipboard_copy_sum_of_transition_list():
            self.clipboard.setText("+".join(self.generate_list_of_available_electronic_transitions()))
            

        self.button_plot_everything.clicked.connect(self.plot_everything)

        # Run
        def generate_command():
            # Check for initial state
            if not len(self.textinput_initial_state.text()):
                pick_from_list_of_available_states()
            self.set_components_from_fields()
            command = self.generateCommandString()
            self.text_output_program_qdacc_command.setText(command)
            self.clipboard.setText(" ".join(self.commandToCLAList(command)))
        self.button_generate_run.clicked.connect(generate_command)

        def run_command(input_command: str | None = None, start_already: bool = True, plot_afterwards: bool = False):
            # Strip QDaCC Path and Destination Path
            destination, qdacc_executable, qdacc_path_str = self.getQDaCCPaths()
            print(f"QDaCC Executable: {qdacc_executable}")
            print(f"QDaCC Working Directory: {destination}")
            # Build command
            if input_command is None:
                input_command = self.text_output_program_qdacc_command.toPlainText()
            # Insert Destination and QDaCC Path
            #input_command = self.commandToCLAList(input_command)
            #input_command = input_command.replace(qdacc_path_str, qdacc_executable).replace("'"+destination+"'", "")
            #input_command = input_command.split() + [f"{destination}"]

            self.thread = QDaCCMainWoker(parent=self, cwd=qdacc_path_str, command=input_command)
            self.thread.pipeUpdatesTo(lambda text: self.updateTextBrowser(self.text_output_program_main, text), lambda text: self.updateProgressBar(self.progressBar,text)) 
            self.thread.connectStarted(lambda: self.enableRunningButtonAnimation(self.button_run_program, [self.button_plot_everything]))
            self.thread.connectFinished(lambda: self.disableRunningButtonAnimation(self.button_run_program, "Run", [self.button_plot_everything]))
            if plot_afterwards:
                self.thread.connectFinished(lambda: self.plot_everything())

            if start_already:
                self.thread.start()

            return self.thread
        
        def kill_command():
            self.text_output_program_main.append("Killed QDaCC!")
            from signal import CTRL_C_EVENT 
            for thread in [self.thread, self.optimizer_thread, self.plot_thread]:
                try:
                    thread.process.send_signal(CTRL_C_EVENT)
                    thread.process.kill()
                    thread.quit()
                    thread.wait()
                except:
                    print("No QDaCC Thread Running.")
            self.progressBar.setValue(0)
            

        self.button_run_program.clicked.connect(lambda: run_command(None))
        self.button_run_and_plot.clicked.connect(lambda: run_command(None, plot_afterwards=True))
        for btn in [self.button_run_and_plot, self.button_run_program]:
            btn.clicked.connect(lambda: self.text_output_program_main.verticalScrollBar().setValue(self.text_output_program_main.verticalScrollBar().maximum()))
        # Set button icon
        self.button_run_kill.clicked.connect(kill_command)

        # Optimizer
        self.button_optimizer_get_runstring.clicked.connect(lambda: self.text_output_program_qdacc_command_sweep_2.setText(self.text_output_program_qdacc_command.toPlainText()))
        def optimize():
            try:
                files = eval(f"[{self.textinput_optimizer_files.text()}]")
                indices = eval(f"[{self.textinput_optimizer_file_indices.text()}]")
                legend = eval(f"[{self.textinput_optimizer_legend.text()}]")
                initial_parameters = eval(f"[{self.textinput_optimizer_initial_parameters.text()}]")
                bounds = eval(f"[{self.textinput_optimizer_parameter_bounds.text()}]")
                names = eval(f"[{self.textinput_optimizer_parameter_names.text()}]")
                formatter = self.textinput_optimizer_formatfunction.text()
                fitnessfunction = self.textinput_optimizer_fitnessfunction.text()
                eps = float(self.textinput_optimizer_eps.text())
                tolerance = float(self.textinput_optimizer_tol.text())
                maxit = int(self.textinput_optimizer_maxit.text())
            except Exception as e:
                print("Error when parsing inputs. Make sure to use python syntax like [x], where x is your input.")
                self.text_output_program_qdacc_command_sweep_display_2.append("Error when parsing inputs. Make sure to use python syntax like [x], where x is your input.")
                print(e)
                return
            plot_lim = None#[0,1.1]
            plot_lim_q = None

            command = self.text_output_program_qdacc_command_sweep_2.toPlainText()
            destination, _, qdacc_path_str = self.getQDaCCPaths()
            plot_after_iteration = self.optimizer_call_plotscript.isChecked()
            plot_is_folder = "--file" in self.text_output_program_qdacc_command_sweep_2.toPlainText()
            self.optimizer_thread = QDaCCOptimizer(parent=self, cwd=qdacc_path_str, command=command, path=destination, files=files, indices=indices, initial_parameters=initial_parameters, bounds=bounds, eps=eps,
                                    formatter=formatter, fitness=fitnessfunction, tol=tolerance, maxit=maxit, base_eval_dict=self.buildBaseEvaluationDict(), variables=self.system_components["OptimizerFitnessVariables"], 
                                    plot_after_iteration=plot_after_iteration, plot_is_folder=plot_is_folder)
            self.optimizer_thread.pipeUpdatesTo(lambda text: self.updateTextBrowser(self.text_output_program_main, text), lambda text: self.updateProgressBar(self.progressBar,text)) 
            self.optimizer_thread.connectStarted(lambda: self.enableRunningButtonAnimation(self.button_run_program, [self.button_plot_everything]))
            self.optimizer_thread.connectStarted(lambda: self.enableRunningButtonAnimation(self.button_optimizer_optimize, None))
            self.optimizer_thread.connectFinished(lambda: self.disableRunningButtonAnimation(self.button_run_program, "Run", [self.button_plot_everything]))
            self.optimizer_thread.connectFinished(lambda: self.disableRunningButtonAnimation(self.button_optimizer_optimize, "Optimize", None))
            self.optimizer_thread.outputParametersTo(self.text_output_program_qdacc_command_sweep_display_2)

            def plotstuffs():
                #data = input_optimizer_files(self.textinput_file_destination.text(), ["electronic.txt"] ,[[0,1]])
                current_data = self.optimizer_thread.data
                variables_to_plot = self.optimizer_thread.variables_to_plot
                current_quality = self.optimizer_thread.quality_data
                current_params = self.optimizer_thread.parameter_data
                self.current_optimizer_runstring = self.optimizer_thread.runstring
                # Clear Axes
                for axes in [self.label_plot_optimizer_1.canvas.axes, self.label_plot_optimizer_2.canvas.axes, self.label_plot_optimizer_3.canvas.axes]:
                    axes.clear()

                for variable in variables_to_plot:
                    self.label_plot_optimizer_1.canvas.axes.plot(variable)
                for i,(dataset,name) in enumerate(zip(reversed(current_data),reversed(legend))):
                    if name == "None" or name is None:
                        continue
                    for c,(x,y) in enumerate(dataset):
                        self.label_plot_optimizer_1.canvas.axes.plot(y, linewidth=3.5 - 3*i/len(current_data), color="C"+str(c), alpha=1-0.8*i/len(current_data), linestyle = "dotted" if i > 0 else "solid")
                self.label_plot_optimizer_2.canvas.axes.plot(current_quality)
                for parameter_set in current_params:
                    self.label_plot_optimizer_3.canvas.axes.plot(parameter_set)
                self.latest_optimizer_parameters = [p[-1] for p in current_params]
                
                # Limits
                self.label_plot_optimizer_1.canvas.axes.set_ylim(plot_lim)
                self.label_plot_optimizer_2.canvas.axes.set_ylim(plot_lim_q)

                # Legends
                self.label_plot_optimizer_1.canvas.axes.legend(["Variable" for _ in variables_to_plot] + [l for l in legend if l is not None and l != "None"])
                self.label_plot_optimizer_2.canvas.axes.legend(["Fitness"])
                self.label_plot_optimizer_3.canvas.axes.legend(names)

                # Draw Canvas
                for canvas in [self.label_plot_optimizer_1.canvas, self.label_plot_optimizer_2.canvas, self.label_plot_optimizer_3.canvas]:
                    canvas.draw()
            
            self.optimizer_thread.plot_hint.connect(plotstuffs)
            self.optimizer_thread.finished.connect(plotstuffs)
            self.optimizer_thread.start()

        self.button_optimizer_optimize.clicked.connect(optimize)

        self.button_optimizer_runstring_to_main.clicked.connect(lambda: self.text_output_program_qdacc_command.setText(self.current_optimizer_runstring))
        self.button_optimizer_runstring_to_main.clicked.connect(lambda: self.tabWidget.setCurrentIndex(9))
        self.button_optimizer_fitness_function.clicked.connect(lambda: DialogAddFitness(main_window=self, style_sheet=self.styleSheet()))

        # Helper Functions
        def getOptimizerAvailableFiles():
            files = [f for f in os.listdir(self.textinput_file_destination.text()) if f.endswith(".txt")]
            items, ok = getGeneralItems([{"Title": file, "Type": QCheckBox} for file in files], parent=self) 
            if not ok:
                return
            new_text = ",".join( [item for item,include in zip(files, items) if include] )
            self.textinput_optimizer_files.setText(new_text)
        self.button_optimizer_files.clicked.connect(getOptimizerAvailableFiles)
    
        def getOptimizerFileIndices():
            files = eval("["+self.textinput_optimizer_files.text()+"]")
            new_indices = ""
            for file in files:
                try:
                    with open(os.path.join(self.textinput_file_destination.text(), file), "r") as f:
                        data_header = f.readline()
                except Exception as e:
                    print("No Valid File")
                    continue
                if not len(data_header):
                    continue
                data_header = data_header.split()
                items, ok = getGeneralItems([{"Title": file, "Type": QCheckBox} for file in data_header], parent=self)
                if not ok:
                    return
                if not len(items):
                    new_indices += ",[]"
                    continue
                new_indices += ",[" + ",".join( [str(i) for i,(item,include) in enumerate(zip(data_header, items)) if include] ) + "]"
            self.textinput_optimizer_file_indices.setText(new_indices[1:])
        self.button_optimizer_files_2.clicked.connect(getOptimizerFileIndices)

        # Optimizer Helper Functions
        def moveCurrentOpzimizerParametersToInitialParameters():
            try:
                self.textinput_optimizer_initial_parameters.setText( ",".join([str(el) for el in self.latest_optimizer_parameters]) )
            except AttributeError as e:
                print(f"Error when trying to move parameters to initial parameters. Make sure to run an optimizer first.")
        def clearOptimizerPlots():
            for axes in [self.label_plot_optimizer_1.canvas.axes, self.label_plot_optimizer_2.canvas.axes, self.label_plot_optimizer_3.canvas.axes]:
                axes.clear()
            for canvas in [self.label_plot_optimizer_1.canvas, self.label_plot_optimizer_2.canvas, self.label_plot_optimizer_3.canvas]:
                canvas.draw()
        def forceKillOptimizer():
            try:
                self.optimizer_thread.kill()
            except Exception as e:
                print("Killed Optimizer")
        def seedInitialOptimizerParameters():
            input_bounds = self.textinput_optimizer_parameter_bounds.text().replace("None,","-1").replace(",None","1")
            bounds = eval(input_bounds)
            if not bounds or not len(bounds):
                return
            initial_parameters = [ np.random.rand() * (b[1]-b[0]) + b[0] for b in bounds ]
            self.textinput_optimizer_initial_parameters.setText( ",".join([str(el) for el in initial_parameters]) )
        def seedInitialOptimizerParametersInRange():
            vals, ok = getGeneralItems([{"Title": "Lower Bound", "Type": QLineEdit, "Text": "0"}, {"Title": "Upper Bound", "Type": QLineEdit, "Text": "1"}], self)
            if not ok or vals is None:
                print("Invalid Inputs!")
                return
            lower_bound, upper_bound = float(vals[0]), float(vals[1])
            length = len(self.textinput_optimizer_initial_parameters.text().split(","))
            self.textinput_optimizer_initial_parameters.setText( ",".join([str(np.random.rand() * (upper_bound-lower_bound) + lower_bound) for _ in range(length)]) )


        # Menu
        actions_to_add = [  
            ["Print Component Dict", lambda: print(self.system_components), self.menuDeveloper_Tools, None, None, None],
            ["Set Components from Fields", self.set_components_from_fields, self.menuDeveloper_Tools, None, None, None],
            ["Set Fields from Components", self.set_fields_from_components, self.menuDeveloper_Tools, None, None, None],
            ["Connect Fields", self.connect_config_to_fields, self.menuDeveloper_Tools, None, None, None],
            ["Plot Predicted Spectra", spectrum_predict_plot, self.menuFunctions, self.resources["graph2"], None, None],
            ["Plot Phonon Functions", plot_phonon_spectral_function, self.menuFunctions, self.resources["graph2"], None, None],
            ["Optimizer", None, self.menuFunctions, None, [
                ["Set Initial Parameters to latest Parameters", moveCurrentOpzimizerParametersToInitialParameters, "parent", None, None, None],
                ["Randomly Initialize Parameters in bounds", seedInitialOptimizerParameters, "parent", None, None, None],
                ["Randomly Initialize Parameters in range", seedInitialOptimizerParametersInRange, "parent", None, None, None],
                ["Clear Optimizer Plots", clearOptimizerPlots, "parent", None, None, None],
                ["Cancel Optimization", forceKillOptimizer, "parent", None, None, None],
            ], None],
            ["Add N TLS with statistical deviation", dialog_add_N_levels, self.menuEdit, self.resources["Tree"], None, None],
            ["Print All Transitions", print_all_transitions, self.menuDeveloper_Tools, None, None, None],
            ["Copy List of Transitions", clipboard_copy_transition_list, self.menuEdit, self.resources["marrow_right"], None, "Ctrl+C"],
            ["Copy Sum of Transitions", clipboard_copy_sum_of_transition_list, self.menuEdit, self.resources["marrow_right"], None, "Ctrl+Shift+C"],
            ["Abbreviate State Names", abbreviate_names, self.menuEdit, self.resources["marrow_right"], None, None],
            ["Export", lambda: export_command(), self.menuMenu, self.resources["Arrow_Up_Load"], None, "Ctrl+E"],
            ["Import", import_command, self.menuMenu, self.resources["Arrow_Down_Save"], None, "Ctrl+I"],
            ["Import", None, self.menuMenu, self.resources["Arrow_Down_Save"], [
                ["States", lambda: import_command("EnergyLevels"), "parent", None, None, None],
                ["Cavities", lambda: import_command("CavityLevels"), "parent", None, None, None],
                ["Pulses", lambda: import_command("Pulse"), "parent", None, None, None],
                ["Shifts", lambda: import_command("Shift"), "parent", None, None, None],
                ["Paths", lambda: import_command("RunConfig"), "parent", None, None, None],
                ["Sweeper", lambda: import_command("Sweeper"), "parent", None, None, None],
                ["System Config", lambda: import_command("ConfigSystem"), "parent", None, None, None],], None],
            ["Save Current", export_save_existing, self.menuMenu, self.resources["Save"], None, "Ctrl+S"],
            ["Redraw System", self.drawSystem, self.menuDeveloper_Tools, None, None, None],
            ["Clear System", self.clearSystem, self.menuDeveloper_Tools, None, None, None],
            ["Generate QDaCC Command", generate_command, self.menuDeveloper_Tools, None, None, None],
            ["Set initial State", pick_from_list_of_available_states, self.menuDeveloper_Tools, None, None, None],
            ["Set File Destination", set_file_path, self.menuDeveloper_Tools, None, None, None],
            ["Set QDaCC Filepath", set_qdacc_filepath, self.menuDeveloper_Tools, None, None, None],
            ["Run QDaCC", lambda: run_command(None), self.menuMenu, self.resources["Gear"], None, None],
        ]
        def add_to_menu(name, connect, where, icon, children, shortcut):
            if children:
                submenu = where.addMenu(name)
                if icon:
                    submenu.setIcon(QIcon(icon))
                for child in children:
                    child[2] = submenu
                    add_to_menu(*child)
                return
            action = QAction(name, self)
            action.triggered.connect(connect)
            if shortcut:
                action.setShortcut(shortcut)
            if icon:
                action.setIcon(QIcon(icon))
            where.addAction(action)
        for name, connect, where, icon, children, shortcut in actions_to_add:
            add_to_menu(name, connect, where, icon, children, shortcut)


        self.slider_state_grouping.valueChanged.connect(self.drawSystem)
        self.slider_state_separator.valueChanged.connect(self.drawSystem)

        # Connect Sweeper
        self.button_sweeper_plot.clicked.connect(self.generate_scan_or_sweep)
        self.button_sweeper_get_runstring.clicked.connect(lambda: self.text_output_program_qdacc_command_sweep.setText(self.text_output_program_qdacc_command.toPlainText()))

        # Copy Button
        self.button_generate_copy.clicked.connect(lambda: self.clipboard.setText(" ".join(self.commandToCLAList(self.text_output_program_qdacc_command.toPlainText()))))

    def getListOfTransitions(self) -> str:
        states = self.generate_list_of_available_electronic_transitions() + self.generate_list_of_available_cavity_states()
        print(f"Picking from {states}")
        checked_items, ok = getCheckedItems(states, parent=self)
        print(f"Checked {checked_items}")
        if not ok:
            return
        new_states = ",".join(checked_items)
        # Prune final ","
        if new_states.endswith(","):
            new_states = new_states[:-1]
        return new_states

    def getQDaCCPaths(self):
        qdacc_path_str = self.textinput_file_qdacc.text() or "./QDaCC.exe"
        destination = self.textinput_file_destination.text()
        qdacc_path = qdacc_path_str.split("/")
        qdacc_executable = qdacc_path[-1]
        return destination, qdacc_executable, f"{os.sep}".join(qdacc_path[:-1])

    def enableRunningButtonAnimation(self, button: QPushButton, disable_along: list[QPushButton] | None = None):
        current_text = button.text()
        timer = self.thread_timer[current_text]
        timer.setInterval(self.loading_animation_fps)
        timer.timeout.connect(lambda: button.setIcon(QIcon(self.loading_animation.currentPixmap())))
        timer.start()
        button.setText("")
        button.setDisabled(True)
        if disable_along is not None:
            for other_button in disable_along:
                other_button.setDisabled(True)
        return current_text

    def disableRunningButtonAnimation(self, button: QPushButton, text: str, enable_along: list[QPushButton] | None = None):
        self.thread_timer[text].stop()
        button.setText(text)
        button.setIcon(QIcon())
        button.setDisabled(False)
        if enable_along is not None:
            for other_button in enable_along:
                other_button.setDisabled(False)
        self.progressBar.setValue(0)

    def generate_list_of_available_electronic_transitions(self):
            transitions = []
            for state in self.system_components["EnergyLevels"].values():
                for transition in state["CoupledTo"]:
                    transitions.append(f"{state['Name']}={transition}")
            return transitions
    def generate_list_of_available_electronic_states(self):
            return list(self.system_components["EnergyLevels"].keys())
    def generate_list_of_available_cavity_states(self):
            return list(self.system_components["CavityLevels"].keys())

    def generate_list_of_available_total_states(self):
            available_states = []
            for state in self.system_components["EnergyLevels"]:
                new_state = f"{state}" + "".join([f":0{name}" for name in self.system_components["CavityLevels"]])
                available_states.append(new_state)
            return available_states

    def pushCursorToBack(self, field):
        cursor = field.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        cursor.movePosition(QTextCursor.MoveOperation.Left)
        field.setTextCursor(cursor)

    def updateTextBrowser(self, browser: QTextBrowser, text: str):
        self.pushCursorToBack(browser)
        if "br>" in text:
            browser.insertHtml(text)
        else:
            browser.append(text)

    def updateProgressBar(self, pb: QProgressBar, value: int | str):
        if isinstance(value, int):
            pb.setValue(value)
        else:
            try:
                pb.setValue(int(value.split("%")[0].split()[-1]))
            except Exception as e:
                pass

    def sendMessage(self, bar: str, title: str, message: str):
        msg = QMessageBox()
        #msg.setIcon(QMessageBox.Critical)
        msg.setText(title)
        msg.setInformativeText(message)
        msg.setWindowTitle(bar)
        msg.setStyleSheet(self.styleSheet())
        msg.exec()
    def sendErrorMessage(self, error: str = "Error!", message: str = "Error!"):
        self.sendMessage("Error!",error,message)
    def sendWarningMessage(self, warning: str = "Warning!", message: str = "Warning!"):
        self.sendMessage("Warning!",warning,message)
    def sendHintMessage(self, message: str = "Attention!"):
        self.sendMessage("Attention!","Attention!",message)

    def clearSystem(self):
        self.system_components["EnergyLevels"] = {}
        self.system_energy_level_groups = list()
        self.system_components["CavityLevels"] = {}
        self.system_cavity_level_groups = list()
        self.system_components["Pulse"] = {}
        self.system_components["Shift"] = {}
        self.update_component_list()
        self.drawSystem()

    def sort_energy_levels(self) -> None:
        levels = [a for a in self.system_components["EnergyLevels"].values()]
        if len(levels) < 2:
            return
        levels.sort(key=lambda l: get_uv_scaled(l["Energy"]))
        group_threshold = (self.slider_state_grouping.value()*0.01)**6
        # Check grouping
        grouping_threshold = abs(get_uv_scaled(levels[0]["Energy"]) - get_uv_scaled(levels[-1]["Energy"])) * group_threshold
        self.system_energy_level_groups = list()
        self.system_energy_level_groups.append([levels[0]]) # List of Groupings
        for level in levels[1:]:
            if abs(get_uv_scaled(level["Energy"]) - get_uv_scaled(self.system_energy_level_groups[-1][-1]["Energy"])) < grouping_threshold:
                # Is Part of Group
                self.system_energy_level_groups[-1].append(level)
            else:
                self.system_energy_level_groups.append([level])

    ###########################################################################################################
    ########################################### Adding System Components ######################################
    ###########################################################################################################
    def add_component(self, category: str, struct: dict, replaced: str | None = None) -> None:
        name = struct["Name"]
        changed = "Added" if name not in self.system_components[category] else "Replaced"
        if replaced:
            # Get Ok Dialog for replacing
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setText(f"Replace {replaced} with {name}?")
            msg.setInformativeText(f"Are you sure you want to replace {replaced} with {name}?")
            msg.setWindowTitle("Replace")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setStyleSheet(self.styleSheet())
            retval = msg.exec()
            if retval == QMessageBox.Cancel:
                return
            # Replace Elements in CoupledTo in ElectronicLevels, CavityLevels, Pulse and Shift with new name
            for cat in ["EnergyLevels", "CavityLevels", "Pulse", "Shift"]:
                for level, lstruct in self.system_components[cat].items():
                    if any([replaced in a for a in lstruct["CoupledTo"]]):
                        self.system_components[cat][level]["CoupledTo"] = tuple([ct.replace(replaced,name) for ct in self.system_components[cat][level]["CoupledTo"]])
        self.system_components[category][name] = struct

        self.update_component_list()
        self.drawSystem()
        print(changed, self.system_components[category][name])

    def update_component_list(self) -> None:
        model = self.list_components.model()
        model.clear()
        for cat in self.system_components:
            if cat not in ["EnergyLevels", "CavityLevels", "Pulse", "Shift"]:
                continue 
            for name in self.system_components[cat]:
                item = QStandardItem(name + " - " + cat)
                model.appendRow(item)
        model = self.text_output_list_of_spectra.model()
        model.clear()
        for name,struct in self.system_components["Spectrum"].items():
            item = QStandardItem(f"For modes {','.join(struct['Modes'])} at center {struct['Center']} with resolution {struct['Res']} and range {struct['Range']}")
            item.setToolTip(name)
            model.appendRow(item)
        model = self.text_output_list_of_indists.model()
        model.clear()
        for name, struct in self.system_components["Indistinguishability"].items():
            item = QStandardItem(f"For mode(s): {struct['Mode']}")
            item.setToolTip(name)
            model.appendRow(item)
        model = self.text_output_list_of_concurrences.model()
        model.clear()
        for name, struct in self.system_components["Concurrence"].items():
            item = QStandardItem(f"For mode(s): {struct['Mode']}")
            item.setToolTip(name)
            model.appendRow(item)
        model = self.text_output_list_of_gfuncs.model()
        model.clear()
        for name, struct in self.system_components["G1G2"].items():
            item = QStandardItem(f"For mode(s): {struct['Mode']} using G{2 if struct['Order'] else 1} with output method {struct['Method']}")
            item.setToolTip(name)
            model.appendRow(item)
        model = self.text_output_list_of_wigner_funcs.model()
        model.clear()
        for name, struct in self.system_components["Wigner"].items():
            item = QStandardItem(f"For mode(s): {struct['Mode']} with x in [-{struct['XMax']},{struct['XMax']}] and y in [-{struct['YMax']},{struct['YMax']}] at resoultion {struct['Resolution']}. Outputting every {struct['Skip']} timesteps.")
            item.setToolTip(name)
            model.appendRow(item)
        model = self.text_output_list_of_detector_time.model()
        model.clear()
        for name, struct in self.system_components["DetectorTime"].items():
            item = QStandardItem(f"At t0 = {struct['t0']} with width {struct['t1']} and power falloff {struct['Power']}")
            item.setToolTip(name)
            model.appendRow(item)
        model = self.text_output_list_of_detector_spec.model()
        model.clear()
        for name, struct in self.system_components["DetectorSpectrum"].items():
            item = QStandardItem(f"At w0 = {struct['w0']} with width {struct['w1']} and power falloff {struct['Power']}. Using {struct['Points']} fourier points.")
            item.setToolTip(name)
            model.appendRow(item)

    def addEnergyLevel(self, p: dict, replaced: str | None = None ):
        self.add_component( "EnergyLevels", p , replaced)
        
    def addCavity(self, p: dict, replaced: str | None = None):
        self.add_component( "CavityLevels", p , replaced)

    def addPulse(self, p: dict):
        # Confirm that Pulse sizes are the same:
        a,f,c,w,t = len(p["Amplitudes"]), len(p["Frequencies"]), len(p["Centers"]), len(p["Widths"]), len(p["Type"])
        if not (a==f and f==c and c==w and w==t):
            self.sendErrorMessage("Wrong Pulse Dimensions", "The arrays you entered for the Pulse parameters must be of equal length!")
            return
        self.add_component( "Pulse", p )
        
    def addShift(self, p: dict):
        self.add_component( "Shift", p )

    # Parses All configs from always-on entries like time, solver, etc.
    def connect_config_to_fields(self):
        error_message_wrong_energy_units = "Error when inputting Units.\nUnits supported by QDaCC:\n- Hz\n- eV\n- meV\n- mueV"
        error_message_must_be_numerical = "Must be a numerical"
        error_message_wrong_time_units = "Error when inputting Units.\nUnits supported by QDaCC:\n- s\n- ns\n- ps\n- fs"
        # Time
        self.system_components_fields["ConfigTime"] = {
            "Start" : {"field": self.textinput_time_startingtime, "parse": self.textinput_time_startingtime.text, "set": self.textinput_time_startingtime.setText, "typeof" : str, "default": "0", "callback": error_message_wrong_time_units, "filters": ("NotEmpty", "IsUnitConvertible", "MustBeTime")},
            "End" : {"field": self.textinput_time_endtime, "parse": self.textinput_time_endtime.text, "set": self.textinput_time_endtime.setText, "typeof" : str, "default": "auto", "callback": error_message_wrong_time_units, "filters": ("NotEmpty", "IsUnitConvertible", "MustBeTime")},
            "Step" : {"field": self.textinput_time_timestep, "parse": self.textinput_time_timestep.text, "set": self.textinput_time_timestep.setText, "typeof" : str, "default": "auto", "callback": error_message_wrong_time_units, "filters": ("NotEmpty", "IsUnitConvertible", "MustBeTime")},
        }
        self.system_components_fields["ConfigGrid"] = {
            "Resolution" : {"field": self.textinput_time_gridresolution, "parse": self.textinput_time_gridresolution.text, "set": self.textinput_time_gridresolution.setText, "typeof" : str, "default": "auto", "callback": "Must be positive integer", "filters": ("NotEmpty", "PositiveInteger")},
        }
        self.system_components_fields["ConfigTolerances"] = {
            "Resolution" : {"field": self.textinput_time_tolerance, "parse": self.textinput_time_tolerance.text, "set": self.textinput_time_tolerance.setText, "typeof" : str, "default": "1E-6", "callback": "Must be positive float", "filters": ("NotEmpty", "PositiveFloat")},
        }
        self.system_components_fields["ConfigSolver"] = {
            "Solver" : {"field": self.input_rungekutta_order, "parse": self.input_rungekutta_order.currentIndex, "set": self.input_rungekutta_order.setCurrentIndex, "typeof" : int, "default": None, "callback": None, "filters": None},
            "Interpolator" : {"field": self.input_interpolator_t, "parse": self.input_interpolator_t.currentIndex, "set": self.input_interpolator_t.setCurrentIndex, "typeof" : int, "default": None, "callback": None, "filters": None},
            "InterpolatorGrid" : {"field": self.input_interpolator_tau, "parse": self.input_interpolator_tau.currentIndex, "set": self.input_interpolator_tau.setCurrentIndex, "typeof" : int, "default": None, "callback": None, "filters": None},
            "NC" : {"field": self.textinput_phonons_nc, "parse": self.textinput_phonons_nc.text, "set": self.textinput_phonons_nc.setText, "typeof" : str, "default": "4", "callback": "Must be a positive Integer.\nIdeally, NC is greater than 3.", "filters": ("NotEmpty", "PositiveInteger")},
        }
        self.system_components_fields["ConfigSystem"] = {
            "Coupling" : {"field": self.textinput_rates_cavity_coupling, "parse": self.textinput_rates_cavity_coupling.text, "set": self.textinput_rates_cavity_coupling.setText, "typeof" : str, "default": "0", "callback": error_message_wrong_energy_units, "filters": ("NotEmpty", "IsUnitConvertible", "MustBeEnergy")},
            "CavityLosses" : {"field": self.textinput_rates_cavity_loss, "parse": self.textinput_rates_cavity_loss.text, "set": self.textinput_rates_cavity_loss.setText, "typeof" : str, "default": "0", "callback": error_message_wrong_energy_units, "filters": ("NotEmpty", "IsUnitConvertible", "MustBeEnergy")},
            "RadiativeLosses" : {"field": self.textinput_rates_radiative_decay, "parse": self.textinput_rates_radiative_decay.text, "set": self.textinput_rates_radiative_decay.setText, "typeof" : str, "default": "0", "callback": error_message_wrong_energy_units, "filters": ("NotEmpty", "IsUnitConvertible", "MustBeEnergy")},
            "DephasingLosses" : {"field": self.textinput_rates_pure_dephasing, "parse": self.textinput_rates_pure_dephasing.text, "set": self.textinput_rates_pure_dephasing.setText, "typeof" : str, "default": "0", "callback": error_message_wrong_energy_units, "filters": ("NotEmpty", "IsUnitConvertible", "MustBeEnergy")},
        }
        self.system_components_fields["ConfigPhonons"] = {
            "Temperature" : {"field": self.textinput_phonons_temperature, "parse": self.textinput_phonons_temperature.text, "set": self.textinput_phonons_temperature.setText, "typeof" : str, "default": "No Phonons", "callback": "Must be a numerical >= 0", "filters": "IsFloat"},
            "IteratorStep" : {"field": self.textinput_phonons_iterator_stepsize, "parse": self.textinput_phonons_iterator_stepsize.text, "set": self.textinput_phonons_iterator_stepsize.setText, "typeof" : str, "default": "auto", "callback": "Must be a numerical >= 0 or 'auto'", "filters": ("NotEmpty","PositiveUnitConvertible")},
            "Approximation" : {"field": self.input_phonons_approximation, "parse": self.input_phonons_approximation.currentIndex, "set": self.input_phonons_approximation.setCurrentIndex, "typeof" : int, "default": None, "callback": None, "filters": None},
            "ARRad" : {"field": self.input_phonons_adjust_radiativeloss, "parse": self.input_phonons_adjust_radiativeloss.isChecked, "set": self.input_phonons_adjust_radiativeloss.setChecked, "typeof" : bool, "default": None, "callback": None, "filters": None},
            "ARDep" : {"field": self.input_phonons_adjust_pure_dephasing, "parse": self.input_phonons_adjust_pure_dephasing.isChecked, "set": self.input_phonons_adjust_pure_dephasing.setChecked, "typeof" : bool, "default": None, "callback": None, "filters": None},
            "Renormalization" : {"field": self.input_phonons_adjust_renormalization, "parse": self.input_phonons_adjust_renormalization.isChecked, "set": self.input_phonons_adjust_renormalization.setChecked, "typeof" : bool, "default": None, "callback": None, "filters": None},
            "Alpha" : {"field": self.textinput_phonons_sd_alpha, "parse": self.textinput_phonons_sd_alpha.text, "set": self.textinput_phonons_sd_alpha.setText, "typeof" : str, "default": "0.03E-24", "callback": "Must be a numerical", "filters": "PositiveFloat"},
            "SpectralCutoff" : {"field": self.textinput_phonons_sd_wcutoff, "parse": self.textinput_phonons_sd_wcutoff.text, "set": self.textinput_phonons_sd_wcutoff.setText, "typeof" : str, "default": "1meV", "callback": error_message_wrong_energy_units, "filters": ("NotEmpty", "PositiveUnitConvertible","MustBeEnergy")},
            "SpectralDelta" : {"field": self.textinput_phonons_sd_wdelta, "parse": self.textinput_phonons_sd_wdelta.text, "set": self.textinput_phonons_sd_wdelta.setText, "typeof" : str, "default": "0.01meV", "callback": error_message_wrong_energy_units, "filters": ("NotEmpty", "PositiveUnitConvertible","MustBeEnergy")},
            "TimeCutoff" : {"field": self.textinput_phonons_sd_tcutoff, "parse": self.textinput_phonons_sd_tcutoff.text, "set": self.textinput_phonons_sd_tcutoff.setText, "typeof" : str, "default": "4ps", "callback": error_message_wrong_time_units, "filters": ("NotEmpty", "PositiveUnitConvertible", "MustBeTime")},
            "Ohm" : {"field": self.textinput_phonons_sd_ohmamp, "parse": self.textinput_phonons_sd_ohmamp.text, "set": self.textinput_phonons_sd_ohmamp.setText, "typeof" : str, "default": "3", "callback": "Must be a positive float", "filters": "PositiveFloat"},
            "UseQD" : {"field": self.input_phonons_use_qd, "parse": self.input_phonons_use_qd.isChecked, "set": self.input_phonons_use_qd.setChecked, "typeof" : bool, "default": None, "callback": None, "filters": None},
            "QDde" : {"field": self.textinput_phonons_sd_qd_de, "parse": self.textinput_phonons_sd_qd_de.text, "set": self.textinput_phonons_sd_qd_de.setText, "typeof" : str, "default": "7eV", "callback": error_message_wrong_energy_units, "filters": ("NotEmpty", "PositiveUnitConvertible","MustBeEnergy")},
            "QDdh" : {"field": self.textinput_phonons_sd_qd_dh, "parse": self.textinput_phonons_sd_qd_dh.text, "set": self.textinput_phonons_sd_qd_dh.setText, "typeof" : str, "default": "-3.5eV", "callback": error_message_wrong_energy_units, "filters": ("NotEmpty", "NegativeUnitConvertible","MustBeEnergy")},
            "QDrho" : {"field": self.textinput_phonons_sd_qd_rho, "parse": self.textinput_phonons_sd_qd_rho.text, "set": self.textinput_phonons_sd_qd_rho.setText, "typeof" : str, "default": "5370", "callback": "Material Density in kg/m^3. Must be positive float.", "filters": ("NotEmpty","PositiveFloat")},
            "QDcs" : {"field": self.textinput_phonons_sd_qd_cs, "parse": self.textinput_phonons_sd_qd_cs.text, "set": self.textinput_phonons_sd_qd_cs.setText, "typeof" : str, "default": "5110", "callback": "Speed of Sound in m/s. Must be positive float", "filters": ("NotEmpty","PositiveFloat")},
            "QDeh" : {"field": self.textinput_phonons_sd_qd_aeah_ratio, "parse": self.textinput_phonons_sd_qd_aeah_ratio.text, "set": self.textinput_phonons_sd_qd_aeah_ratio.setText, "typeof" : str, "default": "1.15", "callback": "Must be positive float", "filters": ("NotEmpty","PositiveFloat")},
            "QDs" : {"field": self.textinput_phonons_sd_qd_size, "parse": self.textinput_phonons_sd_qd_size.text, "set": self.textinput_phonons_sd_qd_size.setText, "typeof" : str, "default": "3", "callback": "Must be positive float", "filters": ("NotEmpty","PositiveFloat")},
            "DTPI" : {"field": self.textinput_phonons_tsteppath, "parse": self.textinput_phonons_tsteppath.text, "set": self.textinput_phonons_tsteppath.setText, "typeof" : str, "default": "auto", "callback": error_message_wrong_time_units, "filters": ("NotEmpty", "PositiveUnitConvertible", "MustBeTime")},
        }
        self.system_components_fields["InitialState"] = {
            "State" : {"field": self.textinput_initial_state, "parse": self.textinput_initial_state.text, "set": self.textinput_initial_state.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
        }
        self.system_components_fields["RunConfig"] = {
            "Pathqdacc" : {"field": self.textinput_file_qdacc, "parse": self.textinput_file_qdacc.text, "set" : self.textinput_file_qdacc.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "PathOutput" : {"field": self.textinput_file_destination, "parse": self.textinput_file_destination.text, "set" : self.textinput_file_destination.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "LoggingLevel" : {"field": self.input_logginglevel, "parse": self.input_logginglevel.currentIndex, "set" : self.input_logginglevel.setCurrentIndex, "typeof" : int, "default": None, "callback": None, "filters": None},
            "DMOutputMode" : {"field": self.input_dm_mode, "parse": self.input_dm_mode.currentIndex, "set" : self.input_dm_mode.setCurrentIndex, "typeof" : int, "default": None, "callback": None, "filters": None},
            "OutputFrame" : {"field": self.input_dm_frame, "parse": self.input_dm_frame.currentIndex, "set" : self.input_dm_frame.setCurrentIndex, "typeof" : int, "default": None, "callback": None, "filters": None},
            "CPUCores" : {"field": self.textinput_cpucores, "parse": self.textinput_cpucores.text, "set" : self.textinput_cpucores.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "Settingfile" : {"field": self.textinput_path_to_settingfile, "parse": self.textinput_path_to_settingfile.text, "set" : self.textinput_path_to_settingfile.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "qdaccRun" : {"field": self.text_output_program_qdacc_command, "parse": self.text_output_program_qdacc_command.toPlainText, "set" : self.text_output_program_qdacc_command.setPlainText, "typeof" : str, "default": None, "callback": None, "filters": None},
        }
        self.system_components_fields["OutputFlags"] = {
            "eigenvalues" : {"field": self.input_add_output_eigenvalues, "parse": self.input_add_output_eigenvalues.isChecked, "set" : self.input_add_output_eigenvalues.setChecked, "typeof" : bool, "default": None, "callback": None, "filters": None},
            "operators" : {"field": self.input_add_output_operators, "parse": self.input_add_output_operators.isChecked, "set" : self.input_add_output_operators.setChecked, "typeof" : bool, "default": None, "callback": None, "filters": None},
            "rkerror" : {"field": self.input_add_output_rkerror, "parse": self.input_add_output_rkerror.isChecked, "set" : self.input_add_output_rkerror.setChecked, "typeof" : bool, "default": None, "callback": None, "filters": None},
            "path" : {"field": self.input_add_output_vonneumannpath, "parse": self.input_add_output_vonneumannpath.isChecked, "set" : self.input_add_output_vonneumannpath.setChecked, "typeof" : bool, "default": None, "callback": None, "filters": None},
            "detectortrafo" : {"field": self.input_add_output_detecotrtrafo, "parse": self.input_add_output_detecotrtrafo.isChecked, "set" : self.input_add_output_detecotrtrafo.setChecked, "typeof" : bool, "default": None, "callback": None, "filters": None},
            "greenf" : {"field": self.input_add_output_greenf, "parse": self.input_add_output_greenf.isChecked, "set" : self.input_add_output_greenf.setChecked, "typeof" : bool}, # also for PIkernel if PI is , "default": None, "callback": None, "filters": Noneused
            "phononJ" : {"field": self.input_add_output_phononj, "parse": self.input_add_output_phononj.isChecked, "set" : self.input_add_output_phononj.setChecked, "typeof" : bool, "default": None, "callback": None, "filters": None},
            "phononcoefficients" : {"field": self.input_add_output_phononcoeffs, "parse": self.input_add_output_phononcoeffs.isChecked, "set" : self.input_add_output_phononcoeffs.setChecked, "typeof" : bool, "default": None, "callback": None, "filters": None}, 
            "conc" : {"field": self.input_add_output_concurrence_eigs, "parse": self.input_add_output_concurrence_eigs.isChecked, "set" : self.input_add_output_concurrence_eigs.setChecked, "typeof" : bool, "default": None, "callback": None, "filters": None},
            "tpm" : {"field": self.input_add_output_tpm, "parse": self.input_add_output_tpm.isChecked, "set" : self.input_add_output_tpm.setChecked, "typeof" : bool, "default": None, "callback": None, "filters": None},
            "chirpf" : {"field": self.input_add_output_chirp_fourier, "parse": self.input_add_output_chirp_fourier.isChecked, "set" : self.input_add_output_chirp_fourier.setChecked, "typeof" : bool, "default": None, "callback": None, "filters": None},
            "pulsef" : {"field": self.input_add_output_pulse_fourier, "parse": self.input_add_output_pulse_fourier.isChecked, "set" : self.input_add_output_pulse_fourier.setChecked, "typeof" : bool, "default": None, "callback": None, "filters": None},
            "photons" : {"field": self.input_add_output_photon_expv, "parse": self.input_add_output_photon_expv.isChecked, "set" : self.input_add_output_photon_expv.setChecked, "typeof" : bool, "default": None, "callback": None, "filters": None},
        }
        self.system_components_fields["ConcurrenceSpectrum"] = {
            "Active" : {"field": self.input_concurrence_add_spectra, "parse": self.input_concurrence_add_spectra.isChecked, "set" : self.input_concurrence_add_spectra.setChecked, "typeof" : bool, "default": None, "callback": None, "filters": None},
            "Center" : {"field": self.textinput_concurrence_spec_freq, "parse": self.textinput_concurrence_spec_freq.text, "set" : self.textinput_concurrence_spec_freq.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "Range" : {"field": self.textinput_concurrence_spec_range, "parse": self.textinput_concurrence_spec_range.text, "set" : self.textinput_concurrence_spec_range.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "Res" : {"field": self.textinput_concurrence_spec_res, "parse": self.textinput_concurrence_spec_res.text, "set" : self.textinput_concurrence_spec_res.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
        }
        self.system_components_fields["Sweeper"] = {
            "Parameter1" : {"field": self.checkbox_activate_scan_parameter_1, "parse": self.checkbox_activate_scan_parameter_1.isChecked, "set" : self.checkbox_activate_scan_parameter_1.setChecked, "typeof" : bool, "default": None, "callback": None, "filters": None},
            "Parameter2" : {"field": self.checkbox_activate_scan_parameter_1, "parse": self.checkbox_activate_scan_parameter_1.isChecked, "set" : self.checkbox_activate_scan_parameter_1.setChecked, "typeof" : bool, "default": None, "callback": None, "filters": None},
            "From1" : {"field": self.textinput_scan_parameter_1_from, "parse": self.textinput_scan_parameter_1_from.text, "set" : self.textinput_scan_parameter_1_from.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "From2" : {"field": self.textinput_scan_parameter_2_from, "parse": self.textinput_scan_parameter_2_from.text, "set" : self.textinput_scan_parameter_2_from.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "to1" : {"field": self.textinput_scan_parameter_1_to, "parse": self.textinput_scan_parameter_1_to.text, "set" : self.textinput_scan_parameter_1_to.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "to2" : {"field": self.textinput_scan_parameter_2_to, "parse": self.textinput_scan_parameter_2_to.text, "set" : self.textinput_scan_parameter_2_to.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "Points1" : {"field": self.textinput_scan_parameter_1_points, "parse": self.textinput_scan_parameter_1_points.text, "set" : self.textinput_scan_parameter_1_points.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "Points2" : {"field": self.textinput_scan_parameter_2_points, "parse": self.textinput_scan_parameter_2_points.text, "set" : self.textinput_scan_parameter_2_points.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "Lambda1" : {"field": self.textinput_scan_parameter_1_lambda, "parse": self.textinput_scan_parameter_1_lambda.text, "set" : self.textinput_scan_parameter_1_lambda.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "Lambda2" : {"field": self.textinput_scan_parameter_2_lambda, "parse": self.textinput_scan_parameter_2_lambda.text, "set" : self.textinput_scan_parameter_2_lambda.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "DisplayField" : {"field": self.text_output_program_qdacc_command_sweep, "parse": self.text_output_program_qdacc_command_sweep.toPlainText, "set" : self.text_output_program_qdacc_command_sweep.setPlainText, "typeof" : str, "default": None, "callback": None, "filters": None},
        }
        self.system_components_fields["Detector"] = {}
        self.system_components_fields["Plotting"] = {}
        self.system_components_fields["Optimizer"] = {
            "Files" : {"field": self.textinput_optimizer_files, "parse": self.textinput_optimizer_files.text, "set" : self.textinput_optimizer_files.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "Indices" : {"field": self.textinput_optimizer_file_indices, "parse": self.textinput_optimizer_file_indices.text, "set" : self.textinput_optimizer_file_indices.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "Legend" : {"field": self.textinput_optimizer_legend, "parse": self.textinput_optimizer_legend.text, "set" : self.textinput_optimizer_legend.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "Parameters" : {"field": self.textinput_optimizer_initial_parameters, "parse": self.textinput_optimizer_initial_parameters.text, "set" : self.textinput_optimizer_initial_parameters.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "Bounds" : {"field": self.textinput_optimizer_parameter_bounds, "parse": self.textinput_optimizer_parameter_bounds.text, "set" : self.textinput_optimizer_parameter_bounds.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "Names" : {"field": self.textinput_optimizer_parameter_names, "parse": self.textinput_optimizer_parameter_names.text, "set" : self.textinput_optimizer_parameter_names.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "OutputField" : {"field": self.text_output_program_qdacc_command_sweep_2, "parse": self.text_output_program_qdacc_command_sweep_2.toPlainText, "set" : self.text_output_program_qdacc_command_sweep_2.setPlainText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "Fitness" : {"field": self.textinput_optimizer_fitnessfunction, "parse": self.textinput_optimizer_fitnessfunction.text, "set" : self.textinput_optimizer_fitnessfunction.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "Format" : {"field": self.textinput_optimizer_formatfunction, "parse": self.textinput_optimizer_formatfunction.text, "set" : self.textinput_optimizer_formatfunction.setText, "typeof" : str, "default": None, "callback": None, "filters": None},
            "Tol" : {"field": self.textinput_optimizer_tol, "parse": self.textinput_optimizer_tol.text, "set" : self.textinput_optimizer_tol.setText, "typeof" : str, "default": "1e-6", "callback": "Must be positive float", "filters": ("NotEmpty","PositiveFloat")},
            "Eps" : {"field": self.textinput_optimizer_eps, "parse": self.textinput_optimizer_eps.text, "set" : self.textinput_optimizer_eps.setText, "typeof" : str, "default": "1e-6", "callback": "Must be positive float", "filters": ("NotEmpty","PositiveFloat")},
            "MaxIt" : {"field": self.textinput_optimizer_maxit, "parse": self.textinput_optimizer_maxit.text, "set" : self.textinput_optimizer_maxit.setText, "typeof" : str, "default": "100", "callback": "Must be positive float", "filters": ("NotEmpty","PositiveFloat")},
            "CallPlot" : {"field": self.optimizer_call_plotscript, "parse": self.optimizer_call_plotscript.isChecked, "set" : self.optimizer_call_plotscript.setChecked, "typeof" : bool, "default": None, "callback": None, "filters": None},
        }

        # Connect Basic Input Checkers
        for cat in self.system_components_fields.values():
            for field in cat.values():
                if "default" in field and field["default"] is not None:
                    filters = (field["filters"],) if isinstance(field["filters"],str) else field["filters"]
                    field["field"].editingFinished.connect( lambda cat=cat, field=field, default=field["default"], callback=field["callback"], filters=filters: field["set"](component_filter(field["parse"](), default, lambda: self.forceToolTip(field["field"], callback), *filters)) )


        # Connect Sweeper Dropdown boxes to caching functions. Whenever dropdown is changed, cache current value and change current text to cached value
        self.textinput_scan_parameter_1_lambda.textChanged.connect(lambda: self.system_components["SweeperLambdas"].update({self.combobox_p1_input.currentText() : self.textinput_scan_parameter_1_lambda.text()}))
        self.textinput_scan_parameter_2_lambda.textChanged.connect(lambda: self.system_components["SweeperLambdas"].update({self.combobox_p2_input.currentText() : self.textinput_scan_parameter_2_lambda.text()}))
        self.combobox_p1_input.currentIndexChanged.connect(lambda: self.textinput_scan_parameter_1_lambda.setText(self.system_components["SweeperLambdas"][self.combobox_p1_input.currentText()] if self.combobox_p1_input.currentText() in self.system_components["SweeperLambdas"] else ""))
        self.combobox_p2_input.currentIndexChanged.connect(lambda: self.textinput_scan_parameter_2_lambda.setText(self.system_components["SweeperLambdas"][self.combobox_p2_input.currentText()] if self.combobox_p2_input.currentText() in self.system_components["SweeperLambdas"] else ""))

    def set_fields_from_components(self):
        for cat, content in self.system_components_fields.items():
            for name, struct in content.items():
                if cat in self.system_components and name in self.system_components[cat]:
                    print(f"Setting {cat} {name} to {struct['typeof'](self.system_components[cat][name])}")
                    struct["set"]( struct["typeof"](self.system_components[cat][name]) )
    
    def set_components_from_fields(self):
        for cat,content in self.system_components_fields.items():
            for name, struct in content.items():
                self.system_components[cat][name] = struct["parse"]()

    def forceToolTip(self, where: QObject, error: str = "Error"):
        from PySide6.QtCore import QTimer
        original_tooltop = where.toolTip()
        where.setToolTip(error)
        QTimer.singleShot(100, lambda: QToolTip.showText(where.mapToGlobal(where.rect().center()), where.toolTip(), where, msecShowTime=10000))
        QTimer.singleShot(200, lambda: where.setToolTip(original_tooltop))

    def buildBaseEvaluationDict(self):
        eval_dict = {"np": np, 
                     "sp" : sp,
                     "g" : get_uv_scaled(self.textinput_rates_cavity_coupling.text()),
                     "G" : get_unit_value(self.textinput_rates_cavity_coupling.text()),
                     "k" : get_uv_scaled(self.textinput_rates_cavity_loss.text()),
                     "K" : get_unit_value(self.textinput_rates_cavity_loss.text()),
                     "y" : get_uv_scaled(self.textinput_rates_radiative_decay.text()),
                     "Y" : get_unit_value(self.textinput_rates_radiative_decay.text()),
                     "d" : get_uv_scaled(self.textinput_rates_pure_dephasing.text()),
                     "D" : get_unit_value(self.textinput_rates_pure_dephasing.text()),
                     "T" : float(self.textinput_phonons_temperature.text()) if self.textinput_phonons_temperature.text() != "No Phonons" else 0,
                     }
        return eval_dict

    # Sweeper.
    def generate_scan_or_sweep(self):
        # Generate scans
        x1,x2 = 0,0
        span1,span2 = (0,0), (0,0)
        self.scan_sweep_values = defaultdict(lambda: None)
        
        if self.checkbox_activate_scan_parameter_1.isChecked():
            span1 = (float(self.textinput_scan_parameter_1_from.text()), float(self.textinput_scan_parameter_1_to.text()))
            points = int(self.textinput_scan_parameter_1_points.text())
            x1 = np.linspace(span1[0], span1[1], points, endpoint=True)
        if self.checkbox_activate_scan_parameter_2.isChecked():
            span2 = (float(self.textinput_scan_parameter_2_from.text()), float(self.textinput_scan_parameter_2_to.text()))
            points = int(self.textinput_scan_parameter_2_points.text())
            x2 = np.linspace(span2[0], span2[1], points, endpoint=True)
        self.mgx,self.mgy = np.meshgrid(x1,x2)
        
        eval_dict = self.buildBaseEvaluationDict()
        eval_dict.update({"x1" : self.mgx, "x2" : self.mgy})
        #print(self.system_components["SweeperLambdas"])
        try:
            self.scan_sweep_values = {}
            for name, lambda_str in self.system_components["SweeperLambdas"].items():
                if len(lambda_str) > 0:
                    self.scan_sweep_values[name] = eval(lambda_str, eval_dict)
                    cname = name.split("(",1)[0]
                    eval_dict[cname] = self.scan_sweep_values[name]
            #name : eval(lambda_str, eval_dict) for name,lambda_str in self.system_components["SweeperLambdas"].items() if len(lambda_str) > 0}
        except Exception as e:
            self.text_output_program_qdacc_command_sweep_display.append(f"Error in Sweeper: {e}")
            return
        # Plot
        self.plot_sweep_parameter_first.canvas.axes.clear()
        self.plot_sweep_parameter_second.canvas.axes.clear()
        for cname,current in self.scan_sweep_values.items():
            if "P1" in cname:
                if "x2" in self.system_components["SweeperLambdas"][cname] or "P2" in self.system_components["SweeperLambdas"][cname]:
                    self.plot_sweep_parameter_first.canvas.axes.pcolormesh(x1, x2, current)
                else:
                    self.plot_sweep_parameter_first.canvas.axes.plot(x1, current[0])
            else:
                if "x1" in self.system_components["SweeperLambdas"][cname] or "P1" in self.system_components["SweeperLambdas"][cname]:
                    self.plot_sweep_parameter_second.canvas.axes.pcolormesh(x1, x2, current)
                else:
                    self.plot_sweep_parameter_second.canvas.axes.plot(x2, current[:,0])
        self.plot_sweep_parameter_first.canvas.draw()
        self.plot_sweep_parameter_second.canvas.draw()

        self.save_settings_file()



    ###########################################################################################################
    ################################################ Draw #####################################################
    ###########################################################################################################
    def drawSystem(self) -> None:
        self.sort_energy_levels()
        #if self.fixed_energy_h is None:
        self.fixed_energy_x,self.fixed_energy_y,self.fixed_energy_w, self.fixed_energy_h = self.label_output_system.geometry().getCoords()
        x0,y0,w,h = self.fixed_energy_x, self.fixed_energy_y, int(self.fixed_energy_w), int(self.fixed_energy_h) 
        self.output_system_canvas = QPixmap(w, h)
        qp = QPainter(self.output_system_canvas)
        qp.setRenderHint(QPainter.RenderHints.Antialiasing)
        #qp.setRenderHints(qp.Antialiasing)
        self.output_system_canvas.fill( QColor(self.colors["Background"]) )
        if len(self.system_components["EnergyLevels"].keys()) < 2:
            qp.end()
            self.label_output_system.setPixmap(self.output_system_canvas)
            self.update()
            return 
        
        state_color = QColor(self.colors["State"])
        statename_color = QColor(self.colors["StateName"])
        transition_color = QColor(self.colors["Transition"])
        reset_color = QColor(self.colors["Neutral"])

        def draw_rect(_x,_y,_w,_h, name = None, offset_name = (0,0), font_size = 0.8, color = state_color):
            if isinstance(color, str):
                color = QColor(color)
            pen = QPen(reset_color)
            pen.setWidth(1)
            qp.setPen(pen)   
            qp.setBrush(color)
            #qp.drawRect(int(_x),int(_y),int(_w), int(_h))
            path = QPainterPath()
            path.addRoundedRect(int(_x),int(_y),int(_w), int(_h), int(0.4*_h), int(0.4*_w))
            qp.fillPath(path, state_color)
            qp.drawPath(path)
            if name is not None:
                pen = QPen(statename_color)
                pen.setWidth(2)
                qp.setPen(pen)   
                font = QFont()
                font.setFamily('Times')
                font.setBold(True)
                font.setPointSize(int(font_size*_h))
                qp.setFont(font)
                qp.drawText(int(_x - 12 + offset_name[0]), int(_y+0.9*_h + offset_name[1]), name)

        def draw_line(x1,y1,x2,y2, _w = 8, _color = transition_color, _style = Qt.PenStyle.DotLine):
            pen = QPen(_color)
            pen.setWidth(_w)
            pen.setStyle(_style)
            qp.setPen(pen)   
            qp.drawLine(int(x1),int(y1),int(x2),int(y2))

        def draw_arc(x1,y1,_w,_h,startangle,arcangle, _pw = 2, _color = transition_color):
            pen = QPen(_color)
            pen.setWidth(int(_pw))
            #pen.setStyle(Qt.PenStyle.DotLine)
            pen.setCapStyle(Qt.PenCapStyle.SquareCap)
            qp.setPen(pen)
            qp.drawArc(int(x1),int(y1),int(_w),int(_h),int(startangle),int(arcangle))

        def draw_exp(x1,y1,_w,_h,_lw = 3,_color = transition_color):
            x = np.linspace(-1,1,300)
            xfunc = _w*x
            func = _h*np.exp(-8*x*x)*np.sin(10*np.pi*x)
            for x1,x2,y1,y2 in zip(x1+xfunc,x1+xfunc[1:],y1-func,y1-func[1:]):
                draw_line(int(x1), int(y1), int(x2),int(y2), _w = _lw, _style = Qt.PenStyle.SolidLine, _color = _color)
            

        # Draw Energy Levels from bottom to top
        lowest_energy = 0 if len(self.system_components["EnergyLevels"].keys()) < 1 else min(get_uv_scaled(a["Energy"]) for a in self.system_components["EnergyLevels"].values())
        energy_normalization = max([get_uv_scaled(a["Energy"]) for a in self.system_components["EnergyLevels"].values()]) - lowest_energy
        lowest_level = 0.8*h
        highest_level = 0.2*h
        level_height = (lowest_level - highest_level) * 0.05
        level_width_factor = 0.3
        artificial_grouping_offset = self.slider_state_separator.value()/10 # Group members get seperated by this much times the level height at least
        for group_of_levels in self.system_energy_level_groups:
            level_width = max(2,w*level_width_factor if len(group_of_levels) < 2 else 0.6*w/(len(group_of_levels)))
            last_y = lowest_energy
            for l,level in enumerate(group_of_levels,1):
                # X,Y
                y_seperation = 0 
                if abs(last_y - get_uv_scaled(level["Energy"])) / energy_normalization < artificial_grouping_offset * level_height: 
                    y_seperation = level_height*artificial_grouping_offset*(l-1)
                level_y = lowest_level - (lowest_level - highest_level)*(get_uv_scaled(level["Energy"])-lowest_energy) / energy_normalization - y_seperation
                level_x = w/(len(group_of_levels)+1)*l - level_width/2.# center of individual level - delta/2
                last_y = get_uv_scaled(level["Energy"])
                if self.plot_system_details:
                    name = f"{level['Name']} - E = {level['Energy']}, |{level['DecayScaling']}|{level['DephasingScaling']}|{level['PhononScaling']}|"
                else:
                    name = f"{level['Name']}"
                # Determine Color
                color_to_draw = state_color
                for t,transto in enumerate(level["CoupledTo"]):
                    if transto not in self.system_components["EnergyLevels"]:
                        color_to_draw = self.colors["Red"]
                draw_rect(level_x,level_y,level_width,level_height,name,(0.05*level_width,0) if self.plot_system_details else (0.5*level_width,0), color=color_to_draw)
                # Save Coordinates for easier drawing
                level["Coords"] = (level_x, level_y, level_width, level_height) #x,y,w,h
        # Draw Transitions
        for level in self.system_components["EnergyLevels"].values():
            for t,transto in enumerate(level["CoupledTo"]):
                if transto is None or len(transto) == 0 or transto not in self.system_components["EnergyLevels"]:
                    continue

                level2 = self.system_components["EnergyLevels"][transto]
                if len(level2) == 0:
                    continue
                x1 = level["Coords"][0] + level["Coords"][2]/2.
                y1 = level["Coords"][1] + level["Coords"][3]/2 - level_height
                x2 = level2["Coords"][0] + level2["Coords"][2]/2.
                y2 = level2["Coords"][1] + level2["Coords"][3]/2 + level_height
                draw_line(x1, y1, x2, y2)

        # Draw Cavities
        self.system_cavity_level_groups = [a for a in self.system_components["CavityLevels"].values()]
        for c,cavity in enumerate(self.system_cavity_level_groups):
            cavity_x1 = 0.1*w
            cavity_width = 0.03*w
            cavity_x_delta = 0.04*w
            cavity_strokewidth = 0.011*w
            cavity_x2 = 0.9*w - cavity_width
            cavity_color = QColor(self.colors["Cavity"][c%len(self.colors["Cavity"])])
            # Special Case where cavity is alone:
            if len(cavity["CoupledTo"]) == 0 or None in cavity["CoupledTo"]:
                cavity_y1 = lowest_level
                cavity_height = -get_uv_scaled(cavity["Energy"])/energy_normalization*(lowest_level-highest_level)#-abs(e1[1]-e0[1])
                detuning = 0
                cavity_color.setAlpha(255-int(min(200,10.*detuning/get_uv_scaled(cavity['Energy']))))
                draw_arc(cavity_x1 - c*cavity_x_delta, cavity_y1, cavity_width, cavity_height,90*16,16*180,cavity_strokewidth,cavity_color)
                draw_arc(cavity_x2 + c*cavity_x_delta, cavity_y1, cavity_width, cavity_height,270*16,16*180,cavity_strokewidth,cavity_color)
            else:
                for transition in cavity["CoupledTo"]:
                    if transition in self.system_components["CavityLevels"]:
                        continue
                    t0,t1 = transition.split("=")
                    if t0 not in self.system_components["EnergyLevels"] or t1 not in self.system_components["EnergyLevels"]:
                        if t0 not in self.system_components["CavityLevels"] or t1 not in self.system_components["CavityLevels"]:
                            continue
                    e0,e1 = self.system_components["EnergyLevels"][t0]["Coords"], self.system_components["EnergyLevels"][t1]["Coords"]
                    cavity_y1 = e0[1] + level_height/2
                    cavity_height = -get_uv_scaled(cavity["Energy"])/energy_normalization*(lowest_level-highest_level)#-abs(e1[1]-e0[1])
                    detuning = abs(abs(e0[1]-e1[1]) - abs(cavity_height))
                    cavity_color.setAlpha(255-int(min(200,10.*detuning/get_uv_scaled(cavity['Energy']))))
                    draw_arc(cavity_x1 - c*cavity_x_delta, cavity_y1, cavity_width, cavity_height,90*16,16*180,cavity_strokewidth,cavity_color)
                    draw_arc(cavity_x2 + c*cavity_x_delta, cavity_y1, cavity_width, cavity_height,270*16,16*180,cavity_strokewidth,cavity_color)
                    #draw_line(cavity_x1 - c*cavity_x_delta, cavity_y1, cavity_x1 - c*cavity_x_delta, cavity_y1 + cavity_height, _color = cavity_color, _style = Qt.PenStyle.SolidLine)
                    #draw_line(cavity_x1 - c*cavity_x_delta - cavity_width/4, cavity_y1, cavity_x1 - c*cavity_x_delta + cavity_width/4, cavity_y1, _color = cavity_color, _style = Qt.PenStyle.SolidLine)
                    #draw_line(cavity_x1 - c*cavity_x_delta - cavity_width/4, cavity_y1+cavity_height, cavity_x1 - c*cavity_x_delta + cavity_width/4, cavity_y1+cavity_height, _color = cavity_color, _style = Qt.PenStyle.SolidLine)
                    #draw_line(cavity_x2 + c*cavity_x_delta, cavity_y1, cavity_x2 + c*cavity_x_delta, cavity_y1 + cavity_height, _color = cavity_color, _style = Qt.PenStyle.SolidLine)
                    #draw_line(cavity_x2 + c*cavity_x_delta - cavity_width/4, cavity_y1, cavity_x2 + c*cavity_x_delta + cavity_width/4, cavity_y1, _color = cavity_color, _style = Qt.PenStyle.SolidLine)
                    #draw_line(cavity_x2 + c*cavity_x_delta - cavity_width/4, cavity_y1+cavity_height, cavity_x2 + c*cavity_x_delta + cavity_width/4, cavity_y1+cavity_height, _color = cavity_color, _style = Qt.PenStyle.SolidLine)
        
        # Draw Indicator for Pulses
        for i,el in enumerate(list(self.system_components["Pulse"].values())): #+ list(self.system_components["Shift"].values())):
            text = "Pulse: " if el["Name"] in self.system_components["Pulse"] else "Shift: "
            lowest_level = 0.9*h
            highest_level = 0.2*h
            level_height = 0.05
            level_width = 0.1
            #xpos = 0.01 * w
            xpos = 0.01 * w + i*(lowest_level-highest_level)*0.9*level_width*2
            #ypos = lowest_level - i*(lowest_level-highest_level)*0.9*level_height
            ypos = lowest_level
            width = level_width*w
            height = level_height*h
            name = el["Name"]
            transitions = [t.split("=") if "=" in t else t for t in el["CoupledTo"]]
            for transition in transitions:
                if isinstance(transition, list) and len(transition) > 1 and transition[0] in self.system_components["EnergyLevels"] and transition[1] in self.system_components["EnergyLevels"]: # electronic transition
                    e0 = self.system_components["EnergyLevels"][transition[0]]["Coords"]
                    e1 = self.system_components["EnergyLevels"][transition[1]]["Coords"]
                    x1 = e0[0] + e0[2]/2.
                    y1 = e0[1] + e0[3]/2
                    x2 = e1[0] + e1[2]/2.
                    y2 = e1[1] + e1[3]/2
                    x = (x1+x2)/2
                    y = (y1+y2)/2
                    draw_exp(x,y, 100, 50)
        qp.end()

        self.label_output_system.setPixmap(self.output_system_canvas)
        self.update()

    def generateCommandString(self, escape_symbol = "'"):
        escaped = self.input_escape_output_command.isChecked()
        # Generate Commands
        commands = [component_parser(component,escaped,self.system_components,escape_symbol=escape_symbol,callback=self.sendHintMessage) for component in self.system_components.keys()]

        final_command = f"[QDaCC] {' '.join(commands)} [FILEPATH]"
        while "  " in final_command:
            final_command = final_command.replace("  "," ")
        return final_command
        #self.output_start_command.setText(final_command)

    def commandToCLAList(self, commands = None, escape_symbol = "'") -> str:
        if commands is None:
            commands = self.generateCommandString(escape_symbol=escape_symbol)
        commands = commands.split()
        _, qdacc_executable, _ = self.getQDaCCPaths()
        filepath = f"{escape_symbol}{self.textinput_file_destination.text() or self.filepath}{escape_symbol}"
        settingfilepath = f"{escape_symbol}{self.textinput_path_to_settingfile.text() or self.filepath}{escape_symbol}"
        for el,rep in zip(["[QDaCC]", "[FILEPATH]", "[SETTINGFILE]"],[qdacc_executable, filepath, settingfilepath]):
            if el not in commands:
                continue
            index = commands.index(el)
            commands[index] = rep
        return commands

    def resizeEvent(self, event):
        self.drawSystem()
        QMainWindow.resizeEvent(self, event)

    # Plot Task
    # Mode can be "all", "bloch", "dm". The latter two will ask for additional parameters
    def plot_everything(self, force_folder: bool = False):
        path_to_destination, qdacc_executable, qdacc_path_str = self.getQDaCCPaths()
        is_folder = "--file" in self.text_output_program_qdacc_command.toPlainText() or force_folder # self.checkbox_activate_scan_parameter_1.isChecked() or self.checkbox_activate_scan_parameter_2.isChecked()
        plot_command = ["python3", "-m", "QDLC.eval_tools.get_files", "all", path_to_destination,"-folder" if is_folder else "", "--type=pdf,png(50)"]
        mode = self.input_plot_mode.currentText()
        # Check for additional inputs for bloch and dm
        if mode == "Animated Blochsphere":
            if not "Bloch" in self.system_components:
                self.system_components["Bloch"] = {"Re" : "", "Im" : "", "f" : "", "File" : "densitymatrix.txt", "Bitrate" : "5000", "Skip" : "0", "2f" : False, "FPS" : "60", "LW" : "1", "flags" : ""}
            items, ok = getGeneralItems([{"Title": "Re(p)", "Type": QLineEdit, "Text": self.system_components["Bloch"]["Re"]}, 
                                            {"Title": "Im(p)", "Type": QLineEdit, "Text": self.system_components["Bloch"]["Im"]}, 
                                            {"Title": "Population", "Type": QLineEdit, "Text": self.system_components["Bloch"]["f"]}, 
                                            {"Title": "File", "Type": QLineEdit, "Text": self.system_components["Bloch"]["File"]}, 
                                            {"Title": "Bitrate", "Type": QLineEdit, "Text": self.system_components["Bloch"]["Bitrate"]}, 
                                            {"Title": "FPS", "Type": QLineEdit, "Text": self.system_components["Bloch"]["FPS"] if "FPS" in self.system_components["Bloch"] else "60"}, 
                                            {"Title": "Line Width", "Type": QLineEdit, "Text": self.system_components["Bloch"]["LW"] if "LW" in self.system_components["Bloch"] else "1"}, 
                                            {"Title": "Skip Iterations", "Type": QLineEdit, "Text": self.system_components["Bloch"]["Skip"]}, 
                                            {"Title": "Additional Flags", "Text": self.system_components["Bloch"]["flags"] if "flags" in self.system_components["Bloch"] else "", "Type": QLineEdit},
                                            {"Text": "Normalize Data", "Checked": False, "Type": QCheckBox},
                                            ], self)
            if ok:
                re,im,f,ffile,bitrate,fps,lw,skip,flags,norm = items
                self.system_components["Bloch"] = {"Re" : re, "Im" : im, "f" : f, "File" : ffile, "Bitrate" : bitrate, "Skip" : skip, "FPS" : fps, "LW" : lw, "Norm": norm, "flags": flags}
                plot_command = ["python3", "-m", "QDLC.plot_tools.plot_blochsphere_animated", "-no2f", "--file="+os.path.join(path_to_destination,ffile), "--bitrate="+bitrate, "--skip="+skip, "--fps="+fps, "--lw="+lw, "-norm" if norm else ""] + [f"--indices={re},{im},{f}".replace('|','^|').replace('>','^>').replace('<','^<') for re,im,f in zip(re.split(";"),im.split(";"),f.split(";"))] + flags.split(";")  
                print(f"Plotting Blochsphere with {plot_command}")
            else:
                return
        elif mode == "Animated Density Matrix":
            if not "AnimDM" in self.system_components:
                self.system_components["AnimDM"] = {"File" : "densitymatrix.txt", "Bitrate" : "5000", "Skip" : "0", "Indices" : ""}
            items, ok = getGeneralItems([{"Title": "File", "Type": QLineEdit, "Text": self.system_components["AnimDM"]["File"]},
                                            {"Title": "Bitrate", "Type": QLineEdit, "Text": self.system_components["AnimDM"]["Bitrate"]}, 
                                            {"Title": "Skip Iterations", "Type": QLineEdit, "Text": self.system_components["AnimDM"]["Skip"]}, 
                                            {"Title": "Indices", "Type": QLineEdit, "Text": self.system_components["AnimDM"]["Indices"]}, 
                                            ], self)
            if ok:
                ffile,bitrate,skip,indices = items
                self.system_components["AnimDM"] = {"File" : ffile, "Bitrate" : bitrate, "Skip" : skip, "Indices" : indices}
                plot_command = ["python3", "-m", "QDLC.plot_tools.plot_dm_animated", "--file="+os.path.join(path_to_destination,ffile), "--bitrate="+bitrate, "--skip="+skip, "--indices="+indices]
                print(f"Plotting Density Matrix with {plot_command}")
            else:
                return
        
        cwd = qdacc_path_str.replace(qdacc_executable, "")
        self.plot_thread = QDaCCMainWoker(parent=self, cwd=cwd, command=plot_command)
        self.plot_thread.pipeUpdatesTo(lambda text: self.updateTextBrowser(self.text_output_program_main, text), lambda text: self.updateProgressBar(self.progressBar,text)) 
        self.plot_thread.connectStarted(lambda: self.enableRunningButtonAnimation(self.button_plot_everything, [self.button_run_program]))
        self.plot_thread.connectFinished(lambda: self.disableRunningButtonAnimation(self.button_plot_everything, "Plot", [self.button_run_program]))
        if "QDLC.eval_tools.get_files" in plot_command:
            def insert_plots():
                folders = [path_to_destination] if not is_folder else [os.path.join(path_to_destination, f, "img") for f in os.listdir(path_to_destination) if os.path.isdir(os.path.join(path_to_destination, f))]
                print(f"Plotting everything in {folders}")
                for folder in folders:
                    for file in os.listdir(folder):
                        complete_path = os.path.join(folder, file)
                        if file.endswith(".png"):
                            self.plot_thread.progress.emit(f"Plotting {complete_path}\n")
                            print(f'<br><img  src="{complete_path}?' + str(time()) +'"></br>')
                            self.plot_thread.progress.emit(f'<br><img  src="file:///{complete_path}?' + str(time()) +'"></br>')
                            self.plot_thread.progress.emit(f'<br><a href="file:///{complete_path.replace(".png",".pdf")}">Open this file<\a></br>')
            self.plot_thread.connectFinished(insert_plots)
        self.plot_thread.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())