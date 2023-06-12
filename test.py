import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import Actor, Movie, Category, Oscar


class CapstoneTestCase(unittest.TestCase):
    """This class represents the capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app('testing')
        self.client = self.app.test_client
        self.header = {'Content-Type': 'application/json', 'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxuUEp4X0lYQ3pVTVdwU3drU3kzVSJ9.eyJpc3MiOiJodHRwczovL2Rldi1uNnBodDh1enI3OHpkbmx4LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDg2MGU4NzE0NmRkZGU1Mzg2ZjU2YTciLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTY4NjUyMjE1NiwiZXhwIjoxNjg2NTI5MzU2LCJhenAiOiJ2MTVVTUxZUTB6Nm5sSE4yWVNGVUhrNFBMa1UzeEdUZSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOmNhdGVnb3J5IiwiZGVsZXRlOm1vdmllIiwiZGVsZXRlOm9zY2FyIiwiZ2V0OmFjdG9ycyIsImdldDpjYXRlZ29yaWVzIiwiZ2V0Om1vdmllcyIsImdldDpvc2NhcnMiLCJwYXRjaDphY3RvciIsInBhdGNoOmNhdGVnb3J5IiwicGF0Y2g6bW92aWUiLCJwYXRjaDpvc2NhciIsInBvc3Q6YWN0b3IiLCJwb3N0OmNhdGVnb3J5IiwicG9zdDptb3ZpZSIsInBvc3Q6b3NjYXIiXX0.k_sC8FLN3ipEVKKCudLIfyGocdnhtYD7h4df2OmZQfsuXmDshQBuhPPxQtwcm-dRc7FNLnvfG7MJARkFKfIwmk393CiSXnU_OC_wiagiVrADQvRvR9kDEDWdHQSQFe3sns8NjhofBNTOSygERpRyxIJotgWiPd3M1r4ewy8MEMM0Qnyqu29i6i3kjZ5f30eAwTZ-icYAnrbFpJHRMsM_Co6SuLkP6x23D957C3UKFbIr8I4_L9OUpNzhwJGyxNl03RMh_iP3ZWBBoInGXN8xyJuDF2OmOVmEa788F2hbcbm5zAzFisULXWSvSeTh9UV-TDVX8g0crfHFO0QiSN0FKg"}

    def tearDown(self):
        """Executed after reach test"""
        pass

    # movies
    def test_get_actors(self):
        res = self.client().get("/movies", headers=self.header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movies"])
        self.assertTrue(data["total_movies"])

    # actors
    def test_get_actors(self):
        res = self.client().get("/actors", headers=self.header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])
        self.assertTrue(data["total_actors"])

    # categories
    def test_get_categories(self):
        res = self.client().get("/categories", headers=self.header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["categories"])
        self.assertTrue(data["total_categories"])

    # oscars
    def test_get_oscars(self):
        res = self.client().get("/oscars", headers=self.header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["oscars"])
        self.assertTrue(data["total_oscars"])

    # Delete a movie
    def test_delete_movie(self):
        newMovie = Movie("The White Shark", "2010-08-11")
        newMovie.insert()
        new_id = newMovie.id
        moviesBeforeDelete = len(Movie.query.all())
        res = self.client().delete(f'/movies/{new_id}', headers=self.header)
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == new_id).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted_movie"], new_id)
        self.assertEqual(data["total_movies"], moviesBeforeDelete - 1)
        self.assertEqual(movie, None)

    # Delete an actor
    def test_delete_actor(self):
        newActor = Actor("Ann", 24, "Female")
        newActor.insert()
        new_id = newActor.id
        actorsBeforeDelete = len(Actor.query.all())
        res = self.client().delete(f'/actors/{new_id}', headers=self.header)
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == new_id).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted_actor"], new_id)
        self.assertEqual(data["total_actors"], actorsBeforeDelete - 1)
        self.assertEqual(actor, None)

    # Delete a category
    def test_delete_category(self):
        newCategory = Category("Best Actor")
        newCategory.insert()
        new_id = newCategory.id
        categoriesBeforeDelete = len(Category.query.all())
        res = self.client().delete(
            f'/categories/{new_id}',
            headers=self.header)
        data = json.loads(res.data)

        category = Category.query.filter(Category.id == new_id).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted_category"], new_id)
        self.assertEqual(data["total_categories"], categoriesBeforeDelete - 1)
        self.assertEqual(category, None)

    # Delete an oscar
    def test_delete_oscar(self):
        newOscar = Oscar(2024, 3, winner_actor_id=1)
        newOscar.insert()
        new_id = newOscar.id
        oscarsBeforeDelete = len(Oscar.query.all())
        res = self.client().delete(f'/oscars/{new_id}', headers=self.header)
        data = json.loads(res.data)

        oscar = Oscar.query.filter(Oscar.id == new_id).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted_oscar"], new_id)
        self.assertEqual(data["total_oscars"], oscarsBeforeDelete - 1)
        self.assertEqual(oscar, None)

    # Delete a movie that does not exist
    def test_404_if_movie_does_not_exist(self):
        res = self.client().delete("/movies/1000", headers=self.header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Resource Not Found")

    # Delete an actor that does not exist
    def test_404_if_actor_does_not_exist(self):
        res = self.client().delete("/actors/1000", headers=self.header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Resource Not Found")

    # Delete a category that does not exist
    def test_404_if_category_does_not_exist(self):
        res = self.client().delete("/categories/1000", headers=self.header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Resource Not Found")

    # Delete an oscar that does not exist
    def test_404_if_oscar_does_not_exist(self):
        res = self.client().delete("/oscars/1000", headers=self.header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Resource Not Found")

    # Create a new movie
    def test_create_new_movie(self):
        new_movie = {
            'title': "Two White Shark",
            'release_date': "2021-09-09",
        }
        moviesBeforeCreate = len(Movie.query.all())
        res = self.client().post("/movies", json=new_movie, headers=self.header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["total_movies"], moviesBeforeCreate + 1)

    # Create a new actor
    def test_create_new_actor(self):
        new_actor = {
            'name': 'Bob',
            'age': 33,
            'gender': 'Male'
        }
        actorsBeforeCreate = len(Actor.query.all())
        res = self.client().post("/actors", json=new_actor, headers=self.header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["total_actors"], actorsBeforeCreate + 1)

    # Create a new category
    def test_create_new_category(self):
        new_category = {
            'award': 'Best Assistant Director'
        }
        categoriesBeforeCreate = len(Category.query.all())
        res = self.client().post("/categories", json=new_category, headers=self.header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["total_categories"], categoriesBeforeCreate + 1)

    # Create a new oscar
    def test_create_new_oscar(self):
        new_oscar = {
            'year': 2054,
            'category': 3,
            'winner_actor_id': 2
        }
        oscarsBeforeCreate = len(Oscar.query.all())
        res = self.client().post("/oscars", json=new_oscar, headers=self.header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["total_oscars"], oscarsBeforeCreate + 1)

    # Create a new movie but missing some fields
    def test_400_create_movie_but_any_field_is_missed(self):
        new_movie = {
            'title': 'Black Sheep'
        }
        moviesBeforeCreate = len(Movie.query.all())
        res = self.client().post("/movies", json=new_movie, headers=self.header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Bad Request")

    # Create a new actor but missing some fields
    def test_400_create_actor_but_any_field_is_missed(self):
        new_actor = {
            'name': 'Ben',
        }
        actorsBeforeCreate = len(Actor.query.all())
        res = self.client().post("/actors", json=new_actor, headers=self.header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Bad Request")

    # Create a new category but missing some fields
    def test_400_create_category_but_any_field_is_missed(self):
        categoriesBeforeCreate = len(Category.query.all())
        res = self.client().post("/categories", headers=self.header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Bad Request")

    # Create a new oscar but missing some fields
    def test_400_create_oscar_but_any_field_is_missed(self):
        new_oscar = {
            'year': 2019,
            'category': 'Best Short Subject'
        }
        res = self.client().post("/oscars", json=new_oscar, headers=self.header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Bad Request")

    # update a movie
    def test_update_movie(self):
        update = {
            'release_date': '2003-05-06'
        }
        res = self.client().patch('/movies/1', json=update, headers=self.header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["movie_id"], 1)

    # update an actor
    def test_update_actor(self):
        update = {
            'name': 'Will'
        }
        res = self.client().patch('/actors/1', json=update, headers=self.header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["actor_id"], 1)

    # update a category
    def test_update_category(self):
        update = {
            'award': 'Best Costume Design'
        }
        res = self.client().patch('/categories/1', json=update, headers=self.header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["category_id"], 1)

    # update an oscar
    def test_update_oscar(self):
        update = {
            'year': 1999,
        }
        res = self.client().patch('/oscars/2', json=update, headers=self.header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["oscar_id"], 2)

    # update a movie but missing some fields
    def test_400_update_movie_but_any_field_is_missed(self):
        res = self.client().patch("/movies/1", headers=self.header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Bad Request")

    # update a actor but missing some fields
    def test_400_update_actor_but_any_field_is_missed(self):
        res = self.client().patch("/actors/1", headers=self.header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Bad Request")

    # update a category but missing some fields
    def test_400_update_actor_but_any_field_is_missed(self):
        res = self.client().patch("/categories/1", headers=self.header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Bad Request")

    # update an oscar but missing some fields
    def test_400_update_oscar_but_any_field_is_missed(self):
        res = self.client().patch("/oscars/2", headers=self.header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Bad Request")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
