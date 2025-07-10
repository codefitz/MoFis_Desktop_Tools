#!/usr/bin/env python3
# Mouse Jiggle
#
# Author: Wes Moskal-Fitzpatrick
#
# Jiggle the mouse a little bit and prevent remote desktop logout.
#

import argparse
import pyautogui


def main(distance, interval):
    while True:
        pyautogui.moveRel(distance, 0, duration=0)
        pyautogui.PAUSE = interval
        pyautogui.moveRel(-distance, 0, duration=0)
        pyautogui.press("shift")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Keep the system active")
    parser.add_argument(
        "-d",
        "--distance",
        type=int,
        default=5,
        help="Distance in pixels to move the mouse",
    )
    parser.add_argument(
        "-i",
        "--interval",
        type=float,
        default=0.5,
        help="Pause between movements in seconds",
    )
    args = parser.parse_args()
    main(args.distance, args.interval)
