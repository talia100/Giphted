import json
from urllib import parse, request
from flask import Flask, render_template, redirect
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField,SubmitField
# from wtforms.validators import DataRequired, Length, EqualTo, Email
# from flask_login import current_user, login_user, login_required, logout_user
from models import db, login, UserModel
app = Flask(__name__)

# class loginForm(FlaskForm):
#   email = StringField(label="Enter email", validators=[DataRequired(), Email()])
#   password = PasswordField(label="Enter password", validators=[DataRequired(), Length(min=6, max=16)])
#   submit = SubmitField(label="Login")


# app.secret_key="a secret"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/login.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db.init_app(app)
# login.init_app(app)

# def addUser(email, password):
#     #check if email or username exits
#     user=UserModel()
#     user.set_password(password)
#     user.email=email
#     db.session.add(user)
#     db.session.commit()

# @app.before_first_request
# def create_table():
#     db.create_all()
#     user = UserModel.query.filter_by(email = "talia100@uw.edu").first()
#     if user is None:
#         addUser("talia100@uw.edu","qwerty")

def gif(mood):
  gifs = []
  url = "http://api.giphy.com/v1/gifs/search"

  params = parse.urlencode({
    "q": mood,
    "api_key": "3m4gf6qKSc1vuLPwwPVyCGVk3K5su1nZ",
    "limit": "20"
  })

  with request.urlopen("".join((url, "?", params))) as response:
    data = json.loads(response.read())

  for gif in data['data']:
    gifs.append(gif['images']['fixed_height']['url'])

  return gifs

@app.route("/")
def login():
  return render_template('login.html')


@app.route("/login", methods = ["POST"])
def postLogin():
  return redirect('/home')


@app.route("/home")
def home():
  return render_template('home.html')

# @app.route("/",methods=['GET','POST'])
# def login():
#     form=loginForm()
#     if form.validate_on_submit():
#         if request.method == "POST":
#             email=request.form["email"]
#             pw=request.form["password"]
#             user = UserModel.query.filter_by(email = email).first()
#             if user is not None and user.check_password(pw) :
#                 login_user(user)
#                 return redirect('/home')
#     return render_template("login.html",form=form)

# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect('/login')

@app.route("/sad")
def sad():
  title = "Sad moods"
  gifs = gif("sad")
  return render_template('moods.html', title=title, gifs=gifs)

@app.route("/happy")
def happy():
  title = "Happy moods"
  gifs = gif("happy")
  return render_template('moods.html', title=title, gifs=gifs)

@app.route("/anxious")
def anxious():
  title = "Anxious moods"
  gifs = gif("anxious")
  return render_template('moods.html', title=title, gifs=gifs)

@app.route("/angry")
def angry():
  title = "Angry moods"
  gifs = gif("angry")
  return render_template('moods.html', title=title, gifs=gifs)


if __name__ == "__main__":
  app.run(debug=True)
