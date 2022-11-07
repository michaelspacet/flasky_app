from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_user, logout_user
from flask_login.mixins import UserMixin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Length
from werkzeug.security import generate_password_hash, check_password_hash

from dash_apps.ngp.ngp_app import create_ngp_app

app = Flask(__name__)
app.config['SECRET_KEY'] = 'testymctesttest'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager()
login.init_app(app)

create_ngp_app(app)


@login.user_loader
def user_loader(user_id):
    return User.query.filter_by(id=user_id).first()


class User(db.Model, UserMixin):
    id = db.Column(db.String(128), primary_key=True)
    password = db.Column(db.String(128), nullable=False)


class LoginForm(FlaskForm):
    id = StringField("brid")
    password = PasswordField("password", validators=[Length(min=5)])


class RegisterForm(FlaskForm):
    id = StringField("brid")
    password = PasswordField("password", validators=[Length(min=5)])
    repeat_password = PasswordField("repated_password", validators=[Length(min=5)])


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home/')
def home():
    return render_template('home.html')


@app.route('/user_guide/')
def user_guide():
    return render_template('user_guide.html')


@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(id=form.id.data).first()

        if check_password_hash(user.password, form.password.data):
            login_user(user)

            return redirect("/home")

    return render_template("login.html", form=form)


@app.route("/register/", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit() and form.password.data == form.repeat_password.data:
        user = User(
            id=form.id.data, password=generate_password_hash(form.password.data)
        )

        db.session.add(user)
        db.session.commit()

        return redirect("/home")

    return render_template("register.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=80,
            debug=True)
