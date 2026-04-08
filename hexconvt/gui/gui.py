import os
import sys
import tkinter as tk
from tkinter import Tk

from ..defaults import ICONS_DIR
from ..core.hex2rgb import MainModel
from ..gui.controllers.main_controller import MainViewController
from ..gui.views.main import MainView


class Gui:
    def __init__(self):
        pass


class AppController(Tk):
    def __init__(self, title, width, height):
        super().__init__()
        self.title(title)
        self.geometry(self.center_window_on_screen(width, height))
        self.resizable(False, False)
        self.set_icon()
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.model = MainModel()
        self.view = MainView(self)
        self.controller = MainViewController(self, self.model, self.view)
        self.view.set_controller(self.controller)

    def center_window_on_screen(self,
                                window_width: int, window_height: int) -> str:
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        margin_left = int(screen_width/2 - window_width/2)
        margin_top = int(screen_height/2 - window_height/2)
        return f"{window_width}x{window_height}+{margin_left}+{margin_top}"

    def set_icon(self) -> None:
        try:
            if sys.platform == "win32":
                self.iconbitmap(os.path.join(ICONS_DIR, "win_icon.ico"))
            elif sys.platform == "darwin":
                image_path = os.path.join(ICONS_DIR, "mac_icon.png")
                icon_image = tk.PhotoImage(file=image_path)
                self.iconphoto(False, icon_image)
        except Exception as exc:
            print(exc)
