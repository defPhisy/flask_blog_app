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
        content = request.form.get("content")

        STORAGE.add_post(title, author, content)

        return redirect(url_for("index"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
