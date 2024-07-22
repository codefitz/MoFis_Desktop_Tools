# Pasta

## Summary

A small app for working with remote environments (such as Citrix) where copy and paste functionality has been disabled.

Pasta uses modules like pyautogui and keyboard to read the text in your clipboard and will re-type the text wherever you place the mouse pointer (even inside of a virtual environment).

Because this is not true copy and paste functionality, there may be bugs - particularly on non-QWERTY keyboards. Use at your own discretion.

## OS Support

| OS | Support |
| - | -
| **Windows** | Yes |
| **Linux** | Maybe? |
| **Mac** | No |

## How to Use

1. Copy the block of text you need

![Copy Text](../images/4c91b4ec95d542dab9234bc67db414c7.png?raw=true)

3. Run the executable "pasta.exe"
4. Have your Notepad/Text app open on the target desktop

![Ready to Paste](../images/2bf244f3161541a1a0a0949e5f0a0b18.png?raw=true)

5. Click the "Ready" button
6. During the 3 second countdown, hover over your target window
7. Marvel at how quickly you typed that document!

![Marvel](../images/f1956e3209c5413ba13db32ccc0581f4.png?raw=true)

# FAQ

### Can I modify this?

Absolutely - if you have any improvements, please send a pull request!

### Can this copy rich text format or pictures?

No, this is using modules that are only capable of using keyboard functionality - text only.

### Will it work on a MacBook?

Not yet.

### Does this connect to the internet?

No. It only handles text that is already available on the client system that the user could already type by hand. There are no API calls or anything like that.

### This is a hacker tool!

Only if you consider logging into a Citrix desktop as an authorised user and painstakingly typing out lots of text or code manually - to be a hacker activity.
