import os
from random import random, choice

from .defaults import COMMENTS_DIR
from .filehelper import import_text_file, import_json_file


class Comments:
    NAMED_CODES = import_json_file(
        os.path.join(COMMENTS_DIR, "named_codes.json"))
    EIGHT_DIGIT_CODES = import_text_file(
        os.path.join(COMMENTS_DIR, "eight_digits.txt"))
    FOUR_DIGIT_CODES = import_text_file(
        os.path.join(COMMENTS_DIR, "four_digits.txt"))
    THREE_DIGIT_CODES = import_text_file(
        os.path.join(COMMENTS_DIR, "three_digits.txt"))
    MISC_CODES = import_text_file(
        os.path.join(COMMENTS_DIR, "valid_codes.txt"))
    RANDOM = import_text_file(
        os.path.join(COMMENTS_DIR, "random_remarks.txt"))
    NO_INPUT = import_text_file(
        os.path.join(COMMENTS_DIR, "missing_input.txt"))
    MISC_INVALID_INPUTS = import_text_file(
        os.path.join(COMMENTS_DIR, "invalid_input.txt"))


class FrameTitles:
    VALID_CODE = [
        "Die KI kommentiert anerkennend:",
        "Die KI gibt sich gönnerhaft:",
        "Die KI lobt Sie und Ihr Tun:",
        "Die KI bestärkt Ihre Eingabe:"
    ]
    RANDOM_REMARK = [
        "Die KI gerät in Plauderlaune:",
        "Die KI kommt vom Thema ab:",
        "Die KI beginnt zu halluzinieren:",
        "Die KI tut allzu menschlich:"
    ]
    WEB_COLOR = [
        "Die KI zitiert unbekannte Quellen:",
        "Die KI prahlt mit fremdem Wissen:",
        "Die KI greift in ihre Blackbox:",
        "Die KI tut erfahren und eloquent:"
    ]
    BAD_INPUT = [
        "Die KI wundert sich:",
        "Die KI ist irritiert:",
        "Die KI gibt zu bedenken:",
        "Die KI zweifelt an Ihnen:"
    ]
    TRANSPARENCY = [
        "Die KI gibt kleinlaut nach:",
        "Die KI stößt an ihre Grenzen:",
        "Die KI kann auch nicht alles:",
        "Die KI verabscheut Transparenz:",
    ]


class AiController():

    def __init__(self) -> None:
        pass

    def comment_on_hex_code(self, hex_code: str) -> tuple[str, str]:
        match len(hex_code):
            case 3:
                frame_title = choice(FrameTitles.VALID_CODE)
                comment = choice(Comments.THREE_DIGIT_CODES)
            case 6:
                try:
                    frame_title = choice(
                        FrameTitles.WEB_COLOR)
                    comment = choice(Comments.NAMED_CODES[hex_code.upper()])
                except Exception:
                    if random() < 0.75:
                        frame_title = choice(
                            FrameTitles.VALID_CODE)
                        comment = choice(Comments.MISC_CODES)
                    else:
                        frame_title = choice(
                            FrameTitles.RANDOM_REMARK)
                        comment = choice(Comments.RANDOM)
        return (frame_title, comment)

    def comment_on_missing_input(self) -> tuple[str, str]:
        frame_title = choice(FrameTitles.BAD_INPUT)
        comment = choice(Comments.NO_INPUT)
        return (frame_title, comment)

    def comment_on_invalid_input(self) -> tuple[str, str]:
        frame_title = choice(FrameTitles.BAD_INPUT)
        comment = choice(Comments.MISC_INVALID_INPUTS)
        return (frame_title, comment)

    def comment_on_transparency(self, length: int) -> tuple[str, str]:
        frame_title = choice(FrameTitles.TRANSPARENCY)
        if length == 4:
            comment = choice(Comments.FOUR_DIGIT_CODES)
        else:
            comment = choice(Comments.EIGHT_DIGIT_CODES)
        return (frame_title, comment)

    def get_default_frame_title(self) -> str:
        return "Die allwissende KI rät:"

    def get_default_message(self) -> str:
        return "Bitte geben Sie einen gültigen\nHex-Wert ein oder " \
               "wählen Sie eine\nder vordefinierten Webfarben aus."
