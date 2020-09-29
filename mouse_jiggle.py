# Mouse Jiggle
#
# Author: Wes Moskal-Fitzpatrick
#
# Jiggle the mouse a little bit and prevent remote desktop logout.
#

import pyautogui

while True:
    pyautogui.moveRel(5,0, duration=0)
    #pyautogui.moveRel(0,5, duration=0.25)
    pyautogui.PAUSE = 0.5
    pyautogui.moveRel(-5,0, duration=0)
    #pyautogui.moveRel(0,-5, duration=0.25)
    #pyautogui.click()
    pyautogui.press('shift')