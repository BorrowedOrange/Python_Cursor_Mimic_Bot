# Python Cursor Mimicing Bot
Mouse Gesture Bot
This is a Python script that allows you to record and execute mouse gestures using the PyAutoGUI library.

**Requirements**<br>
Python 3.x
PyAutoGUI library (you can install it using pip install pyautogui)

Usage
To record a mouse gesture:

1.Run the script using python mouse_gesture_bot.py.
2.Move the mouse to record the desired gesture.
3.Click the mouse to perform clicks during the gesture (optional).
4.Press the esc key to stop recording the gesture.

To execute a recorded gesture:

1.Open the mouse_gesture_bot.py script in a text editor.
2.Copy the recorded gesture from the gesture list in the script.
3.Paste the gesture as an argument to the do_gesture() function in the script.
4.Run the script using python mouse_gesture_bot.py.

Note: The do_gesture() function assumes that the recorded gesture only contains mouse movements and clicks. If the recorded gesture also includes other keyboard or mouse events, you will need to modify the function accordingly.

Disclaimer
Please use this script responsibly and ethically. Do not use it to automate tasks that may violate the terms of service of any software or website. The author of this script is not responsible for any damages or legal issues caused by its use.
