from random import randint
from flask import Flask, render_template, g
from app import app
from .database import *


@app.route('/')
@app.route('/index/')
def index():
    query = 'select max(id) from Movie_List'
    max = query_db(query, one=True)
    randid = tuple(str(randint(1, max[0])) for x in range(3))
    query = '''select backdrop, title, imdb_id
               from Movie_List
               where id in {0} and backdrop is not null limit 1'''.format(randid)
    background = query_db(query, one=True)
    print(background)
    return render_template('index.html',
                           background=background,
                           title='Home')


@app.route('/list/')
def list():
    query = 'select * from Movie_List order by Title'
    movies = query_db(query)
    return render_template('movie_list.html',
                           title='Movie List',
                           movies=movies)


@app.route('/recent/')
def recent():
    query = 'select * from Movie_List order by ID desc limit 12'
    # args = '10'
    movies = query_db(query)
    return render_template('recent_adds.html',
                           title='Recent Adds',
                           movies=movies)


@app.route('/3d/')
def movie_3d():
    query = 'select * from Movie_List where filename like "%3D%" order by Title'
    movies = query_db(query)
    return render_template('movie_3d.html',
                           title='3D',
                           movies=movies)


@app.route('/movie/<imdb_id>')
def movie_page(imdb_id):
    query = 'select * from Movie_List where imdb_id = ?'
    movie = query_db(query, (imdb_id,))
    return render_template('movie_page.html',
                           title=movie[0][4],
                           movie=movie[0])
