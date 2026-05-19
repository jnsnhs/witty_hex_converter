import os
import sys

from tkinter import (
    BooleanVar,
    Label,
    LabelFrame,
    PhotoImage,
    StringVar,
    Tk,
    ttk)
from tkinter.font import Font

from .aicontroller import AiController
from .color import Color
from .colormanager import (
    ColorManager,
    MissingInputError,
    InvalidInputError,
    TransparentColorError)
from .defaults import ICONS_DIR, STATIC_DIR
from .filehelper import import_color_names_as_dict


class Gui(Tk):

    MONOSPACE_FONT = "Courier"
    PADDING_X = PADDING_Y = 15
    COLOR_NAMES = import_color_names_as_dict(os.path.join(
        STATIC_DIR, "named_colors.csv"))

    def __init__(
        self,
        color_manager: ColorManager,
        ai_controller: AiController
    ):
        super().__init__()
        self.color_manager = color_manager
        self.ai_controller = ai_controller
        self.configure_window()
        self.create_widgets()
        self.set_initial_color()

    def configure_window(self) -> None:
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.title("HEX 9000")
        self.geometry(self.center_window_on_screen(275, 445))
        self.resizable(False, False)
        self.set_icon()

    def center_window_on_screen(
            self, window_width: int, window_height: int) -> str:
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
                icon_image = PhotoImage(file=image_path)
                self.iconphoto(False, icon_image)
        except Exception as exc:
            print(exc)

    def set_initial_color(self) -> None:
        self.user_input.set(
            f"#{self.color_manager.get_current_color().hex_code}")
        self.display_color(self.color_manager.get_current_color())

    def create_widgets(self) -> None:
        self.label_rgb_code = self.create_rgb_color_box()
        self.label_css_name = self.create_color_name_label()
        self.comment_frame = self.create_comment_label()
        self.cbox_color_select = self.create_combobox()
        self.convertbutton = self.create_convert_button()
        self.button_random = self.create_random_button()
        self.checkbox_topmost = self.create_checkbox()

    def create_rgb_color_box(self) -> Label:
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
        label_rgb_code = Label(
            self, text="", font=FONT_STYLE,
            height=LABEL_HEIGHT, relief="groove")
        label_rgb_code.grid(
            row=0, column=0, sticky="ew", ipadx=0, ipady=0,
            padx=self.PADDING_X, pady=self.PADDING_Y)
        return label_rgb_code

    def create_color_name_label(self) -> Label:
        match sys.platform:
            case "win32":
                FONT_STYLE = Font(size=9, weight="bold")
            case "darwin":
                FONT_STYLE = Font()
            case _:
                FONT_STYLE = Font()
        label_css_name = Label(self, text="", font=FONT_STYLE)
        label_css_name.grid(
            row=0,
            column=0,
            sticky="",
            padx=self.PADDING_X+7,
            pady=(45, 0)
            )
        label_css_name.grid_remove()
        return label_css_name

    def create_comment_label(self) -> LabelFrame:
        comment_frame = LabelFrame(
            self,
            text=self.ai_controller.get_default_frame_title(),
            labelanchor="n",
            relief="groove"
            )
        comment_frame.grid(
            row=1, column=0, sticky="nesw", padx=self.PADDING_X)
        self.comment = StringVar()
        comment_frame.grid_rowconfigure(0, weight=1)
        comment_frame.grid_columnconfigure(0, weight=1)
        label_comment = Label(
            comment_frame, textvariable=self.comment, wraplength=220,
            height=6, justify="center", anchor="center"
            )
        label_comment.grid(
            row=0, column=0, sticky="ew")
        self.insert_comment(self.ai_controller.get_default_message())
        return comment_frame

    def create_combobox(self) -> ttk.Combobox:
        match sys.platform:
            case "win32":
                COMBO_BOX_WIDTH = 20
                FONT_STYLE = Font(family=self.MONOSPACE_FONT, size=14)
            case "darwin":
                COMBO_BOX_WIDTH = 28
                FONT_STYLE = Font(family=self.MONOSPACE_FONT)
            case _:
                COMBO_BOX_WIDTH = 30
                FONT_STYLE = Font(family=self.MONOSPACE_FONT, size=14)
        self.user_input = StringVar()
        cbox_color_select = ttk.Combobox(
            self,
            textvariable=self.user_input,
            font=FONT_STYLE,
            width=COMBO_BOX_WIDTH,
            justify="center", state="normal",
            values=tuple(self.COLOR_NAMES.keys())
            )
        cbox_color_select.grid(
            row=2, column=0, sticky="nesw",
            pady=(self.PADDING_Y, self.PADDING_Y/2),
            padx=self.PADDING_X
            )
        cbox_color_select.bind(
            "<<ComboboxSelected>>", self.on_select_color_name)
        cbox_color_select.bind("<Return>", self.on_return_combobox)
        cbox_color_select.focus()
        cbox_color_select.select_range(0, 7)
        return cbox_color_select

    def create_convert_button(self) -> ttk.Button:
        button_convert = ttk.Button(
            self,
            text="Eingabe konvertieren",
            command=lambda: self.on_click_convert_button()
            )
        button_convert.grid(
            row=3, column=0, sticky="ew",
            pady=(0, self.PADDING_Y/2), padx=self.PADDING_X
            )
        return button_convert

    def create_random_button(self) -> ttk.Button:
        button_random = ttk.Button(
            self,
            text="Zufälligen Wert erzeugen",
            command=lambda: self.on_click_random_button()
            )
        button_random.grid(
            row=4, column=0, sticky="ew",
            padx=self.PADDING_X, pady=(0, self.PADDING_Y/2)
            )
        return button_random

    def create_checkbox(self) -> ttk.Checkbutton:
        self.is_window_topmost = BooleanVar()
        checkbox_topmost = ttk.Checkbutton(
            self,
            text="Fenster im Vordergrund halten",
            variable=self.is_window_topmost,
            command=lambda: self.toggle_topmost_status()
            )
        checkbox_topmost.grid(
            row=6, column=0, sticky="",
            padx=self.PADDING_X, pady=(self.PADDING_Y/2, self.PADDING_Y)
            )
        return checkbox_topmost

    def on_return_combobox(self, event):
        self.handle_input(self.user_input.get())

    def on_click_convert_button(self):
        self.handle_input(self.user_input.get())

    def on_select_color_name(self, event):
        selected_color_name = self.user_input.get()
        self.user_input.set(
            f"#{self.COLOR_NAMES[selected_color_name].lower()}")
        self.cbox_color_select.select_range(0, 7)
        self.handle_input(self.user_input.get())

    def on_click_random_button(self):
        self.set_input_to_random_hex_code()
        self.handle_input(self.user_input.get())

    def toggle_topmost_status(self) -> None:
        self.call("wm", "attributes", ".", "-topmost",
                  self.is_window_topmost.get())

    def set_user_input_to_value(self, value: str) -> None:
        self.user_input.set(value)

    def set_rgb_label_bg_color(self, hex_code: str) -> None:
        self.style = ttk.Style()
        self.style.configure("Color.TFrame",  background=f"#{hex_code}")
        self.label_rgb_code["background"] = f"#{hex_code}"
        self.label_css_name["background"] = f"#{hex_code}"

    def set_font_color(self, color) -> None:
        self.label_rgb_code["foreground"] = color
        self.label_css_name["foreground"] = color

    def set_input_to_random_hex_code(self) -> None:
        random_hex_code = self.color_manager.get_random_hex_string(6)
        self.user_input.set(f"#{random_hex_code}")

    def insert_comment(self, comment: str) -> None:
        self.comment.set(comment)

    def get_contrasting_color(self, color: Color) -> str:
        rgb_code = color.rgb_code
        luminance = (rgb_code[0] * 0.2126 +
                     rgb_code[1] * 0.7152 +
                     rgb_code[2] * 0.0722)
        return "white" if luminance < 140 else "black"

    def display_color(self, color: Color) -> None:
        self.label_css_name.grid_remove()
        rgb = color.rgb_code
        self.label_rgb_code["text"] = f"({rgb[0]},{rgb[1]},{rgb[2]})"
        self.set_rgb_label_bg_color(color.hex_code)
        self.set_font_color(self.get_contrasting_color(color))
        if css_color_name := color.css_name:
            self.label_css_name['text'] = css_color_name
            self.label_css_name.grid()

    def handle_input(self, string: str) -> None:
        string = string.strip("# ")
        try:
            color = self.color_manager.create_color(string)
        except TransparentColorError as exception:
            self.display_error_message(exception)
            self.user_input.set(f'#{string}')
            n = len(string)
            title, comment = self.ai_controller.comment_on_transparency(n)
        except MissingInputError as exception:
            self.display_error_message(exception)
            title, comment = self.ai_controller.comment_on_missing_input()
        except InvalidInputError as exception:
            self.display_error_message(exception)
            title, comment = self.ai_controller.comment_on_invalid_input()
        else:
            self.display_color(color)
            self.set_user_input_to_value(f'#{color.hex_code}')
            title, comment = self.ai_controller.comment_on_hex_code(string)
        self.set_frame_title(title)
        self.insert_comment(comment)

    def display_error_message(self, message: Exception) -> None:
        self.label_css_name.grid_remove()
        self.set_rgb_label_bg_color("dddddd")
        self.set_font_color("#aaaaaa")
        self.label_rgb_code['text'] = message

    def set_frame_title(self, title: str) -> None:
        self.comment_frame.config(text=title)

    def comment_on_hex_code(self, hex_input: str) -> None:
        heading, comment = self.ai_controller.comment_on_hex_code(hex_input)
        self.set_frame_title(heading)
        self.insert_comment(comment)
