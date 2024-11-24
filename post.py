import uuid


class Post:
    """
    Represents a blog post with a unique identifier, title, author, and text.
    """

    def __init__(self, title: str, author: str, text: str) -> None:
        """
        Initializes a new Post instance.

        Args:
            title (str): The title of the post.
            author (str): The author of the post.
            text (str): The content of the post.
        """
        self.id = uuid.uuid4().hex
        self.title = title
        self.author = author
        self.text = text

    def get_content(self) -> dict:
        """
        Retrieves the post's content as a dictionary.

        Returns:
            dict: A dictionary containing the post's title, author, and text.
        """
        return {
            "author": self.author,
            "title": self.title,
            "text": self.text,
        }
