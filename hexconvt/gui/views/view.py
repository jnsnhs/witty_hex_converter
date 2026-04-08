from tkinter import ttk


class View(ttk.Frame):

    def __init__(self, parent_window) -> None:
        super().__init__(parent_window)
        self.window = parent_window
        self.grid(row=0, column=0, sticky="nesw")
        self.controller = None

    def set_controller(self, controller) -> None:
        self.controller = controller

    def create_grid(self, rows, cols) -> None:
        for i in range(rows):
            self.rowconfigure(i, weight=1)
        for i in range(cols):
            self.columnconfigure(i, weight=1)
