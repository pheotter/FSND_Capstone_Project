# Capstone Project Backend
This project is a Capstone Project of the Udacity. In this project you can see movies, actors and Oscars. If you are an acting assistant, you can only access to all get actions. If you are an acting director, you can perform almost all actions. However, if you are an executive producer, you can perform all actions; like get, edit, delete and create movies, actors and Oscars. As part of the Fullstack Nanodegree, this is a final projetc for ** Full Stack Web Developer Nanodegree Program**. In this project, I applied API endpoint structuring, implementation, Authentication with AUTH0, based on role access management strategies to control different types of user. The last, but not least deploying server with Render Cloud Platform.

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
export FLASK_APP=app.py
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
     - JWT `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxuUEp4X0lYQ3pVTVdwU3drU3kzVSJ9.eyJpc3MiOiJodHRwczovL2Rldi1uNnBodDh1enI3OHpkbmx4LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDg2MGUxZjdjMjZjMmI2NGUwM2IzNzIiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTY4NjU0NzY1MSwiZXhwIjoxNjg2NTU0ODUxLCJhenAiOiJ2MTVVTUxZUTB6Nm5sSE4yWVNGVUhrNFBMa1UzeEdUZSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDpjYXRlZ29yaWVzIiwiZ2V0Om1vdmllcyIsImdldDpvc2NhcnMiXX0.ll8ig37Zxt0C5nF2w6IAFws15HEh97rl_03EjMGHqbU_lJ7id3XP65YBouP8Uub_PZm14AhwPzq4FV5imCAsz5qlI6GBqLnqYK1-AkCs8pPzT-a4vn5yT3yIOnb5gAA2Z9Cqk0PJd1qUz2T-q7j0ZJcCuB2FUrR1a-ESCvbyVwnlvh9ymq1xGRaj1Z2EoO39Pc9ddpjefZmox622wPFlles-2ouMldt1-TNVERLSQIbDAhenmycXwj3Ir5xkBZlenVQp5GaeUsCAvfqKm4y6RtcUnNtJRd1r8QZ8XDvlXnzsvH1wu1cVKPxfErueEh0KstIopCRHkievouSh6jsbaA`
   - Casting Director
     - can `get:movies` `get:actors` `get:categories` `get:oscars`
     - can `post:actor` `delete:actor` `patch:actor`
     - can `patch:movie`
     - User: casting_director@udacity.com
     - Password: @udacity987
     - JWT `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxuUEp4X0lYQ3pVTVdwU3drU3kzVSJ9.eyJpc3MiOiJodHRwczovL2Rldi1uNnBodDh1enI3OHpkbmx4LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDg2MGU1ZjE0NmRkZGU1Mzg2ZjU2OTciLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTY4NjU0NzY4NywiZXhwIjoxNjg2NTU0ODg3LCJhenAiOiJ2MTVVTUxZUTB6Nm5sSE4yWVNGVUhrNFBMa1UzeEdUZSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOmNhdGVnb3J5IiwiZ2V0OmFjdG9ycyIsImdldDpjYXRlZ29yaWVzIiwiZ2V0Om1vdmllcyIsImdldDpvc2NhcnMiLCJwYXRjaDphY3RvciIsInBhdGNoOmNhdGVnb3J5IiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDpjYXRlZ29yeSJdfQ.zPsFZv-1n1mtC3RaMcfZnqsrxwfVNYr0djrqbRXTR5r4yH-OIHpRNxSBWl1vYvNl4QxfcQAO7KmgrftGtRcldgaBJJOpP7dNmJSux1imsJbfYYmOpEz9d9dM-Ns3a4Zf2XLpqPT7H7xsSu87tCYMCW1yS0RjWhdG3dL7CSn7WUSCxgpwydCVAXDuByMuBd2HL8LcZBXnVbmidp7PFBUit4lusoju-Uvayi-5louypSzce5cWr0htmN3faao66XW9zquTsfZMuduxmNQqE09dpgeuJGswYPxv98YGPoTiarz3lSiLo7hKtkZy_I5CBpdCBcbBS8Cm9Vs-PSiuUVllKw`
   - Executive Producer
     - can perform all actions
     - User: executive_producer@udacity.com
     - Password: @udacity987
     - JWT `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxuUEp4X0lYQ3pVTVdwU3drU3kzVSJ9.eyJpc3MiOiJodHRwczovL2Rldi1uNnBodDh1enI3OHpkbmx4LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDg2MGU4NzE0NmRkZGU1Mzg2ZjU2YTciLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTY4NjU0NzcyNCwiZXhwIjoxNjg2NTU0OTI0LCJhenAiOiJ2MTVVTUxZUTB6Nm5sSE4yWVNGVUhrNFBMa1UzeEdUZSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOmNhdGVnb3J5IiwiZGVsZXRlOm1vdmllIiwiZGVsZXRlOm9zY2FyIiwiZ2V0OmFjdG9ycyIsImdldDpjYXRlZ29yaWVzIiwiZ2V0Om1vdmllcyIsImdldDpvc2NhcnMiLCJwYXRjaDphY3RvciIsInBhdGNoOmNhdGVnb3J5IiwicGF0Y2g6bW92aWUiLCJwYXRjaDpvc2NhciIsInBvc3Q6YWN0b3IiLCJwb3N0OmNhdGVnb3J5IiwicG9zdDptb3ZpZSIsInBvc3Q6b3NjYXIiXX0.a10Tk-BfT4EgJc3yUFImv8ji7X_kYFErTjOdf-PR4nKBRtW2Moizx1OXrEAdDTVF8K5PVuPH9bYJXrBGdMKpv8xsJCUjJFIGRb3f_MxmVnZEqNRJcGSv0hBdrj8kXjdWYSyDuPuHj8mnqxiuU3668fqoO5pMTqBLBEIB-VoR9Y0NaskFvQbxSR2aYIDqpUZGfXKEB3cNA1d6Kapp3_0ryn7Nk08D8Ipwolh_dynVWJJns49I23By5ZLiYNyl6iqAMo88TKtHyNCD_aF7_bu7J0h7TCVjeOZ-iCYg9kSC2pmszSX04z6puBxr9qpaq7LMDvu2FPfG-pny4jN-U_aY2Q`

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
```
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
```
## Deployment: Render Cloud Platform
### Steps:
1. Create a Render Account
2. Set up a Database Service with PostgreSQL
    On the "New Postgres" page:
    - Provide a name for the new database service: `postgres-deployment-example`
    - Select an instance type: `Free`
    - Click `Create Database` button
3. Deploy Apps with Render's Web Service
    On the "New Web Service" page:
    - Provide a name for the new database service: `render-deployment-example`
    - Select an instance type: `Free`
    - Enter the build command: `pip install -r requirements.txt`
    - Enter the Start command: `gunicorn app:app`
4. Connect the Database Service and Web Service
    - Copy the Postgres database URL (Internal Database URL) and paste it into the environment variable DATABASE_URI within the web service
    - note: the Internal Database URL must use the `postgresql` dialect instead of `postgres`
    - set environment variable `EXITED` to true
    - set other environment variables used in the auth.py file:
        - AUTH0_DOMAIN
        - ALGORITHMS
        - API_AUDIENCE
        - AUTH0_CLIENT_ID
5. After the Web Service is ready, you can open your Flask app on the browser by clicking the App URL

### My URL of the hosted API: `https://render-deployment-example-b090.onrender.com`

## Authors
Ann Yang
