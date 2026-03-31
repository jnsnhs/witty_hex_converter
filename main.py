# Die Zahlen, die in der Funktion get_contrasting_color() mit den
# RGB-Werten multipliziert weden, sind folgendem Blog-Artikel entnommen:
# https://nemecek.be/blog/172/how-to-calculate-contrast-color-in-python
# Mir ist nicht bekannt, wie der Autor auf die Werte gekommen ist, vielleicht
# durch Ausprobieren. Möglicherweise steckt auch mehr dahinter. Jedenfalls 
# sorgen die Werte dafür, dass für eine beliebige RGB-Farbe sehr treffsicher
# ermittelt wird, ob Schwarz oder Weiß den besseren Kontrast darstellt.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox
import sys
from random import random, choice, choices
import csv, json

def display_file_loading_error(path_to_file):
    msgbox.showerror(
        title="Fehlermeldung", 
        message="Das Programm kann nicht gestartet werden.", 
        detail=f"Die Datei\n\n{path_to_file}\n\nkonnte nicht eingelesen werden."
    )
    sys.exit(0)
    
def import_color_names_as_dict(path_to_file) -> dict:
    result = dict()
    try:    
        with open(path_to_file, "r", encoding="utf8") as csv_file:
            for (color_name, color_value) in csv.reader(csv_file):
                result[color_name] = color_value
    except Exception:
        display_file_loading_error(path_to_file)
    else:
        return result

def import_text_file_as_list(path_to_file: str) -> list|None:
    result = list()
    try:
        with open(path_to_file, "r", encoding="utf8") as text_file:
            for line in text_file.readlines():
                line = line.strip("\n")
                result.append(line)
    except Exception:
        display_file_loading_error(path_to_file)
    else:
        return result

def import_json_file_as_dict(path_to_file) -> dict|None:
    try:
        with open(path_to_file, "r", encoding="utf8") as json_file:
            json_data = json_file.read()
            return json.loads(json_data)
    except Exception:
        display_file_loading_error(path_to_file)

COLOR_NAMES = import_color_names_as_dict("./res/named_colors.csv")

class TEXT:
    APP_TITLE = "HEX 9000"
    DEFAULT_COMMENT = "Bitte geben Sie einen gültigen\nHex-Wert ein oder wählen Sie eine\nder vordefinierten Webfarbe aus."
    LABEL_RANDOM_BTN = "Zufälligen Wert erzeugen"
    LABEL_CONVERT_BTN = "Eingabe konvertieren"
    LABEL_CHECKBOX = "Fenster im Vordergrund halten"
    LABEL_INVALID_INPUT = "Eingabe\nungültig"
    LABEL_EMPTY_INPUT = "Leere\nEingabe"
    LABEL_TRANSPARENT_COLOR = "Anzeige\nnicht\nmöglich"
    
    NAMED_CODES = import_json_file_as_dict("./res/comments_named_codes.json")
    EIGHT_DIGIT_CODES = import_text_file_as_list("./res/comments_eight-digit_codes.txt")
    FOUR_DIGIT_CODES = import_text_file_as_list("./res/comments_four-digit_codes.txt")
    THREE_DIGIT_CODES = import_text_file_as_list("./res/comments_three-digit_codes.txt")
    MISC_CODES = import_text_file_as_list("./res/comments_misc_codes.txt")
    RANDOM = import_text_file_as_list("./res/comments_random.txt")
    NO_INPUT = import_text_file_as_list("./res/comments_no_input.txt")
    MISC_INVALID_INPUTS = import_text_file_as_list("./res/comments_invalid_input.txt")



class View(ttk.Frame):
    
    def __init__(self, parent_window):
        super().__init__(parent_window)
        self.window = parent_window
        self.grid(row = 0, column = 0, sticky = "nesw")
        self.controller = None
    
    def set_controller(self, controller):
        self.controller = controller

    def create_grid(self, rows, cols):
        for i in range(rows):
            self.rowconfigure(i, weight = 1)
        for i in range(cols):
            self.columnconfigure(i, weight = 1)


