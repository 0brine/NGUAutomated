import pyautogui
import cv2 as cv
import numpy as np
import time
from Button import Button

print(pyautogui.size())

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

priorityOrder = [defensivButtons[5], defensivButtons[3], defensivButtons[4], offensivButtons[5], offensivButtons[4],
                 offensivButtons[2], miscButtons[0], defensivButtons[2], miscButtons[1], offensivButtons[1]]

while True:
    time.sleep(0.02)
    for bu in priorityOrder:
        if not bu.is_on_cooldown():
            bu.click()
            break

print("end")
