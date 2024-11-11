class Post:
    __ID = 0

    def __init__(self, title, author, content) -> None:
        self.id = self.__ID
        self.title = title
        self.author = author
        self.content = content
        self.__ID += 1

    def get_dict(self) -> dict:
        return {
            "id": self.id,
            "author": self.author,
            "title": self.title,
            "content": self.content,
        }
