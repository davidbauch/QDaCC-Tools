import re
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

ansi_escape = re.compile(r'\x1b\[([\d;]+)m')

def replace_ansi_escape_sequences(text):
    """Replace ANSI escape sequences with their PyQt counterparts."""
    text = ansi_escape.sub(lambda match: _translate_ansi_escape_sequence(match.group(1)), text)
    return text

def _translate_ansi_escape_sequence(sequence):
    """Translate an individual ANSI escape sequence to its PyQt counterpart."""
    codes = [int(code) for code in sequence.split(';')]
    fg_color, bg_color, bold, underline = Qt.black, Qt.white, False, False
    for code in codes:
        if code == 0:  # reset
            fg_color, bg_color, bold, underline = Qt.black, Qt.white, False, False
        elif code == 1:  # bold
            bold = True
        elif code == 4:  # underline
            underline = True
        elif code == 30:  # black fg
            fg_color = Qt.black
        elif code == 31:  # red fg
            fg_color = Qt.red
        elif code == 32:  # green fg
            fg_color = Qt.green
        elif code == 33:  # yellow fg
            fg_color = Qt.yellow
        elif code == 34:  # blue fg
            fg_color = Qt.blue
        elif code == 35:  # magenta fg
            fg_color = Qt.magenta
        elif code == 36:  # cyan fg
            fg_color = Qt.cyan
        elif code == 37:  # white fg
            fg_color = Qt.white
        elif code == 40:  # black bg
            bg_color = Qt.black
        elif code == 41:  # red bg
            bg_color = Qt.red
        elif code == 42:  # green bg
            bg_color = Qt.green
        elif code == 43:  # yellow bg
            bg_color = Qt.yellow
        elif code == 44:  # blue bg
            bg_color = Qt.blue
        elif code == 45:  # magenta bg
            bg_color = Qt.magenta
        elif code == 46:  # cyan bg
            bg_color = Qt.cyan
        elif code == 47:  # white bg
            bg_color = Qt.white
    # Build the PyQt style sheet for the given formatting options
    style_sheet = "color: {}; background-color: {};".format(fg_color, bg_color)
    if bold:
        style_sheet += " font-weight: bold;"
    if underline:
        style_sheet += " text-decoration: underline;"
    # parse carriage return
    if sequence == '0m\r':
        return "</span><br>"
    return "<span style='{}'>".format(style_sheet)

if __name__ == "__main__":
    # Test the ANSI escape sequence parser
    text = "This is \x1b[31mred\x1b[0m and this is \x1b[32mgreen\x1b[0m."
    print(text)
    print(replace_ansi_escape_sequences(text))