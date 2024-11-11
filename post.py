import uuid


class Post:
    def __init__(self, title, author, text) -> None:
        self.id = uuid.uuid4().hex
        self.title = title
        self.author = author
        self.text = text

    def get_content(self) -> dict:
        return {
            "author": self.author,
            "title": self.title,
            "text": self.text,
        }
