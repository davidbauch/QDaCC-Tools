from .ui_add_chirp import Ui_AddChirp
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QStandardItem, QStandardItemModel
import numpy as np
from .unit_seperator import get_uv_scaled
from .dialogs import getCheckedItems

class DialogAddChirp(QDialog, Ui_AddChirp):
    def __init__(self, *args, main_window=None, load_existing = None, style_sheet = "", **kwargs):
        super(DialogAddChirp, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.retranslateUi(self)
        self.vector = []
        self.setStyleSheet(style_sheet)
        self.listView.setModel(QStandardItemModel())
        def finished(replace=False):
            name = self.textinput_name.text()
            states = tuple(self.textinput_states.text().split(","))
            state_couplings = tuple(self.textinput_state_couplings.text().split(","))
            shift_type = self.textinput_type.text()
            if replace:
                main_window.system_components["Shift"].pop(self.name_when_loaded)
                self.name_when_loaded = self.textinput_name.text()
            main_window.addShift({"Name": name, "CoupledTo": states, "CoupledToScalings": state_couplings, "Amplitudes" : tuple(a for t,a in self.vector), "Times": tuple(t for t,a in self.vector), "Type" : shift_type})
            main_window.drawSystem()
        def reset():
            for t in [self.textinput_name, self.textinput_states, self.textinput_time, self.textinput_energy, self.textinput_state_couplings]:
                t.setText("")
            self.vector = []
            self.textinput_type.setText("monotone")
            set_list()
        def load():
            name = self.textinput_name.text()
            self.name_when_loaded = name
            if name not in main_window.system_components["Shift"]:
                main_window.sendErrorMessage("No Exist Error","A Shift with this name does not exist!")
                return
            shift = main_window.system_components["Shift"][name]
            self.textinput_states.setText(",".join(shift["CoupledTo"]))
            self.textinput_state_couplings.setText(",".join(shift["CoupledToScalings"]))
            self.textinput_type.setText(shift["Type"])
            for t,p in zip(shift["Times"], shift["Amplitudes"]):
                self.vector.append((t,p))
            set_list()
        def set_list():
            model = self.listView.model()
            model.clear()
            for t,p in self.vector:
                item = QStandardItem("At {}: {}".format(t,p))
                model.appendRow(item)
        def add():
            times = self.textinput_time.text().split(",")
            amps = self.textinput_energy.text().split(",")
            for t,a in zip(times,amps):
                if (t,a) in self.vector:
                    self.vector.remove((t,a))
                self.vector.append((t,a))
            self.vector.sort(key=lambda tup: get_uv_scaled(tup[0]))
            self.textinput_time.setText("")
            self.textinput_energy.setText("")
            set_list()
        def remove_points():
            #times = self.textinput_time.text().split(",")
            #amps = self.textinput_energy.text().split(",")
            index = self.listView.currentIndex()
            t,p = index.data().replace("At ","").split(": ")
            if (t,p) in self.vector:
                self.vector.remove((t,p))
            self.vector.sort(key=lambda tup: tup[0])
            set_list()
        def set_scalings():
            self.textinput_state_couplings.setText(",".join(["1" for _ in self.textinput_states.text().split(",")]))
        def plot():
            # Get Time From timeconfig if checkbox is checked, else use bare minimum
            times = [get_uv_scaled(t) for t,a in self.vector]
            amps = [get_uv_scaled(a) for t,a in self.vector]
            ctype = self.textinput_type.text()
            if ctype == "monotone"  or ctype == "hermite":
                if ctype == "hermite":
                    from scipy.interpolate import CubicHermiteSpline as interpolator
                    f = interpolator(times, amps, dydx=np.zeros_like(times))
                else:
                    from scipy.interpolate import PchipInterpolator as interpolator
                    f = interpolator(times, amps)
                times = np.linspace(min(times), max(times), 100)
                amps = f(times)
            if self.input_use_timeconfig.isChecked() and main_window.textinput_time_endtime.text() != "auto":
                t0,t1 = get_uv_scaled(main_window.textinput_time_startingtime.text()), get_uv_scaled(main_window.textinput_time_endtime.text())
            else:
                t0 = min(times)
                t1 = max(times)
            self.plot_chirp.canvas.axes.clear()
            self.plot_chirp.canvas.axes.plot(times,amps)
            #self.plot_chirp.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
            #self.plot_chirp.canvas.axes.set_title('Cosinus - Sinus Signals')
            self.plot_chirp.canvas.draw()
        def pick_states():
            states = main_window.generate_list_of_available_electronic_states() + main_window.generate_list_of_available_cavity_states()
            checked_items, ok = getCheckedItems(states, parent=self)
            if not ok:
                return
            current_states = self.textinput_states.text().split(",")
            new_states = ",".join(checked_items+current_states)
            # Prune final ","
            if new_states.endswith(","):
                new_states = new_states[:-1]
            self.textinput_states.setText(new_states)
        self.button_coupled_to.clicked.connect(pick_states)
        self.button_plot.clicked.connect(plot)
        self.button_confirm.clicked.connect(finished)
        self.button_confirm_replace.clicked.connect(lambda: finished(replace=True))
        self.button_reset.clicked.connect(reset)
        self.button_load.clicked.connect(load)
        self.button_add.clicked.connect(add)
        self.button_remove_points.clicked.connect(remove_points)
        self.button_setone.clicked.connect(set_scalings)
        if load_existing is not None:
            self.textinput_name.setText(load_existing)
            load()
        self.exec()
        
if __name__ == "__main__":
    print(f"This file ({__file__}) is part of the QDaCC GUI and should be imported, not executed.")