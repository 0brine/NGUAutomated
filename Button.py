import pyautogui


class Button:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __init__(self, x, y, w, h):
        self.x = int(x + w)
        self.y = int(y + h / 2)
        self.active = False
        self.onCooldown = False

    def click(self):
        pyautogui.click(x=self.x, y=self.y)

    def is_on_cooldown(self):
        pix = pyautogui.pixel(self.x, self.y)
        return pix in [(124, 78, 78), (51, 68, 82), (98, 74, 74)]
