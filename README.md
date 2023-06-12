# Coffee Shop Backend
This project is a Capstone Project that I do myself for Udacity. In this project you can see movies and actors. If you are director or manager access to much actions; like get, edit, delete and create movies and actors according your asigned rol. As part of the Fullstack Nanodegree, this is a final projetc for ** Full Stack Web Developer Nanodegree Program**. In this project, I applied API endpoint structuring, implementation, Authentication with AUTH0, based on role access management strategies to control different types of user. The last, but not least deploying server with Render Cloud Platform.
All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/).
## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the root directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py
export FLASK_DEBUG=1
flask run
```

Setting the FLASK_DEBUG variable to true means that we are working in development mode and it shows an interactive debugger in the console and restarts the server whenever changes are made.

The application is run on http://127.0.0.1:5000/ by default.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
   - in API Settings:
     - Enable RBAC
     - Enable Add Permissions in the Access Token
5. Create new API permissions:
   - `get:movies` `post:movie` `patch:movie` `delete:movie`
   - `get:actors` `post:actor` `patch:actor` `delete:actor`
   - `get:categories` `post:category` `patch:category` `delete:category`
   - `get:oscars` `post:oscar` `patch:oscar` `delete:oscar`
6. Create new roles for:
   - Casting Assitant
     - can `get:movies`
     - can `get:actors`
     - can `get:categories`
     - can `get:oscars`
     - User: casting_assistant@udacity.com
     - Password: @udacity987
     - JWT `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxuUEp4X0lYQ3pVTVdwU3drU3kzVSJ9.eyJpc3MiOiJodHRwczovL2Rldi1uNnBodDh1enI3OHpkbmx4LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDg2MGUxZjdjMjZjMmI2NGUwM2IzNzIiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTY4NjUyMjA0MiwiZXhwIjoxNjg2NTI5MjQyLCJhenAiOiJ2MTVVTUxZUTB6Nm5sSE4yWVNGVUhrNFBMa1UzeEdUZSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDpjYXRlZ29yaWVzIiwiZ2V0Om1vdmllcyIsImdldDpvc2NhcnMiXX0.MinYe5JXzIgUcirF3yp2sFOo619WsTEGGwhGO7teLBgb0TSwnMyaTfL933NGcjAMNFVgdmXG0QrPzjSYM25k48BpkFsJOtmoiRI6DDSGDPsCoNP65owKQDW7FEtxhu7VFEMtXgTObyO96FyFrLVR41LyQh2jMVlbei5KK39fRyQ2FgpLpCoxdvR-ry26yjkyyNqoV5aqaOJwhD0-pFKN06v7ldBbYH8piIthG_eUvKVARew_cfh4epHRsMbsXblzhC5VfPHb9blvEmzlrZN801sWZu1rtWvrXxHCMyTjYnvpQw1RUWKRfIZGU1hTvIOJU2fxHPz0wLEAdmDHKPTvxg`
   - Casting Director
     - can `get:movies` `get:actors` `get:categories` `get:oscars`
     - can `post:actor` `delete:actor` `patch:actor`
     - can `patch:movie`
     - User: casting_director@udacity.com
     - Password: @udacity987
     - JWT `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxuUEp4X0lYQ3pVTVdwU3drU3kzVSJ9.eyJpc3MiOiJodHRwczovL2Rldi1uNnBodDh1enI3OHpkbmx4LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDg2MGU1ZjE0NmRkZGU1Mzg2ZjU2OTciLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTY4NjUyMjExMSwiZXhwIjoxNjg2NTI5MzExLCJhenAiOiJ2MTVVTUxZUTB6Nm5sSE4yWVNGVUhrNFBMa1UzeEdUZSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOmNhdGVnb3J5IiwiZ2V0OmFjdG9ycyIsImdldDpjYXRlZ29yaWVzIiwiZ2V0Om1vdmllcyIsImdldDpvc2NhcnMiLCJwYXRjaDphY3RvciIsInBhdGNoOmNhdGVnb3J5IiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDpjYXRlZ29yeSJdfQ.TqiiIVcLcVhnpvZvcR1aJtTlVAcNvcOiX-CLvZcJ6suOXari_D-faI09sbZ79cvF1ao6lgM2wX1jsgx8dsxBxZ9bcZSabxTqsu5r64SK1lAmbIpY-D_PkXuSOpL2luoCMeK1YdYsMEm8x0QYlcOstMR7L6vkAvNnHaR9Gq2-vbLxp8wKw6KhpqgSW8JapJleVRbrgI-ZKPETnIZNAanZzkIiHhKBAh9IbnfpQDgtq7VC8rW1U6hQlqtOnCnRNz6npph1HFutC8pBX-TDIfw-0T7xq7A7JKyQFqrbSUhOqujT5RoVZXJ3VEeH03DsgWtNiBtF4IjaQPvYGj5eQ4NdGg`
   - Executive Producer
     - can perform all actions
     - User: executive_producer@udacity.com
     - Password: @udacity987
     - JWT `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxuUEp4X0lYQ3pVTVdwU3drU3kzVSJ9.eyJpc3MiOiJodHRwczovL2Rldi1uNnBodDh1enI3OHpkbmx4LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDg2MGU4NzE0NmRkZGU1Mzg2ZjU2YTciLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTY4NjUyMjE1NiwiZXhwIjoxNjg2NTI5MzU2LCJhenAiOiJ2MTVVTUxZUTB6Nm5sSE4yWVNGVUhrNFBMa1UzeEdUZSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOmNhdGVnb3J5IiwiZGVsZXRlOm1vdmllIiwiZGVsZXRlOm9zY2FyIiwiZ2V0OmFjdG9ycyIsImdldDpjYXRlZ29yaWVzIiwiZ2V0Om1vdmllcyIsImdldDpvc2NhcnMiLCJwYXRjaDphY3RvciIsInBhdGNoOmNhdGVnb3J5IiwicGF0Y2g6bW92aWUiLCJwYXRjaDpvc2NhciIsInBvc3Q6YWN0b3IiLCJwb3N0OmNhdGVnb3J5IiwicG9zdDptb3ZpZSIsInBvc3Q6b3NjYXIiXX0.k_sC8FLN3ipEVKKCudLIfyGocdnhtYD7h4df2OmZQfsuXmDshQBuhPPxQtwcm-dRc7FNLnvfG7MJARkFKfIwmk393CiSXnU_OC_wiagiVrADQvRvR9kDEDWdHQSQFe3sns8NjhofBNTOSygERpRyxIJotgWiPd3M1r4ewy8MEMM0Qnyqu29i6i3kjZ5f30eAwTZ-icYAnrbFpJHRMsM_Co6SuLkP6x23D957C3UKFbIr8I4_L9OUpNzhwJGyxNl03RMh_iP3ZWBBoInGXN8xyJuDF2OmOVmEa788F2hbcbm5zAzFisULXWSvSeTh9UV-TDVX8g0crfHFO0QiSN0FKg`
7. Test your endpoints with [Postman](https://getpostman.com).
   - Register 2 users - assign the Barista role to one and Manager role to the other.
   - Sign into each account and make note of the JWT.
   - Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
   - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
   - Run the collection and correct any errors.
   - Export the collection overwriting the one we've included so that we have your proper JWTs during review!
   - My test results containing 20 successful cases: `/backend/udacity-fsnd-udaspicelatte.postman_collection_result.json`

### Implement The Server

There are `@TODO` comments throughout the `./backend/src`. We recommend tackling the files in order and from top to bottom:

1. `./src/auth/auth.py`
2. `./src/api.py`

## API Reference
### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`
- Authentication: using Auth0.

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False,
    "error": 400,
    "message": "bad request"
}
```
The API will return seven error types when requests fail:
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Resource Not Found
- 405: Method Not Allowed
- 422: Not Processable
- 500: Internal Server Error

### Endpoints
#### GET /movies
- General:
    - Returns a success value, a list of available movies and total number of movies.
- Sample: `curl http://127.0.0.1:5000/movies -H "Authorization: Bearer JWT"`
```
{
   "movies":[
      {
         "id":1,
         "release_date":"Sun, 03 Jan 2021 00:00:00 GMT",
         "title":"Spider-Man: No Way Home"
      },
      {
         "id":2,
         "release_date":"Wed, 03 Feb 2021 00:00:00 GMT",
         "title":"The Battle at Lake Changjin"
      },
      {
         "id":3,
         "release_date":"Sun, 21 Mar 2021 00:00:00 GMT",
         "title":"Hi, Mom"
      },
      {
         "id":4,
         "release_date":"Wed, 12 May 2021 00:00:00 GMT",
         "title":"No Time to Die"
      },
      {
         "id":5,
         "release_date":"Mon, 11 Oct 2021 00:00:00 GMT",
         "title":"Detective Chinatown 3"
      }
   ],
   "success":true,
   "total_movies":5
}
```
#### POST /movies
- General:
    - Creates a movie using the submitted title and release_date. Returns success value, movie's id and the total number of movies.
