import tkinter as tk

class ClickThroughOverlay(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Screen Share Window")  # Set the window title
        self.attributes('-topmost', True)  # Keep the window on top

        # Create a border frame with a different background color
        self.border_frame = tk.Frame(self, bg='red', width=620, height=420)
        self.border_frame.pack_propagate(False)
        self.border_frame.pack(fill=tk.BOTH, expand=True)

        # Create an inner frame with a different background color to be made transparent
        self.inner_frame = tk.Frame(self.border_frame, bg='cyan', width=600, height=400)
        self.inner_frame.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)  # Ensure padding for border

        self.resizing = False
        self.start_x = None
        self.start_y = None

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

    def close(self):
        self.destroy()

    def minimize(self):
        self.iconify()  # Minimize the window

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

if __name__ == "__main__":
    app = ClickThroughOverlay()
    app.mainloop()
