from post import Post
from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/5abcca6f4e39b4955965")
posts = response.json()

post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/post/<int:index>')
def get_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects)

if __name__ == "__main__":
    app.run(debug=True)
