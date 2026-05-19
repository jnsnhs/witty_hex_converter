import os

from .defaults import STATIC_DIR
from .filehelper import import_color_names_as_dict


class Color():

    HEX_CHARACTERS = "abcdef"
    COLOR_NAMES: dict = import_color_names_as_dict(
        os.path.join(STATIC_DIR, "named_colors.csv"))

    def __init__(self, hex_code: str) -> None:
        self.hex_code: str = hex_code
        self.rgb_code: tuple[int, int, int] = self.get_rgb_from_hex_code(
            self.hex_code)
        self.css_name: str = self.get_name_of_hex_code(self.hex_code)

    def get_decimal_from_hex_string(self, hex_str: str) -> int:
        decimal_value = 0
        for i in range(len(hex_str)):
            if hex_str[i].casefold() in self.HEX_CHARACTERS:
                summand = self.HEX_CHARACTERS.index(hex_str[i].casefold()) + 10
            else:
                summand = hex_str[i]
            decimal_value += int(summand) * 16 ** (len(hex_str) - 1 - i)
        return decimal_value

    def get_rgb_from_hex_code(self, hex_code: str) -> tuple:
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

    def get_name_of_hex_code(self, hex_code: str) -> str:
        for css3_name, hex in self.COLOR_NAMES.items():
            if hex.casefold() == hex_code.casefold():
                return css3_name
        return ""

    def get_full_hex_code(self, short_hex_code: str) -> str:
        return "".join([i * 2 for i in short_hex_code])
