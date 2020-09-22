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
# 2020-09-22 : 0.1 : WMF : Created. Ignore the comments.
#

import tkinter
import time
import pyautogui
import win32api
import keyboard

def countDown():
    '''start countdown seconds'''
    #clock.config(bg='yellow')
    for k in range(3, -1, -1):
        clock["text"] = k
        time.sleep(1)
        root.update() # Tk needs this after sleep()
    # clock.config(bg='red')
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
    # Special Characters
    #clipboard = clipboard.replace("#", "\#")
    # Paste / Type
    
    #print(clipboard)
    #pyautogui.typewrite(clipboard)
    #print(pyautogui._pyautogui_win.keyboardMapping['@'])
    #print()
    #pyautogui.platformModule.keyboardMapping['#'] = 478
    #print(pyautogui._pyautogui_win.keyboardMapping['~'])
    
    #default_layout = win32api.GetKeyboardLayout()
    #print (default_layout)
    #print (hex(default_layout))
    
    #win32api.LoadKeyboardLayout('00000409',1) # to switch to US english
    #print (win32api.GetKeyboardLayout())
    #win32api.LoadKeyboardLayout(default_layout,1) # switch back
    #print (win32api.GetKeyboardLayout())
    
    #pyautogui.typewrite("###")
    keyboard.write(clipboard)
    ready.set(1)
    #root.destroy()

# label_font = ('helvetica', 40)
# clock = tkinter.Label(font=label_font)

clipboard = root.clipboard_get()

clock = tkinter.Label()
clock.place(relx=.5, rely=.7, anchor="c")

ready = tkinter.IntVar()
info = tkinter.Label(text="Click 'Ready' and select the window to paste to...", wraplength=150, justify="left")
info.place(relx=.1, rely=.1)
button = tkinter.Button(root, text="Ready", command=submitFunction)
button.place(relx=.5, rely=.7, anchor="c")

root.wait_variable(ready)

# root.mainloop()

#--------

#B1 = tkinter.Button(root, text ="circle",  cursor="circle")
#B2 = tkinter.Button(root, text ="plus",  cursor="plus")
#B1.pack()
#B2.pack()
#root.mainloop()

#--------

#var = tkinter.IntVar()
#button = tkinter.Button(root, text="Ready", command=lambda: var.set(1))
#button.place(relx=.5, rely=.8, anchor="c")

#print("Ready to paste...")
#button.wait_variable(var)
#print("Paste Now.")