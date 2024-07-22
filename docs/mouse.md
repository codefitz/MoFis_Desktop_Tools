# Mouse Jiggle

## Overview

Mouse Jiggle is a simple Python script designed to keep your remote desktop session active by slightly moving the mouse cursor at regular intervals. This prevents the remote desktop from logging out due to inactivity.

## Author

Wes Moskal-Fitzpatrick

## Features

- Moves the mouse cursor periodically to simulate activity.
- Prevents remote desktop sessions from timing out.

## Requirements

- Python 3.x
- `pyautogui` library

## Installation

1. Make sure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/).

2. Install the `pyautogui` library using pip:

   ```bash
   pip install pyautogui
   ```

## Usage

1. Clone this repository or download the script directly.

2. Run the script using Python:

   ```bash
   python mouse_jiggle.py
   ```

### How It Works

- The script uses an infinite loop to continuously move the mouse cursor slightly to the right and then back to the left.
- It includes a short pause between movements to avoid rapid execution.
- Additionally, it simulates a 'shift' key press to ensure that the system registers activity.

## Note

This script is intended for personal use. Please ensure that you have permission to use such scripts in your work environment.

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
