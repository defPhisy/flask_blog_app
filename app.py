from flask import Flask, redirect, render_template, request, url_for
from storage import Storage
from werkzeug import Response

STORAGE = Storage("blog_posts.json")
app = Flask(__name__)


@app.route("/")
def index() -> str:
    """
    Displays the homepage with a list of all blog posts.

    Returns:
        str: Rendered HTML of the homepage.
    """
    blog_posts = STORAGE.get_posts()
    return render_template("index.html", posts=blog_posts)


@app.route("/add", methods=["GET", "POST"])
def add() -> Response | str:
    """
    Handles adding a new blog post.

    - On GET: Displays the add post form.
    - On POST: Adds the new post and redirects to the homepage.

    Returns:
        str: Rendered HTML or redirect response.
    """
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        text = request.form.get("text")

        STORAGE.add_post(title, author, text)
        return redirect(url_for("index"))
    return render_template("add.html")


@app.route("/delete/<post_id>")
def delete(post_id) -> Response:
    """
    Deletes a blog post by its ID and redirects to the homepage.

    Args:
        post_id (str): The ID of the post to delete.

    Returns:
        Response: Redirect to the homepage.
    """
    STORAGE.delete(post_id)
    return redirect(url_for("index"))


@app.route("/update/<post_id>", methods=["GET", "POST"])
def update(post_id: str):
    """
    Handles updating an existing blog post.

    - On GET: Displays the update form for the post.
    - On POST: Updates the post and redirects to the homepage.

    Args:
        post_id (str): The ID of the post to update.

    Returns:
        str: Rendered HTML or redirect response.
    """
    post = STORAGE.get_post(post_id)

    if post is None:
        return "Post not found", 404

    if request.method == "POST":
        title = request.form.get("title", "N/A")
        author = request.form.get("author", "N/A")
        text = request.form.get("text", "N/A")
        STORAGE.update_post(post_id, title, author, text)
        return redirect(url_for("index"))

    return render_template("update.html", post_id=post_id, post=post)


@app.errorhandler(404)
def page_not_found(error):
    """
    Handles 404 errors with a custom error page.

    Args:
        error: The error object.

    Returns:
        tuple: Rendered HTML of the 404 page and status code.
    """
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
