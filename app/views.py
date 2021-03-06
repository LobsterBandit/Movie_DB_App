from random import randint
from os import path
from flask import Flask, render_template, g, redirect, request, url_for, flash
from app import app, db, models
from .database import *
from .forms import SearchForm
from config import PER_PAGE
from sqlalchemy.sql import func


@app.route('/')
@app.route('/index/')
def index():
    form = SearchForm()
    query = 'select max(id) from Movie_List'
    maxid = query_db(query, one=True)
    randid = tuple(str(randint(1, maxid[0])) for x in range(3))
    query = '''select backdrop, title, imdb_id
               from Movie_List
               where id in {0} and backdrop is not null limit 1'''.format(randid)
    background = query_db(query, one=True)
    return render_template('index.html',
                           background=background,
                           title='Home',
                           form=form)


@app.route('/movies/', defaults={'page': 1})
@app.route('/movies/<int:page>')
def paged_list(page):
    form = SearchForm()
    movies = models.MovieList.query.order_by(models.MovieList.Title).paginate(page, PER_PAGE, True)
    return render_template('paged_list.html',
                           title='Movie List',
                           movies=movies,
                           form=form)


@app.route('/recent/')
def recent():
    form = SearchForm()
    movies = models.MovieList.query.order_by(models.MovieList.id.desc()).all()[:24]
    return render_template('recent_adds.html',
                           title='Recent Adds',
                           movies=movies,
                           form=form)


@app.route('/3d/')
def movie_3d():
    form = SearchForm()
    query = 'select * from Movie_List where filename like "%3D%" order by Title'
    movies = query_db(query)
    return render_template('movie_3d.html',
                           title='3D',
                           movies=movies,
                           form=form)


@app.route('/top-rated/')
def top_rated():
    form = SearchForm()
    movies = models.MovieList.query.order_by(models.MovieList.Rating.desc()).all()[:24]
    return render_template('top_rated.html',
                           title='Top Rated',
                           movies=movies,
                           form=form)


@app.route('/movie/<imdb_id>')
def movie_page(imdb_id):
    form = SearchForm()
    # query = """select ml.*, vid.Key
    #            from Movie_List ml
    #            join Video vid
    #            on ml.id = vid.movie_id
    #            where ml.imdb_id = ?
    #            and vid.Type like '%trailer%'
    #            and vid.Site = 'YouTube'"""
    # query = """select ml.*
    #            from Movie_List ml
    #            where ml.imdb_id = ?"""
    # movie = query_db(query, (imdb_id,))
    movie = models.MovieList.query.filter(models.MovieList.imdb_id == imdb_id).first()
    active = path.exists(path.join(movie.Path, movie.Filename))
    return render_template('movie_page.html',
                           title=movie.Title,
                           movie=movie,
                           form=form,
                           play=active)


@app.route('/search', methods=('GET', 'POST'))
def search():
    form = SearchForm()
    if form.validate_on_submit():
        result = models.MovieList.query.filter(models.MovieList.Title.like('%' + form.search.data + '%')).order_by(models.MovieList.Title).all()
        return render_template('top_rated.html',
                               title='Search',
                               movies=result,
                               form=form)
    return redirect(url_for('index'))


@app.route('/genre/<genre>')
def genre(genre):
    form = SearchForm()
    movie_list = models.MovieList.query.filter(models.MovieList.Genre.like('%'+genre+'%')).all()
    return render_template('top_rated.html',
                           title=genre,
                           movies=movie_list,
                           form=form)


@app.route('/genre')
def genre_list():
    form = SearchForm()
    genre_list = models.GenreList.query.distinct()
    return render_template('genres.html',
                           title='Genres',
                           genres=genre_list,
                           form=form)


@app.route('/random')
def random_list():
    form = SearchForm()
    movies = models.MovieList.query.order_by(func.random()).all()[:12]
    return render_template('top_rated.html',
                           title='Random Sampling',
                           movies=movies,
                           form=form)

# @app.route('/play/<movie>', methods='POST')
# def play_movie(movie):
#     if movie:

