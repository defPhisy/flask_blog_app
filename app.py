from flask import Flask, render_template, request, redirect, url_for
from storage import Storage

STORAGE = Storage("blog_posts.json")
app = Flask(__name__)


@app.route("/")
def index():
    blog_posts = STORAGE.get_posts()
    return render_template("index.html", posts=blog_posts)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # We will fill this in the next step

        title = request.form.get("title")
        author = request.form.get("author")
        text = request.form.get("text")

        STORAGE.add_post(title, author, text)

        return redirect(url_for("index"))
    return render_template("add.html")


@app.route("/delete/<post_id>")
def delete(post_id):
    STORAGE.delete(post_id)

    return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
