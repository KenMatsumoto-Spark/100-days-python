from flask import Flask, render_template
import random
import datetime
import requests

GENDERIZE_ENDPOINT = "https://api.genderize.io"
AGIFY_ENDPOINT = "https://agify.io"

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(0, 223)
    year = datetime.datetime.now().year
    return render_template("index.html",
                           rand=random_number,
                           year=year)

@app.route('/guess/<name>')
def guess(name):
    params= {
        "name": name,
    }
    response_gender = requests.get(url=GENDERIZE_ENDPOINT, params=params)
    predict_gender = response_gender.json()["gender"]
    response_age = requests.get(url=f"https://api.agify.io?name={name}")

    predict_age = response_age.json()["age"]

    return render_template("guess.html",
                           name = name,
                           gender = predict_gender,
                           age = predict_age)

@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)