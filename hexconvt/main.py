from .aicontroller import AiController
from .colormanager import ColorManager
from .gui import Gui


class Application:

    def __init__(self):
        color_manager = ColorManager()
        ai_controller = AiController()
        self.gui = Gui(color_manager, ai_controller)

    def run(self):
        self.gui.mainloop()
