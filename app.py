from flask import Flask, render_template, redirect, request, url_for
import pyjokes
import random
import requests
from dadjokes import Dadjoke


app = Flask(__name__)
jokes = pyjokes.get_jokes("en")
programmingJokeList = []
dadJokeList = []
for i in jokes:
        programmingJokeList.append(i)

def CollectDadJokes():
      i = 0
      while i < 100:
            dadJoke = Dadjoke().joke
            dadJokeList.append(dadJoke)
            i += 1
CollectDadJokes()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/newprogrammingjoke")
def get_programming_joke():
      programmingJoke = random.choice(programmingJokeList)
      return render_template("index.html", programmingJoke=programmingJoke)

@app.route("/newdadjoke")
def get_dad_joke():
    dadJoke = random.choice(dadJokeList)
    return render_template("index.html", dadJoke=dadJoke)