class MainModel():

    def __init__(self):
        self.HEX_DIGITS = "0123456789"
        self.HEX_CHARACTERS = "abcdef"
        self.HEX_SYMBOLS = self.HEX_DIGITS + self.HEX_CHARACTERS
        self.hex_code = self.get_random_hex_string(6)
        self.rgb_code = self.get_rgb_from_hex_code(self.hex_code)
        self.css_name = self.get_name_of_hex_code(self.hex_code)
        self.colors_converted = list()

    @property
    def hex_code(self):
        return self._hex_code
    
    @hex_code.setter
    def hex_code(self, value):
        if self.is_hex_code(value, (3, 6)):
            self._hex_code = value
            self.rgb_code = self.get_rgb_from_hex_code(value)
            self.css_name = self.get_name_of_hex_code(value)
        else:
            raise ValueError()

    def is_hex_string(self, str_value) -> bool:
        for i in str_value:
            if i.casefold() not in self.HEX_SYMBOLS:
                return False
        return True

    def is_hex_code(self, str_value, valid_lengths = (3, 4, 6, 8)) -> bool:
        if self.is_hex_string(str_value):
            return True if len(str_value) in valid_lengths else False
        else:
            return False

    def get_decimal_from_hex_string(self, hex_str) -> int:
        decimal_value = 0
        for i in range(len(hex_str)):
            if hex_str[i].casefold() in self.HEX_CHARACTERS:
                summand = self.HEX_CHARACTERS.index(hex_str[i].casefold()) + 10
            else:
                summand = hex_str[i]
            decimal_value += int(summand) * 16 ** (len(hex_str) - 1 - i)
        return decimal_value

    def get_rgb_from_hex_code(self, hex_code) -> tuple:
        if len(hex_code) in (3, 4):
            hex_code = self.get_full_hex_code(hex_code)
        red = self.get_decimal_from_hex_string(hex_code[0:2])
        green = self.get_decimal_from_hex_string(hex_code[2:4])
        blue = self.get_decimal_from_hex_string(hex_code[4:6])
        if len(hex_code) == 8:
            alpha = 100 * self.get_decimal_from_hex_string(hex_code[6:8])//255
            return (red, green, blue, alpha)
        else:
            return (red, green, blue)

    def get_name_of_hex_code(self, search_hex) -> str:
        for css3_name, hex in COLOR_NAMES.items():  
            if hex.casefold() == search_hex.casefold():
                return css3_name
        return ""

    def get_random_hex_string(self, length) -> str:
        return ''.join(choices(self.HEX_SYMBOLS, k=length))

    def get_full_hex_code(self, short_hex_code) -> str:
        return ''.join([i * 2 for i in short_hex_code])

    def unique_colors_converted(self):
        return len(set(self.colors_converted))


