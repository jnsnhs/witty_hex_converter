# DISCLAIMER: Die Inhalte in der Klasse TEXT sind zum Großteil mit Hilfe von
# Google Gemini generiert worden. Normalerweise wäre es mein Anspruch, solche
# Texte selbst zu formulieren, aber dafür war nun wirklich keine Zeit ;)
# Außerhalb der Klasse TEXT wurde selbstverständlich nicht auf den Einsatz der
# KI zurückgegriffen. Dafür macht mir das Basteln und Tüfteln am Code viel zu
# viel Spaß. Warum sollte ich mir dieses Vergnügen von einer KI rauben lassen?
#
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
from random import random, randint, choice, choices
import time
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

from csv import reader
import json

CANVAS_WIDTH = 1024    # Diese Werte können auf 1920x1080 gesetzt werden,
CANVAS_HEIGHT = 768    # um das versteckte Spiel in HD spielen zu können ;)


COLOR_NAMES = dict()

with open("./res/named_colors.csv", "r", encoding="utf8") as csv_file:
    for (color_name, color_value) in reader(csv_file):
        COLOR_NAMES[color_name] = color_value

def import_text_file_as_list(path_to_file: str) -> list:
    result = list()
    with open(path_to_file, "r", encoding="utf8") as text_file:
        for line in text_file.readlines():
            line = line.strip("\n")
            result.append(line)
    return result

def import_json_file_as_dict(path_to_file) -> dict:
    with open(path_to_file, "r", encoding="utf8") as file:
        json_data = file.read()
        return json.loads(json_data)

