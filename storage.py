import json
import os
from post import Post


class Storage:
    __DB_FOLDER = "./data"

    def __init__(self, filename) -> None:
        self.filename = filename
        self.folder = self.__DB_FOLDER
        self.path = os.path.join(self.folder, self.filename)
        self.posts = self.get_posts()

    def get_posts(self) -> list:
        with open(self.path, "r") as file:
            return json.load(file)

    def save_posts(self) -> None:
        with open(self.path, "w") as file:
            file.write(json.dumps(self.posts))

    def add_post(self, title, author, content) -> None:
        new_post = Post(title, author, content)
        new_dict = new_post.get_dict()
        self.posts.append(new_dict)
        self.save_posts()
