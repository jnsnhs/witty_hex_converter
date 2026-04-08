import os

from ..defaults import PROJECT_DIR


class Settings:

    def __init__(self, root_dir=PROJECT_DIR):
        self.root = root_dir
        self.static = os.path.join(self.root, "static")
