
import serial
import time
from pynput.keyboard import Controller
from pynput.keyboard import Key

keyboard = Controller()
ser = serial.Serial("COM3", 9600, timeout=0.01)
tick = 0

holding = {
    "2": False,
    "3": False,
    "4": False,
    "5": False,
    "6": False,
    "7": False,
    "8": False
}

key_labels = {
    "2": "top right",
    "3": "bottom right",
    "4": "bottom left",
    "5": "top left",
    "6": "middle right",
    "7": "middle left",
    "8": "middle"
}

button_mapping = {
    "2": "hold",
    "3": "hold",
    "4": "hold",
    "5": "hold",
    "6": Key.up,
    "7": Key.up,
    "8": Key.up
}

print("on COM3")

while True:
    tick += 1

    code = ser.readline().decode("utf-8").strip()
    line = list(code)

    for k in holding:
        if k in line:
            if not holding[k]:
                holding[k] = True
                print(f"pressed {key_labels[k]}")
                if button_mapping[k] != "hold":
                    keyboard.press(button_mapping[k])
                else:
                    keyboard.press(Key.up)
        else:
            if holding[k]:
                holding[k] = False
                print(f"released {key_labels[k]}")
                if button_mapping[k] != "hold":
                    keyboard.release(button_mapping[k])
                else:
                    time.sleep(0.5)
                    keyboard.release(Key.up)


    # end of loop