- Sample: `curl http://127.0.0.1:5000/movies -X POST -H "Content-Type: application/json" -d '{"title":"Sing 2", "release_date": "2021-09-08"}' -H "Authorization: Bearer JWT"`
```
{
   "created":13,
   "success":true,
   "total_movies":6
}
```
#### PATCH /movies/{movie_id}
- General:
    - Updates the movie of the given ID if it exists. Returns success value and id of the updated movie.
- Sample: `curl -X PATCH http://127.0.0.1:5000/movies/2 -H "content-type: application/json" -d '{"release_date": "2022-10-10"}' -H "Authorization: Bearer JWT"`

```
{
   "movie_id":2,
   "success":true
}
```
#### DELETE /movies/{movie_id}
- General:
    - Deletes the movie of the given ID if it exists. Returns the success value, the id of the deleted movies and total number of movies.
- Sample: `curl -X DELETE http://127.0.0.1:5000/movies/6 -H "Authorization: Bearer JWT"`

```
{
   "deleted_movie":6,
   "success":true,
   "total_movies":5
}
```
#### GET /actors
- General:
    - Returns a success value, a list of actors and total number of actors.
- Sample: `curl http://127.0.0.1:5000/actors`
```
{
   "actors":[
      {
         "age":55,
         "gender":"Male",
         "id":1,
         "name":"Jack Nicholson"
      },
      {
         "age":50,
         "gender":"Male",
         "id":2,
         "name":"Marlon Brando"
      },
      {
         "age":33,
         "gender":"Female",
         "id":3,
         "name":"Katharine Hepburn"
      },
      {
         "age":57,
         "gender":"Female",
         "id":4,
         "name":"Meryl Streep"
      }
   ],
   "success":true,
   "total_actors":4
}
```
#### POST /actors
- General:
    - Creates an actor using the submitted name, age and gender. Returns success value, actor's id and the total number of actors.
