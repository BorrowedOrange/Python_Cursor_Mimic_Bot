# Python_Cursor_Mimic_Bot
Mouse Gesture Bot
This is a Python script that allows you to record and execute mouse gestures using the PyAutoGUI library.

Requirements
Python 3.x
PyAutoGUI library (you can install it using pip install pyautogui)
Usage
To record a mouse gesture:

Run the script using python mouse_gesture_bot.py.
Move the mouse to record the desired gesture.
Click the mouse to perform clicks during the gesture (optional).
Press the esc key to stop recording the gesture.
To execute a recorded gesture:

Open the mouse_gesture_bot.py script in a text editor.
Copy the recorded gesture from the gesture list in the script.
Paste the gesture as an argument to the do_gesture() function in the script.
Run the script using python mouse_gesture_bot.py.
Note: The do_gesture() function assumes that the recorded gesture only contains mouse movements and clicks. If the recorded gesture also includes other keyboard or mouse events, you will need to modify the function accordingly.

Disclaimer
Please use this script responsibly and ethically. Do not use it to automate tasks that may violate the terms of service of any software or website. The author of this script is not responsible for any damages or legal issues caused by its use.