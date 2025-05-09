
import serial
import time
from pynput.keyboard import Key, Controller as keyboard_controller
from pynput.mouse import Button, Controller as mouse_controller
import button_maps_file as bm

keyboard = keyboard_controller()
mouse = mouse_controller()
ser = serial.Serial("COM3", 9600, timeout=0.01)

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

# ===================== manually swap button_maps =====================
controls = [bm.button_mapping_gd]

current_control_set = 0
mouse_move_inst = ["m_up", "m_down", "m_left", "m_right"]
mouse_click_inst = [Button.left, Button.right]
complex_inst = ["hold_long", "hold_short", "shift_controls"] + mouse_move_inst + mouse_click_inst

print("on COM3")

while True:

    code = ser.readline().decode("utf-8").strip()
    line = list(code)

    for k in holding:
        if k in line:
            if not holding[k]:
                holding[k] = True
                print(f"pressed {key_labels[k]}")
                if controls[current_control_set][k] not in complex_inst:
                    keyboard.press(controls[current_control_set][k])

                elif controls[current_control_set][k] == "shift_controls":
                    current_control_set += 1
                    if current_control_set > len(controls):
                        current_control_set = 0

                elif controls[current_control_set][k] in mouse_move_inst:
                    if controls[current_control_set][k] == "m_up":
                        mouse.move(0, -10)
                    elif controls[current_control_set][k] == "m_down":
                        mouse.move(0, 10)
                    elif controls[current_control_set][k] == "m_left":
                        mouse.move(-10, 0)
                    elif controls[current_control_set][k] == "m_right":
                        mouse.move(10, 0)

                elif controls[current_control_set][k] in mouse_click_inst:
                    if controls[current_control_set][k] == Button.left:
                        mouse.press(controls[current_control_set][k])
                    elif controls[current_control_set][k] == Button.right:
                        mouse.press(controls[current_control_set][k])


                else:
                    keyboard.press(Key.up)

        else:
            if holding[k]:
                holding[k] = False
                print(f"released {key_labels[k]}")
                if controls[current_control_set][k] not in complex_inst:
                    keyboard.release(controls[current_control_set][k])

                elif controls[current_control_set][k] in mouse_click_inst:
                    if controls[current_control_set][k] == Button.left:
                        mouse.release(controls[current_control_set][k])
                    elif controls[current_control_set][k] == Button.right:
                        mouse.release(controls[current_control_set][k])


                elif controls[current_control_set][k] == "hold_long":
                    time.sleep(0.75)
                    keyboard.release(Key.up)
                else:
                    time.sleep(0.25)
                    keyboard.release(Key.up)


    # end of loop
