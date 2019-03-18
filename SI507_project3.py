#__author__ == "Jen Foran (jforan)"

# import os
from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./movies.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
session = db.session



##### Set up Models #####

# Set up association Table between artists and albums

class Director(db.Model):
    __tablename__ = "directors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    movies = db.relationship('Movie',backref='Director')

    def __repr__(self):
        return "{} (ID: {})".format(self.name,self.id)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250),unique=True)
    director_id = db.Column(db.Integer, db.ForeignKey("directors.id")) # ok to be null for now
    mpaa_rating = db.Column(db.String(5))

    def __repr__(self):
        return "{} by {} | {}".format(self.title, self.director_id,self.mpaa_rating)


##### Helper functions #####

def get_or_create_director(director_name):
    director = Director.query.filter_by(name=director_name).first()
    if director:
        return director
    else:
        director = Director(name=director_name)
        session.add(director)
        session.commit()
        return director

##### Set up Controllers (route functions) #####

## Main route
@app.route('/')
def homepage():
    return 'Welcome to this movie list!'

@app.route('/movie_count')
def count():
    movies = Movie.query.all()
    num_movies = len(movies)
    return render_template('movie_count.html', num_movies=num_movies)

@app.route('/movie/new/<title>/<mpaarating>/<director>')
def new_movie(title, mpaarating, director):
    if Movie.query.filter_by(title=title).first():
        return "That movie already exists, go back to the homepage!"
    else:
        director = get_or_create_director(director)
        movie = Movie(title=title, director_id=director.id,mpaa_rating=mpaarating)
        session.add(movie)
        session.commit()
        return "New movie: {} by {}.".format(movie.title, director.name)


@app.route('/all_movies')
def see_all():
    all_movies = []
    movies = Movie.query.all()
    for m in movies:
        director = Director.query.filter_by(id=m.director_id).first()
        all_movies.append((m.title,director.name, m.mpaa_rating))
    return render_template('all_movies.html',all_movies=all_movies)


if __name__ == '__main__':
    db.create_all()
    app.run()
