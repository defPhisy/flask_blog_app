import json
import os

from post import Post


class Storage:
    """
    Handles storage and retrieval of posts from a JSON file.
    """

    __DB_FOLDER = "./data"

    def __init__(self, filename: str) -> None:
        """
        Initializes the Storage object and loads posts.

        Args:
            filename (str): The name of the JSON file to store posts.
        """
        self.filename = filename
        self.folder = self.__DB_FOLDER
        self.path = os.path.join(self.folder, self.filename)
        self.posts = self.get_posts()

    def get_posts(self) -> dict:
        """
        Loads all posts from the JSON file.

        Returns:
            dict: A dictionary of posts.
        """
        with open(self.path, "r") as file:
            data = json.load(file)
            return data

    def get_post(self, post_id: str) -> dict:
        """
        Retrieves a single post by its ID.

        Args:
            post_id (str): The ID of the post to retrieve.

        Returns:
            dict: The post content.
        """
        return self.posts[post_id]

    def save_posts(self) -> None:
        """
        Saves all posts to the JSON file.
        """
        with open(self.path, "w") as file:
            file.write(json.dumps(self.posts))

    def add_post(self, title, author, text) -> None:
        """
        Adds a new post to the storage.

        Args:
            title (str): The title of the post.
            author (str): The author of the post.
            text (str): The content of the post.
        """
        new_post = Post(title, author, text)
        content_dict = new_post.get_content()
        post_id = new_post.id
        self.posts[post_id] = content_dict
        self.save_posts()

    def delete(self, post_id: str) -> None:
        """
        Deletes a post by its ID.

        Args:
            post_id (str): The ID of the post to delete.
        """
        if post_id in self.posts:
            del self.posts[post_id]
            self.save_posts()

    def update_post(
        self, post_id: str, title: str, author: str, text: str
    ) -> None:
        """
        Updates an existing post with new content.

        Args:
            post_id (str): The ID of the post to update.
            title (str): The new title of the post.
            author (str): The new author of the post.
            text (str): The new content of the post.
        """
        post_content = {"title": title, "author": author, "text": text}
        self.posts[post_id] = post_content
        self.save_posts()
