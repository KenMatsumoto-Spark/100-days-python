from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#-------------------------------------- USING DATA BASE WITH SQLITE3 -----------------
# db = sqlite3.connect("book-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

#-------------------------------------- USING DATA BASE WITH SQLALCHEMY -------------
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

db.create_all()

@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books, shelf_empty=len(all_books))


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

