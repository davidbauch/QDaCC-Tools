from .ui_add_pulse import Ui_AddPulse
from PySide6.QtWidgets import QDialog
import numpy as np
from .unit_seperator import get_uv_scaled
from .dialogs import getCheckedItems

class DialogAddPulse(QDialog, Ui_AddPulse):
    def __init__(self, *args, main_window=None, load_existing = None, style_sheet = "", **kwargs):
        super(DialogAddPulse, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.retranslateUi(self)
        self.setStyleSheet(style_sheet)
        def finished(replace=False):
            name = self.textinput_name.text()
            transitions = tuple(self.textinput_transitions.text().split(","))
            amp = tuple(self.textinput_amp.text().split(","))
            freq = tuple(self.textinput_energy.text().split(","))
            t0 = tuple(self.textinput_center.text().split(","))
            width = tuple(self.textinput_width.text().split(","))
            pulse_type = tuple(self.textinput_type.text().split(","))
            if replace:
                main_window.system_components["Pulse"].pop(self.name_when_loaded)
            main_window.addPulse({"Name": name, "CoupledTo": transitions, "Amplitudes" : amp, "Frequencies" : freq, "Centers": t0, "Widths": width, "Type" : pulse_type})
            main_window.drawSystem()
        def reset():
            for t in [self.textinput_name, self.textinput_energy, self.textinput_transitions, self.textinput_amp, self.textinput_center, self.textinput_width]:
                t.setText("")
            for t,u in zip([self.textinput_energy_unit, self.textinput_amp_unit, self.textinput_center_unit, self.textinput_width_unit],["eV","pi","ps","ps"]):
                t.setText(u)
            self.textinput_type.setText("")
        def plot():
            # Get Time From timeconfig if checkbox is checked, else use bare minimum
            widths = [get_uv_scaled(t) for t in self.textinput_width.text().split(",")]
            centers = [get_uv_scaled(t) for t in self.textinput_center.text().split(",")]
            amps = [get_uv_scaled(t) for t in self.textinput_amp.text().split(",")]
            freqs = [get_uv_scaled(t) for t in self.textinput_energy.text().split(",")]
            types = self.textinput_type.text().split(",")
            if self.input_use_timeconfig.isChecked() and main_window.textinput_time_endtime.text() != "auto":
                t0,t1 = get_uv_scaled(main_window.textinput_time_startingtime.text()), get_uv_scaled(main_window.textinput_time_endtime.text())
            else:
                margin = max( widths )
                t0 = min( centers ) - 5*margin
                t1 = max( centers ) + 5*margin
            t = np.linspace(t0,t1,500)
            self.plot_pulse.canvas.axes.clear()
            max_freq = max(freqs)
            for i,(a,f,c,w,type) in enumerate(zip( amps, freqs, centers, widths, types )):
                madeup_freq = 4*3.1415*10/(t1-t0) * f/max_freq
                if type == "cw":                    
                    y = a*np.sin(madeup_freq*(t-c) + w)
                else:
                    phase = 0 if not "phase" in type else float(type.split("phase(")[-1].split(")")[0])
                    exponent = 2 if not "exponent" in type else int(type.split("exponent(")[-1].split(")")[0])
                    if exponent % 2 != 0:
                        print(f"The pulse exponent should be even! You picked {exponent}. Pick {exponent-1} or {exponent+1} instead!")
                    y = a*np.exp( -(t-c)**exponent / w**exponent / 2 )
                    y2 = y*np.sin(madeup_freq*(t-c) + 3.1415*phase)
                    self.plot_pulse.canvas.axes.plot(t,y2,color=f"C{i}")
                self.plot_pulse.canvas.axes.plot(t,y,color=f"C{i}")
            #self.plot_pulse.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
            #self.plot_pulse.canvas.axes.set_title('Cosinus - Sinus Signals')
            self.plot_pulse.canvas.draw()
            
        def load():
            name = self.textinput_name.text()
            self.name_when_loaded = name
            if name not in main_window.system_components["Pulse"]:
                main_window.sendErrorMessage("No Exist Error","A Pulse with this name does not exist!")
                return
            pulse = main_window.system_components["Pulse"][name]
            self.textinput_transitions.setText( ",".join(pulse["CoupledTo"]) )
            self.textinput_amp.setText( ",".join(pulse["Amplitudes"] )) 
            self.textinput_center.setText( ",".join(pulse["Centers"] )) 
            self.textinput_energy.setText( ",".join(pulse["Frequencies"] )) 
            self.textinput_name.setText( pulse["Name"] ) 
            self.textinput_type.setText( ",".join(pulse["Type"]) ) 
            self.textinput_width.setText( ",".join(pulse["Widths"] )) 
            plot()
        def pick_states():
            states = main_window.generate_list_of_available_electronic_transitions() + main_window.generate_list_of_available_cavity_states()
            checked_items, ok = getCheckedItems(states, parent=self)
            if not ok:
                return
            current_states = self.textinput_transitions.text().split(",")
            new_states = ",".join(checked_items+current_states)
            # Prune final ","
            if new_states.endswith(","):
                new_states = new_states[:-1]
            self.textinput_transitions.setText(new_states)
        self.button_coupled_to.clicked.connect(pick_states)
        
        self.button_plot.clicked.connect(plot)
        self.button_confirm.clicked.connect(finished)
        self.button_confirm_replace.clicked.connect(lambda: finished(replace=True))
        self.button_reset.clicked.connect(reset)
        self.button_load.clicked.connect(load)
        if load_existing is not None:
            self.textinput_name.setText(load_existing)
            load()
        self.exec()
        
if __name__ == "__main__":
    print(f"This file ({__file__}) is part of the QDaCC GUI and should be imported, not executed.")