import json
import os


class Storage:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.path = os.path.join("./data", self.filename)

    def get_posts(self):
        with open(self.path, "r") as file:
            return json.load(file)
