import os
from flask import Flask, request, jsonify, abort
from models import db, Movie, Actor, Category, Oscar
from flask_cors import CORS
import json
import sys
from auth.auth import AuthError, requires_auth
from datetime import datetime, date
from flask_migrate import Migrate
from config import config

migrate = Migrate()


def create_app(config_file='development'):
    # create and configure the app
    app = Flask(__name__)
    app.app_context().push()
    app.config.from_object(config[config_file])
    config[config_file].init_app(app)
    app.config.from_pyfile("config.py")
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # CORS Headers

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response

    @app.route('/')
    def index():
        return jsonify({
            'code': 200,
            'success': True,
            'message': "This is a movie-actor-Oscars application."
        })

    # get all movies

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(jwt):
        movies = Movie.query.order_by(Movie.id).all()
        if movies is None:
            abort(404)
        formatted_movies = [movie.format() for movie in movies]
        try:
            return jsonify({
                'success': True,
                'movies': formatted_movies,
                'total_movies': len(formatted_movies)
            }), 200
        except BaseException:
            print(sys.exc_info())
            abort(500)

    # create a movie

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movie')
    def create_movie(jwt):
        body = request.get_json()
        title = body.get('title', None)
        release_date = body.get('release_date', None)

        # If any field is missed, abort with 400.
        if (release_date is None) or (title is None):
            abort(400)
        try:
            new_release_date = date.fromisoformat(str(release_date))
            # new_release_date = datetime.strptime(release_date, '%Y-%m-%d')
            movie = Movie(title, new_release_date)
            movie.insert()

            return jsonify({
                'success': True,
                'created': movie.id,
                'total_movies': len(Movie.query.all())
            }), 200
        except BaseException:
            print(sys.exc_info())
            abort(500)

    # update a movie

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def update_movie(jwt, movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(404)
        body = request.get_json()
        title = body.get('title', None)
        release_date = body.get('release_date', None)
        new_release_date = date.fromisoformat(release_date)

        # If two fields are all missed, abort with 400.
        if (not title) and (not release_date):
            abort(400)

        # update title if the request contains title information
        if title:
            movie.title = title

        # update release_date if the request contains title information
        if release_date:
            movie.release_date = new_release_date
        try:
            movie.update()
            return jsonify({
                'success': True,
                'movie_id': movie_id,
            }), 200
        except BaseException:
            print(sys.exc_info())
            abort(500)

    # delete a movie

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(jwt, movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

        # If the movie does not exist, abort with 404
        if movie is None:
            abort(404)
        try:
            movie.delete()
            return jsonify({
                'success': True,
                'deleted_movie': movie_id,
                'total_movies': len(Movie.query.all())
            }), 200
        except BaseException:
            print(sys.exc_info())
            abort(500)

    # get all actors

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(jwt):
        actors = Actor.query.order_by(Actor.id).all()
        if actors is None:
            abort(404)
        formatted_actors = [actor.format() for actor in actors]
        try:
            return jsonify({
                'success': True,
                'actors': formatted_actors,
                'total_actors': len(formatted_actors)
            }), 200
        except BaseException:
            print(sys.exc_info())
            abort(500)

    # create an actor

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actor')
    def create_actor(jwt):
        body = request.get_json()
        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)

        # If any field is missed, abort with 400.
        if (not name) or (not age) or (not gender):
            abort(400)
        try:
            actor = Actor(name, age, gender)
            actor.insert()

            return jsonify({
                'success': True,
                'created': actor.id,
                'total_actors': len(Actor.query.all())
            }), 200
        except BaseException:
            print(sys.exc_info())
            abort(500)

    # update an actor

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def update_actor(jwt, actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor is None:
            abort(404)
        body = request.get_json()
        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)

        # If three fields are all missed, abort with 400.
        if (not name) and (not age) and (not gender):
            abort(400)

        # update name if the request contains name information
        if name:
            actor.name = name

        # update age if the request contains age information
        if age:
            actor.age = age

        # update gender if the request contains gender information
        if gender:
            actor.gender = gender

        try:
            actor.update()
            return jsonify({
                'success': True,
                'actor_id': actor_id,
            }), 200
        except BaseException:
            print(sys.exc_info())
            abort(500)

    # delete an actor

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(jwt, actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

        # If the actor does not exist, abort with 404
        if actor is None:
            abort(404)
        try:
            actor.delete()
            return jsonify({
                'success': True,
                'deleted_actor': actor_id,
                'total_actors': len(Actor.query.all())
            }), 200
        except BaseException:
            print(sys.exc_info())
            abort(500)

    # get all categories

    @app.route('/categories', methods=['GET'])
    @requires_auth('get:categories')
    def get_categories(jwt):
        categories = Category.query.order_by(Category.id).all()
        if categories is None:
            abort(404)
        formatted_categories = [category.format() for category in categories]
        try:
            return jsonify({
                'success': True,
                'categories': formatted_categories,
                'total_categories': len(formatted_categories)
            }), 200
        except BaseException:
            print(sys.exc_info())
            abort(500)

    # create a category

    @app.route('/categories', methods=['POST'])
    @requires_auth('post:category')
    def create_category(jwt):
        body = request.get_json()
        award = body.get('award', None)

        # If award field is missed, abort with 400.
        if not award:
            abort(400)
        try:
            category = Category(award)
            category.insert()

            return jsonify({
                'success': True,
                'created': category.id,
                'total_categories': len(Category.query.all())
            }), 200
        except BaseException:
            print(sys.exc_info())
            abort(500)

    # update a category

    @app.route('/categories/<int:category_id>', methods=['PATCH'])
    @requires_auth('patch:category')
    def update_category(jwt, category_id):
        category = Category.query.filter(
            Category.id == category_id).one_or_none()
        if category is None:
            abort(404)
        body = request.get_json()
        award = body.get('award', None)

        # If award field is missed, abort with 400.
        if not award:
            abort(400)

        category.award = award
        try:
            category.update()
            return jsonify({
                'success': True,
                'category_id': category_id,
            }), 200
        except BaseException:
            print(sys.exc_info())
            abort(500)

    # delete a category

    @app.route('/categories/<int:category_id>', methods=['DELETE'])
    @requires_auth('delete:category')
    def delete_category(jwt, category_id):
        category = Category.query.filter(
            Category.id == category_id).one_or_none()

        # If the actor does not exist, abort with 404
        if category is None:
            abort(404)
        try:
            category.delete()
            return jsonify({
                'success': True,
                'deleted_category': category_id,
                'total_categories': len(Category.query.all())
            }), 200
        except BaseException:
            print(sys.exc_info())
            abort(500)

    # get all oscars

    @app.route('/oscars', methods=['GET'])
    @requires_auth('get:oscars')
    def get_oscars(jwt):
        oscars = Oscar.query.order_by(Oscar.id).all()
        if oscars is None:
            abort(404)

        data = []
        for oscar in oscars:
            text = {
                "oscar_id": oscar.id,
                "year": oscar.year,
                "category": oscar.categories.award,
                "actor_id": oscar.winner_actor_id,
                "movie_id": oscar.winner_movie_id,
            }
            if oscar.winner_actor_id is None:
                text['actor_name'] = ""
            else:
                text['actor_name'] = oscar.actor.name
            if oscar.winner_movie_id is None:
                text['movie_title'] = ""
            else:
                text['movie_title'] = oscar.movie.title
            data.append(text)
        try:
            return jsonify({
                'success': True,
                'oscars': data,
                'total_oscars': len(data)
            }), 200
        except BaseException:
            print(sys.exc_info())
            abort(500)

    # create an oscar

    @app.route('/oscars', methods=['POST'])
    @requires_auth('post:oscar')
    def create_oscar(jwt):
        body = request.get_json()
        year = body.get('year', None)
        category = body.get('category', None)
        winner_actor_id = body.get('winner_actor_id', None)
        winner_movie_id = body.get('winner_movie_id', None)

        # If year and category two fields are missed, abort with 400.
        if (not year) or (not category) or (
                not winner_actor_id and not winner_movie_id):
            abort(400)
        try:
            oscar = Oscar(
                year,
                category,
                winner_actor_id=winner_actor_id,
                winner_movie_id=winner_movie_id)
            oscar.insert()

            return jsonify({
                'success': True,
                'created': oscar.id,
                'total_oscars': len(Oscar.query.all())
            }), 200
        except BaseException:
            print(sys.exc_info())
            abort(500)

    # update an oscar

    @app.route('/oscars/<int:oscar_id>', methods=['PATCH'])
    @requires_auth('patch:oscar')
    def update_oscar(jwt, oscar_id):
        oscar = Oscar.query.filter(Oscar.id == oscar_id).one_or_none()
        if oscar is None:
            abort(404)
        body = request.get_json()
        year = body.get('year', None)
        category = body.get('category', None)
        winner_actor_id = body.get('winner_actor_id', None)
        winner_movie_id = body.get('winner_movie_id', None)

        # If all fields are missed, abort with 400.
        if (not year) and (not category) and (
                not winner_actor_id) and (not winner_movie_id):
            abort(400)

        if year:
            oscar.year = year
        if category:
            oscar.category = category
        if winner_actor_id and winner_movie_id is None:
            oscar.winner_actor_id = winner_actor_id
            oscar.winner_movie_id = None
        else:
            oscar.winner_actor_id = None
            oscar.winner_movie_id = winner_movie_id
        try:
            oscar.update()
            return jsonify({
                'success': True,
                'oscar_id': oscar_id,
            }), 200
        except BaseException:
            print(sys.exc_info())
            abort(500)

    # delete an oscar

    @app.route('/oscars/<int:oscar_id>', methods=['DELETE'])
    @requires_auth('delete:oscar')
    def delete_oscar(jwt, oscar_id):
        oscar = Oscar.query.filter(Oscar.id == oscar_id).one_or_none()

        # If the Oscar does not exist, abort with 404
        if oscar is None:
            abort(404)
        try:
            oscar.delete()
            return jsonify({
                'success': True,
                'deleted_oscar': oscar_id,
                'total_oscars': len(Oscar.query.all())
            }), 200
        except BaseException:
            print(sys.exc_info())
            abort(500)

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': "Bad Request"
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': "Resource Not Found"
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': "Method Not Allowed"
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': "Unprocessable Entity"
        }), 422

    @app.errorhandler(500)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': "Internal Server Error"
        }), 500

    @app.errorhandler(AuthError)
    def handle_auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error
        }), error.status_code

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