class TEXT:
    APP_TITLE = "HEX 9000"
    DEFAULT_COMMENT = "Bitte geben Sie einen gültigen\nHex-Wert ein oder wählen Sie eine\nder vordefinierten Webfarbe aus."
    LABEL_RANDOM_BTN = "Zufälligen Hex-Wert erzeugen"
    LABEL_SECRET_BTN = "\"Hex-Huhn\" spielen"
    LABEL_CONVERT_BTN = "Eingabe nach RGB konvertieren"
    LABEL_CHECKBOX = "Fenster immer oben anzeigen"
    LABEL_INVALID_INPUT = "Eingabe\nungültig"
    LABEL_EMPTY_INPUT = "Leere\nEingabe"
    LABEL_TRANSPARENT_COLOR = "Anzeige\nnicht möglich"
    LABEL_SECRET_UNLOCKED = "Bonus-Spiel\nfreigeschaltet"
    EXIT_CONF_TITLE = "Obacht!"
    EXIT_CONF_MSG = "Wollen Sie das Programm wirklich beenden?"
    EXIT_CONF_DETAIL = "Sie haben noch längst nicht alles gesehen, was dieses unscheinbare Tool zu bieten hat. Konvertieren Sie doch noch ein paar weitere Farben. Es könnte sich lohnen... Oder haben Sie heute noch etwas vor?"
    SECRET_TITLE = "Herzlichen Glückwunsch!"
    SECRET_MSG = "Menschenskind, jetzt Sie haben schon 42 verschiedene Farben konvertiert! Wissen Sie, was das bedeutet? "
    SECRET_DETAIL = "Erstens: Sie sind ein ganz schöner Farben-Nerd...\n\nZweitens: Sie haben ein verstecktes Spiel freigeschaltet! Ja, ganz richtig! Klicken Sie doch mal auf den Button, der neu hinzugekommen ist.\n\nKleiner Tipp: In Zukunft brauchen Sie nicht mehr endlos zu klicken, sondern können das Spiel direkt freischalten, indem Sie \"hexhuhn\" eingeben. Praktisch, oder?"
    CHEAT_USED = "Sie machen es sich ja sehr einfach..."
    CHEAT_CODE = "hexhuhn"
    
    NAMED_CODES = import_json_file_as_dict("./res/comments_named_codes.json")
    EIGHT_DIGIT_CODES = import_text_file_as_list("./res/comments_eight-digit_codes.txt")
    FOUR_DIGIT_CODES = import_text_file_as_list("./res/comments_four-digit_codes.txt")
    THREE_DIGIT_CODES = import_text_file_as_list("./res/comments_three-digit_codes.txt")
    MISC_CODES = import_text_file_as_list("./res/comments_misc_codes.txt")
    RANDOM = import_text_file_as_list("./res/comments_random.txt")
    NO_INPUT = import_text_file_as_list("./res/comments_no_input.txt")
    MISC_INVALID_INPUTS = import_text_file_as_list("./res/comments_invalid_input.txt")
    
    GAME_INTRO1 = "Willkommen, Pixeljägerinnen und Farb-Enthusiasten, in der verrückten Welt von..."
    GAME_TITLE = "Hex-Huhn: Das Farben-Chaos!"
    GAME_INTRO2 = 'Habt ihr gedacht, nach "Moorhuhn" wäre das Kapitel\n"sinnfreies Ballerspiel mit Tieren" abgeschlossen? Ha! Weit gefehlt! \n\nIm neuen Jahrtausend ist die Evolution einen Schritt weitergegangen.\nStatt der sumpfbraunen Moorhühner jagt ihr nun die schillernden\nund geheimnisvollen Hex-Hühner aus dem Land der viereckigen Eier!\n\nOb #FF0000 (knallrot!), #00FFFF (türkis!) oder das kaum sichtbare\n#E6E6FA (Lavendelblush!) – zielt präzise, denn jeder Treffer zählt.\nUnd wer weiß, vielleicht entdeckt ihr ja beim fröhlichen Ballern\neure neue Lieblingsfarbe für die nächste Wohnzimmerwand.\n\nAlso, schnapp dir deine Maus, visiere die fliegenden Farbcodes an\nund beweise, dass du nicht nur Hühner, sondern auch Hex-Werte\nauf\'s Korn nehmen kannst. Mit der <LINKEN MAUSTASTE> wird geschossen\nund mit der <RECHTEN MAUSTASTE> nachgeladen... Weidmannsheil!'
    NEW_HIGHSCORE = (
        "Herzlichen Glückwunsch! Du hast es geschafft, die Pixel-Prominenz zu blamieren.",
        "Unglaublich! Deine Präzision bei Hex-Farben ist fast schon beängstigend.",
        "Ein wahrer Meister der digitalen Farbpalette! Dein Name wird in leuchtenden #Farben erstrahlen!",
        "Respekt! Du hast nicht nur Hühner, sondern auch Hex-Werte erlegt – das muss dir erstmal einer nachmachen!",
        "Phänomenal! Die Moorhühner hätten bei deinem Talent erst recht keine Chance gehabt.",
        "Chapeau! Du bist offiziell der Hex-Huhn-Flüsterer.",
        "Fantastisch! Du hast bewiesen, dass hinter den Farben mehr steckt, als man denkt.",
        "Gratulation! Du hast den Algorithmus des Chaos bezwungen und dich in die Annalen der Pixel-Jagd eingetragen.")
    NO_HIGHSCORE = (
        "Nicht traurig sein! Die Hex-Hühner sind heute einfach besonders flink gewesen. Dein Monitor muss mal wieder kalibriert werden.",
        "Uff, knapp daneben! Aber hey, Hauptsache, du hattest deinen Spaß beim Farb-Gemetzel.",
        "Manchmal tanzen die Pixel einfach anders. Kopf hoch, beim nächsten Mal zerlegst du die Farbwolken!",
        "Kein Grund zum Verzweifeln! Vielleicht waren die Hex-Hühner einfach zu gut getarnt. Das war bestimmt #FAFAFA auf #FDFDFD!",
        "Der Highscore ist nur eine Zahl – deine gesammelten Grautöne sind der wahre Schatz! (Wirklich!)",
        "Puh, das war wohl nichts mit Ruhm und Ehre. Aber immerhin hast du den digitalen Hühnerhof ordentlich aufgemischt!",
        "Die Farben waren heute einfach nicht auf deiner Seite. Versuch's morgen nochmal, wenn das Universum dich mehr liebt.",
        "Auch ein Meister der Farbpalette fängt klein an. Oder sehr, sehr niedrig auf der Highscore-Liste.",
        "Vielleicht hast du einfach zu viel auf die schönen Farben geachtet und nicht genug auf die Punkte. Kunst ist halt subjektiv!",
        "Egal, ob du gewonnen oder verloren hast – du hast auf jeden Fall eine Menge Zeit vor dem Bildschirm verbracht. Das ist doch auch was, oder?")
    NAME_ENTRY = "BITTE NAMEN EINGEBEN"
    START_GAME = "Spiel starten"
    END_GAME = "Spiel beenden"
    GAME_SCORE_TITLE = "Highscore"
    PLAY_AGAIN = "Neues Spiel"
    LIST_OF_PLAYERS = [
        ("Chroma-Königin Xenia", 1429),
        ("Johnny Walker", 1308),
        ("Frau Bratbecker", 1257),
        ("Die Grauschattige Eminenz", 1191),
        ("Henry M. Betrix", 1128),
        ("Baroness Buntstift", 1024),
        ("Art Vandelay (Import-Export)", 994),
        ("Herr Spektral-Specht", 913),
        ("Lady Lila-Laune", 863),
        ("Sir RGB von Schnelldruck", 754),]


