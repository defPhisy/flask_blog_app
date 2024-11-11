from flask import Flask, render_template
from storage import Storage

app = Flask(__name__)


@app.route("/")
def index():
    storage = Storage("blog_posts.json")
    blog_posts = storage.get_posts()
    return render_template("index.html", posts=blog_posts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
