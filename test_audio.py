from pynput.keyboard import Key, Controller

keyboard = Controller()

# Press and release space
keyboard.press(Key.space)
print("Space presses")
keyboard.release(Key.space)
print("Space release")
   