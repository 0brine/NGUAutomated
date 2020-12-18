import pyautogui
import cv2 as cv
import numpy as np
from Button import Button
import time

print(pyautogui.size())

pimg = pyautogui.screenshot()
print(pimg)

open_cv_image = np.array(pimg)

# Convert RGB to BGR
open_cv_image = open_cv_image[:, :, ::-1].copy()

temp1 = list(pyautogui.locateAllOnScreen('res/buOffensive.PNG'))
temp2 = list(pyautogui.locateAllOnScreen('res/buDefensive.PNG'))
temp3 = list(pyautogui.locateAllOnScreen('res/buMisc.PNG'))

print(len(temp1))
print(len(temp2))
print(len(temp3))

offensivButtons = []
defensivButtons = []
miscButtons = []

for b in temp1:
    offensivButtons.append(Button(b.left, b.top, b.width, b.height))

for b in temp2:
    defensivButtons.append(Button(b.left, b.top, b.width, b.height))

for b in temp3:
    miscButtons.append(Button(b.left, b.top, b.width, b.height))

offensivButtons[1].click()

while True:
    time.sleep(0.02)
    if not offensivButtons[1].is_on_cooldown():
        offensivButtons[1].click()


print("end")
