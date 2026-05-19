from random import choices

from .color import Color


class ColorManager():

    HEX_SYMBOLS = "0123456789abcdef"

    def __init__(self) -> None:
        self.colors_converted = list()
        self.set_initial_color()

    def set_initial_color(self) -> None:
        self.colors_converted.append(self.get_random_color())

    def get_random_color(self) -> Color:
        return Color(self.get_random_hex_string(6))

    def get_number_of_unique_colors_converted(self) -> int:
        return len(set(self.colors_converted))

    def is_hex_string(self, string: str) -> bool:
        for i in string:
            if i.casefold() not in self.HEX_SYMBOLS:
                return False
        return True

    def is_color_code(self, string: str, valid_lengths=(3, 4, 6, 8)) -> bool:
        if self.is_hex_string(string):
            return True if len(string) in valid_lengths else False
        else:
            return False

    def get_random_hex_string(self, length: int) -> str:
        return "".join(choices(self.HEX_SYMBOLS, k=length))

    def create_color(self, string: str) -> Color:
        if self.is_color_code(string, (3, 6)):
            return Color(string)
        else:
            if self.is_color_code(str(string), (4,)):
                raise TransparentColorError
            elif self.is_color_code(str(string), (8,)):
                raise TransparentColorError
            elif string == "":
                raise MissingInputError
            else:
                raise InvalidInputError

    def add_to_converted_colors(self, color: Color) -> None:
        self.colors_converted.append(color)

    def get_current_color(self) -> Color:
        return self.colors_converted[-1]


class InvalidInputError(Exception):

    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return "Eingabe\nungültig"


class MissingInputError(Exception):

    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return "Leere\nEingabe"


class TransparentColorError(Exception):

    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return "Anzeige\nnicht\nmöglich"
