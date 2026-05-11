from pynput import keyboard
import sys

def on_press(key):
    try:
        print(f"{key.char} was pressed")
    except AttributeError:
        pass
    sys.stdout.write('\b \b')
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()