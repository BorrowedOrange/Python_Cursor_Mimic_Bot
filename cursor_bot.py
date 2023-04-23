import pyautogui
# Make sure you have Python (3.x) installed
# 'x' is just the release version
# Install PyAutoGUI library by using using :pip install pyautogui
gesture = []

def record_gesture():
    while True:
        current_pos = pyautogui.position()
        click = pyautogui.mouseDown()  # check if user is clicking
        if click:
            pyautogui.mouseUp()  # release the mouse button
            continue  # skip this iteration and restart the loop
        gesture.append(current_pos)
        if pyautogui.press('esc'):  # check if the user pressed the esc key
            break  # exit the loop

def do_gesture(gesture):
    for pos in gesture:
        pyautogui.moveTo(pos[0], pos[1])
        pyautogui.click()

record_gesture()  # record the gesture
do_gesture(gesture)  # execute the gesture