- Sample: `curl http://127.0.0.1:5000/actors -X POST -H "Content-Type: application/json" -d '{"name":"Daniel Day-Lewis", "age": 60, "gender": "Male"}' -H "Authorization: Bearer JWT"`
```
{
   "created":5,
   "success":true,
   "total_actors":5
}
```
#### PATCH /actors/{actor_id}
- General:
    - Updates the actor of the given ID if it exists. Returns success value and it's id.
- Sample: `curl -X PATCH http://127.0.0.1:5000/actors/3 -H "content-type: application/json" -d '{"age": 34}' -H "Authorization: Bearer JWT"`

```
{
   "actor_id":3,
   "success":true
}
```
#### DELETE /actors/{actor_id}
- General:
    - Deletes the actor of the given ID if it exists. Returns the success value, the id of the deleted actor and total number of actors.
- Sample: `curl -X DELETE http://127.0.0.1:5000/actors/5 -H "Authorization: Bearer JWT"`

```
{
   "deleted_actor":5,
   "success":true,
   "total_actors":4
}
```
#### GET /categories
- General:
    - Returns a success value, a list of categories and total number of categories.
- Sample: `curl http://127.0.0.1:5000/categories`
```
{
   "categories":[
      {
         "award":"Best Picture",
         "id":1
      },
      {
         "award":"Best Director",
         "id":2
      },
      {
         "award":"Best Actor",
         "id":3
      },
      {
         "award":"Best Actress",
         "id":4
      },
      {
         "award":"Best Production Design",
         "id":5
      },
      {
         "award":"Best Adapted Screenplay",
         "id":6
      },
      {
         "award":"Best Sound",
         "id":7
      }
   ],
   "success":true,
   "total_categories":7
}
```
#### POST /categories
- General:
    - Creates a category using the submitted award. Returns success value, category's id and the total number of categories.
