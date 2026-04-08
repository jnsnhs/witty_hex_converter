import tkinter as tk
import tkinter.font
from tkinter import ttk
from tkinter import messagebox as msgbox

import csv
import os
import sys

from ...defaults import STATIC_DIR
from ...gui.views.view import View
from ...guitext import GuiText


def import_color_names_as_dict(path_to_file) -> dict:
    result = dict()
    try:
        with open(path_to_file, "r", encoding="utf8") as csv_file:
            for (color_name, color_value) in csv.reader(csv_file):
                result[color_name] = color_value
    except Exception:
        display_file_loading_error(path_to_file)
        sys.exit(0)
    else:
        return result


def display_file_loading_error(path_to_file) -> None:
    msgbox.showerror(
        title="Fehlermeldung",
        message="Das Programm kann nicht gestartet werden.",
        detail=f"Die Datei\n\n{path_to_file}\n\nkonnte nicht importiert "
        "werden."
    )


COLOR_NAMES = import_color_names_as_dict(os.path.join(
    STATIC_DIR, "named_colors.csv"))


class MainView(View):

    def __init__(self, parent_window):
        super().__init__(parent_window)
        self.MONOSPACE_FONT = "Courier"
        self.PADDING_X = 15
        self.PADDING_Y = 15
        self.create_grid(6, 1)
        for i in range(6):
            if i != 1:
                self.grid_rowconfigure(i, weight=0)
        self.grid_rowconfigure(1, weight=1)

        self.create_rgb_color_box()
        self.create_color_name_label()
        self.create_comment_label()
        self.create_combobox()
        self.create_convert_button()
        self.create_random_button()
        self.create_checkbox()

    def create_rgb_color_box(self):
        match sys.platform:
            case "win32":
                FONT_STYLE = (self.MONOSPACE_FONT, 20, "bold")
                LABEL_HEIGHT = 4
            case "darwin":
                FONT_STYLE = (self.MONOSPACE_FONT, 22)
                LABEL_HEIGHT = 5
            case _:
                FONT_STYLE = (self.MONOSPACE_FONT, 20)
                LABEL_HEIGHT = 5
        self.label_rgb_code = tk.Label(
            self, text='', font=FONT_STYLE,
            height=LABEL_HEIGHT, relief="groove")
        self.label_rgb_code.grid(
            row=0, column=0, sticky="ew",
            ipadx=0, ipady=0, padx=self.PADDING_X, pady=self.PADDING_Y)

    def create_color_name_label(self):
        match sys.platform:
            case "win32":
                FONT_STYLE = tkinter.font.Font(size=9, weight="bold")
            case "darwin":
                FONT_STYLE = tkinter.font.Font()
            case _:
                FONT_STYLE = tkinter.font.Font()
        self.label_css_name = tk.Label(self, text="", font=FONT_STYLE)
        self.label_css_name.grid(
            row=0,
            column=0,
            sticky="",
            padx=self.PADDING_X+7,
            pady=(45, 0)
            )
        self.label_css_name.grid_remove()

    def create_comment_label(self):
        self.comment_frame = tk.LabelFrame(
            self,
            text="",
            labelanchor="n",
            relief="groove"
            )
        self.comment_frame.grid(
            row=1, column=0, sticky="nesw", padx=self.PADDING_X)
        self.comment = tk.StringVar()
        self.comment_frame.grid_rowconfigure(0, weight=1)
        self.comment_frame.grid_columnconfigure(0, weight=1)
        self.label_comment = tk.Label(
            self.comment_frame, textvariable=self.comment, wraplength=220,
            height=6, justify="center", anchor="center"
            )
        self.label_comment.grid(
            row=0, column=0, sticky="ew")

    def create_combobox(self):
        match sys.platform:
            case "win32":
                COMBO_BOX_WIDTH = 20
                FONT_STYLE = tkinter.font.Font(family=self.MONOSPACE_FONT,
                                               size=14)
            case "darwin":
                COMBO_BOX_WIDTH = 28
                FONT_STYLE = tkinter.font.Font(family=self.MONOSPACE_FONT)
            case _:
                COMBO_BOX_WIDTH = 30
                FONT_STYLE = tkinter.font.Font(family=self.MONOSPACE_FONT,
                                               size=14)
        self.user_input = tk.StringVar()
        self.cbox_color_select = ttk.Combobox(
            self,
            textvariable=self.user_input,
            font=FONT_STYLE,
            width=COMBO_BOX_WIDTH,
            justify="center", state="normal",
            values=tuple(COLOR_NAMES.keys())
            )
        self.cbox_color_select.grid(
            row=2, column=0, sticky="nesw",
            pady=(self.PADDING_Y, self.PADDING_Y/2),
            padx=self.PADDING_X
            )
        self.cbox_color_select.bind(
            "<<ComboboxSelected>>", self.on_select_color_name)
        self.cbox_color_select.bind("<Return>", self.on_return_combobox)
        self.cbox_color_select.focus()

    def create_convert_button(self):
        self.button_convert = ttk.Button(
            self,
            text=GuiText.LABEL_CONVERT_BTN,
            command=lambda: self.on_click_convert_button()
            )
        self.button_convert.grid(
            row=3, column=0, sticky="ew",
            pady=(0, self.PADDING_Y/2), padx=self.PADDING_X
            )

    def create_random_button(self):
        self.button_random = ttk.Button(
            self,
            text=GuiText.LABEL_RANDOM_BTN,
            command=lambda: self.on_click_random_button()
            )
        self.button_random.grid(
            row=4, column=0, sticky="ew",
            padx=self.PADDING_X, pady=(0, self.PADDING_Y/2)
            )

    def create_checkbox(self):
        self.window_is_topmost = tk.BooleanVar()
        self.checkbox_topmost = ttk.Checkbutton(
            self,
            text=GuiText.LABEL_CHECKBOX,
            variable=self.window_is_topmost,
            command=lambda: self.on_click_checkbox()
            )
        self.checkbox_topmost.grid(
            row=6, column=0, sticky="",
            padx=self.PADDING_X, pady=(self.PADDING_Y/2, self.PADDING_Y)
            )

    def on_click_checkbox(self):
        self.controller.toggle_topmost(self.window_is_topmost.get())

    def on_return_combobox(self, event):
        self.controller.validate_input(self.user_input.get())

    def on_click_convert_button(self):
        self.controller.validate_input(self.user_input.get())

    def on_select_color_name(self, event):
        selected_color_name = self.user_input.get()
        self.user_input.set(f"#{COLOR_NAMES[selected_color_name].lower()}")
        self.cbox_color_select.select_range(0, 7)
        self.controller.validate_input(self.user_input.get())

    def on_click_random_button(self):
        self.controller.set_input_to_random_hex_code()
        self.controller.validate_input(self.user_input.get())

    def set_user_input_to_value(self, value):
        self.user_input.set(value)

    def set_rgb_label_bg_color(self, hex_code):
        self.style = ttk.Style()
        self.style.configure('Color.TFrame',  background=f'#{hex_code}')
        self.label_rgb_code["background"] = f'#{hex_code}'
        self.label_css_name["background"] = f'#{hex_code}'

    def set_font_color(self, color):
        self.label_rgb_code["foreground"] = color
        self.label_css_name["foreground"] = color
