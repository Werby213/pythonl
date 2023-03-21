import pyautogui
import time
import cv2
import numpy as np
counter = 0
delay = 0.  # seconds
x, y, width, height = 500, 360, 200, 50  # coordinates of he monitoring area
time.sleep(5)
while True:
    # convert the integer to a string and get its length
    num_str = str(counter)
    num_len = len(num_str)

    pyautogui.typewrite(num_str)
    # press 'backspace' key num_len times
    for i in range(num_len):
        pyautogui.press('backspace')
    counter += 1
    time.sleep(delay)

    # monitoring area on the screen
    img = pyautogui.screenshot()
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 255), 2)
    cv2.imshow("screenshot", img)
    cv2.waitKey(1)
    if pyautogui.pixelMatchesColor(x, y, (100, 100, 14)):
        print("color changed")
        break

cv2.destroyAllWindows()