- Sample: `curl http://127.0.0.1:5000/categories -X POST -H "Content-Type: application/json" -d '{"award":"	Best Supporting Actor"}' -H "Authorization: Bearer JWT"`
```
{
   "created":8,
   "success":true,
   "total_categories":8
}
```
#### PATCH /categories/{category_id}
- General:
    - Updates the category of the given ID if it exists. Returns success value and it's id.
- Sample: `curl -X PATCH http://127.0.0.1:5000/categories/8 -H "content-type: application/json" -d '{"award": "Best Supporting actor"}' -H "Authorization: Bearer JWT"`

```
{
   "category_id":8,
   "success":true
}
```
#### DELETE /categories/{category_id}
- General:
    - Deletes the category of the given ID if it exists. Returns the success value, the id of the deleted category and total number of categories.
- Sample: `curl -X DELETE http://127.0.0.1:5000/categories/8 -H "Authorization: Bearer JWT"`

```
{
   "deleted_category":8,
   "success":true,
   "total_categories":7
}
#### GET /oscars
- General:
    - Returns a success value, a list of oscars and total number of oscars.
- Sample: `curl http://127.0.0.1:5000/oscars`
```
{
   "oscars":[
      {
         "actor_id":2,
         "actor_name":"Marlon Brando",
         "category":"Best Actor",
         "movie_id":null,
         "movie_title":"",
         "oscar_id":1,
         "year":2024
      },
      {
         "actor_id":3,
         "actor_name":"Katharine Hepburn",
         "category":"Best Actress",
         "movie_id":null,
         "movie_title":"",
         "oscar_id":2,
         "year":2025
      }
   ],
   "success":true,
   "total_oscars":2
}
```
#### POST /oscars
- General:
    - Creates an oscar using the submitted year, category id, actor id and movie id. Returns success value, oscar's id and the total number of oscars.
- Sample: `curl http://127.0.0.1:5000/oscars -X POST -H "Content-Type: application/json" -d '{"year": 2030, "category": 3, "winner_actor_id": 1}' -H "Authorization: Bearer JWT"`
```
{
   "created":3,
   "success":true,
   "total_oscars":3
}
```
#### PATCH /oscars/{oscar_id}
- General:
    - Updates the oscar of the given ID if it exists. Returns success value and it's id.
- Sample: `curl -X PATCH http://127.0.0.1:5000/oscars/3 -H "content-type: application/json" -d '{"winner_actor_id": 2}' -H "Authorization: Bearer JWT"`

```
{
   "oscar_id":3,
   "success":true
}
```
#### DELETE /oscars/{oscar_id}
- General:
    - Deletes the oscar of the given ID if it exists. Returns the success value, the id of the deleted oscar and total number of oscars.
- Sample: `curl -X DELETE http://127.0.0.1:5000/oscars/3 -H "Authorization: Bearer JWT"`

```
{
   "deleted_oscar":3,
   "success":true,
   "total_oscars":2
}
## Deployment N/A

## Authors
Ann Yang
