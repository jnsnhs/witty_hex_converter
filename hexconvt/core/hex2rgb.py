import csv
import os
import sys
from random import choices

from tkinter import messagebox as msgbox
from ..defaults import STATIC_DIR


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
        detail=f"Die Datei\n\n{path_to_file}\n\n""konnte nicht importiert "
        "werden."
    )


color_names_csv_path = os.path.join(STATIC_DIR, "named_colors.csv")
COLOR_NAMES = import_color_names_as_dict(color_names_csv_path)


class MainModel():

    def __init__(self) -> None:
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

    def is_hex_code(self, str_value, valid_lengths=(3, 4, 6, 8)) -> bool:
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
        return "".join(choices(self.HEX_SYMBOLS, k=length))

    def get_full_hex_code(self, short_hex_code) -> str:
        return "".join([i * 2 for i in short_hex_code])

    def get_number_of_unique_colors_converted(self) -> int:
        return len(set(self.colors_converted))
