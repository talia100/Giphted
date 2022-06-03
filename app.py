import json
from urllib import parse, request
from flask import Flask, render_template
app = Flask(__name__)
from flask_login import current_user, login_user, login_required, logout_user
from models import db, login, UserModel

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
def home():
  return render_template('home.html')

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
