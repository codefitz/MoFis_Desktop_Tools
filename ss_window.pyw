#!/usr/bin/env python3
import tkinter as tk
import ctypes
import sys

class Overlay(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Overlay")
        self.attributes('-topmost', True)
        self.geometry("622x422")
        # self.overrideredirect(True)  # Comment out this line to keep window decorations

        # Create a border frame with a different background color
        self.border_frame = tk.Frame(self, bg='white', width=622, height=422)
        self.border_frame.pack_propagate(False)
        self.border_frame.pack(fill=tk.BOTH, expand=True)

        # Create an inner frame with a different background color to be made transparent
        self.inner_frame = tk.Frame(self.border_frame, bg='cyan', width=600, height=400)
        self.inner_frame.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)  # Ensure padding for border

        # Create a handle for dragging the overlay
        self.drag_handle = tk.Frame(self.inner_frame, bg='grey', width=100, height=20)
        self.drag_handle.place(relx=0.5, rely=0, anchor='n')
        self.drag_handle.bind("<ButtonPress-1>", self.start_drag)
        self.drag_handle.bind("<B1-Motion>", self.do_drag)

        # Add text to the drag handle
        self.drag_text = tk.Label(self.drag_handle, text="Overlay", bg='grey', fg='white')
        self.drag_text.pack(fill=tk.BOTH, expand=True)

        self.resizing = False
        self.start_x = None
        self.start_y = None
        self.dragging = False

        # Make the window click-through
        self.wm_attributes("-transparentcolor", 'cyan')

        # Bind mouse events for moving and resizing
        self.border_frame.bind("<ButtonPress-1>", self.start_resize)
        self.border_frame.bind("<B1-Motion>", self.do_resize)
        self.border_frame.bind("<ButtonRelease-1>", self.stop_resize)

        # Bind mouse events for changing the cursor
        self.border_frame.bind("<Motion>", self.change_cursor)
        self.border_frame.bind("<Leave>", self.reset_cursor)

        self.cursor_direction = None

        # Center the window on the screen
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (self.border_frame.winfo_reqwidth() // 2)
        y = (screen_height // 2) - (self.border_frame.winfo_reqheight() // 2)
        self.geometry(f"+{x}+{y}")

        # Set the window style to shrink the title bar (for Windows only)
        if sys.platform == "win32":
            hwnd = ctypes.windll.user32.GetParent(self.winfo_id())
            self.set_window_style(hwnd)

    def set_window_style(self, hwnd):
        # Constants for setting window styles
        GWL_STYLE = -16
        WS_CAPTION = 0x00C00000
        WS_BORDER = 0x00800000
        WS_THICKFRAME = 0x00040000

        # Get the current style
        current_style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE)

        # Remove the thickframe (resizable border) and border, but keep the title bar
        new_style = current_style & ~WS_THICKFRAME & ~WS_BORDER

        # Apply the new style
        ctypes.windll.user32.SetWindowLongW(hwnd, GWL_STYLE, new_style)

        # Apply the changes immediately
        ctypes.windll.user32.SetWindowPos(hwnd, None, 0, 0, 0, 0, 0x0273)

    def start_drag(self, event):
        self.dragging = True
        self.start_x = event.x
        self.start_y = event.y

    def do_drag(self, event):
        if self.dragging:
            x = self.winfo_x() + event.x - self.start_x
            y = self.winfo_y() + event.y - self.start_y
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()
            snap_threshold = 20  # Pixels within which the window snaps to screen edges

            # Snap to edges
            if abs(x) < snap_threshold:
                x = 0
            elif abs(x + self.winfo_width() - screen_width) < snap_threshold:
                x = screen_width - self.winfo_width()
            if abs(y) < snap_threshold:
                y = 0
            elif abs(y + self.winfo_height() - screen_height) < snap_threshold:
                y = screen_height - self.winfo_height()

            self.geometry(f"+{x}+{y}")

    def stop_drag(self, event):
        self.dragging = False

    def start_resize(self, event):
        self.start_x = event.x_root
        self.start_y = event.y_root
        self.start_width = self.winfo_width()
        self.start_height = self.winfo_height()
        self.start_x_root = self.winfo_x()
        self.start_y_root = self.winfo_y()
        self.resizing = True
        self.cursor_direction = self.get_cursor_direction(event)

    def do_resize(self, event):
        if self.resizing:
            delta_x = event.x_root - self.start_x
            delta_y = event.y_root - self.start_y
            new_width = self.start_width
            new_height = self.start_height
            new_x = self.start_x_root
            new_y = self.start_y_root

            if "e" in self.cursor_direction:
                new_width = max(self.start_width + delta_x, 50)
            if "s" in self.cursor_direction:
                new_height = max(self.start_height + delta_y, 50)
            if "w" in self.cursor_direction:
                new_width = max(self.start_width - delta_x, 50)
                new_x = self.start_x_root + delta_x
            if "n" in self.cursor_direction:
                new_height = max(self.start_height - delta_y, 50)
                new_y = self.start_y_root + delta_y

            self.geometry(f"{new_width}x{new_height}+{new_x}+{new_y}")

    def stop_resize(self, event):
        self.resizing = False

    def get_cursor_direction(self, event):
        edge_margin = 10
        x = event.x
        y = event.y
        width = self.border_frame.winfo_width()
        height = self.border_frame.winfo_height()
        direction = ""
        if x < edge_margin and y < edge_margin:
            direction = "nw"
        elif x > width - edge_margin and y < edge_margin:
            direction = "ne"
        elif x < edge_margin and y > height - edge_margin:
            direction = "sw"
        elif x > width - edge_margin and y > height - edge_margin:
            direction = "se"
        elif x < edge_margin:
            direction = "w"
        elif x > width - edge_margin:
            direction = "e"
        elif y < edge_margin:
            direction = "n"
        elif y > height - edge_margin:
            direction = "s"
        return direction

    def change_cursor(self, event):
        direction = self.get_cursor_direction(event)
        cursor = "arrow"
        if direction == "nw":
            cursor = "top_left_corner"
        elif direction == "ne":
            cursor = "top_right_corner"
        elif direction == "sw":
            cursor = "bottom_left_corner"
        elif direction == "se":
            cursor = "bottom_right_corner"
        elif direction == "n":
            cursor = "top_side"
        elif direction == "s":
            cursor = "bottom_side"
        elif direction == "w":
            cursor = "left_side"
        elif direction == "e":
            cursor = "right_side"
        self.config(cursor=cursor)

    def reset_cursor(self, event):
        self.config(cursor="arrow")

    def expand_fullscreen(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")

    def expand_left_screen(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width//2}x{screen_height}+0+0")

    def expand_right_screen(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width//2}x{screen_height}+{screen_width//2}+0")


class ControlWindow(tk.Toplevel):
    def __init__(self, master=None, overlay=None):
        super().__init__(master)
        self.overlay = overlay
        self.title("Screen-Share Window")
        self.geometry("200x250")

        # Create control buttons
        self.open_button = tk.Button(self, text="Open", command=self.open_overlay)
        self.close_button = tk.Button(self, text="Close", command=self.close_overlay)
        self.minimize_button = tk.Button(self, text="Minimize", command=self.minimize_overlay)
        self.restore_button = tk.Button(self, text="Restore", command=self.restore_overlay)
        self.expand_fullscreen_button = tk.Button(self, text="Expand Fullscreen", command=self.expand_fullscreen)
        self.expand_left_button = tk.Button(self, text="Expand Left", command=self.expand_left)
        self.expand_right_button = tk.Button(self, text="Expand Right", command=self.expand_right)

        self.open_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.close_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.minimize_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.restore_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.expand_fullscreen_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.expand_left_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.expand_right_button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

    def open_overlay(self):
        if not self.overlay or not self.overlay.winfo_exists():
            self.overlay = Overlay(self)

    def close_overlay(self):
        if self.overlay:
            self.overlay.destroy()

    def minimize_overlay(self):
        if self.overlay:
            self.overlay.state('withdrawn')

    def restore_overlay(self):
        if self.overlay:
            self.overlay.state('normal')

    def expand_fullscreen(self):
        if self.overlay:
            self.overlay.expand_fullscreen()

    def expand_left(self):
        if self.overlay:
            self.overlay.expand_left_screen()

    def expand_right(self):
        if self.overlay:
            self.overlay.expand_right_screen()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    overlay = Overlay(root)
    control_window = ControlWindow(root, overlay)

    root.mainloop()
