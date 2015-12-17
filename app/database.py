from flask import Flask, g
from app import app
import sqlite3


def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = connect_db()
	return db

@app.teardown_appcontext
def teardown_request(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()

def query_db(query, args=(), one=False):
	cur = get_db().execute(query, args)
	rv = cur.fetchall()
	cur.close()
	return (rv[0] if rv else None) if one else rv