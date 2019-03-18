# Route Functionality

## /

Welcomes users to the site

## /movie_count

Displays the number of movies in the database

## /movie/new/<title>/<mpaaratings>/<director>/

Allows users to add to add a movie to the database. It requires a movie title, a rating, and a director

## /all_movies

Displays all movies (and the associated information) to the user.


# Requirements

* Flask
* Flasj_sqlalchemy

note: all library and package requirements can be found acquired by running the requirements.txt file.


# How to Run

type 'python SI507_project3.py runserver' into the command terminal

## Possible thing to type in the URL

note: you will change things in <>. it will begin with either http://127.0.0.1:5000/ or http://localhost:5000/, followed by the below options. typing in the URLs mentioned will bring users to the homepage.

* /
* /movie_count
* /movie/new/<title>/<mpaaratings>/<directory>/
* /all_movies
