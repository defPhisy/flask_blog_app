import uuid


class Post:
    def __init__(self, title, author, content) -> None:
        self.id = uuid.uuid4().hex
        self.title = title
        self.author = author
        self.content = content

    def get_dict(self) -> dict:
        return {
            "id": self.id,
            "author": self.author,
            "title": self.title,
            "content": self.content,
        }
