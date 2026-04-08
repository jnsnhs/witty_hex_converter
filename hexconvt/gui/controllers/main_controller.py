from random import choice, random
from ...guitext import GuiText, LabelFrameTitles


class MainViewController:

    def __init__(self, app, model, view) -> None:
        self.app = app
        self.model = model
        self.view = view
        self.view.user_input.set(f"#{self.model.hex_code}")
        self.validate_input(self.model.hex_code)
        self.view.comment_frame.config(
            text=LabelFrameTitles.COMMENT_FRAME_DEFAULT)
        self.insert_comment(GuiText.DEFAULT_COMMENT)
        self.view.cbox_color_select.select_range(0, 7)

    def set_input_to_random_hex_code(self) -> None:
        random_hex_code = self.model.get_random_hex_string(6)
        self.view.user_input.set(f"#{random_hex_code}")

    def validate_input(self, str_value) -> None:
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
                rnd_frame_title = choice(
                    LabelFrameTitles.COMMENT_FRAME_TRANSPARENCY)
                self.insert_comment(choice(GuiText.FOUR_DIGIT_CODES))
                self.display_message('TRANSPARENT')
            elif self.model.is_hex_code(str(str_value), (8,)):
                self.view.user_input.set(f'#{str_value}')
                rnd_frame_title = choice(
                    LabelFrameTitles.COMMENT_FRAME_TRANSPARENCY)
                self.insert_comment(choice(GuiText.EIGHT_DIGIT_CODES))
                self.display_message('TRANSPARENT')
            elif str_value == "":
                rnd_frame_title = choice(
                    LabelFrameTitles.COMMENT_FRAME_BAD_INPUT)
                self.insert_comment(choice(GuiText.NO_INPUT))
                self.display_message('EMPTY_INPUT')
            else:
                rnd_frame_title = choice(
                    LabelFrameTitles.COMMENT_FRAME_BAD_INPUT)
                self.insert_comment(choice(GuiText.MISC_INVALID_INPUTS))
                self.display_message('INVALID_INPUT')
            self.view.comment_frame.config(text=rnd_frame_title)

    def display_rgb_code(self) -> None:
        self.view.label_css_name.grid_remove()
        rgb = self.model.rgb_code
        self.view.label_rgb_code["text"] = f"({rgb[0]},{rgb[1]},{rgb[2]})"
        self.view.set_rgb_label_bg_color(self.model.hex_code)
        self.view.set_font_color(self.get_contrasting_color())
        if self.model.css_name:
            self.view.label_css_name['text'] = self.model.css_name
            self.view.label_css_name.grid()

    def display_message(self, type) -> None:
        self.view.label_css_name.grid_remove()
        self.view.set_rgb_label_bg_color("dddddd")
        self.view.set_font_color("#aaaaaa")
        match type:
            case 'INVALID_INPUT':
                self.view.label_rgb_code['text'] = GuiText.LABEL_INVALID_INPUT
            case 'EMPTY_INPUT':
                self.view.label_rgb_code['text'] = GuiText.LABEL_EMPTY_INPUT
            case 'TRANSPARENT':
                self.view.label_rgb_code['text'] = \
                    GuiText.LABEL_TRANSPARENT_COLOR

    def comment_on_hex_code(self, hex_input) -> None:
        match len(hex_input):
            case 3:
                rnd_frame_title = choice(
                    LabelFrameTitles.COMMENT_FRAME_VALID_CODE)
                rnd_comment = choice(GuiText.THREE_DIGIT_CODES)
            case 6:
                try:
                    rnd_frame_title = choice(
                        LabelFrameTitles.COMMENT_FRAME_WEB_COLOR)
                    rnd_comment = choice(
                        GuiText.NAMED_CODES[hex_input.upper()])
                except Exception:
                    if random() < 0.75:
                        rnd_frame_title = choice(
                            LabelFrameTitles.COMMENT_FRAME_VALID_CODE)
                        rnd_comment = choice(GuiText.MISC_CODES)
                    else:
                        rnd_frame_title = choice(
                            LabelFrameTitles.COMMENT_FRAME_RANDOM_REMARK)
                        rnd_comment = choice(GuiText.RANDOM)
        self.view.comment_frame.config(text=rnd_frame_title)
        self.insert_comment(rnd_comment)

    def insert_comment(self, comment) -> None:
        self.view.comment.set(comment)

    def get_contrasting_color(self) -> str:
        luminance = (self.model.rgb_code[0] * 0.2126 +
                     self.model.rgb_code[1] * 0.7152 +
                     self.model.rgb_code[2] * 0.0722)
        return 'white' if luminance < 140 else 'black'

    def toggle_topmost(self, bool_value) -> None:
        self.app.call('wm', 'attributes', '.', '-topmost', bool_value)
