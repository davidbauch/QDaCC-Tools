import sys, os
from PySide6.QtWidgets import QWidget,QMainWindow, QApplication,QLabel,QGraphicsScene, QLineEdit,QTextEdit, QGridLayout, QTextBrowser, QTabWidget, QBoxLayout, QPushButton, QDialog, QFormLayout, QMessageBox, QFileDialog, QInputDialog, QToolTip, QMenu, QCheckBox, QProgressBar
from PySide6.QtGui import QIcon, QAction, QPainter, QColor, QPixmap,QFont, QPen, QPainterPath, QStandardItemModel, QStandardItem, QGuiApplication, QDesktopServices, QTextCursor, QMovie
from PySide6.QtCore import Qt,QRect,QPropertyAnimation,QThread,Signal,QObject, QUrl, QTimer, QSize

import sys, os
#from hoverbutton import HoverButton
from gui.ui_main_window import Ui_MainWindow
from gui.unit_seperator import get_unit, get_unit_scaling, get_unit_value, get_uv_scaled, seperate_unit
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
from gui.helperfunctions import changeIconColor,changePixmapColor,changePixmapGradient

import psutil

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.retranslateUi(self)
        self.filepath = os.path.dirname(os.path.realpath(__file__))

        self.design_colors = {
            "active_primary_color" : "#0674e8",
            "active_secondary_color" : "#50b79c",
            "primary_color" : "#181e36",
            "secondary_color" : "#2e3349",
            "background_color" : "#252a40",
            "text_color" : "#d2d4e1",
            "gradient_color" : ("#97f9fc", "#5eafe7","#3b86e5","#3779d8")
        }

        # Set Stylesheet from file
        with open(os.path.join(self.filepath,"style.qss"),"r") as f:
            data = f.read()
            for key,val in self.design_colors.items():
                if isinstance(val, str):
                    data = data.replace(key,val)
            self.setStyleSheet(data)
            
        # Config
        self.render_colors = {
        "State" : self.design_colors["active_primary_color"],#"#88282A3A",
        "StateName" : self.design_colors["text_color"],
        "Transition" : self.design_colors["active_secondary_color"],
        "Cavity" : self.design_colors["gradient_color"],
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
            "tab_system" : os.path.join(self.filepath,"gui/resources/tab_icons/system.png"),
            "tab_datasets" : os.path.join(self.filepath,"gui/resources/tab_icons/datasets.png"),
            "tab_time" : os.path.join(self.filepath,"gui/resources/tab_icons/time.png"),
            "tab_statistics" : os.path.join(self.filepath,"gui/resources/tab_icons/statistics.png"),
            "tab_run" : os.path.join(self.filepath,"gui/resources/tab_icons/run.png"),
            "tab_output" : os.path.join(self.filepath,"gui/resources/tab_icons/output.png"),
            "tab_optimizer" : os.path.join(self.filepath,"gui/resources/tab_icons/optimizer.png"),
            "tab_howto" : os.path.join(self.filepath,"gui/resources/tab_icons/howto.png"),
            "tab_environment" : os.path.join(self.filepath,"gui/resources/tab_icons/environment.png"),
            "main" : os.path.join(self.filepath,"gui/resources/main.png"),
            "header" : os.path.join(self.filepath,"gui/resources/header.png"),
        }
        self.main_window_tab_sizes = QSize(50,150)

        self.loading_animation = QMovie(self.resources["loading"])
        self.thread_timer = defaultdict(self.generateQAnimationTimer)
        self.loading_animation_fps = 1000/360
        self.button_run_program.setIconSize(QSize(120,28))
        self.button_plot_everything.setIconSize(QSize(120,28))
        self.button_sweeper_plot.setIconSize(QSize(120,28))
        self.button_optimizer_optimize.setIconSize(QSize(120,28))

        # Test Logo
        logo = changePixmapGradient(QPixmap(self.resources["main"]), self.design_colors["gradient_color"],45)
        self.main_logo.setPixmap(logo.scaled(200,200,Qt.KeepAspectRatio,Qt.SmoothTransformation))
        self.main_logo.setMinimumSize(200,200)
        self.main_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header = changePixmapGradient(QPixmap(self.resources["header"]), self.design_colors["gradient_color"],0)
        aspect_ratio = header.width()/header.height()
        self.main_descriptor.setPixmap(header.scaled(200*aspect_ratio,200,Qt.KeepAspectRatio,Qt.SmoothTransformation))

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

        # Set Tabs
        self.generateTabIcons()

        self.show()
        self.connect_config_to_fields()
        self.set_components_from_fields()
        
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.update_component_list()
        self.drawSystem()

        # CPU Timer
        self.cpu_timer = QTimer()
        self.cpu_timer.timeout.connect(self.updateUseStatistics)
        self.cpu_timer.start(1000)

        # Set progressbar colors
        for progressbar in (self.progressBar, self.progressBarCPU, self.progressBarRAM):
            progressbar.color = self.design_colors["active_primary_color"]
            progressbar.color_bar = self.design_colors["active_secondary_color"]

        # Clear Plots. TODO: plotting via member functions!
        for plot in (self.label_plot_time_prediction, self.label_plot_spectral_density, self.label_plot_spectral_prediction, self.label_plot_optimizer_1, self.label_plot_optimizer_2, self.label_plot_optimizer_3, self.plot_sweep_parameter_first, self.plot_sweep_parameter_second):
            plot.resetPlot(self)

        # If first argument was passed, load it
        if len(sys.argv) > 1:
            self.load_from_qdacc_file(sys.argv[1])


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
        self.update_component_list()
        self.drawSystem()
        self.is_currently_unsaved = False
        self.refreshWindowTitle()

    def generateTabIcons(self):
        """
        Adds icons to tabs, removes tab text and sets tab size.
        """
        for i,icon in enumerate( ("tab_system", "tab_environment", "tab_time", "tab_statistics", "tab_output", "tab_run", "tab_datasets", "tab_optimizer", "tab_howto") ):
            icon = changeIconColor(QIcon(self.resources[icon]), self.design_colors["active_primary_color"], self.main_window_tab_sizes)
            self.main_tab_widget.setTabIcon(i,icon)
            self.main_tab_widget.setTabText(i,"")
        self.main_tab_widget.setIconSize(self.main_window_tab_sizes)

    def delete_input(self):
        """
        Deletes the currently selected system component from the components list
        This function also calls drawSystem and update_component_list to ensure
        the gui is updated correctly.
        """
        current = self.list_components.currentIndex().data()
        if current is None or current == "None":
            return
        name, category = current.split(" - ")
        self.system_components[category].pop(name)
        print(f"Dropped {name} from {category}")
        self.drawSystem()
        self.update_component_list()

    def edit_input(self):
        """
        Opens the currently selected system component from the components list
        If no component is selected, nothing happens.
        The component is opened in a new window and loaded into the dialog.
        """
        current = self.list_components.currentIndex().data()
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

    def openToleranceDialog(self):
        """
        Opens the Grid/Tolerance Dialog to input RK45 Tolerances.
        This function should also do some checks to ensure the tolerances are
        valid later. The dialog could maybe already check that.
        """
        DialogAddGridOrTolerance(main_window=self,name="Tolerances", style_sheet=self.styleSheet())

    def openGridDialog(self):
        """
        Opens the Grid/Tolerance Dialog to input a correlation Grid.
        """
        DialogAddGridOrTolerance(main_window=self,name="Grid", style_sheet=self.styleSheet())

    def openReadmeFile(self) -> str:
        try:
            html = markdown.markdown(open(os.path.join(self.filepath,"../README.md")).read(),extensions=['markdown.extensions.fenced_code']) #.replace('<img src="','<img src="../')
        except FileNotFoundError as e:
            html = ""
        rep = os.path.join(self.filepath,"../")
        html = html.replace('<img src="',f'<img style="max-width:100%" src="{rep}')
        html = html.replace(".svg",".png")
        html = html.replace('px"','"')
        return html

    def openDestinationFolder(self):
        """
        Opens the destination folder using the QDesktopServices module.
        """
        QDesktopServices.openUrl(QUrl.fromLocalFile(self.textinput_file_destination.text()))

    def empty_target_folder(self, to_delete = (".txt", ".png", ".log", ".pdf"), subfolders = True):
        """
        Empties the target destination folder.
        This function asks for permission before deleting the files.

        Parameters:
            to_delete: A tuple of file endings that should be deleted.
            subfolders: If True, also delete files in subfolders.
        """
        dest = self.textinput_file_destination.text()
        # Get Files to delete
        files = [f for f in os.listdir(dest) if any([f.endswith(ending) for ending in to_delete])]
        if subfolders:
            folders = [f for f in os.listdir(dest) if os.path.isdir(os.path.join(dest,f))]
            for folder in folders:
                files += [os.path.join(folder,f) for f in os.listdir(os.path.join(dest,folder)) if any([f.endswith(ending) for ending in to_delete])]
        # Ask for permission
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

    def export_command(self, name = None):
        """
        Exports the current settings to a QDaCC Command file.
        
        Parameters:
            name: The name of the file to save to. If None, a file dialog is opened.
        """
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

    def import_command(self, key: str | None = None):
        """
        Imports a .qdacc command file and loads it into the system.

        Parameters:
            key: If not None, only the component with the given key is loaded.
                 This enables filetring of the component dict.
                 Note: this parameter will be passed to load_from_qdacc_file.
        """
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setAcceptMode(QFileDialog.AcceptOpen)
        dlg.setNameFilters(["*.qdacc", "*.log"])
        if dlg.exec():
            filenames = dlg.selectedFiles()
            self.load_from_qdacc_file(filepath = filenames[0], key=key )
            self.drawSystem()
            self.update_component_list()

    def export_save_existing(self):
        """
        Exports the current settings to a .qdacc Command file.
        This function uses the current_qdacc_file_path variable to determine
        the file to save to. This variable is set by the save_to_qdacc_file 
        method.
        """
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
            self.export_command(name = filename)

    def set_file_path(self):
        """
        Opens a file dialog to select a file destination folder.
        """
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)
        if dlg.exec():
            filename = dlg.selectedFiles()[0]
            if not filename.endswith("/"):
                filename += "/"
            self.textinput_file_destination.setText(filename)

    def set_qdacc_filepath(self):
        """
        Opens a file dialog to select a QDaCC executable.
        """
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setAcceptMode(QFileDialog.AcceptOpen)
        dlg.setNameFilters(["*.exe", "*.out", "*.*"])
        if dlg.exec():
            filenames = dlg.selectedFiles()
            self.textinput_file_qdacc.setText(filenames[0])

    def set_settingfile_path(self):
        """
        Opens a file dialog to select a target settingfile.
        """
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setAcceptMode(QFileDialog.AcceptSave)
        dlg.setNameFilters(["*.txt", "*.*"])
        if dlg.exec():
            filename = dlg.selectedFiles()[0]
            self.textinput_path_to_settingfile.setText(filename)

    def save_to_setting_file(self, filepath: str, project_name: str) -> None:
        """
        This function saves the current QDaCC settings into a settings.txt
        file. This file can then be used to run the QDaCC executable.

        This method checks whether a single parameter scan or a dual parameter
        scan is used and generates the correct settingfile using the 
        QDaCCSettingGenerator class.
        
        Parameters:
            filepath: The path to the file to save to.
            project_name: The name of the project. This is used to identify
                          the project in the QDaCC executable.
        """
        one: bool = self.checkbox_activate_scan_parameter_1.isChecked()
        dual: bool = self.checkbox_activate_scan_parameter_2.isChecked()
        runstring: str = self.text_output_program_qdacc_command_sweep.toPlainText()
        
        qdacc_path_str: str = self.textinput_file_qdacc.text()
        qdacc_path: str = qdacc_path_str.split("/")
        qdacc_executable: str = qdacc_path[-1]
        cwd: str = qdacc_path_str.replace(qdacc_executable, "")
        
        # Create the QDaCCSettingGenerator thread
        self.settings_thread = QDaCCSettingGenerator(parent=self, mgx = self.mgx, mgy = self.mgy, values = self.scan_sweep_values, file = filepath, name = project_name, converter = self.commandToCLAList, runstring = runstring, one = one, two = dual)

        # Connect the thread to the GUI
        self.settings_thread.pipeUpdatesTo(lambda text: self.updateTextBrowser(self.text_output_program_main, text), lambda text: self.updateProgressBar(text)) 
        self.settings_thread.pipeUpdatesTo(lambda text: self.updateTextBrowser(self.text_output_program_qdacc_command_sweep_display, text), None) 
        self.settings_thread.connectStarted(lambda: self.enableRunningButtonAnimation(self.button_sweeper_plot, [self.button_run_program, self.button_plot_everything]))
        self.settings_thread.connectFinished(lambda: self.disableRunningButtonAnimation(self.button_sweeper_plot, "Generate Settingfile", [self.button_run_program, self.button_plot_everything]))
        self.settings_thread.connectStarted(lambda: self.button_run_and_plot.setEnabled(False))
        self.settings_thread.connectFinished(lambda: self.button_run_and_plot.setEnabled(True))

        # Finally, start the thread
        self.settings_thread.start()

    def save_settings_file(self):
        """
        This function saves the current QDaCC settings into a settings.txt
        file using the save_to_setting_file method. This method extracts the
        most probable project name from the settings file path, aks the user to
        change it on demand and then calls the save_to_setting_file method.
        """
        filepath = self.textinput_path_to_settingfile.text()
        if filepath == "":
            return
        project_name, ok = QInputDialog.getText(self, "Save Settings", "Project Name", QLineEdit.Normal, filepath.split("/")[-1].replace(".txt", "").replace("settings_",""))
        self.text_output_program_main.append(f"Saving Settingfile to {filepath}")
        if not ok or not len(project_name):
            self.sendErrorMessage("No Name given")
            return
        self.save_to_setting_file(filepath, project_name)

    def toggle_runstring_full_settingfile(self):
        """
        This function is used to toggle between evaluating a single parameter 
        set and evaluating a setting file. This is done by changing the
        runstring of the QDaCC executable. This way of changing the evaluation
        method is probably subject to change in the future.

        Note, that at this time, the function does NOT cache the current command
        string, but instead re-generates it every time. This is not optimal, because
        local changes done to the string by the user are disgarded.
        """
        current_text = self.text_output_program_qdacc_command.toPlainText()
        if "--file" in current_text:
            self.generate_command()
        else:   
            runstr = f"[QDaCC] --file [SETTINGFILE] [FILEPATH]"
            self.text_output_program_qdacc_command.setPlainText(runstr)

    def pick_from_list_of_available_states(self):
        """
        Generates a list of available states and opens a dialog to pick one.
        The picked state is then set as the initial state.
        """
        items = self.generate_list_of_available_total_states()
        print(f"Picking initial state from '{items}'")
        item, ok = QInputDialog.getItem(self, "Select Input State", "Valid States", items, 0, False)
        if ok and item:
            print(f" -> Setting initial state to '{item}'")
            self.textinput_initial_state.setText(item)

    def toggle_phonon_inputs(self):
        """
        Toggles the phonon inputs on the GUI.
        When the checkbox is checked, the corresponding inputs are enabled or
        disabled, respectively.
        """
        enable = self.input_phonons_use_qd.isChecked()
        for a in [self.textinput_phonons_sd_qd_de,self.textinput_phonons_sd_qd_dh,self.textinput_phonons_sd_qd_rho,self.textinput_phonons_sd_qd_cs,self.textinput_phonons_sd_qd_aeah_ratio,self.textinput_phonons_sd_qd_size]:
            a.setEnabled(enable)
        self.textinput_phonons_sd_alpha.setEnabled(not enable)

    def spectrum_add(self):
        """
        Adds a spectrum to the system components.
        This function is subject to change in the future, as the spectrum
        adding mechanism is quite bad right now.

        This function calls the update_component_list method to update the
        components list.
        """
        spec_modes = self.textinput_spectrum_modes.text().split(",")
        spec_range = self.textinput_spectrum_range.text()
        spec_center = self.textinput_spectrum_center.text()
        spec_res = self.textinput_spectrum_res.text()
        spec_order = self.input_spectrum_order.currentIndex()
        spec_norm = self.input_spectrum_normalize.isChecked()
        name = f"{''.join(spec_modes)}{spec_range}{spec_center}{spec_res}{spec_order}{spec_norm}"
        self.add_component( "Spectrum", {"Name" : name, "Modes" : spec_modes, "Range" : spec_range, "Center" : spec_center, "Res" : spec_res, "Order" : spec_order, "Norm": spec_norm} )
        self.update_component_list()

    def spectrum_remove(self):
        """
        Removes the currently selected spectrum.

        This function calls the update_component_list method to update the
        components list.
        """
        index = self.text_output_list_of_spectra.currentIndex().row()
        name = self.text_output_list_of_spectra.model().item(index).toolTip()
        self.system_components["Spectrum"].pop(name)
        self.update_component_list()
        
    def spectrum_active_change(self):
        """
        When changing the spectrum active state, this function is called.
        It sets the spectrum inputs fields to the values of the selected
        spectrum.
        """
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

    def spectrum_predict_plot(self):
        """
        Plots the predicted spectra using the current system components.
        For all cavities and transitions, a Lorentzian peak is plotted at the
        correct energy and linewidth. Rabi Splitting is taken into account for
        the cavity peaks. The predicted spectra are plotted in blue and red
        """
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

    def spectrumAddModeToModes(self, retain_modes: bool = False) -> None:
        """
        This method calls the getListOfTransitions method and adds the returned
        string to the spectrum modes input field. If retain_modes is True, the
        current modes are retained.
        """
        transitions: str = self.getListOfTransitions()
        if retain_modes:
            transitions = self.textinput_spectrum_modes.text() + "," + transitions
        self.textinput_spectrum_modes.setText(transitions)

    def indist_add(self):
        """
        Adds an indistinguishability mode to the system components.
        This function is subject to change in the future, as the indist
        adding mechanism is quite bad right now.

        This function calls the update_component_list method to update the
        components list.
        """
        indist_modes = self.textinput_indist_modes.text().split(",")
        if not len(indist_modes):
            return
        for mode in indist_modes:
            if not len(mode):
                continue
            self.add_component( "Indistinguishability", {"Name" : mode, "Mode" : mode} )
        self.update_component_list()

    def indist_remove(self):
        """
        Removes the currently selected indistinguishability mode.

        This function calls the update_component_list method to update the
        components list.
        """
        index = self.text_output_list_of_indists.currentIndex().row()
        name = self.text_output_list_of_indists.model().item(index).toolTip()
        if name is None or not len(name):
            return
        if name not in self.system_components["Indistinguishability"]:
            return
        self.system_components["Indistinguishability"].pop(name)
        self.update_component_list()

    def indist_active_change(self):
        """
        When changing the indistinguishability active state, this function is called.
        It sets the indistinguishability inputs fields to the values of the selected
        indistinguishability.
        """
        try:
            index = self.text_output_list_of_indists.currentIndex().row()
            name = self.text_output_list_of_indists.model().item(index).toolTip()
        except:
            return
        struct = self.system_components["Indistinguishability"][name]
        self.textinput_indist_modes.setText(struct["Mode"])

    def indistAddModeToModes(self, retain_modes: bool = False) -> None:
        """
        This method calls the getListOfTransitions method and adds the returned
        string to the indistinguishability modes input field. If retain_modes is True, the
        current modes are retained.
        """
        transitions: str = self.getListOfTransitions()
        if retain_modes:
            transitions = self.textinput_indist_modes.text() + "," + transitions
        self.textinput_indist_modes.setText(transitions)

    def concurrence_add(self):
        """
        This method adds a concurrence mode to the system components.
        This function is subject to change in the future, as the concurrence
        adding mechanism is quite bad right now.

        This function calls the update_component_list method to update the
        components list.
        """
        concurrence_mode_1 = self.textinput_concurrence_first.text()
        concurrence_mode_2 = self.textinput_concurrence_second.text()
        if not len(concurrence_mode_1) or not len(concurrence_mode_2):
            return
        self.add_component( "Concurrence", {"Name" : concurrence_mode_1+concurrence_mode_2, "Mode" : concurrence_mode_1+"-"+concurrence_mode_2} )
        self.update_component_list()

    def concurrence_remove():
        """
        This method removes the currently selected concurrence mode from the
        system components.

        This function calls the update_component_list method to update the
        components list.
        """
        index = self.text_output_list_of_concurrences.currentIndex().row()
        name = self.text_output_list_of_concurrences.model().item(index).toolTip()
        if name is None or not len(name):
            return
        if name not in self.system_components["Concurrence"]:
            return
        self.system_components["Concurrence"].pop(name)
        self.update_component_list()

    def toggle_concurrence_spectrum(self):
        """
        Enables or disables the concurrence spectrum inputs. This function is
        called when the "Add Spectra" checkbox is toggled.

        Note, that calculating the G2 spectra is pretty useless, so this feature
        may as well be removed from the GUI in the future.
        """
        enable = self.input_concurrence_add_spectra.isChecked()
        for a in [self.textinput_concurrence_spec_freq,self.textinput_concurrence_spec_range,self.textinput_concurrence_spec_res]:
            a.setEnabled(enable)

    def concurrenceAddModeToModes(self, which: str = "first", retain_modes: bool = False) -> None:
        """
        This method calls the getListOfTransitions method and adds the returned
        string to the concurrence modes input field. If retain_modes is True, the
        current modes are retained.

        Parameters:
            which: Either "first" or "second". Determines which input field is
                    used.
        """
        transitions = self.getListOfTransitions()
        out_field = self.textinput_concurrence_first if which == "first" else self.textinput_concurrence_second
        if retain_modes:
            transitions = out_field.text() + "," + transitions
        out_field.setText(transitions)

    def concurrence_active_change(self):
        """
        When changing the concurrence active state, this function is called.
        It sets the concurrence inputs fields to the values of the selected
        concurrence.
        """
        try:
            index = self.text_output_list_of_concurrences.currentIndex().row()
            name = self.text_output_list_of_concurrences.model().item(index).toolTip()
        except:
            return
        struct = self.system_components["Concurrence"][name]
        self.textinput_concurrence_first.setText(struct["Mode"].split("-")[0])
        self.textinput_concurrence_second.setText(struct["Mode"].split("-")[1])

    def gfunc_add(self):
        """
        This method adds a G1G2 mode to the system components.
        This function is subject to change in the future, as the G1G2
        adding mechanism is quite bad right now.

        This function calls the update_component_list method to update the
        components list.
        """
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

    def gfunc_remove(self):
        """
        Method to remove the currently selected G1G2 mode from the system
        components.
        """
        index = self.text_output_list_of_gfuncs.currentIndex().row()
        name = self.text_output_list_of_gfuncs.model().item(index).toolTip()
        if name is None or not len(name):
            return
        if name not in self.system_components["G1G2"]:
            return
        self.system_components["G1G2"].pop(name)
        self.update_component_list()

    def gfuncAddToModes(self, retain_modes: bool = False) -> None:
        """
        This method calls the getListOfTransitions method and adds the returned
        string to the G1G2 modes input field. If retain_modes is True, the
        current modes are retained.
        """
        transitions = self.getListOfTransitions()
        if retain_modes:
            transitions = self.textinput_correlation_modes.text() + "," + transitions
        self.textinput_correlation_modes.setText(transitions)

    def gfunc_active_change(self):
        """
        When changing the G1G2 active state, this function is called.
        It sets the G1G2 inputs fields to the values of the selected
        G1G2.
        """
        try:
            index = self.text_output_list_of_gfuncs.currentIndex().row()
            name = self.text_output_list_of_gfuncs.model().item(index).toolTip()
        except:
            return
        struct = self.system_components["G1G2"][name]
        self.textinput_correlation_modes.setText(struct["Mode"])
        self.input_gfunc_order.setCurrentIndex(struct["Order"])
        self.input_gfunc_integration.setCurrentIndex(struct["Method"])

    def wigner_func_add(self):
        """
        This function adds a Wigner function mode to the system components.
        This function is subject to change in the future, as the Wigner
        function adding mechanism is quite bad right now.

        This function calls the update_component_list method to update the
        components list.
        """
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

    def wigner_func_remove(self):
        """
        Method to remove the currently selected Wigner function mode from the system
        components.
        """
        index = self.text_output_list_of_wigner_funcs.currentIndex().row()
        name = self.text_output_list_of_wigner_funcs.model().item(index).toolTip()
        if name is None or not len(name):
            return
        if name not in self.system_components["Wigner"]:
            return
        self.system_components["Wigner"].pop(name)
        self.update_component_list()

    def wignerFuncAddModeToModes(self, retain_modes: bool = False) -> None:
        """
        This method calls the getListOfStates method and adds the returned
        string to the Wigner function modes input field. If retain_modes is True, the
        current modes are retained.
        """
        states = self.getListOfStates()
        if retain_modes:
            states = self.textinput_wigner_modes.text() + "," + states
        self.textinput_wigner_modes.setText(states)

    def wigner_func_active_change(self):
        """
        When changing the Wigner function active state, this function is called.
        It sets the Wigner function inputs fields to the values of the selected
        Wigner function.
        """
        try:
            index = self.text_output_list_of_wigner_funcs.currentIndex().row()
            name = self.text_output_list_of_wigner_funcs.model().item(index).toolTip()
        except:
            return
        struct = self.system_components["Wigner"][name]
        self.textinput_wigner_modes.setText(struct["Mode"])
        self.textinput_wigner_x.setText(struct["XMax"])
        self.textinput_wigner_y.setText(struct["YMax"])
        self.textinput_wigner_resolution.setText(struct["Resolution"])
        self.textinput_wigner_skip.setText(struct["Skip"])

    def detector_time_add(self):
        """
        This function adds a detector time mode to the system components.
        This function is subject to change in the future, as the detector
        time adding mechanism is quite bad right now.

        This function calls the update_component_list method to update the
        components list.
        """
        t0 = self.textinput_detector_t0.text()
        t1 = self.textinput_detector_t1.text()
        power = self.textinput_detector_tpower.text()
        if not len(t0) or not len(t1) or not len(power):
            return
        name = t0+t1+power
        self.add_component( "DetectorTime", {"Name" : name, "t0" : t0, "t1" : t1, "Power" : power} )
        self.update_component_list()

    def detector_time_remove(self):
        """
        Method to remove the currently selected detector time mode from the system
        components.

        This function calls the update_component_list method to update the
        components list.
        """
        index = self.text_output_list_of_detector_time.currentIndex().row()
        name = self.text_output_list_of_detector_time.model().item(index).toolTip()
        if name is None or not len(name):
            return
        if name not in self.system_components["DetectorTime"]:
            return
        self.system_components["DetectorTime"].pop(name)
        self.update_component_list()

    def detector_time_active_change(self):
        """
        When changing the detector time active state, this function is called.
        It sets the detector time inputs fields to the values of the selected
        detector time.
        """
        try:
            index = self.text_output_list_of_detector_time.currentIndex().row()
            name = self.text_output_list_of_detector_time.model().item(index).toolTip()
        except:
            return
        struct = self.system_components["DetectorTime"][name]
        self.textinput_detector_t0.setText(struct["t0"])
        self.textinput_detector_t1.setText(struct["t1"])
        self.textinput_detector_tpower.setText(struct["Power"])

    def detector_spec_add(self):
        """
        This function adds a detector spectrum mode to the system components.
        This function is subject to change in the future, as the detector
        spectrum adding mechanism is quite bad right now.

        This function calls the update_component_list method to update the
        components list.
        """
        w0 = self.textinput_detector_wcenter.text()
        w1 = self.textinput_detector_wrange.text()
        res = self.textinput_detector_wnum.text()
        power = self.textinput_detector_wpower.text()
        if not len(w0) or not len(w1) or not len(res) or not len(power):
            return
        name = w0+w1+res+power
        self.add_component( "DetectorSpectrum", {"Name" : name, "w0" : w0, "w1" : w1, "Points" : res, "Power" : power} )
        self.update_component_list()
    
    def detector_spec_remove(self):
        """
        Method to remove the currently selected detector spectrum mode from the system
        components.

        This function calls the update_component_list method to update the
        components list.
        """
        index = self.text_output_list_of_detector_spec.currentIndex().row()
        name = self.text_output_list_of_detector_spec.model().item(index).toolTip()
        if name is None or not len(name):
            return
        if name not in self.system_components["DetectorSpectrum"]:
            return
        self.system_components["DetectorSpectrum"].pop(name)
        self.update_component_list()

    def detector_spec_active_change(self):
        """
        When changing the detector spectrum active state, this function is called.
        It sets the detector spectrum inputs fields to the values of the selected
        detector spectrum.
        """
        try:
            index = self.text_output_list_of_detector_spec.currentIndex().row()
            name = self.text_output_list_of_detector_spec.model().item(index).toolTip()
        except:
            return
        struct = self.system_components["DetectorSpectrum"][name]
        self.textinput_detector_wcenter.setText(struct["w0"])
        self.textinput_detector_wrange.setText(struct["w1"])
        self.textinput_detector_wnum.setText(struct["Points"])
        self.textinput_detector_wpower.setText(struct["Power"])

    def phonon_spectral_function(self, multi: bool = False):
        """
        Calculates the phonon spectral density distribution function.
        This function is called when any of the phonon inputs change.

        Parameters:
            multi: If False, the simple spectral density is calculated.
        """
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

    def plot_phonon_spectral_function(self):
        """
        Calculates the current phonon spectral density distribution function
        and plots it in the label_plot_spectral_density widget.
        """
        self.label_plot_spectral_density.canvas.axes.clear()
        if self.input_phonons_use_qd.isChecked():
            x,y = self.phonon_spectral_function(True)
            c = "C1"
        else:
            x,y = self.phonon_spectral_function()
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

    def get_N_level_couplings(self, cl: str, prefix: str, energy):
        """
        Iteratively generates a state of a N-level ensemble and adds it to the
        system components.

        Parameters:
            cl: The current state of the ensemble.
            prefix: The prefix of the state name.
            energy: A function that returns the energy of the state.
        Returns:
            A list of the states coupled to the current state.
        """
        coupled_to = []
        for i in range(len(cl)):
            if cl[i] != "1":
                state = f"{cl[:i] + '1' + cl[i+1:]}"
                coupled_to.append( state ) 
        # Add state to system
        self.addEnergyLevel({"Name": f"{prefix}{cl}","Energy": energy(),"CoupledTo": tuple([f"{prefix}{ct}" for ct in coupled_to]),"DecayScaling" : "1" if "1" in cl else "0","DephasingScaling": "1","PhononScaling": "1" if "1" in cl else "0"} )
        return coupled_to

    def add_N_levels(self, n_tls: int = 2, energy: float = 1.0, sd = 1E-3, unit: str = "eV", prefix: str = "X"):
        """
        Generates N Two Level Systems, Tensors them into a unified Hilbert Space
        and adds them to the system components.

        Parameters:
            n_tls: The number of TLS to generate.
            energy: The energy of the TLS.
            sd: The standard deviation of the energy.
            unit: The unit of the energy.
            prefix: The prefix of the state names.
        """
        states = ["0"*n_tls]
        current_deph = 0
        while len(states):
            if energy is not None:                    
                # random value between -sd and +sd
                senergy = lambda current_deph=current_deph: f"{current_deph * (energy + (np.random.rand() - 0.5) * sd)}{unit}"
            else:
                en = QInputDialog.getDouble(self, 'Energy', f'Energy for State {current_deph} in eV', 1, 0, 1000, 10)[0]
                senergy = lambda current_deph=current_deph: f"{en}{unit}"
            states = [self.get_N_level_couplings(state, prefix, senergy) for state in states]
            states = [item for sebstates in states for item in sebstates]
            states = list(set(states))
            current_deph += 1

    def dialog_add_N_levels(self):
        """
        Dialog to add N TLS to the system components.
        """
        n_tls, ok = QInputDialog.getInt(self, "Add N TLS", "Number of TLS", 2, 1, 30, 1)
        if ok:
            energy, ok2 = QInputDialog.getDouble(self, "Energy", "Singe State Energy in eV", 1, 0, 1000, 1)
        if ok and ok2:
            stv, ok3 = QInputDialog.getDouble(self, "Energy Uncertainty", "Energy Uncertainty in mueV", 0, 0, 100000,1)
        if ok and ok2 and ok3:
            self.add_N_levels(n_tls, energy, stv*1E-6)

    def abbreviate_names(self):
        """
        Method to abbreviate the names of the system components.
        This is done by replacing the names with letters A-Z, then A0, B0, ...
        A1, B1, ... and so on.
        Components renamed are Energy Levels, Cavity Levels, Shifts and Pulses.

        This function calls the set_fields_from_components method to update the
        input fields.
        This function calls the update_component_list method to update the
        components list.
        This function calls the drawSystem method to update the system drawing.
        """
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

    def print_all_transitions(self):
        """
        Print all Available transitions into the console
        """
        print(",".join(self.generate_list_of_available_electronic_transitions()))
    
    def clipboard_copy_transition_list(self):
        """
        Copy a comma seperated list of all available electronic transitions to the clipboard.
        """
        self.clipboard.setText(",".join(self.generate_list_of_available_electronic_transitions()))

    def clipboard_copy_sum_of_transition_list(self):
        """
        Copy a "+" seperated list of all available electronic transitions to the clipboard.
        """
        self.clipboard.setText("+".join(self.generate_list_of_available_electronic_transitions()))

    def generate_command(self):
        """
        Generate the command string from the current system components, set the
        corresponding textoutput field and also copy it to the clipboard.

        This function calls the generateCommandString method to generate the
        command string.
        This function calls the commandToCLAList method to generate the command
        line arguments.
        """
        # Check for initial state
        if not len(self.textinput_initial_state.text()):
            self.pick_from_list_of_available_states()
        self.set_components_from_fields()
        command = self.generateCommandString()
        self.text_output_program_qdacc_command.setText(command)
        self.clipboard.setText(" ".join(self.commandToCLAList(command)))

    def run_command(self, input_command: str | None = None, start_already: bool = True, plot_afterwards: bool = False) -> QDaCCMainWoker:
        """
        Run the command string from the current text in the QDaCC input field.
        This command does NOT regenerate the command string, but uses the
        current text in the QDaCC input field.

        Parameters:
            input_command: The command string to run. If None, the current text
                            in the QDaCC input field is used.
            start_already: If True, the command is started immediately.
            plot_afterwards: If True, the plot_everything method is called after
                                the command has finished.
        """
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
        self.thread.pipeUpdatesTo(lambda text: self.updateTextBrowser(self.text_output_program_main, text), lambda text: self.updateProgressBar(text)) 
        self.thread.connectStarted(lambda: self.enableRunningButtonAnimation(self.button_run_program, [self.button_plot_everything]))
        self.thread.connectFinished(lambda: self.disableRunningButtonAnimation(self.button_run_program, "Run", [self.button_plot_everything]))
        self.thread.connectStarted(lambda: self.button_run_and_plot.setEnabled(False))
        self.thread.connectFinished(lambda: self.button_run_and_plot.setEnabled(True))
        if plot_afterwards:
            self.thread.connectFinished(lambda: self.plot_everything())

        if start_already:
            self.thread.start()

        return self.thread

    def kill_command(self):
        """
        Kills all of the QDaCC processes.
        This includes the main QDaCC Thread, the optimizer thread and the plot
        thread. Use this to cancel any of those operations.

        This function also sets the progress bar to 0.

        FIXME: Sometimes, when killing the optimizer thread, the main thread
        locks up. This is probably due to the optimizer thread not being
        properly killed.
        """
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

    def optimizerGetCurrentRunstring(self, current_runstring: str, replace_fields: bool = True):
        """
        Generates the optimizer runstring from the current runstring. This
        function is called when the optimizer is started. It replaces all
        fields in the current runstring with the values from the current
        system components, where some parameters are replaced by the optimizer.

        The replaced / to-replace values are marked using the python f-string 
        format "{}", with "{}" containing the name of the parameter to replace,
        e.g. "{P1}", "{0}", etc.

        Parameters:
            current_runstring: The current runstring.
            replace_fields: If True, the fields in the current runstring are
                            replaced by the values from the current system
                            components.
        Returns:
            The runstring with the replaced fields.
        """
        new_runstring = self.text_output_program_qdacc_command.toPlainText()
        if not replace_fields or not len(current_runstring):
            return new_runstring
        replace_threshold = 5
        # Replace fields.
        # Find indices of all "{" and "}" pairs in new_runstring. Assume a "}" follows a "{" before a new "{" is found."
        indices = [(i,j) for i,j in zip([i for i, ltr in enumerate(current_runstring) if ltr == "{"],[j for j, ltr in enumerate(current_runstring) if ltr == "}"])]
        print(f"Indices = {indices}")
        previous_start = 0
        for start,end in indices:
            # Get previous replace_threshold characters
            key_from = current_runstring[start-replace_threshold:start]
            key_to = current_runstring[end+1:end+replace_threshold]
            between = current_runstring[start:end+1]
            print(f"Trying to find {key_from} ... {key_to}, between is {between}")
            # If we find $key_from ... $key_to in the new runstring, replace it with the $between from the current runstring
            if key_from in new_runstring and key_to in new_runstring:
                index_from_new = new_runstring.index(key_from, previous_start)+1
                index_to_new = new_runstring.index(key_to, previous_start)
                print(f"Replacing {key_from} ... {key_to} with {between}, previous start is {previous_start}")
                print(f"New partial stirings:\n - {new_runstring[:index_from_new+len(key_to)]}\n - {new_runstring[index_to_new:]}")
                new_runstring = new_runstring[:index_from_new+len(key_to)] + between + new_runstring[index_to_new:]
                previous_start = index_to_new+1
        return new_runstring    

    def optimize(self):
        """
        This method reads the inputs from the optimizer input fields and
        invokes the QDaCCOptimizer class to optimize the system towards the
        given goal/fitness.

        This function is probably also highly subject to change in the future.
        """
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
        self.optimizer_thread.pipeUpdatesTo(lambda text: self.updateTextBrowser(self.text_output_program_main, text), lambda text: self.updateProgressBar(text)) 
        self.optimizer_thread.connectStarted(lambda: self.enableRunningButtonAnimation(self.button_run_program, [self.button_plot_everything]))
        self.optimizer_thread.connectStarted(lambda: self.enableRunningButtonAnimation(self.button_optimizer_optimize, None))
        self.optimizer_thread.connectFinished(lambda: self.disableRunningButtonAnimation(self.button_run_program, "Run", [self.button_plot_everything]))
        self.optimizer_thread.connectFinished(lambda: self.disableRunningButtonAnimation(self.button_optimizer_optimize, "Optimize", None))
        self.optimizer_thread.connectStarted(lambda: self.button_run_and_plot.setEnabled(False))
        self.optimizer_thread.connectFinished(lambda: self.button_run_and_plot.setEnabled(True))
        self.optimizer_thread.outputParametersTo(self.text_output_program_qdacc_command_sweep_display_2)

        def _plot_current():
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
            
            if len(current_params) and len(current_params[0]):
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
        
        self.optimizer_thread.plot_hint.connect(_plot_current)
        self.optimizer_thread.finished.connect(_plot_current)
        self.optimizer_thread.start()

    def transferRunString(self):
        """
        Transfers the current optimizer runstring to the QDaCC input field using
        the latest optimizer parameters for the replacement fields.
        """
        try: 
            self.text_output_program_qdacc_command.setText(self.current_optimizer_runstring)
        except Exception as e:
            try:
                command = self.text_output_program_qdacc_command_sweep_2.toPlainText()
                formatter = self.textinput_optimizer_formatfunction.text()
                parameters = eval(f"[{self.textinput_optimizer_initial_parameters.text()}]")
                runstring = eval(formatter, {"basestring" : command, "parameters" : parameters} | {f"P{i}" : p for i,p in enumerate(parameters,1)})
                self.text_output_program_qdacc_command.setText(runstring)
            except Exception as e2:
                self.updateTextBrowser(self.text_output_program_main, "Could not transfer runstring. Try running the optimizer first.")
                self.updateTextBrowser(self.text_output_program_main, f"Error(s): {e}\n{e2}")
        self.tabWidget.setCurrentIndex(9)

    def addFitnessFunction(self):
        """
        Adds a fitness function to the system components.
        """
        DialogAddFitness(main_window=self, style_sheet=self.styleSheet())

    def getOptimizerAvailableFiles(self):
        """
        Method to get the available files in the optimizer file destination
        folder.
        The user is then prompted to select the files to use for the optimizer.
        The selected files are then added to the optimizer input fields.
        """
        files = [f for f in os.listdir(self.textinput_file_destination.text()) if f.endswith(".txt")]
        items, ok = getGeneralItems([{"Text": file, "Type": QCheckBox} for file in files], parent=self) 
        if not ok:
            return
        new_text = ",".join( ['"'+item+'"' for item,include in zip(files, items) if include] )
        self.textinput_optimizer_files.setText(new_text)

    def getOptimizerFileIndices(self):
        """
        Method to get the indices of the files to use for the optimizer.
        The user is prompted to select the indices of the files to use for the
        optimizer. The selected indices are then added to the optimizer input
        fields.

        Note, that this function uses the "eval" method to parse the input.
        As this is a security risk, this is highly subject to change.
        """
        files = eval("["+self.textinput_optimizer_files.text()+"]")
        new_indices = ""
        new_labels = ""
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
            items, ok = getGeneralItems([{"Text": file, "Type": QCheckBox} for file in data_header], parent=self)
            if not ok:
                return
            if not len(items):
                new_indices += ",[]"
                continue
            new_indices += ",[" + ",".join( [str(i) for i,(item,include) in enumerate(zip(data_header, items)) if include] ) + "]"
            new_labels += ",".join( ['"'+item+'"' for i,(item,include) in enumerate(zip(data_header, items)) if include] )
        self.textinput_optimizer_file_indices.setText(new_indices[1:])
        self.textinput_optimizer_legend.setText(new_labels)

    def moveCurrentOptimizerParametersToInitialParameters(self):
        """
        Helper function to move the current optimizer parameters to the initial
        parameters input field. This is useful to continue an optimizer run
        with the current parameters.
        """
        try:
            self.textinput_optimizer_initial_parameters.setText( ",".join([str(el) for el in self.latest_optimizer_parameters]) )
        except AttributeError as e:
            print(f"Error when trying to move parameters to initial parameters. Make sure to run an optimizer first.")
    
    def clearOptimizerPlots(self):
        """
        Helper function to clear the optimizer plotwindows.
        """
        for axes in [self.label_plot_optimizer_1.canvas.axes, self.label_plot_optimizer_2.canvas.axes, self.label_plot_optimizer_3.canvas.axes]:
            axes.clear()
        for canvas in [self.label_plot_optimizer_1.canvas, self.label_plot_optimizer_2.canvas, self.label_plot_optimizer_3.canvas]:
            canvas.draw()

    def forceKillOptimizer(self):
        """
        Helper function to force kill the optimizer thread.
        """
        try:
            self.optimizer_thread.kill()
        except Exception as e:
            print("Killed Optimizer")

    def seedInitialOptimizerParameters(self):
        """
        Helper function to randomly initialize the initial parameters input
        field using the parameter bounds as a minimum and maximum for the random
        number. This is useful to start an optimizer run with random parameters.
        """
        input_bounds = self.textinput_optimizer_parameter_bounds.text().replace("None,","-1").replace(",None","1")
        bounds = eval(input_bounds)
        if not bounds or not len(bounds):
            return
        initial_parameters = [ np.random.rand() * (b[1]-b[0]) + b[0] for b in bounds ]
        self.textinput_optimizer_initial_parameters.setText( ",".join([str(el) for el in initial_parameters]) )
    
    def seedInitialOptimizerParametersInRange(self):
        """
        Helper function to randomly initialize the initial parameters input
        field using the users input as a minimum and maximum for the random
        number. This is useful to start an optimizer run with random parameters.
        """
        vals, ok = getGeneralItems([{"Title": "Lower Bound", "Type": QLineEdit, "Text": "0"}, {"Title": "Upper Bound", "Type": QLineEdit, "Text": "1"}], self)
        if not ok or vals is None:
            print("Invalid Inputs!")
            return
        lower_bound, upper_bound = float(vals[0]), float(vals[1])
        length = len(self.textinput_optimizer_initial_parameters.text().split(","))
        self.textinput_optimizer_initial_parameters.setText( ",".join([str(np.random.rand() * (upper_bound-lower_bound) + lower_bound) for _ in range(length)]) )

    def add_to_menu(self, name: str, connect, where, icon, children, shortcut):
        """
        Non-user available method to add items to the menu bar.
        This function can recursively add items to the menu bar, allowing for
        arbitraryly deep submenus.
        """
        if children:
            submenu = where.addMenu(name)
            if icon:
                submenu.setIcon(QIcon(icon))
            for child in children:
                child[2] = submenu
                self.add_to_menu(*child)
            return
        action = QAction(name, self)
        action.triggered.connect(connect)
        if shortcut:
            action.setShortcut(shortcut)
        if icon:
            action.setIcon(QIcon(icon))
        where.addAction(action)

    def getListOfTransitions(self) -> str:
        """
        Returns a string of all transitions in the system, separated by commas.
        The transitions include electronic state transitions A=B and cavity indentifiers
        like h.
        """
        states = self.generate_list_of_available_electronic_transitions() + self.generate_list_of_available_cavity_states()
        print(f"Picking from {states}")
        checked_items, ok = getCheckedItems(states, parent=self)
        print(f"Checked {checked_items}")
        if not ok:
            return ""
        new_states = ",".join(checked_items)
        # Prune final ","
        if new_states.endswith(","):
            new_states = new_states[:-1]
        return new_states

    def getListOfStates(self) -> str:
        """
        Returns a string of all states in the system, separated by commas.
        The states include electronic state transitions A=B and cavity indentifiers
        like h.
        """
        states = self.generate_list_of_available_total_states() + self.generate_list_of_available_cavity_states()
        print(f"Picking from {states}")
        checked_items, ok = getCheckedItems(states, parent=self)
        print(f"Checked {checked_items}")
        if not ok:
            return ""
        new_states = ",".join(checked_items)
        # Prune final ","
        if new_states.endswith(","):
            new_states = new_states[:-1]
        return new_states

    def getQDaCCPaths(self):
        """
        Method to get the QDaCC executable path and the destination path from
        the input fields.
        """
        qdacc_path_str = self.textinput_file_qdacc.text() or "./QDaCC.exe"
        destination = self.textinput_file_destination.text()
        qdacc_path = qdacc_path_str.split("/")
        qdacc_executable = qdacc_path[-1]
        return destination, qdacc_executable, f"{os.sep}".join(qdacc_path[:-1])

    def enableRunningButtonAnimation(self, button: QPushButton, disable_along: list[QPushButton] | None = None) -> str:
        """
        Enables the running animation for a button. This is used to indicate
        that the program is currently running. The button is disabled and the
        text is replaced by the animation. The button is re-enabled when the
        program is finished using the disableRunningButtonAnimation method.

        Parameters:
            button: The button to enable the animation for.
            disable_along: A list of buttons to disable along with the button, 
                            without enabling the animation for them.
        Returns:
            The current text of the button.
        """
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
        """
        Disables the running animation for a button. This is used to indicate
        that the program has finished. The button is re-enabled and the text is
        set to the input text.

        Parameters:
            button: The button to disable the animation for.
            text: The text to set the button to.
            enable_along: A list of buttons to enable along with the button,
        """
        self.thread_timer[text].stop()
        button.setText(text)
        button.setIcon(QIcon())
        button.setDisabled(False)
        if enable_along is not None:
            for other_button in enable_along:
                other_button.setDisabled(False)
        self.progressBar.setValue(0)

    def generate_list_of_available_electronic_transitions(self) -> list[str]:
        """
        Generates a list of available electronic transitions using the system
        components.
        """
        transitions = []
        for state in self.system_components["EnergyLevels"].values():
            for transition in state["CoupledTo"]:
                transitions.append(f"{state['Name']}={transition}")
        return transitions

    def generate_list_of_available_electronic_states(self) -> list[str]:
        """
        Generates a list of available electronic states using the system
        components. This is just the list of all keys in the EnergyLevels
        dictionary.
        """
        return list(self.system_components["EnergyLevels"].keys())

    def generate_list_of_available_cavity_states(self) -> list[str]:
        """
        Generates a list of available cavity states using the system
        components. This is just the list of all keys in the CavityLevels
        dictionary.
        """
        return list(self.system_components["CavityLevels"].keys())

    def generate_list_of_available_total_states(self) -> list[str]:
        """
        Generates a list of available states in the total Hilbert space
        of the system using the system components. This is the list of all
        possible combinations of electronic states and cavity photon number
        states.
        """
        available_states = []
        for state in self.system_components["EnergyLevels"]:
            new_state = f"{state}" + "".join([f":0{name}" for name in self.system_components["CavityLevels"]])
            available_states.append(new_state)
        return available_states

    def pushCursorToBack(self, field):
        """
        Method to push the cursor of a textfield back to the end of the text.
        """
        cursor = field.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        cursor.movePosition(QTextCursor.MoveOperation.Left)
        field.setTextCursor(cursor)

    def updateTextBrowser(self, browser: QTextBrowser, text: str):
        """
        Updates a QTextBrowser by appending the input text to the end of the
        current text.
        if the input text contains a <br>, the text is inserted as html instead
        of appended as plain text. The former is much slower and thus only used
        when actual html code is present.

        Parameters:
            browser: The QTextBrowser to update.
            text: The text to append to the QTextBrowser.
        """
        self.pushCursorToBack(browser)
        if "br>" in text:
            browser.insertHtml(text)
        else:
            browser.append(text)

    def updateProgressBar(self, value: int | str):
        """
        Updates a progressbar by setting the value to the input value.
        If the input value is a string, it is parsed as an integer.

        Parameters:
            value: The value to set the progressbar to.
        """
        if isinstance(value, int):
            self.progressBar.setValue(value)
        else:
            try:
                self.progressBar.setValue(int(value.split("%")[0].split()[-1]))
            except Exception as e:
                pass
        

    def updateUseStatistics(self):
        cpu_percent = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        self.progressBarCPU.setValue(cpu_percent)
        self.progressBarRAM.setValue(ram_usage)

    def sendMessage(self, bar: str, title: str, message: str):
        """
        Used to send informative messages to the user.

        Parameters:
            bar: The title of the message box.
            title: The title of the message box message field.
            message: The message to display.
        """
        msg = QMessageBox()
        msg.setIcon(QIcon(self.resources["Icon"]))
        msg.setText(title)
        msg.setInformativeText(message)
        msg.setWindowTitle(bar)
        msg.setStyleSheet(self.styleSheet())
        msg.setBaseSize(600, 600)
        msg.exec()

    def sendErrorMessage(self, error: str = "Error!", message: str = "Error!"):
        """
        Wrapper around the sendMessage method to send error messages.
        """
        self.sendMessage("Error!",error,message)

    def sendWarningMessage(self, warning: str = "Warning!", message: str = "Warning!"):
        """
        Wrapper around the sendMessage method to send warning messages.
        """
        self.sendMessage("Warning!",warning,message)

    def sendHintMessage(self, message: str = "Attention!"):
        """
        Wrapper around the sendMessage method to send hint messages.
        """
        self.sendMessage("Attention!","Attention!",message)

    def clearSystem(self):
        """
        Clears the system components and redraws the system.

        This function calles the update_component_list and drawSystem methods.
        """
        self.system_components["EnergyLevels"] = {}
        self.system_energy_level_groups = list()
        self.system_components["CavityLevels"] = {}
        self.system_cavity_level_groups = list()
        self.system_components["Pulse"] = {}
        self.system_components["Shift"] = {}
        self.update_component_list()
        self.drawSystem()

    def sort_energy_levels(self) -> None:
        """
        Method to sort the energy levels from lowest to highest and group them
        into groups of similar energy levels. The groups are determined using
        the grouping slider.

        This function is called when the system is drawn.
        """
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

    def add_component(self, category: str, struct: dict, replaced: str | None = None) -> None:
        """
        Method to add a component to the system components.

        Parameters:
            category: The category of the component. This is one of the keys in
                        the system_components dictionary.
            struct: The component to add. This is a dictionary containing the
                    component information.
            replaced: The name of the component to replace. If this is not None,
                        the component is replaced instead of added.
        """
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
        """
        Method to update the component lists in the different tabs.
        The QListView widgets are updated with the current system components.
        """
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
        """
        Wrapper around the add_component method to add an energy level to the
        system components.
        """
        self.add_component( "EnergyLevels", p , replaced)
        
    def addCavity(self, p: dict, replaced: str | None = None):
        """
        Wrapper around the add_component method to add a cavity level to the
        system components.
        """
        self.add_component( "CavityLevels", p , replaced)

    def addPulse(self, p: dict):
        """
        Wrapper around the add_component method to add a pulse to the
        system components.
        """
        # Confirm that Pulse sizes are the same:
        a,f,c,w,t = len(p["Amplitudes"]), len(p["Frequencies"]), len(p["Centers"]), len(p["Widths"]), len(p["Type"])
        if not (a==f and f==c and c==w and w==t):
            self.sendErrorMessage("Wrong Pulse Dimensions", "The arrays you entered for the Pulse parameters must be of equal length!")
            return
        self.add_component( "Pulse", p )
        
    def addShift(self, p: dict):
        """
        Wrapper around the add_component method to add a shift to the
        system components.
        """
        self.add_component( "Shift", p )

    def repeatPulseNTimes(self):
        """
        Helper function to repeat a pulse n times.
        The user is prompted to enter the number of repeats and the delay
        between the repeats. The user is then prompted to select the pulses to
        repeat. The selected pulses are then repeated n times with the delay
        between the repeats.
        """
        # Get Number of Repeats
        n, ok = getGeneralItems([{"Title": "Number of Repeats", "Type": QLineEdit, "Text": "1"}, {"Title": "Delay", "Type": QLineEdit, "Text": "0"}]+
                                 [{"Text": f"Repeat {p}", "Type": QCheckBox} for p in self.system_components["Pulse"]], self)
        if not ok or n is None:
            return
        print(ok, n)
        reps, delay = int(n[0]), float(n[1])
        pulses = [name for include,name in zip(n[2:],self.system_components["Pulse"].keys()) if include]
        print(reps,delay,pulses)

        for i,pulse in enumerate(pulses):
            current_pulse = {n:v for n,v in self.system_components["Pulse"][pulse].items()}
            # Get rightmost time in pulse
            rightmost_time = current_pulse["Centers"][-1]
            # Remove unit
            rightmost_time,unit,_ = seperate_unit(rightmost_time)
            rightmost_time = float(rightmost_time)
            print(f"Rightmost time: {rightmost_time}")
            amps = list(self.system_components["Pulse"][pulse]["Amplitudes"]) * (reps+1)
            widths = list(self.system_components["Pulse"][pulse]["Widths"]) * (reps+1)
            types = list(self.system_components["Pulse"][pulse]["Type"]) * (reps+1)
            freqs = list(self.system_components["Pulse"][pulse]["Frequencies"]) * (reps+1)
            centers = list(self.system_components["Pulse"][pulse]["Centers"])
            for rep in range(reps):
                starting_time = (rep+1)*(rightmost_time + delay)
                new_times = [ starting_time + get_unit_value(c) for c in current_pulse["Centers"] ]
                centers += [ f"{t}{unit}" for t in new_times ]
            self.system_components["Pulse"][pulse]["Amplitudes"] = tuple(amps)
            self.system_components["Pulse"][pulse]["Widths"] = tuple(widths)
            self.system_components["Pulse"][pulse]["Type"] = tuple(types)
            self.system_components["Pulse"][pulse]["Frequencies"] = tuple(freqs)
            self.system_components["Pulse"][pulse]["Centers"] = tuple(centers)
        self.update_component_list()

    def set_fields_from_components(self):
        """
        Sets the fields of the GUI from the current system components.
        Use this to update the GUI after tinkering with the system dicts.
        """
        for cat, content in self.system_components_fields.items():
            for name, struct in content.items():
                if cat in self.system_components and name in self.system_components[cat]:
                    print(f"Setting {cat} {name} to {struct['typeof'](self.system_components[cat][name])}")
                    struct["set"]( struct["typeof"](self.system_components[cat][name]) )

    def set_components_from_fields(self):
        """
        Set the system components from the current fields of the GUI.
        Use this to update the system dicts after tinkering with the GUI.
        """
        for cat,content in self.system_components_fields.items():
            for name, struct in content.items():
                self.system_components[cat][name] = struct["parse"]()

    def forceToolTip(self, where: QObject, error: str = "Error"):
        """
        Forcefully display a tool tip at the current mouse location.
        This is used to display error messages when the user hovers over a
        button or inputs invalid data into a field.

        Parameters:
            where: The object to display the tool tip for.
            error: The error message to display.
        """
        from PySide6.QtCore import QTimer
        original_tooltop = where.toolTip()
        where.setToolTip(error)
        QTimer.singleShot(100, lambda: QToolTip.showText(where.mapToGlobal(where.rect().center()), where.toolTip(), where, msecShowTime=10000))
        QTimer.singleShot(200, lambda: where.setToolTip(original_tooltop))

    def buildBaseEvaluationDict(self):
        """
        Many parts of the GUI execute the eval function with user input. This
        eval functions needs to know the values of the different variables
        used in the input. This function builds a dictionary of the variables
        used in the eval function and their values. Capital letters indicate 
        that the user input is a unit value, while lower case letters indicate
        that the user input is a scaled value.

        The dictionary also includes numpy, scipy and some additional functions
        including but not limiting to

        s(x) = Sigmoid Function
        """
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
                     # Special Functions
                     "s" : lambda x: 1./(1. + np.exp(-x))
                     }
        return eval_dict

    def generate_scan_or_sweep(self):
        """
        This function generates a scan or sweep depending on the input of the
        user. The user can choose to scan over one parameters or sweep over two.
        The user can choose the range of the scan or sweep and the number of
        points to scan or sweep over.
        """
        # Generate scans
        x1,x2 = 0,0
        span1,span2 = (0,0), (0,0)
        self.scan_sweep_values = defaultdict(lambda: None)
        
        if self.checkbox_activate_scan_parameter_1.isChecked():
            span1 = (float(self.textinput_scan_parameter_1_from.text()), float(self.textinput_scan_parameter_1_to.text()))
            points = self.textinput_scan_parameter_1_points.text()
            if "," in points:
                x1 = [float(point) for point in points.split(",")]
            else:
                points = int(points)
                x1 = np.linspace(span1[0], span1[1], points, endpoint=True)
        if self.checkbox_activate_scan_parameter_2.isChecked():
            span2 = (float(self.textinput_scan_parameter_2_from.text()), float(self.textinput_scan_parameter_2_to.text()))
            points = self.textinput_scan_parameter_2_points.text()
            if "," in points:
                x2 = [float(point) for point in points.split(",")]
            else:
                points = int(points)
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

    def connect_functionality(self):
        # "Next" Buttons
        # DEPRECATED
        #for button in [self.button_next_tab_system_to_config, self.button_next_tab_config_to_timeline, self.button_next_tab_timeline_to_spectrum, self.button_next_tab_spectrum_to_indist, self.button_next_tab_indist_to_conc, self.button_next_tab_sconc_to_stats, self.button_next_tab_stats_to_detector, self.button_next_tab_detector_to_generate]:
        #    button.clicked.connect( lambda: self.tabWidget.setCurrentIndex( self.tabWidget.currentIndex() + 1 ) )
        
        # Add Stuff Dialog
        self.button_add_electronic_state.clicked.connect(lambda: DialogAddElectronic(main_window=self, style_sheet=self.styleSheet()))
        self.button_add_cavity.clicked.connect(lambda: DialogAddCavity(main_window=self, style_sheet=self.styleSheet()))
        self.button_add_optical_pulse.clicked.connect(lambda: DialogAddPulse(main_window=self, style_sheet=self.styleSheet()))
        self.button_add_electronic_shift.clicked.connect(lambda: DialogAddChirp(main_window=self, style_sheet=self.styleSheet()))
        # Modify Stuff
        self.button_modify_clear.clicked.connect(self.clearSystem)
        
        # Set how to as the markdown readme file
        self.output_howto.setHtml(self.openReadmeFile())

        # Set ListView Models
        self.list_components.setModel(QStandardItemModel())
        self.text_output_list_of_spectra.setModel(QStandardItemModel())
        self.text_output_list_of_indists.setModel(QStandardItemModel())
        self.text_output_list_of_concurrences.setModel(QStandardItemModel())        
        self.text_output_list_of_gfuncs.setModel(QStandardItemModel())
        self.text_output_list_of_wigner_funcs.setModel(QStandardItemModel())
        self.text_output_list_of_detector_time.setModel(QStandardItemModel())
        self.text_output_list_of_detector_spec.setModel(QStandardItemModel())

        # Generic Buttons
        self.input_draw_details.clicked.connect(self.drawSystem)
        self.button_modify_delete.clicked.connect(self.delete_input)
        self.button_modify_edit.clicked.connect(self.edit_input)
        self.list_components.doubleClicked.connect(self.edit_input)
        self.button_time_config_tol.clicked.connect(self.openToleranceDialog)
        self.button_time_config_grid.clicked.connect(self.openGridDialog)
        self.button_open_destination_folder.clicked.connect(self.openDestinationFolder)
        self.button_empty_destination_folder.clicked.connect(self.empty_target_folder)
        self.input_destination.clicked.connect(self.set_file_path) 
        self.input_path_to_qdacc.clicked.connect(self.set_qdacc_filepath) 
        self.button_set_setting_file_path.clicked.connect(self.set_settingfile_path)
        self.button_change_rungstring_to_settingfile.clicked.connect(self.toggle_runstring_full_settingfile)
        self.input_initial_state.clicked.connect(self.pick_from_list_of_available_states)
        self.input_phonons_use_qd.stateChanged.connect(self.toggle_phonon_inputs)
        self.text_output_list_of_spectra.selectionModel().selectionChanged.connect(self.spectrum_active_change)
        self.button_add_spectrum_to_output.clicked.connect(self.spectrum_add)
        self.button_remove_spectrum_from_output.clicked.connect(self.spectrum_remove)
        self.button_add_spectrum_mode.clicked.connect(self.spectrumAddModeToModes)
        self.button_add_indist_to_output.clicked.connect(self.indist_add)
        self.button_remove_indist_from_output.clicked.connect(self.indist_remove)
        self.button_add_indist_mode.clicked.connect(self.indistAddModeToModes)
        self.text_output_list_of_indists.selectionModel().selectionChanged.connect(self.indist_active_change)
        self.input_concurrence_add_spectra.stateChanged.connect(self.toggle_concurrence_spectrum)
        self.button_add_concurrence_to_output.clicked.connect(self.concurrence_add)
        self.button_remove_concurrence_from_output.clicked.connect(self.concurrence_remove)
        self.button_add_concurrence_mode_1.clicked.connect(lambda: self.concurrenceAddModeToModes(which="first"))
        self.button_add_concurrence_mode_2.clicked.connect(lambda: self.concurrenceAddModeToModes(which="second"))
        self.text_output_list_of_concurrences.selectionModel().selectionChanged.connect(self.concurrence_active_change)
        self.button_add_gfunc_to_output.clicked.connect(self.gfunc_add)
        self.button_remove_gfunc_from_output.clicked.connect(self.gfunc_remove)
        self.button_add_gfunc_mode.clicked.connect(self.gfuncAddToModes)
        self.text_output_list_of_gfuncs.selectionModel().selectionChanged.connect(self.gfunc_active_change)
        self.button_add_wigner.clicked.connect(self.wigner_func_add)
        self.button_remove_wigner.clicked.connect(self.wigner_func_remove)
        self.button_add_wigner_mode.clicked.connect(self.wignerFuncAddModeToModes)
        self.text_output_list_of_wigner_funcs.selectionModel().selectionChanged.connect(self.wigner_func_active_change)
        self.button_add_detector_time.clicked.connect(self.detector_time_add)
        self.button_add_detector_spectral.clicked.connect(self.detector_spec_add)
        self.text_output_list_of_detector_time.selectionModel().selectionChanged.connect(self.detector_time_active_change)
        self.button_remove_detector_time.clicked.connect(self.detector_time_remove)
        self.button_remove_detector_spectral.clicked.connect(self.detector_spec_remove)
        self.text_output_list_of_detector_spec.selectionModel().selectionChanged.connect(self.detector_spec_active_change)
        self.button_plot_everything.clicked.connect(self.plot_everything)
        self.button_generate_run.clicked.connect(self.generate_command)
        self.button_run_program.clicked.connect(lambda: self.run_command(None))
        self.button_run_and_plot.clicked.connect(lambda: self.run_command(None, plot_afterwards=True))
        self.button_run_kill.clicked.connect(self.kill_command)
        self.button_optimizer_get_runstring.clicked.connect(lambda: self.text_output_program_qdacc_command_sweep_2.setText(self.optimizerGetCurrentRunstring(self.text_output_program_qdacc_command_sweep_2.toPlainText())))
        self.button_optimizer_optimize.clicked.connect(self.optimize)
        self.button_optimizer_runstring_to_main.clicked.connect(self.transferRunString)
        self.button_optimizer_fitness_function.clicked.connect(self.addFitnessFunction)
        self.button_optimizer_files.clicked.connect(self.getOptimizerAvailableFiles)
        self.button_optimizer_files_2.clicked.connect(self.getOptimizerFileIndices)
        self.button_sweeper_plot.clicked.connect(self.generate_scan_or_sweep)
        self.button_sweeper_get_runstring.clicked.connect(lambda: self.text_output_program_qdacc_command_sweep.setText(self.optimizerGetCurrentRunstring(self.text_output_program_qdacc_command_sweep.toPlainText())))
        self.button_generate_copy.clicked.connect(lambda: self.clipboard.setText(" ".join(self.commandToCLAList(self.text_output_program_qdacc_command.toPlainText()))))
        self.button_timeline_force_calculate_time.clicked.connect(self.plotTimePrediction)
        self.button_timeline_force_calculate_spectra.clicked.connect(self.spectrum_predict_plot)


        for btn in [self.button_run_and_plot, self.button_run_program]:
            btn.clicked.connect(lambda: self.text_output_program_main.verticalScrollBar().setValue(self.text_output_program_main.verticalScrollBar().maximum()))

        # Phonon Spectral functions on change of any phonon input.
        for field in [self.textinput_phonons_iterator_stepsize, self.textinput_phonons_sd_wcutoff, self.textinput_phonons_sd_wdelta, self.textinput_phonons_sd_tcutoff, self.textinput_phonons_sd_ohmamp, self.textinput_phonons_sd_alpha,
                      self.textinput_phonons_sd_qd_de, self.textinput_phonons_sd_qd_rho, self.textinput_phonons_sd_qd_aeah_ratio, self.textinput_phonons_sd_qd_dh, self.textinput_phonons_sd_qd_cs, self.textinput_phonons_sd_qd_size]:
            field.editingFinished.connect(self.plot_phonon_spectral_function)

        # Menu
        actions_to_add = [  
            ["Print Component Dict", lambda: print(self.system_components), self.menu_developer_tools, None, None, None],
            ["Set Components from Fields", self.set_components_from_fields, self.menu_developer_tools, None, None, None],
            ["Set Fields from Components", self.set_fields_from_components, self.menu_developer_tools, None, None, None],
            ["Connect Fields", self.connect_config_to_fields, self.menu_developer_tools, None, None, None],
            ["Plot Predicted Spectra", self.spectrum_predict_plot, self.menu_functions, self.resources["graph2"], None, None],
            ["Plot Phonon Functions", self.plot_phonon_spectral_function, self.menu_functions, self.resources["graph2"], None, None],
            ["Plot Temporal Functions", self.plotTimePrediction, self.menu_functions, self.resources["graph2"], None, None],
            ["Repeat Pulse", self.repeatPulseNTimes, self.menu_tools, self.resources["graph2"], None, None],
            ["Optimizer", None, self.menu_tools, None, [
                ["Set Initial Parameters to latest Parameters", self.moveCurrentOptimizerParametersToInitialParameters, "parent", None, None, None],
                ["Randomly Initialize Parameters in bounds", self.seedInitialOptimizerParameters, "parent", None, None, None],
                ["Randomly Initialize Parameters in range", self.seedInitialOptimizerParametersInRange, "parent", None, None, None],
                ["Clear Optimizer Plots", self.clearOptimizerPlots, "parent", None, None, None],
                ["Cancel Optimization", self.forceKillOptimizer, "parent", None, None, None],
            ], None],
            ["Add N TLS with statistical deviation", self.dialog_add_N_levels, self.menu_tools, self.resources["Tree"], None, None],
            ["Print All Transitions", self.print_all_transitions, self.menu_developer_tools, None, None, None],
            ["Copy List of Transitions", self.clipboard_copy_transition_list, self.menu_tools, self.resources["marrow_right"], None, "Ctrl+C"],
            ["Copy Sum of Transitions", self.clipboard_copy_sum_of_transition_list, self.menu_tools, self.resources["marrow_right"], None, "Ctrl+Shift+C"],
            ["Abbreviate State Names", self.abbreviate_names, self.menu_tools, self.resources["marrow_right"], None, None],
            ["Export", lambda: self.export_command(), self.menu_main, self.resources["Arrow_Up_Load"], None, "Ctrl+E"],
            ["Import", self.import_command, self.menu_main, self.resources["Arrow_Down_Save"], None, "Ctrl+I"],
            ["Import", None, self.menu_main, self.resources["Arrow_Down_Save"], [
                ["States", lambda: self.import_command("EnergyLevels"), "parent", None, None, None],
                ["Cavities", lambda: self.import_command("CavityLevels"), "parent", None, None, None],
                ["Pulses", lambda: self.import_command("Pulse"), "parent", None, None, None],
                ["Shifts", lambda: self.import_command("Shift"), "parent", None, None, None],
                ["Paths", lambda: self.import_command("RunConfig"), "parent", None, None, None],
                ["Sweeper", lambda: self.import_command("Sweeper"), "parent", None, None, None],
                ["System Config", lambda: self.import_command("ConfigSystem"), "parent", None, None, None],], None],
            ["Save Current", self.export_save_existing, self.menu_main, self.resources["Save"], None, "Ctrl+S"],
            ["Redraw System", self.drawSystem, self.menu_developer_tools, None, None, None],
            ["Clear System", self.clearSystem, self.menu_developer_tools, None, None, None],
            ["Generate QDaCC Command", self.generate_command, self.menu_developer_tools, None, None, None],
            ["Set initial State", self.pick_from_list_of_available_states, self.menu_developer_tools, None, None, None],
            ["Set File Destination", self.set_file_path, self.menu_developer_tools, None, None, None],
            ["Set QDaCC Filepath", self.set_qdacc_filepath, self.menu_developer_tools, None, None, None],
            ["Run QDaCC", lambda: self.run_command(None), self.menu_main, self.resources["Gear"], None, None],
        ]
        
        for name, connect, where, icon, children, shortcut in actions_to_add:
            self.add_to_menu(name, connect, where, icon, children, shortcut)


        self.slider_state_grouping.valueChanged.connect(self.drawSystem)
        self.slider_state_separator.valueChanged.connect(self.drawSystem)
        self.slider_state_x_seperation.valueChanged.connect(self.drawSystem)

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

    def drawSystem(self) -> None:
        """
        Draws the system in the main window. This includes energy levels, cavities 
        and pulses. For now, shifts are not plotted. 
        The drawing parameters can be changed by the user using the sliders.

        Additional Details are plotted when the user checks the corresponding box.
        """
        scene = QGraphicsScene()
        # Plot System Details?
        self.plot_system_details = self.input_draw_details.isChecked()
        # Sort Energy Levels
        self.sort_energy_levels()
        size = self.label_output_system.size()
        self.fixed_energy_w, self.fixed_energy_h = size.width()*0.99, size.height()*0.99
        #self.label_output_system.setMaximumSize(size)
        w,h = int(self.fixed_energy_w), int(self.fixed_energy_h) 
        self.output_system_canvas = QPixmap(w, h)
        qp = QPainter(self.output_system_canvas)
        qp.setRenderHint(QPainter.RenderHints.Antialiasing)
        #qp.setRenderHints(qp.Antialiasing)
        self.output_system_canvas.fill( self.design_colors["secondary_color"] )
        if len(self.system_components["EnergyLevels"].keys()) < 2:
            qp.end()
            scene.addPixmap(self.output_system_canvas)
            self.label_output_system.setScene(scene)
            self.update()
            return 
        
        state_color = QColor(self.render_colors["State"])
        statename_color = QColor(self.render_colors["StateName"])
        transition_color = QColor(self.render_colors["Transition"])
        reset_color = QColor(self.render_colors["Neutral"])

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
            #qp.drawPath(path)
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
            pen.setCapStyle(Qt.PenCapStyle.RoundCap)
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

        # Draws a sine along a line
        def draw_sine_along(x1,y1,x2,y2, _w = 3, _color = transition_color):
            points = 300
            x = np.linspace(0,1,points)
            # Frequency
            frequcency = 50
            # Angle of line
            angle = abs(np.arctan2(y2-y1,x2-x1))
            # Length of the line
            length = np.sqrt((x2-x1)**2 + (y2-y1)**2)
            # Sine
            func = max(np.sin(angle),np.cos(angle))*length/frequcency*np.cos(frequcency*np.pi*x)
            # Draw lines from x1,y1 to x2,y2 and add the sine onto it weighted by the angle of the line
            new_x = np.linspace(x1,x2,points) + func*np.sin(angle)
            new_y = np.linspace(y1,y2,points) + func*np.cos(angle)
            for x1,x2,y1,y2 in zip(new_x,new_x[1:],new_y,new_y[1:]):
                draw_line(int(x1), int(y1), int(x2),int(y2), _w = _w, _style = Qt.PenStyle.SolidLine, _color = _color)
            

        # Draw Energy Levels from bottom to top
        lowest_energy = 0 if len(self.system_components["EnergyLevels"].keys()) < 1 else min(get_uv_scaled(a["Energy"]) for a in self.system_components["EnergyLevels"].values())
        energy_normalization = max([get_uv_scaled(a["Energy"]) for a in self.system_components["EnergyLevels"].values()]) - lowest_energy
        lowest_level = 0.8*h
        highest_level = 0.2*h
        self.level_height = (lowest_level - highest_level) * 0.05
        level_height = self.level_height
        level_width_factor = 0.3
        artificial_grouping_offset = self.slider_state_separator.value()/10 # Group members get seperated by this much times the level height at least
        articifial_x_offset = self.slider_state_x_seperation.value()
        for current_group,group_of_levels in enumerate(self.system_energy_level_groups):
            level_width = max(2,w*level_width_factor if len(group_of_levels) < 2 else 0.6*w/(len(group_of_levels)))
            last_y = lowest_energy
            for l,level in enumerate(group_of_levels,1):
                # X,Y
                y_seperation = 0 
                if abs(last_y - get_uv_scaled(level["Energy"])) / energy_normalization < artificial_grouping_offset * level_height: 
                    y_seperation = level_height*artificial_grouping_offset*(l-1)
                level_y = lowest_level - (lowest_level - highest_level)*(get_uv_scaled(level["Energy"])-lowest_energy) / energy_normalization - y_seperation
                level_x = w/(len(group_of_levels)+1)*l - level_width/2.# center of individual level - delta/2
                # Add -articifial_x_offset to level_x if the level would be on the left side of the screen, +offset it if it would be on the right side
                if level_x < w/2:
                    level_x -= (current_group%2)*articifial_x_offset
                else:
                    level_x += (current_group%2)*articifial_x_offset
                last_y = get_uv_scaled(level["Energy"])
                if self.plot_system_details:
                    name = f"{level['Name']} - E = {level['Energy']}, |{level['DecayScaling']}|{level['DephasingScaling']}|{level['PhononScaling']}|"
                else:
                    name = f"{level['Name']}"
                # Determine Color
                color_to_draw = state_color
                for t,transto in enumerate(level["CoupledTo"]):
                    if transto not in self.system_components["EnergyLevels"]:
                        color_to_draw = self.render_colors["Red"]
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
            cavity_color = QColor(self.render_colors["Cavity"][c%len(self.render_colors["Cavity"])])
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
        pulses_done = defaultdict(lambda: 0)
        pulse_colors = [QColor("#BD8740"), QColor("#BD5340"), QColor("#97BD40"), QColor("#40BDAC")]
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
                    power = pulses_done["".join(transition)]
                    delta =  (-1)**power*max(power,1)
                    x1 = e0[0] + e0[2]/2. + self.level_height * delta
                    y1 = e0[1] + e0[3]/2 - self.level_height
                    x2 = e1[0] + e1[2]/2. + self.level_height * delta
                    y2 = e1[1] + e1[3]/2 + self.level_height
                    #x = (x1+x2)/2 * delta
                    y = (y1+y2)/2
                    #draw_exp(x,y, 100, 50, 3, QColor("#1A207A"))
                    draw_sine_along(x1+delta,y1,x2+delta,y2, 2, pulse_colors[i%len(pulse_colors)])
                pulses_done["".join(transition)] += 1
                    
        qp.end()

        scene.addPixmap(self.output_system_canvas)
        self.label_output_system.setScene(scene)
        
        self.update()

    def generateCommandString(self, escape_symbol = "'"):
        """
        Generates the final command string from the current system components
        using the component_parser function. 

        Parameters:
        escape_symbol: str
            The symbol to use for escaping the command string

        Returns:
            str: The final command string with placeholders for the executable 
                    and the filepath
        """
        escaped = self.input_escape_output_command.isChecked()
        # Generate Commands
        commands = [component_parser(component,escaped,self.system_components,escape_symbol=escape_symbol,callback=self.sendHintMessage) for component in self.system_components.keys()]

        final_command = f"[QDaCC] {' '.join(commands)} [FILEPATH]"
        while "  " in final_command:
            final_command = final_command.replace("  "," ")
        return final_command

    def commandToCLAList(self, commands = None, escape_symbol = "'") -> str:
        """
        Generates a ready-to-execute command line argument list from the current system components
        or from a given command string.

        Parameters:
        commands: str
            The command string to use. If None, the command string will be generated from the current system components
        escape_symbol: str
            The symbol to use for escaping the command string

        Returns:
            str: The final command string with the excutable and the filepaths inserted.
        """
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
        """
        Resize Event Hook. Redraws the system when the window is resized.
        """
        self.drawSystem()
        QMainWindow.resizeEvent(self, event)

    # Plot Task
    # Mode can be "all", "bloch", "dm". The latter two will ask for additional parameters
    def plot_everything(self, force_folder: bool = False):
        """
        Method to call the plot script on the current working directory.
        The plot script is chosen by the current plot mode.

        This script then determines whether to plot the whole folder, or just a single file.

        Parameters:
        force_folder: bool
            If True, the plot script will be called with the -folder, which will plot all files in the current working directory.
        """
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
        self.plot_thread.pipeUpdatesTo(lambda text: self.updateTextBrowser(self.text_output_program_main, text), lambda text: self.updateProgressBar(text)) 
        self.plot_thread.connectStarted(lambda: self.enableRunningButtonAnimation(self.button_plot_everything, [self.button_run_program]))
        self.plot_thread.connectFinished(lambda: self.disableRunningButtonAnimation(self.button_plot_everything, "Plot", [self.button_run_program]))
        self.plot_thread.connectStarted(lambda: self.button_run_and_plot.setEnabled(False))
        self.plot_thread.connectFinished(lambda: self.button_run_and_plot.setEnabled(True))
        if "QDLC.eval_tools.get_files" in plot_command:
            def insert_plots():
                folders = [path_to_destination] if not is_folder else [os.path.join(path_to_destination, f, "img") for f in os.listdir(path_to_destination) if os.path.isdir(os.path.join(path_to_destination, f))]
                print(f"Plotting everything in {folders}")
                for folder in folders:
                    if not os.path.isdir(folder):
                        print(f"Skipping '{folder}' because it is not a folder")
                        continue
                    for file in os.listdir(folder):
                        complete_path = os.path.join(folder, file)
                        if file.endswith(".png"):
                            self.plot_thread.progress.emit(f"Plotting {complete_path}\n")
                            print(f'<br><img  src="{complete_path}?' + str(time()) +'"></br>')
                            self.plot_thread.progress.emit(f'<br><img  src="file:///{complete_path}?' + str(time()) +'"></br>')
                            self.plot_thread.progress.emit(f'<br><a href="file:///{complete_path.replace(".png",".pdf")}">Open this file<\a></br>')
            self.plot_thread.connectFinished(insert_plots)
        self.plot_thread.start()

    def calculatePulseArray(self, t_array, amp, freq, center, width, ptype):
        """
        Calculates the pulse array for a given pulse type and parameters.
        This is used for the time prediction plot.

        The pulse includes the phase and the exponent setting.
        Types plotted are cw, gauss and sech. If other modes exist in QDaCC, they
        are not included here, such as SUPER pulses or pulse chirps.
        """
        #madeup_freq = 4*3.1415*10/(t1-t0) * f/max_freq
        phase = 0 if "phase" not in ptype else float(ptype.split("phase(")[-1].split(")")[0])
        exponent = 2 if "exponent" not in ptype else int(ptype.split("exponent(")[-1].split(")")[0])
        envelope = None
        if "cw" in ptype:
            y = np.sin(freq*(t_array-center) + width)
        elif "gauss" in ptype:
            envelope = np.exp( -((t_array-center) / width)**exponent / 2 )
            y = envelope*np.sin(freq*(t_array-center) + 3.1415*phase)
        elif "sech" in ptype:
            envelope = 1./np.cosh( 0.5*(t_array-center)/width )
            y = envelope*np.sin(freq*(t_array-center) + 3.1415*phase)
        else:
            y = np.zeros_like(t_array)
        return y, envelope

    def plotTimePrediction(self):
        """
        Plots the time prediction of the current system. This includes excitation
        pulses, decay times and detector times.
        Note, that this is in noway a complete simulation of the system, but rather
        a rough estimate of the time evolution of the system.
        """
        self.set_components_from_fields()
        self.label_plot_time_prediction.canvas.axes.clear()
        start = self.system_components["ConfigTime"].get("Start","0.0")
        end = self.system_components["ConfigTime"].get("End","1ns")
        if end == "auto":
            end = "1ns"
            # Print text on label_plot_time_prediction
            self.label_plot_time_prediction.canvas.axes.text(0.5, 0.5, f"Warning: Set End time != 'auto'!", horizontalalignment='center', verticalalignment='center', transform=self.label_plot_time_prediction.canvas.axes.transAxes, fontsize=20, color='red', weight='bold')
        t_array = np.linspace( get_uv_scaled(start), get_uv_scaled(end) , 500, endpoint=True)
        index = 0
        hatches = ["////","\\\\\\\\","||"]
        # Plot Pulses
        if "Pulse" not in self.system_components:
            return
        for h,(name,pulse) in enumerate(self.system_components["Pulse"].items()):
            for c,(amp,freq,center,width,ptype) in enumerate(list(zip( pulse["Amplitudes"],pulse["Frequencies"],pulse["Centers"],pulse["Widths"],pulse["Type"] ))):
                y_array, y_array_env = self.calculatePulseArray(t_array, get_uv_scaled(amp), get_uv_scaled(freq), get_uv_scaled(center), get_uv_scaled(width), ptype)
                y_array[y_array<0] = 0
                if y_array_env is not None:
                    self.label_plot_time_prediction.canvas.axes.fill_between(t_array, y_array_env, 0, alpha=0.4, color = f"C{index}", hatch = hatches[h%len(hatches)])
                self.label_plot_time_prediction.canvas.axes.plot(t_array, y_array, color = f"C{index}", alpha = 0.1)
                if y_array_env is not None:
                    self.label_plot_time_prediction.canvas.axes.plot(t_array, y_array_env, label=f"Pulse: {name},{c}", color = f"C{index}")
                index += 1
        # Plot Lifetimes of States. If the initial state is found in the energy levels, plot that one. If there is a pulse present that couples to the state, plot that too
        def lifetime(t,t0,gamma):
            values = np.exp(-gamma*(t-t0))
            values[t<t0] = 0
            return values
        lifetimes_plotted = {}
        for name,level in self.system_components["EnergyLevels"].items():
            decay_scaling = get_uv_scaled(level["DecayScaling"])
            decay_rate = get_uv_scaled(self.system_components["ConfigSystem"]["RadiativeLosses"])
            if decay_scaling == 0:
                continue
            print(f"Plotting {name} with decay_scaling {decay_scaling} and decay_rate {decay_rate}")
            decay = decay_scaling*decay_rate
            # Plot General Lifetime as dotted line
            if not lifetimes_plotted.get(name,False):
                self.label_plot_time_prediction.canvas.axes.plot(t_array, lifetime(t_array, t_array[1] , decay), label=f"General Lifetime", color = f"C{index}", linestyle = "dotted")
            lifetimes_plotted[name] = True
            for pname,pulse in self.system_components["Pulse"].items():
                if not any(name in transition for transition in pulse["CoupledTo"]):
                    continue
                current = np.zeros_like(t_array)
                for center,width in zip(pulse["Centers"],pulse["Widths"]):
                    current += lifetime(t_array, get_uv_scaled(center), decay)
                mm = np.max(current)
                current = current/mm
                self.label_plot_time_prediction.canvas.axes.plot(t_array, current, label=f"Pulse Induced: {pname}", color = f"C{index}")
            index += 1
        # Plot Detectors
        for name,detector in self.system_components["DetectorTime"].items():
            t0,t1 = get_uv_scaled(detector["t0"]), get_uv_scaled(detector["t1"])
            power = get_uv_scaled(detector["Power"])
            envelope = np.exp( -((t_array-t0) / t1)**power / 2 )
            self.label_plot_time_prediction.canvas.axes.plot(t_array, envelope, label=f"Detector: {name}", color = f"C{index}")
            index += 1
        self.label_plot_time_prediction.canvas.axes.legend()
        self.label_plot_time_prediction.canvas.draw()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())