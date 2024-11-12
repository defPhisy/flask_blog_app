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

    def get_posts(self) -> dict:
        with open(self.path, "r") as file:
            data = json.load(file)
            return data

    def get_post(self, post_id) -> dict:
        return self.posts[post_id]

    def save_posts(self) -> None:
        with open(self.path, "w") as file:
            file.write(json.dumps(self.posts))

    def add_post(self, title, author, text) -> None:
        new_post = Post(title, author, text)
        content_dict = new_post.get_content()
        post_id = new_post.id
        self.posts[post_id] = content_dict
        self.save_posts()

    def delete(self, post_id) -> None:
        if post_id in self.posts:
            del self.posts[post_id]
            self.save_posts()

    def update_post(self, post_id, title, author, text) -> None:
        post_content = {"title": title, "author": author, "text": text}
        self.posts[post_id] = post_content
        self.save_posts()
