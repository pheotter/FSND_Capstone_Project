import os
from sqlalchemy import Column, String, Integer, Date
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime

# database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""

# def setup_db(app, database_path=database_path):
#     app.config["SQLALCHEMY_DATABASE_URI"] = database_path
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#     db.app = app
#     db.init_app(app)
#     with app.app_context():
#        db.create_all()

'''
Movie

'''


class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    release_date = Column(Date, nullable=False)
    oscar = db.relationship('Oscar', backref='movie', lazy=True)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }


'''
Actor

'''


class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(6), nullable=False)
    oscar = db.relationship('Oscar', backref='actor', lazy=True)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }


'''
Oscar

'''


class Oscar(db.Model):
    __tablename__ = 'oscars'

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    category = Column(Integer, db.ForeignKey('categories.id'), nullable=False)
    winner_actor_id = Column(
        db.Integer,
        db.ForeignKey('actors.id'),
        nullable=True)
    winner_movie_id = Column(
        db.Integer,
        db.ForeignKey('movies.id'),
        nullable=True)

    def __init__(
            self,
            year,
            category,
            *,
            winner_actor_id=None,
            winner_movie_id=None):
        self.year = year
        self.category = category
        if winner_actor_id is not None:
            self.winner_actor_id = winner_actor_id
        if winner_movie_id is not None:
            self.winner_movie_id = winner_movie_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'year': self.year,
            'category': self.category,
            'winner_actor_id': self.winner_actor_id,
            'winner_movie_id': self.winner_movie_id
        }


'''
Category

'''


class Category(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    award = Column(String(40), nullable=False)
    oscar = db.relationship('Oscar', backref='categories', lazy=True)

    def __init__(self, award):
        self.award = award

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'award': self.award
        }
