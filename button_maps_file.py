
from pynput.keyboard import Key
from pynput.mouse import Button

button_mapping_1 = {
    "2": "a",
    "3": "w",
    "4": "s",
    "5": "d",
    "6": "e",
    "7": "f",
    "8": "shift_controls"
}

button_mapping_2 = {
    "2": "m_left",
    "3": "m_up",
    "4": "m_down",
    "5": "m_right",
    "6": Button.left,
    "7": Button.right,
    "8": "shift_controls"
}

button_mapping_gd = {
    "2": "hold_long",
    "3": "hold_short",
    "4": "hold_short",
    "5": "hold_long",
    "6": Key.up,
    "7": Key.up,
    "8": Key.up
}
