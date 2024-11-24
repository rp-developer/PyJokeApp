from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
import pyjokes
import random
import requests
from dadjokes import Dadjoke


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dadjokes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
jokes = pyjokes.get_jokes("en")
programmingJokeList = []
dadJokeList = []
for i in jokes:
        programmingJokeList.append(i)

class DadJoke(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      joke = db.Column(db.String(500), nullable=False)
      
      def __repr__(self):
            return f'<DadJoke {self.id}: {self.joke}>'
def create_db():
      with app.app_context():
            db.create_all()
def CollectDadJokes():
    with app.app_context():
        # Correct query to count the number of jokes in the database
        if db.session.query(DadJoke).count() == 0:  # Corrected this line
            print("No jokes found in the database. Adding jokes now...")
            i = 0
            while i < 100:
                dadJoke = Dadjoke().joke
                new_joke = DadJoke(joke=dadJoke)
                db.session.add(new_joke)  # Add the new joke
                if i % 10 == 0:  # Commit every 10 jokes for better performance
                    db.session.commit()
                i += 1
            db.session.commit()  # Commit any remaining jokes
        else:
            print("Jokes already exist in the database.")

create_db
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
    random_dad_joke = DadJoke.query.order_by(db.func.random()).first()
    return render_template("index.html", dadJoke=random_dad_joke.joke)
if __name__ == "__main__":
      app.run(debug=True)