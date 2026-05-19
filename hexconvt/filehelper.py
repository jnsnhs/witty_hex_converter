import csv
import json
import sys

from tkinter import messagebox as msgbox


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


def show_file_loading_error(path_to_file: str) -> None:
    msgbox.showerror(
        title="Fehlermeldung",
        message="Das Programm kann nicht gestartet werden.",
        detail=f"Die Datei\n\n{path_to_file}\n\nkonnte nicht importiert "
        "werden."
    )


def display_file_loading_error(path_to_file: str) -> None:
    msgbox.showerror(
        title="Fehlermeldung",
        message="Das Programm kann nicht gestartet werden.",
        detail=f"Die Datei\n\n{path_to_file}\n\nkonnte nicht importiert "
        "werden."
    )