class View(ttk.Frame):
    
    def __init__(self, parent_window):
        super().__init__(parent_window)
        self.window = parent_window
        self.grid(row = 0, column = 0, sticky = (tk.N, tk.E, tk.S, tk.W))
        self.controller = None
    
    def set_controller(self, controller):
        self.controller = controller

    def create_grid(self, rows, cols):
        for i in range(rows):
            self.rowconfigure(i, weight = 1)
        for i in range(cols):
            self.columnconfigure(i, weight = 1)


class Window():

    def configure_window(self, title, width, height):
        self.title(title)
        self.window_width = width
        self.window_height = height
        self.resizable(False, False)
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

    def center_window_on_screen(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width / 2 - self.window_width / 2)
        center_y = int(screen_height / 2 - self.window_height / 2)
        self.geometry(
            f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')


class MainModel():

    def __init__(self):
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

    def is_hex_string(self, str_value):
        for i in str_value:
            if i.casefold() not in "0123456789abcdef":
                return False
        return True

    def is_hex_code(self, str_value, valid_lengths = (3, 4, 6, 8)):
        if self.is_hex_string(str_value):
            return True if len(str_value) in valid_lengths else False
        else:
            return False

    def get_decimal_from_hex_string(self, hex_str):
        decimal_value = 0
        for i in range(len(hex_str)):
            if hex_str[i].casefold() in "abcdef":
                summand = "abcdef".index(hex_str[i].casefold()) + 10
            else:
                summand = hex_str[i]
            decimal_value += int(summand) * 16 ** (len(hex_str) - 1 - i)
        return decimal_value

    def get_rgb_from_hex_code(self, hex_code):
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

    def get_name_of_hex_code(self, search_hex):
        for css3_name, hex in COLOR_NAMES.items():  
            if hex.casefold() == search_hex.casefold():
                return css3_name
        return ""

    def get_random_hex_string(self, length):
        return ''.join(choices("0123456789abcdef", k = length))

    def get_full_hex_code(self, short_hex_code):
        return ''.join([i * 2 for i in short_hex_code])

    def unique_colors_converted(self):
        return len(set(self.colors_converted))


class MainView(View):

    def __init__(self, parent_window):
        super().__init__(parent_window)
        self.PADDING_X = 15
        self.PADDING_Y = 15
        self.controller = None
        self.create_grid(7, 1)
        for i in range(7):
            if i != 1: self.grid_rowconfigure(i, weight = 0)
        self.grid_rowconfigure(1, weight = 1)
        self.create_rgb_color_box()
        self.create_color_name_label()
        self.create_comment_label()
        self.create_combobox()
        self.create_convert_button()
        self.create_random_button()
        self.create_secret_button()
        self.create_checkbox()

    def create_rgb_color_box(self):
        self.label_rgb_code = tk.Label(
            self, text = '', font = ('Courier', 20, 'bold'), 
            height = 2, relief = 'groove')
        self.label_rgb_code.grid(
            row = 0, column = 0, sticky = (tk.N, tk.W, tk.E),
            ipadx = 50, ipady = 50, padx = self.PADDING_X, pady=self.PADDING_Y)
        
    def create_color_name_label(self):
        self.label_css_name = tk.Label(
            self, text = '', font = ('Arial', 8, 'bold'))
        self.label_css_name.grid(
            row = 0, column = 0, sticky = (tk.S, tk.W, tk.E), 
            padx = self.PADDING_X + 7, pady = (0, 60))
        self.label_css_name.grid_remove()

    def create_comment_label(self):
        self.comment_frame = ttk.LabelFrame(
            self, text='Die Stimmme der KI sagt:', labelanchor = tk.N)
        self.comment_frame.grid(
            row = 1, column=0, sticky = (tk.N, tk.W, tk.S, tk.E), 
            padx= self.PADDING_X)
        self.comment = tk.StringVar()
        self.comment_frame.grid_rowconfigure(0, weight = 1)
        self.comment_frame.grid_columnconfigure(0, weight = 1)
        self.label_comment = ttk.Label(
            self.comment_frame, textvariable = self.comment, wraplength = 330, 
            justify = tk.CENTER, anchor = tk.N, foreground = "#444444")
        self.label_comment.grid(
            row = 0, column = 0, sticky = (tk.W, tk.E))

    def create_combobox(self):
        self.user_input = tk.StringVar()
        self.cbox_color_select = ttk.Combobox(
            self, textvariable = self.user_input, font = ('Courier', 20),
            justify = tk.CENTER, state = 'normal', height = 20,
            value = tuple(COLOR_NAMES.keys()))
        self.cbox_color_select.grid(
            row = 2, column = 0, sticky = (tk.W, tk.E), ipadx = 30, ipady = 10, 
            pady = (self.PADDING_Y, self.PADDING_Y/2), padx = self.PADDING_X)
        self.cbox_color_select.bind(
            '<<ComboboxSelected>>', self.on_select_color_name)
        self.cbox_color_select.bind('<Return>', self.on_return_combobox)
        self.cbox_color_select.focus()
        self.cbox_color_select.select_range(0, 7)

    def create_convert_button(self):
        self.button_convert = ttk.Button(
            self, text = TEXT.LABEL_CONVERT_BTN, width = 20)
        self.button_convert.grid(
            row = 3, column = 0, sticky = (tk.W, tk.E),
            pady = (0, self.PADDING_Y/2), padx = self.PADDING_X)
        self.button_convert['command'] = self.on_click_convert_button

    def create_random_button(self):
        self.button_random = ttk.Button(self, text = TEXT.LABEL_RANDOM_BTN)
        self.button_random.grid(
            row = 4, column = 0, sticky = (tk.W, tk.E), 
            padx = self.PADDING_X, pady = (0, self.PADDING_Y/2))
        self.button_random['command'] = self.on_click_random_button

    def create_secret_button(self):
        self.secret_button = ttk.Button(self, text = TEXT.LABEL_SECRET_BTN)
        self.secret_button.grid(
            row = 5, column = 0, sticky = (tk.W, tk.E), 
            padx = self.PADDING_X, pady = (0, self.PADDING_Y/2))
        self.secret_button.grid_remove()
        self.secret_button['command'] = self.on_click_secret_button

    def create_checkbox(self):
        self.window_is_topmost = tk.BooleanVar()
        self.checkbox_topmost = ttk.Checkbutton(
            self, text = TEXT.LABEL_CHECKBOX, 
            variable = self.window_is_topmost)
        self.checkbox_topmost.grid(
            row = 6, column = 0, padx = self.PADDING_X, 
            pady = (self.PADDING_Y/2, self.PADDING_Y))
        self.checkbox_topmost['command'] = self.on_click_checkbox

    def on_click_secret_button(self):
        self.controller.open_game_window()

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
            if (self.model.unique_colors_converted() >= 42 and 
                self.app.secret_discovered is False): 
                self.reveal_secret_button()
                self.messagebox_secret_found()
        except ValueError:
            if self.model.is_hex_code(str(str_value), (4,)):
                self.view.user_input.set(f'#{str_value}')
                self.insert_comment(choice(TEXT.FOUR_DIGIT_CODES))
                self.display_message('TRANSPARENT')
            elif self.model.is_hex_code(str(str_value), (8,)):
                self.view.user_input.set(f'#{str_value}')
                self.insert_comment(choice(TEXT.EIGHT_DIGIT_CODES))
                self.display_message('TRANSPARENT')
            elif str_value.casefold() == TEXT.CHEAT_CODE:
                self.insert_comment(TEXT.CHEAT_USED)
                self.display_message('SECRET_FOUND')
                self.reveal_secret_button()
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
            case 'SECRET_FOUND':
                self.view.label_rgb_code['text'] = TEXT.LABEL_SECRET_UNLOCKED
                    
    def reveal_secret_button(self):
        self.app.secret_discovered = True
        self.app.geometry(
            f"{self.app.window_width}x{self.app.window_height + 40}")
        self.view.secret_button.grid()
    
    def messagebox_secret_found(self):
        msgbox.showinfo(title = TEXT.SECRET_TITLE, message = TEXT.SECRET_MSG,
                        detail = TEXT.SECRET_DETAIL)

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

    def open_game_window(self):
        new_window = GameWindow()
        new_window.grab_set()


class MainWindow(Window, tk.Tk):

    def __init__(self):
        super().__init__()
        self.configure_window(TEXT.APP_TITLE, 380, 600)
        self.center_window_on_screen()
        self.model = MainModel()
        self.view = MainView(self)
        self.controller = MainController(self, self.model, self.view)
        self.view.set_controller(self.controller)
        self.secret_discovered = False
        self.protocol('WM_DELETE_WINDOW', self.display_exit_confirmation)

    def display_exit_confirmation(self):
        if self.secret_discovered is False:
            close_window = msgbox.askyesno(
                title = TEXT.EXIT_CONF_TITLE, message = TEXT.EXIT_CONF_MSG, 
                detail=TEXT.EXIT_CONF_DETAIL)
            if close_window: self.destroy()
        else:
            self.destroy()


# # # # # # # # # #    Ab hier wird's komplett albern :)    # # # # # # # # # #


class GamePoints:

    def __init__(self, parent, current_x, current_y, points):
        self.parent = parent
        self.current_x = current_x
        self.current_y = current_y
        self.points = points
        self.time_passed = 0
        self.create_shape()

    def create_shape(self):
        self.shape = self.parent.canvas.create_text(
            (self.current_x, self.current_y), text = self.points,
            fill='#bbbbbb', justify='center', font = ('Arial', 14))
    
    def self_destroy(self):
        self.parent.canvas.delete(self.shape)
        self.parent.points.pop(self.parent.points.index(self))

    def move(self):
        self.parent.canvas.move(self.shape, 0, -1.5)
        self.time_passed += 1


class GameChicken:
    
    def __init__(self, parent, points, size, amplitude, 
                 velocity, flying_range, layer):
        self.parent = parent
        self.points = points
        self.width = self.height = size
        self.amplitude = amplitude
        self.velocity = randint(velocity - 10, velocity + 10) / 100
        self.flying_range = flying_range
        self.layer = layer
        self.alive = True
        self.special = False
        self.set_coordinates()
        self.set_delta_values()
        self.create_shape()

    def set_coordinates(self):
        self.initial_x = choice([0 - self.width, CANVAS_WIDTH])
        self.current_x = self.initial_x
        self.initial_y = randint(
            self.flying_range[0] + self.amplitude,
            self.flying_range[1] - self.height - self.amplitude)
        self.current_y = self.initial_y

    def set_delta_values(self):
        self.delta_x = self.velocity if self.initial_x < 0 else -self.velocity
        self.delta_y = 0.5

    def create_shape(self):
        self.shape = self.parent.canvas.create_rectangle(
            (0, 0), (self.width, self.height),
            fill = f"#{self.get_random_hex_color()}", outline="")
        self.parent.canvas.tag_lower(self.shape, self.layer)
        self.parent.canvas.moveto(self.shape, self.initial_x, self.initial_y)
        self.parent.canvas.tag_bind(
            self.shape, '<Button-1>', lambda event: self.kill())

    def is_on_canvas(self):
        if (self.current_x >= -self.width and 
            self.current_x <= CANVAS_WIDTH and 
            self.current_y <= CANVAS_HEIGHT):
            return True
        else:
            return False
        
    def make_special(self):
        self.special = True
        self.points *= 2

    def get_random_hex_color(self):
        return ''.join(choices("456789abcdef", k = 6))

    def change_color(self):
        self.parent.canvas.itemconfigure(
            self.shape, fill = f"#{self.get_random_hex_color()}")

    def self_destroy(self):
        self.parent.canvas.delete(self.shape)
        self.parent.chickens.pop(self.parent.chickens.index(self))

    def move(self):
        match self.alive:
            case True:
                self.parent.canvas.move(self.shape, self.delta_x, self.delta_y)
                if abs(self.current_y - self.initial_y) >= self.amplitude:
                    self.delta_y *= -1 
            case False:
                    self.parent.canvas.move(self.shape, self.delta_x/2, 2)
        self.current_x += self.delta_x
        self.current_y += self.delta_y

    def kill(self):
        if self.parent.ammo > 0:
            self.alive = False
            self.parent.count += self.points
            self.parent.canvas.tag_unbind(self.shape, '<Button-1>')
            new_points = GamePoints(
                self.parent, self.current_x, self.current_y, self.points)
            self.parent.points.append(new_points)
 

class GameChickenSmall(GameChicken):

    def __init__(self, parent, points = 25, size = 8, 
                 amplitude = 20, velocity = 100, layer = 1,
                 flying_range = (0, CANVAS_HEIGHT*3//5)):
        super().__init__(parent, points, size, amplitude, 
                         velocity, flying_range, layer)
        if random() < 0.05: self.make_special()
    

class GameChickenMedium(GameChicken):

    def __init__(self, parent, points = 10, size = 16, 
                 amplitude = 25, velocity = 125, layer = 2, 
                 flying_range = (CANVAS_HEIGHT*1//5, CANVAS_HEIGHT*4//5)):
        super().__init__(parent, points, size, amplitude, 
                         velocity, flying_range, layer)
        if random() < 0.05: self.make_special()


class GameChickenLarge(GameChicken):

    def __init__(self, parent, points = 5, size = 32, 
                 amplitude = 30, velocity = 150, layer = 3, 
                 flying_range = (CANVAS_HEIGHT*1//5, CANVAS_HEIGHT*3//4)):
        super().__init__(parent, points, size, amplitude, 
                         velocity, flying_range, layer)


class GameChickenHuge(GameChicken):

    def __init__(self, parent, points = 5, size = 64, 
                 amplitude = 25, velocity = 125, layer = 4, 
                 flying_range = (CANVAS_HEIGHT*3//5, CANVAS_HEIGHT*4//5)):
        super().__init__(parent, points, size, amplitude, 
                         velocity, flying_range, layer)


class GameHighscore():
    
    def __init__(self):
        self.user_name = None
        self.user_scores = list()
        self.new_high_score = False
        self.all_scores = TEXT.LIST_OF_PLAYERS
    
    def set_user_name(self, user_name):
        self.user_name = user_name

    def update(self, new_score):
        if new_score > self.all_scores[-1][1]:
            self.all_scores.pop()
            self.all_scores.append((self.user_name, new_score))
            self.all_scores.sort(key = lambda x: int(x[1]), reverse = True)
            self.new_high_score = True


class GameView(View):

    def __init__(self, parent_window):
        super().__init__(parent_window)
        self.window = parent_window
        self.grid(row = 0, column = 0, sticky = (tk.N, tk.E, tk.S, tk.W))
        self.controller = None


class GameViewStart(GameView):

    def __init__(self, parent_window):
        super().__init__(parent_window)
        self.create_grid(5, 1)
        self.rowconfigure(0, weight = 0)
        self.rowconfigure(1, weight = 0)
        self.rowconfigure(2, weight = 0)
        self.rowconfigure(3, weight = 0)
        self.rowconfigure(4, weight = 0)
        self.create_intro1_text()
        self.create_title()
        self.create_intro2_text()
        self.create_user_name_entry()
        self.create_start_button()
        self.configure(style="Game.TFrame")
        self.app = parent_window
        self.highscore = parent_window.highscore

    def create_intro1_text(self):
        self.label_text = ttk.Label(
            self, font = ("Arial", 12), justify = tk.CENTER, 
            style = 'Game.TLabel', anchor = tk.N, 
            text = f"\n\n{TEXT.GAME_INTRO1}", wraplength = 900)
        self.label_text.grid(
            row = 0, column = 0, sticky = (tk.E, tk.W))

    def create_title(self):
        self.label_title = ttk.Label(
            self, text = TEXT.GAME_TITLE, justify = tk.CENTER, 
            style = 'Game.TLabel', anchor = tk.S, 
            font = ("Arial", 18, 'bold'))
        self.label_title.grid(
            row = 1, column = 0, pady = 30, sticky = tk.S)

    def create_intro2_text(self):
        self.label_text = ttk.Label(
            self, font = ("Arial", 12), justify = tk.CENTER, 
            style = 'Game.TLabel', anchor = tk.N, 
            text = f"{TEXT.GAME_INTRO2}\n", wraplength = 900)
        self.label_text.grid(
            row = 2, column = 0, sticky = (tk.E, tk.W))

    def create_user_name_entry(self):
        self.user_name = tk.StringVar()
        self.user_name.set(TEXT.NAME_ENTRY)
        self.entry_name = ttk.Entry(
            self, text = self.user_name, justify = tk.CENTER, width = 25,
            font = ("TkDefaultFont", 12))
        self.entry_name.grid(
            row = 3, column = 0, sticky = tk.N, ipadx=5, ipady=8, pady=10)
        self.entry_name.bind(
            '<KeyRelease>', lambda event: self.on_keyrelease_entry_field())
        self.entry_name.bind(
            '<Return>', lambda event: self.on_return_entry_field(), add = '+')
        self.entry_name.focus()
        self.entry_name.select_range(0,100)
    
    def create_start_button(self):
        self.button_start = ttk.Button(
            self, text = TEXT.START_GAME, state = 'disabled',
            width = 34, command = self.on_click_start_button)
        self.button_start.grid(row = 4, column = 0, pady = 0, sticky = tk.N)
        
    def on_return_entry_field(self):
        if self.entry_name.get().strip() != "":
            self.on_click_start_button()

    def on_keyrelease_entry_field(self):
        if self.entry_name.get().strip() != "":
            self.button_start['state'] = 'enabled'
        else:
            self.button_start['state'] = 'disabled'

    def on_click_start_button(self):
        if self.controller:
            self.controller.prepare_new_game(self.entry_name.get())


class GameViewAction(GameView):

    def __init__(self, parent_window):
        super().__init__(parent_window)
        self.create_grid(1, 1)
        self.create_canvas()
        self.create_landscape()
        self.create_overlay()
        self.MAX_AMMO = 6
        self.DURATION_IN_SECONDS = 90
        self.DELTA_TIME_IN_MS = 10

    def create_canvas(self):
        self.canvas = tk.Canvas(
            self, width = CANVAS_WIDTH, height = CANVAS_HEIGHT,
            bg = '#333333', cursor = 'crosshair')
        self.canvas.grid(row = 0, column = 0)
        self.canvas.bind(
            '<Button-1>', lambda event: self.reduce_ammo())
        self.canvas.bind(
            '<Button-2>', lambda event: self.reload_ammo(), add='+')
        self.canvas.bind(
            '<Button-3>', lambda event: self.reload_ammo(), add='+')

    def create_landscape(self):
        landscape_layers = (
            (0.67, '#444444'), (0.76, '#555555'), (0.87, '#666666'))
        for i in landscape_layers:
            self.canvas.create_rectangle(
                (0, int(i[0] * CANVAS_HEIGHT)), (CANVAS_WIDTH, CANVAS_HEIGHT),
                fill = i[1], outline = '')

    def create_overlay(self):
        PADDING = 20
        self.overlay_time = self.canvas.create_text(
            (PADDING, PADDING), anchor = 'nw',
            fill = 'white', justify = 'left', font = ('Arial', 24))
        self.overlay_score = self.canvas.create_text(
            (CANVAS_WIDTH - PADDING, PADDING), anchor = 'ne',
            fill = 'white', justify = 'right', font = ('Arial', 24))
        self.overlay_ammo = self.canvas.create_text(
            (CANVAS_WIDTH-PADDING, CANVAS_HEIGHT-PADDING), anchor = 'se',
            fill = 'white', justify = 'right', font = ('Arial', 24, 'bold'))

    def start_new_game(self):
        self.set_focus_on_canvas()
        self.chickens = list()
        self.points = list()
        self.count = 0
        self.ammo = self.MAX_AMMO
        self.seconds_remaining = self.DURATION_IN_SECONDS
        self.seconds_passed = 0
        self.start_time = time.time()
        self.run_game()

    def set_focus_on_canvas(self):
        self.canvas.config(highlightthickness = 0)
        self.canvas.focus_set()
        self.canvas.focus()

    def end_game(self):
        for i in self.chickens: self.canvas.delete(i.shape)
        self.chickens.clear()
        for i in self.points: self.canvas.delete(i.shape)
        self.points.clear()
        if self.controller:
            self.controller.update_high_score(self.count)
            self.controller.show_high_score()

    def reduce_ammo(self):
        if self.ammo != 0: self.ammo -= 1

    def reload_ammo(self):
        if self.ammo == 0: self.ammo = self.MAX_AMMO

    def update_time(self):
        if time.time() - (self.start_time + self.seconds_passed) >= 1:
            self.seconds_passed += 1
            self.seconds_remaining -= 1

    def get_time_in_minutes(self):
        minutes = self.seconds_remaining // 60
        seconds = self.seconds_remaining % 60
        return f"{minutes}:{seconds:02d}"

    def spawn_chickens(self):
        if random() < 0.007: self.chickens.append(GameChickenSmall(self))
        if random() < 0.008: self.chickens.append(GameChickenMedium(self))
        if random() < 0.009: self.chickens.append(GameChickenLarge(self))
        if random() < 0.001: self.chickens.append(GameChickenHuge(self))

    def update_overlay(self):
        self.canvas.itemconfigure(self.overlay_score, text=f'{self.count}')
        self.canvas.itemconfigure(self.overlay_time,
                                  text = self.get_time_in_minutes())
        self.canvas.itemconfigure(self.overlay_ammo,
                                  text=f'{' I' * self.ammo}')

    def run_game(self):
        self.spawn_chickens()
        for i in self.chickens:
            i.move() if i.is_on_canvas() else i.self_destroy()
            if i.special is True: i.change_color()
        for i in self.points:
            i.move() if i.time_passed < 25 else i.self_destroy()
        self.update_overlay()
        self.update_time()
        if self.seconds_remaining >= 0:
            return self.canvas.after(self.DELTA_TIME_IN_MS, self.run_game)
        else:
            return self.end_game()


class GameViewScore(GameView):

    def __init__(self, parent_window):
        super().__init__(parent_window)
        self.create_grid(5, 3)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(4, weight=3)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.create_title()
        self.create_list_frame()
        self.create_label_ranks()
        self.create_label_names()
        self.create_label_scores()
        self.create_label_points()
        self.create_label_message()
        self.create_button_again()

    def create_title(self):
        self.label_title = ttk.Label(
            self, text = TEXT.GAME_SCORE_TITLE, justify = tk.CENTER, 
            style = 'Game.TLabel', anchor = tk.S, 
            font = ("Arial", 18, 'bold'))
        self.label_title.grid(
            row = 0, column = 0, pady = 30, sticky = tk.S, columnspan=3)

    def create_list_frame(self):
        self.list_frame = ttk.Frame(self)
        self.list_frame.grid(row = 1, column=1, sticky=(tk.W, tk.E))
        self.list_frame.rowconfigure(0, weight=0)
        self.list_frame.columnconfigure(0, weight=1)
        self.list_frame.columnconfigure(1, weight=1)
        self.list_frame.columnconfigure(2, weight=1)

    def create_label_ranks(self):
        self.label_ranks = ttk.Label(
            self.list_frame, text = "", justify = tk.RIGHT, anchor=tk.E,
            font = ("Arial", 12), style = 'Game.TLabel')
        self.label_ranks.grid(row = 0, column = 0)

    def create_label_names(self):
        self.label_names = ttk.Label(
            self.list_frame, text = "", justify = tk.LEFT, anchor=tk.N,
            font = ("Arial", 12), style = 'Game.TLabel')
        self.label_names.grid(row = 0, column = 1)

    def create_label_scores(self):
        self.label_scores = ttk.Label(
            self.list_frame, text = "", justify = tk.RIGHT, anchor=tk.W,
            font = ("Arial", 12), style = 'Game.TLabel')
        self.label_scores.grid(row = 0, column = 2)

    def create_label_points(self):
        self.label_points = ttk.Label(self, text = "", style = 'Game.TLabel',  
                                      font = ("Arial", 12, 'bold'))
        self.label_points.grid(row = 2, column = 0, columnspan=3)

    def create_label_message(self):
        self.label_msg = ttk.Label(
            self, text = "", wraplength = 500, style = 'Game.TLabel', 
            font = ("Arial", 12), justify = tk.CENTER, anchor = tk.N)
        self.label_msg.grid(row = 3, column = 0, columnspan=3)

    def create_button_again(self):
        self.button_again = ttk.Button(
            self, text = TEXT.PLAY_AGAIN, width = 34,
            command = self.on_click_button_again)
        self.button_again.grid(row = 4, column = 0, columnspan=3)

    def on_click_button_again(self):
        self.controller.prepare_new_game()


class GameController():

    def __init__(self, highscore, views, switcher):
        self.highscore = highscore
        self.views = views
        self.switch_to_view = switcher

    def prepare_new_game(self, user_name = None):
        if user_name is not None: self.highscore.set_user_name(user_name)
        self.highscore.new_high_score = False
        self.switch_to_view('ACTION')
        self.views['ACTION'].start_new_game()

    def update_high_score(self, new_score):
        self.highscore.update(new_score)
        self.views['SCORE'].label_points['text'] = f"{new_score} Punkte"
        if self.highscore.new_high_score is True:
            message = choice(TEXT.NEW_HIGHSCORE)
        else:
            message = choice(TEXT.NO_HIGHSCORE)
        self.views['SCORE'].label_msg['text'] = message
        ranks = ""
        names = ""
        scores = ""
        for i in self.highscore.all_scores:
            ranks += f"{self.highscore.all_scores.index(i)+1}.\n"
            names += f"{i[0]}\n"
            scores += f"{i[1]}\n"
        self.views['SCORE'].label_ranks['text'] = ranks
        self.views['SCORE'].label_names['text'] = names
        self.views['SCORE'].label_scores['text'] = scores

    def show_high_score(self):
        self.switch_to_view('SCORE')


class GameWindow(Window, tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.configure_window(
            TEXT.GAME_TITLE, CANVAS_WIDTH + 4, CANVAS_HEIGHT + 4)
        self.center_window_on_screen()
        self.highscore = GameHighscore()
        self.views = {
            'START' : GameViewStart(self),
            'ACTION' : GameViewAction(self),
            'SCORE' : GameViewScore(self)
        }
        self.set_controller()
        self.switch_to_view('START')

    def set_controller(self):
        self.controller = GameController(
            self.highscore, self.views, self.switch_to_view)
        for view in self.views.values():
            view.set_controller(self.controller)

    def switch_to_view(self, next_view):
        match next_view:
            case 'START': self.views['START'].tkraise()
            case 'ACTION': self.views['ACTION'].tkraise()
            case 'SCORE': self.views['SCORE'].tkraise()


app = MainWindow()
app.mainloop()