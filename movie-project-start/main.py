from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

THE_MOVIE_SEARCH = "https://api.themoviedb.org/3/search/movie"
THE_MOVIE_FETCH = "https://api.themoviedb.org/3/movie/"

API_KEY = ""

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new_movie_collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer)
    description = db.Column(db.String(250))
    rating = db.Column(db.Float())
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250))

db.create_all()

new_movie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)

#db.session.add(new_movie)
db.session.commit()

class MovieForm(FlaskForm):
    rating = StringField('Your rating out of 10')
    review = StringField('Your Review')
    submit = SubmitField('Done')

class AddMovie(FlaskForm):
    name = StringField('Movie TItle', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["POST", "GET"])
def edit():
    form = MovieForm()
    movie_to_update = Movie.query.get(request.args.get("id"))
    if form.validate_on_submit():
        if form.rating.data != "":
            movie_to_update.rating = form.rating.data
        if form.review.data != "":
            movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form)

@app.route("/delete")
def delete():
    movie_to_delete = Movie.query.get(request.args.get("id"))
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["POST", "GET"])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        params = {
            "api_key": API_KEY,
            "query": form.name.data
        }
        response = requests.get(url=THE_MOVIE_SEARCH, params=params)
        movies_list = response.json()['results']
        return render_template('select.html', movies=movies_list)

    return render_template('add.html', form=form)

@app.route('/find')
def add_selected():
    params = {
        "api_key": API_KEY,
    }
    response = requests.get(url=f"{THE_MOVIE_FETCH}{request.args.get('id')}", params=params)
    new_movie_data = response.json()
    new_movie = Movie(
        title=new_movie_data["title"],
        year=new_movie_data["release_date"].split("-")[0],
        description=new_movie_data["overview"],
        img_url="https://image.tmdb.org/t/p/w500/"+new_movie_data["poster_path"]
    )
    db.session.add(new_movie)
    db.session.commit()
    movie = Movie.query.filter_by(title=new_movie_data["title"]).first()
    return redirect(url_for('edit', id=movie.id))

if __name__ == '__main__':
    app.run(debug=True)
