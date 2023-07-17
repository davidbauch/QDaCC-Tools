from .ui_add_fitness_function import Ui_AddFitnessFunction
from PySide6.QtWidgets import QDialog
import numpy as np
import scipy as sp
from .unit_seperator import get_uv_scaled, get_unit_value

class DialogAddFitness(QDialog, Ui_AddFitnessFunction):
    def __init__(self, *args, main_window=None, load_existing = None, style_sheet = "", **kwargs):
        super(DialogAddFitness, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.retranslateUi(self)
        self.setStyleSheet(style_sheet)

        self.variables = main_window.system_components.get("OptimizerFitnessVariables", {"V1": "","V2": "","V3": "","V4": "","V5": "" })
        self.textbrowser_current_fitness_function.setPlainText(main_window.textinput_optimizer_fitnessfunction.text())
        self.textinput_variable.textChanged.connect(lambda: self.variables.update({self.combo_variable.currentText() : self.textinput_variable.text()}))
        self.combo_variable.currentIndexChanged.connect(lambda: self.textinput_variable.setText(self.variables[self.combo_variable.currentText()] if self.combo_variable.currentText() in self.variables else ""))
        self.textinput_variable.setText(self.variables.get("V1",""))

        self.button_confirm.clicked.connect(lambda: main_window.textinput_optimizer_fitnessfunction.setText(self.textbrowser_current_fitness_function.toPlainText()))

        def try_eval(field, resfield):
            text = field.text()
            try:
                res = eval(text)
                resfield.setText(str(res))
            except Exception as e:
                resfield.setText("Cannot Evaluate this Variable here.")

        self.textinput_variable.textChanged.connect(lambda: try_eval(self.textinput_variable, self.textinput_variable_display))

        def finished():
            main_window.system_components["OptimizerFitnessVariables"] = self.variables

        self.button_confirm.clicked.connect(finished)
        self.exec()
        
if __name__ == "__main__":
    print(f"This file ({__file__}) is part of the QDaCC GUI and should be imported, not executed.")