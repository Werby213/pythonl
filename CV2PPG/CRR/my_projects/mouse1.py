import pyautogui
import keyboard
def on_press(key):
    if key == keyboard.Key.f8:
        print("Start Recording")
        pyautogui.mouseDown()
    elif key == keyboard.Key.f9:
        print("Stop Recording")
        pyautogui.mouseUp()

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
