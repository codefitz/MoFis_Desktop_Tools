import tkinter as tk
import pygetwindow as gw

class ClickThroughOverlay(tk.Tk):
    def __init__(self):
        super().__init__()
        self.attributes('-topmost', True)  # Keep the window on top
        self.overrideredirect(True)  # Remove window decorations

        # Create a border frame with red background
        self.border_frame = tk.Frame(self, bg='red', width=620, height=420, cursor="arrow")
        self.border_frame.pack_propagate(False)
        self.border_frame.pack(fill=tk.BOTH, expand=True)

        # Create an inner frame with transparency
        self.inner_frame = tk.Frame(self.border_frame, bg='green', width=600, height=400)
        self.inner_frame.pack_propagate(False)
        self.inner_frame.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

        # Add title bar
        self.title_bar = tk.Frame(self.inner_frame, bg='darkred', height=20)
        self.title_bar.pack(fill=tk.X, side=tk.TOP)
        self.title_label = tk.Label(self.title_bar, text="Screen-Share Window", bg='darkred', fg='white')
        self.title_label.pack(side=tk.LEFT, padx=5)

        # Add close button
        self.close_button = tk.Button(self.title_bar, text="X", command=self.close, bg='darkred', fg='white', borderwidth=0, font=("Helvetica", 14, "bold"))
        self.close_button.pack(side=tk.RIGHT, padx=5)

        # Bind mouse events for moving and resizing
        self.title_bar.bind("<ButtonPress-1>", self.start_move)
        self.title_bar.bind("<B1-Motion>", self.do_move)
        self.title_bar.bind("<ButtonRelease-1>", self.stop_move)
        self.border_frame.bind("<ButtonPress-1>", self.start_resize)
        self.border_frame.bind("<B1-Motion>", self.do_resize)
        self.border_frame.bind("<ButtonRelease-1>", self.stop_resize)

        # Bind mouse events for changing the cursor
        self.border_frame.bind("<Motion>", self.change_cursor)
        self.border_frame.bind("<Leave>", self.reset_cursor)

        self.resizing = False
        self.start_x = None
        self.start_y = None

        # Make the window click-through
        self.lift()
        self.wm_attributes("-transparentcolor", 'green')

        # Center the window on the screen
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (self.border_frame.winfo_reqwidth() // 2)
        y = (screen_height // 2) - (self.border_frame.winfo_reqheight() // 2)
        self.geometry(f"+{x}+{y}")

    def close(self):
        self.destroy()

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

    def stop_move(self, event):
        # Check for snapping
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = self.winfo_x()
        y = self.winfo_y()
        width = self.winfo_width()
        height = self.winfo_height()

        if x <= 0:  # Left edge
            self.geometry(f"{screen_width//2}x{screen_height}+0+0")
        elif x + width >= screen_width:  # Right edge
            self.geometry(f"{screen_width//2}x{screen_height}+{screen_width//2}+0")
        elif y <= 0:  # Top edge
            self.geometry(f"{screen_width}x{screen_height//2}+0+0")
        elif y + height >= screen_height:  # Bottom edge
            self.geometry(f"{screen_width}x{screen_height//2}+0+{screen_height//2}")

    def start_resize(self, event):
        if event.widget != self.close_button:
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
        width = self.winfo_width()
        height = self.winfo_height()
        direction = ""
        if x < edge_margin:
            direction += "w"
        elif x > width - edge_margin:
            direction += "e"
        if y < edge_margin:
            direction += "n"
        elif y > height - edge_margin:
            direction += "s"
        return direction

    def change_cursor(self, event):
        direction = self.get_cursor_direction(event)
        cursor = "arrow"
        if "n" in direction and "w" in direction:
            cursor = "top_left_corner"
        elif "n" in direction and "e" in direction:
            cursor = "top_right_corner"
        elif "s" in direction and "w" in direction:
            cursor = "bottom_left_corner"
        elif "s" in direction and "e" in direction:
            cursor = "bottom_right_corner"
        elif direction == "n":
            cursor = "top_side"
        elif direction == "s":
            cursor = "bottom_side"
        elif direction == "w":
            cursor = "left_side"
        elif direction == "e":
            cursor = "right_side"
        self.border_frame.config(cursor=cursor)

    def reset_cursor(self, event):
        self.border_frame.config(cursor="arrow")

if __name__ == "__main__":
    app = ClickThroughOverlay()
    app.mainloop()
