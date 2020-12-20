from pynput import keyboard
from pynput.keyboard import Controller

COMBINATION = {keyboard.Key.alt_r, keyboard.Key.shift_r}
current = set()


def on_press(key):
    if key in COMBINATION:
        current.add(key)
        if all(k in current for k in COMBINATION):
            controller = Controller()
            controller.press(keyboard.Key.alt)
            controller.release(keyboard.Key.alt)
            controller.press(keyboard.Key.shift)
            controller.release(keyboard.Key.shift)
    if key == keyboard.Key.esc:
        listener.stop()


def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