class MainView(View):

    def __init__(self, parent_window):
        super().__init__(parent_window)
        self.PADDING_X = 15
        self.PADDING_Y = 15
        self.create_grid(6, 1)
        for i in range(6):
            if i != 1: self.grid_rowconfigure(i, weight = 0)
        self.grid_rowconfigure(1, weight = 1)        
        self.create_rgb_color_box()
        self.create_color_name_label()
        self.create_comment_label()
        self.create_combobox()
        self.create_convert_button()
        self.create_random_button()
        self.create_checkbox()

    def create_rgb_color_box(self):
        self.label_rgb_code = tk.Label(
            self, text = '', font = ('Courier', 18, 'bold'), 
            height=4, relief = 'groove')
        self.label_rgb_code.grid(
            row = 0, column = 0, sticky = "ew",
            ipadx = 0, ipady = 0, padx = self.PADDING_X, pady=self.PADDING_Y)
        
    def create_color_name_label(self):
        self.label_css_name = tk.Label(
            self, text = '', font = ('Arial', 8, 'bold'))
        self.label_css_name.grid(
            row=0,
            column=0, 
            sticky="s", 
            padx=self.PADDING_X+7,
            pady=(0, 40)
            )
        self.label_css_name.grid_remove()

    def create_comment_label(self):
        self.comment_frame = tk.LabelFrame(
            self, text='Die Stimmme der KI sagt:', labelanchor="n", height="550"
            )
        self.comment_frame.grid(
            row=1, column=0, sticky="nesw", padx=self.PADDING_X)
        self.comment = tk.StringVar()
        self.comment_frame.grid_rowconfigure(0, weight = 1)
        self.comment_frame.grid_columnconfigure(0, weight = 1)
        self.label_comment = tk.Label(
            self.comment_frame, textvariable=self.comment, wraplength=220, height=5,
            justify = "center", anchor = "center"
            )
        self.label_comment.grid(
            row = 0, column = 0, sticky = "ew")

    def create_combobox(self):
        self.user_input = tk.StringVar()
        self.cbox_color_select = ttk.Combobox(
            self,
            textvariable=self.user_input,
            font=('Courier', 14),
            width= 20,
            justify="center", state='normal', height=20,
            values=tuple(COLOR_NAMES.keys())
            )
        self.cbox_color_select.grid(
            row=2, column=0, sticky="ew", #ipadx = 30,
            ipady = 5, 
            pady = (self.PADDING_Y, self.PADDING_Y/2), 
            padx = self.PADDING_X
            )
        self.cbox_color_select.bind('<<ComboboxSelected>>', self.on_select_color_name)
        self.cbox_color_select.bind('<Return>', self.on_return_combobox)
        self.cbox_color_select.focus()
        self.cbox_color_select.select_range(0, 7)

    def create_convert_button(self):
        self.button_convert = ttk.Button(
            self,
            text=TEXT.LABEL_CONVERT_BTN,
            #width=20,
            command=lambda: self.on_click_convert_button()
            )
        self.button_convert.grid(
            row = 3, column = 0, sticky = "ew",
            pady = (0, self.PADDING_Y/2), padx = self.PADDING_X
            )

    def create_random_button(self):
        self.button_random = ttk.Button(
            self, 
            text=TEXT.LABEL_RANDOM_BTN,
            command=lambda: self.on_click_random_button()
            )
        self.button_random.grid(
            row = 4, column = 0, sticky = "ew", 
            padx = self.PADDING_X, pady = (0, self.PADDING_Y/2)
            )

    def create_checkbox(self):
        self.window_is_topmost = tk.BooleanVar()
        self.checkbox_topmost = ttk.Checkbutton(
            self,
            text=TEXT.LABEL_CHECKBOX,
            variable=self.window_is_topmost,
            command=lambda: self.on_click_checkbox()
            )
        self.checkbox_topmost.grid(
            row = 6, column = 0, sticky="",
            padx = self.PADDING_X, pady = (self.PADDING_Y/2, self.PADDING_Y)
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
        self.cbox_color_select.select_range(0,7)
        self.controller.validate_input(self.user_input.get())

    def on_click_random_button(self):
        self.controller.set_input_to_random_hex_code()
        self.controller.validate_input(self.user_input.get())

    def set_user_input_to_value(self, value):
        self.user_input.set(value)

    def set_rgb_label_bg_color(self, hex_code):
        self.style = ttk.Style()
        self.style.configure('Color.TFrame',  background = f'#{hex_code}')
        self.label_rgb_code['background'] = f'#{hex_code}'
        self.label_css_name['background'] = f'#{hex_code}'

    def set_font_color(self, color):
        self.label_rgb_code['foreground'] = color
        self.label_css_name['foreground'] = color


class MainController:

    def __init__(self, app, model, view):
        self.app = app
        self.model = model
        self.view = view
        self.view.user_input.set(f'#{self.model.hex_code}')
        self.validate_input(self.model.hex_code)
        self.insert_comment(TEXT.DEFAULT_COMMENT)
        self.view.cbox_color_select.select_range(0,7)
        
    def set_input_to_random_hex_code(self):
        random_hex_code = self.model.get_random_hex_string(6)
        self.view.user_input.set(f'#{random_hex_code}')

    def validate_input(self, str_value):
        str_value = str_value.strip('# ')
        try:
            self.model.hex_code = str_value
            self.view.set_user_input_to_value(f'#{str_value}')
            self.model.colors_converted.append(str_value)
            self.display_rgb_code()
            self.comment_on_hex_code(str_value)
        except ValueError:
            if self.model.is_hex_code(str(str_value), (4,)):
                self.view.user_input.set(f'#{str_value}')
                self.insert_comment(choice(TEXT.FOUR_DIGIT_CODES))
                self.display_message('TRANSPARENT')
            elif self.model.is_hex_code(str(str_value), (8,)):
                self.view.user_input.set(f'#{str_value}')
                self.insert_comment(choice(TEXT.EIGHT_DIGIT_CODES))
                self.display_message('TRANSPARENT')
            elif str_value == "":
                self.insert_comment(choice(TEXT.NO_INPUT))
                self.display_message('EMPTY_INPUT')
            else:
                self.insert_comment(choice(TEXT.MISC_INVALID_INPUTS))
                self.display_message('INVALID_INPUT')
    
    def display_rgb_code(self):
        self.view.label_css_name.grid_remove()
        rgb = self.model.rgb_code
        self.view.label_rgb_code['text'] = f"({rgb[0]},{rgb[1]},{rgb[2]})"
        self.view.set_rgb_label_bg_color(self.model.hex_code)
        self.view.set_font_color(self.get_contrasting_color())
        if self.model.css_name:
            self.view.label_css_name['text'] = self.model.css_name
            self.view.label_css_name.grid()

    def display_message(self, type):
        self.view.label_css_name.grid_remove()
        self.view.set_rgb_label_bg_color("dddddd")
        self.view.set_font_color("#aaaaaa")
        match type:
            case 'INVALID_INPUT':
                self.view.label_rgb_code['text'] = TEXT.LABEL_INVALID_INPUT
            case 'EMPTY_INPUT':
                self.view.label_rgb_code['text'] = TEXT.LABEL_EMPTY_INPUT
            case 'TRANSPARENT':
                self.view.label_rgb_code['text'] = TEXT.LABEL_TRANSPARENT_COLOR

    def comment_on_hex_code(self, hex_input):
        match len(hex_input):
            case 3:
                self.insert_comment(choice(TEXT.THREE_DIGIT_CODES))
            case 6:
                try:
                    self.insert_comment(
                        choice(TEXT.NAMED_CODES[hex_input.upper()]))
                except:
                    if random() < 0.75:
                        self.insert_comment(choice(TEXT.MISC_CODES))
                    else:
                        self.insert_comment(choice(TEXT.RANDOM))

    def insert_comment(self, comment):
        self.view.comment.set(comment)

    def get_contrasting_color(self):
        luminance =  (self.model.rgb_code[0] * 0.2126 + 
                      self.model.rgb_code[1] * 0.7152 + 
                      self.model.rgb_code[2] * 0.0722)
        return 'white' if luminance < 140 else 'black'

    def toggle_topmost(self, bool_value):
        self.app.call('wm', 'attributes', '.', '-topmost', bool_value)


class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        # self.configure_window(TEXT.APP_TITLE, 380, 600)
        self.title(TEXT.APP_TITLE)
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.resizable(False, False)
        self.model = MainModel()
        self.view = MainView(self)
        self.controller = MainController(self, self.model, self.view)
        self.view.set_controller(self.controller)
        
    def configure_window(self, title, width, height):
        self.title(title)
        self.window_width = width
        self.window_height = height
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

    def center_window_on_screen(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width / 2 - self.window_width / 2)
        center_y = int(screen_height / 2 - self.window_height / 2)
        self.geometry(
            f"{self.window_width}x{self.window_height}+{center_x}+{center_y}")


app = MainWindow()
app.mainloop()