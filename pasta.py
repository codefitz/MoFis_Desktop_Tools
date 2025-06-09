#!/usr/bin/env python3
# Pasta - One Way Super-Paste
#
# Author: Wes Moskal-Fitzpatrick
#
# Created to get around frustration of working with remote desktop
# configurations (usually Citrix) where copy and paste is disabled.
#
# Pasta uses pyautogui and keyboard to re-type text stored in the
# clipboard as you would with your human digits, only thousands of
# times faster.
#
# Change History
# --------------
# 2020-09-22 : 0.1 : WMF : Created.
# 2020-09-24 : 0.2 : WMF : Removed commented out test code.
#

import tkinter
import time
import pyautogui
import win32api
import keyboard

def countDown():
    '''start countdown seconds'''
    for k in range(3, -1, -1):
        clock["text"] = k
        time.sleep(1)
        root.update() # Tk needs this after sleep()
    clock["text"] = "Done"

root = tkinter.Tk()
root.geometry("200x100")
root.title('Pasta')
root.attributes("-topmost", True)

def submitFunction():
    global clipboard
    button.place_forget()
    countDown()
    
    # Click into window
    x, y = pyautogui.position()
    pyautogui.click(x, y)

    # "Paste"
    keyboard.write(clipboard)
    ready.set(1)

clipboard = root.clipboard_get()

clock = tkinter.Label()
clock.place(relx=.5, rely=.7, anchor="c")

ready = tkinter.IntVar()
info = tkinter.Label(text="Click 'Ready' and select the window to paste to...", wraplength=150, justify="left")
info.place(relx=.1, rely=.1)
button = tkinter.Button(root, text="Ready", command=submitFunction)
button.place(relx=.5, rely=.7, anchor="c")

root.wait_variable(ready)
