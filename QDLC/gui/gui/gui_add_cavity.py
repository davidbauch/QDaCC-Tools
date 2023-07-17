from .ui_add_cavity import Ui_AddCavity
from PySide6.QtWidgets import QDialog
from .dialogs import getCheckedItems

class DialogAddCavity(QDialog, Ui_AddCavity):
    def __init__(self, *args, main_window=None, load_existing = None, style_sheet = "", **kwargs):
        super(DialogAddCavity, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.retranslateUi(self)
        self.setStyleSheet(style_sheet)
        self.name_when_loaded = None
        def finished(replace=False):
            name = self.textinput_name.text()
            energy = self.textinput_energy.text()
            transitions = tuple(self.textinput_transitions.text().split(","))
            transition_scaling = ([a for a in self.textinput_transition_scalings.text().split(",")])
            decay = self.textinput_decay.text()
            photonnumber = self.textinput_photonnumber.text()
            if replace:
                main_window.system_components["CavityLevels"].pop(self.name_when_loaded)
            main_window.addCavity({"Name": name, "Energy": energy, "CoupledTo": transitions, "CoupledToScalings": transition_scaling, "DecayScaling": decay, "PhotonNumber": photonnumber}, replaced=self.name_when_loaded if replace else None)
            main_window.drawSystem()
        def set_scalings():
            self.textinput_transition_scalings.setText(",".join(["1" for _ in self.textinput_transitions.text().split(",")]))
        def reset():
            for t in [self.textinput_name, self.textinput_energy, self.textinput_transitions, self.textinput_transition_scalings, self.textinput_decay, self.textinput_photonnumber]:
                t.setText("")
        def load():
            level = self.textinput_name.text()
            self.name_when_loaded = level
            if level not in main_window.system_components["CavityLevels"]:
                main_window.sendErrorMessage("No Exist Error","A Cavity with this name does not exist!")
                return
            level = main_window.system_components["CavityLevels"][level]
            self.textinput_energy.setText( level["Energy"] ) 
            self.textinput_transitions.setText( ",".join(level["CoupledTo"]) ) 
            self.textinput_transition_scalings.setText( ",".join(level["CoupledToScalings"]) )
            self.textinput_decay.setText( level["DecayScaling"] ) 
            self.textinput_photonnumber.setText( level["PhotonNumber"] ) 
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
        self.button_confirm.clicked.connect(finished)
        self.button_confirm_replace.clicked.connect(lambda: finished(replace=True))
        self.button_setone.clicked.connect(set_scalings)
        self.button_reset.clicked.connect(reset)
        self.button_load.clicked.connect(load)
        if load_existing is not None:
            self.textinput_name.setText(load_existing)
            load()
        self.exec()
        
if __name__ == "__main__":
    print(f"This file ({__file__}) is part of the QDaCC GUI and should be imported, not executed.")