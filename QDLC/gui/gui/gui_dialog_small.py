from .ui_confirm_reject_form_small import Ui_Dialog
from .ui_input_form import Ui_InputDialog
from PySide6.QtWidgets import QDialog

class DialogSmall(QDialog, Ui_Dialog):
    def __init__(self, *args, main_window=None, **kwargs):
        super(DialogSmall, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.retranslateUi(self)
        def finished():
            self.accept()
        def cancel():
            self.reject()

        self.button_confirm.clicked.connect(finished)
        self.button_cancel.clicked.connect(cancel)
        self.exec()

class InputDialogSmall(QDialog, Ui_InputDialog):
    def __init__(self, *args, main_window=None, callback = None, **kwargs):
        super(InputDialogSmall, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.retranslateUi(self)
        def finished():
            if callback is not None:
                callback(self.input.text())
            self.accept()
        def cancel():
            self.input.setText("")
            self.reject()

        self.button_confirm.clicked.connect(finished)
        self.button_cancel.clicked.connect(cancel)
        self.exec()
        
if __name__ == "__main__":
    print(f"This file ({__file__}) is part of the QDaCC GUI and should be imported, not executed.")