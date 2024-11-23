from flask import Flask, render_template, request, url_for
import pyjokes
import random
app = Flask(__name__)
jokes = pyjokes.get_jokes("en")

jokeList = []
for i in jokes:
        jokeList.append(i)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/newjoke")
def get_joke():
      joke = random.choice(jokeList)
      return render_template("index.html", joke=joke)
