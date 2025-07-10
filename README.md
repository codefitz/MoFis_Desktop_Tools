# MoFi's Desktop Tools

A small collection of desktop tools to work around silly corporate environment restrictions and improve productivity!

> **Important**
> These scripts simulate user input to bypass certain restrictions. Always verify that you have permission from your organisation before running them.

## Tools

- [pasta.py](./docs/pasta.md)
- [ss_window.py](./docs/ss-window.md)
- [mouse_jiggle.py](./docs/mouse.md)

Both `pasta.py` and `mouse_jiggle.py` now accept command line arguments. Run each
script with the `-h` flag to see available options.

## Installation

Clone the repository and install the required packages:

```bash
pip install -r requirements.txt
```

These tools are primarily tested on Windows. `pasta.py` may work on some Linux
desktops if clipboard and automation permissions are enabled. macOS is not
supported.


## Version History

| Version | Description |
| - | - |
| 0.2 | Added a mouse-jiggler tool. |
| 0.3 | Added screen-sharing window for ultra-wide monitor setups. Renamed repository. |
| 0.0.4 | Added dependency list and shebangs; general cleanup. |
