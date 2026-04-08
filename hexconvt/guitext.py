import json
import os
import sys
from tkinter import messagebox

from .defaults import COMMENTS_DIR


def import_text_file(path_to_file: str) -> list:
    result = list()
    try:
        with open(path_to_file, "r", encoding="utf8") as text_file:
            for line in text_file.readlines():
                line = line.strip("\n")
                result.append(line)
    except Exception:
        show_file_loading_error(path_to_file)
        sys.exit(0)
    else:
        return result


def import_json_file(path_to_file: str) -> dict:
    try:
        with open(path_to_file, "r", encoding="utf8") as json_file:
            json_data = json_file.read()
            return json.loads(json_data)
    except Exception:
        show_file_loading_error(path_to_file)
        sys.exit(0)


def show_file_loading_error(path_to_file: str) -> None:
    messagebox.showerror(
        title="Fehlermeldung",
        message="Das Programm kann nicht gestartet werden.",
        detail=f"Die Datei\n\n{path_to_file}\n\nkonnte nicht importiert "
        "werden."
    )


class GuiText:

    LABEL_RANDOM_BTN = "Zufälligen Wert erzeugen"
    LABEL_CONVERT_BTN = "Eingabe konvertieren"
    LABEL_CHECKBOX = "Fenster im Vordergrund halten"

    LABEL_INVALID_INPUT = "Eingabe\nungültig"
    LABEL_EMPTY_INPUT = "Leere\nEingabe"
    LABEL_TRANSPARENT_COLOR = "Anzeige\nnicht\nmöglich"

    DEFAULT_COMMENT = "Bitte geben Sie einen gültigen\nHex-Wert ein oder "
    "wählen Sie eine\nder vordefinierten Webfarben aus."
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


class LabelFrameTitles:

    COMMENT_FRAME_DEFAULT = "Die allwissende KI rät:"
    COMMENT_FRAME_VALID_CODE = [
        "Die KI kommentiert anerkennend:",
        "Die KI gibt sich gönnerhaft:",
        "Die KI lobt Sie und Ihr Tun:",
        "Die KI bestärkt Ihre Eingabe:"
    ]
    COMMENT_FRAME_RANDOM_REMARK = [
        "Die KI gerät in Plauderlaune:",
        "Die KI kommt vom Thema ab:",
        "Die KI beginnt zu halluzinieren:",
        "Die KI tut allzu menschlich:"
    ]
    COMMENT_FRAME_WEB_COLOR = [
        "Die KI zitiert unbekannte Quellen:",
        "Die KI prahlt mit fremdem Wissen:",
        "Die KI greift in ihre Blackbox:",
        "Die KI tut erfahren und eloquent:"
    ]
    COMMENT_FRAME_BAD_INPUT = [
        "Die KI wundert sich:",
        "Die KI ist irritiert:",
        "Die KI gibt zu bedenken:",
        "Die KI zweifelt an Ihnen:"
    ]
    COMMENT_FRAME_TRANSPARENCY = [
        "Die KI gibt kleinlaut nach:",
        "Die KI stößt an ihre Grenzen:",
        "Die KI kann auch nicht alles:",
        "Die KI verabscheut Transparenz:",
    ]
