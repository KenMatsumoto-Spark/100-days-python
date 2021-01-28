from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


#Line below only required once, when creating DB. 
db.create_all()

# class Registrationform(FlaskForm):
#     email = StringField('Email', validators=[DataRequired()])
#     name = StringField('Name', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     submit = SubmitField('Register')



@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        if User.query.filter_by(email=request.form.get('email')).first():
            flash("Your email is already registered, please sign in")
            return redirect(url_for('login'))
        hashed_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )

        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=hashed_and_salted_password)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        return redirect(url_for("secrets"))

    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        user_in_db = User.query.filter_by(email=email).first()
        if user_in_db:
            if check_password_hash(user_in_db.password, request.form.get('password')):
                login_user(user_in_db)
                return redirect(url_for("secrets"))
            else:
                flash("Your password is invalid")
        else:
            flash("Your email is invalid")

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', filename='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
