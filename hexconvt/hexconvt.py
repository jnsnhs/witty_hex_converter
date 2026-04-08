from .gui.gui import AppController


class Application:

    def __init__(self):
        self.controller = AppController("HEX 9000", 275, 445)

    def run(self):
        self.controller.mainloop()
