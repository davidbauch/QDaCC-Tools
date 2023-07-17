from .ui_grid_and_tolerance import Ui_AddGridTolerance
from PySide6.QtWidgets import QDialog
import numpy as np
from .unit_seperator import get_uv_scaled

class DialogAddGridOrTolerance(QDialog, Ui_AddGridTolerance):
    def __init__(self, *args, main_window=None, name = "Grid", style_sheet = "", **kwargs):
        super(DialogAddGridOrTolerance, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.retranslateUi(self)
        self.setStyleSheet(style_sheet)
        self.label_2.setText(self.label_2.text().replace("Title",f"Configure {name}"))
        # Load Existing Grid or Tolerances on creation:
        if f"Config{name}" in main_window.system_components:
            c = main_window.system_components[f"Config{name}"]
            if "Time" in c and "Value" in c:
                print(f"Loading Existing {name} configuration.")
                self.textinput_time.setText(",".join(c["Time"]))
                self.textinput_value.setText(",".join(c["Value"]))
        def finished():
            #main_window.addShift({"Name": name, "CoupledTo": states, "CoupledToScalings": state_couplings, "Amplitudes" : tuple(a for t,a in self.vector), "Times": tuple(t for t,a in self.vector), "Type" : shift_type})
            time = self.textinput_time.text().split(",")
            values = self.textinput_value.text().split(",")
            if len(time) == len(values) and len(time) > 0:
                print(f"Setting new {name} with length {len(time)}")
                main_window.system_components[f"Config{name}"]["Time"] = time
                main_window.system_components[f"Config{name}"]["Value"] = values
        def reset():
            for t in [self.textinput_time, self.textinput_value]:
                t.setText("")
        def plot():
            # Get Time From timeconfig if checkbox is checked, else use bare minimum
            times = [get_uv_scaled(t) for t in self.textinput_time.text().split(",")]
            values = [get_uv_scaled(t) for t in self.textinput_value.text().split(",")]
            if self.input_use_timeconfig.isChecked() and main_window.textinput_time_endtime.text() != "auto":
                t0,t1 = get_uv_scaled(main_window.textinput_time_startingtime.text()), get_uv_scaled(main_window.textinput_time_endtime.text())
            else:
                t0 = min(times)
                t1 = max(times)
            # Change values to represent stair function
            if t0 < min(times):
                times.insert(0,t0)
                values.insert(0,values[0])
            if t1 > max(times):
                times.append(t0)
                values.append(values[0])
            times = sum([[a,b] for a,b in zip(times,times)],list())[:-2]
            values = sum([[a,b] for a,b in zip(values[:-1],values[1:])],list())
            self.plot_points.canvas.axes.clear()
            self.plot_points.canvas.axes.plot(times,values)
            ##self.plot_points.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
            ##self.plot_points.canvas.axes.set_title('Cosinus - Sinus Signals')
            self.plot_points.canvas.draw()
        self.button_plot.clicked.connect(plot)
        self.button_confirm.clicked.connect(finished)
        self.button_reset.clicked.connect(reset)
        self.exec()
        
if __name__ == "__main__":
    print(f"This file ({__file__}) is part of the QDaCC GUI and should be imported, not executed.")