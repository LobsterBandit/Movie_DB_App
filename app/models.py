import datetime as dt
from app import db


class Cast(db.Model):
    __tablename__ = 'Cast'

    Cast_ID = db.Column(db.Integer, primary_key=True)
    tmdb_cast_id = db.Column(db.Integer)
    Cast_Name = db.Column(db.Text)
    Cast_Char = db.Column(db.Text)
    Cast_Order = db.Column(db.Integer)
    Profile = db.Column(db.Text)
    Movie_id = db.Column(db.Integer, db.ForeignKey('Movie_List.id'), nullable=False)
    Date_Updated = db.Column(db.DateTime, default=dt.datetime.utcnow())
    Date_Added = db.Column(db.DateTime, default=dt.datetime.utcnow())


class Genre(db.Model):
    __tablename__ = 'Genre'

    Genre_ID = db.Column(db.Integer, primary_key=True)
    tmdb_genre_id = db.Column(db.Integer)
    Genre_Desc = db.Column(db.Text)
    Movie_id = db.Column(db.ForeignKey('Movie_List.id'), nullable=False)
    Date_Updated = db.Column(db.DateTime, default=dt.datetime.utcnow())
    Date_Added = db.Column(db.DateTime, default=dt.datetime.utcnow())


class MovieList(db.Model):
    __tablename__ = 'Movie_List'

    id = db.Column(db.Integer, primary_key=True)
    Filename = db.Column(db.Text)
    Size = db.Column(db.Float)
    Path = db.Column(db.Text)
    Title = db.Column(db.Text, index=True)
    Year = db.Column(db.Integer, index=True)
    tmdb_id = db.Column(db.Integer, index=True)
    Overview = db.Column(db.Text)
    imdb_id = db.Column(db.Text)
    Rating = db.Column(db.Float)
    Runtime = db.Column(db.Float)
    Release_Date = db.Column(db.Text)
    Poster = db.Column(db.Text)
    Backdrop = db.Column(db.Text)
    Tagline = db.Column(db.Text)
    Date_Updated = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow())
    Date_Added = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow())


class Video(db.Model):
    __tablename__ = 'Video'

    Video_ID = db.Column(db.Integer, primary_key=True)
    Type = db.Column(db.Text)
    Key = db.Column(db.Text)
    Name = db.Column(db.Text)
    Size = db.Column(db.Integer)
    Site = db.Column(db.Text)
    Movie_id = db.Column(db.ForeignKey('Movie_List.id'), nullable=False)
    Date_Updated = db.Column(db.DateTime, default=dt.datetime.utcnow())
    Date_Added = db.Column(db.DateTime, default=dt.datetime.utcnow())
