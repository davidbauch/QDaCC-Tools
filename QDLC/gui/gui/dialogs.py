from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QCheckBox, QDialogButtonBox, QLabel
from PySide6.QtCore import QObject

def getCheckedItems(items: list[str], parent = None) -> tuple[list[str],bool] | tuple[None,bool]:
    #checked_items, ok = getGeneralItems(items, [None for _ in items], [QCheckBox for _ in items], parent=parent)
    checked_items, ok = getGeneralItems([{ "Type" : QCheckBox, "Text" : item} for item in items], parent=parent)
    if checked_items is None or not ok:
        return None, False
    return [list_item for (list_item,checked_item) in zip(items,checked_items) if checked_item ], True

from PySide6.QtWidgets import QDialog, QVBoxLayout, QGridLayout, QCheckBox, QDialogButtonBox, QLabel

def getGeneralItems(items: list[dict], parent=None) -> tuple[list[str | bool], bool] | tuple[None, bool]:
    if not len(items):
        return None, False
    dialog = QDialog()
    if parent:
        dialog.setStyleSheet(parent.styleSheet())
    layout = QVBoxLayout(dialog)
    content = []
    grid_layout = QGridLayout()
    row = 0
    col = 0
    for item in items:
        if not "Type" in item:
            continue
        q_item = item["Type"]()
        if "PHText" in item:
            q_item.setPlaceholderText(item["PHText"])
        if "Text" in item:
            q_item.setText(item["Text"])
        if "Checked" in item:
            q_item.setChecked(item["Checked"])
        if "Title" in item:
            q_title = QLabel(item["Title"])
            grid_layout.addWidget(q_title, row, col)
            row += 1
        grid_layout.addWidget(q_item, row, col)
        row += 1
        if row >= 10:
            row = 0
            col += 1
        content.append(q_item)
    layout.addLayout(grid_layout)
    button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    layout.addWidget(button_box)
    button_box.accepted.connect(dialog.accept)
    button_box.rejected.connect(dialog.reject)
    if dialog.exec_() == QDialog.Accepted:
        return [item.isChecked() if isinstance(item, QCheckBox) else item.text() for item in content], True
    return None, False