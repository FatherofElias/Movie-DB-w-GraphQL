# Movie Database API

## Overview

This project is a GraphQL API for a movie database, built using Flask, SQLAlchemy, and Graphene. The API allows users to manage movies and genres, including creating, updating, deleting, and querying movies and genres.

## Features

- Create, update, and delete movies and genres.
- Retrieve movies by genre and genres by movie.
- Utilize a robust many-to-many relationship between movies and genres.


## Requirements.txt
aniso8601==7.0.0
blinker==1.9.0
cffi==1.17.1
click==8.1.7
colorama==0.4.6
cryptography==44.0.0
cryptograpy==0.0.0
Flask==3.1.0
Flask-GraphQL==2.0.1
Flask-Script==2.0.6
Flask-SQLAlchemy==3.1.1
graphene==2.1.9
graphene-sqlalchemy==2.1.0
graphql-core==2.3.2
graphql-relay==2.0.1
graphql-server-core==1.2.0
greenlet==3.1.1
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==3.0.2
promise==2.3
pycparser==2.22
PyMySQL==1.1.1
Rx==1.6.3
singledispatch==4.1.0
six==1.17.0
SQLAlchemy==2.0.36
typing_extensions==4.12.2
Werkzeug==3.1.3


## Installation

1. **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd <your-repo-directory>
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Setup

1. **Database Configuration:**

    Update the database configuration in `app.py`:
    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<username>:<password>@localhost/<database_name>'
    ```


## Running the Application

1. **Start the Flask server:**


2.   Open your web browser and navigate to `http://127.0.0.1:5000/graphql` to access the GraphiQL interface for testing your API.

## Endpoints

### Mutations

- **Create Genre**
    ```graphql
    mutation {
      createGenre(name: "Action") {
        genre {
          id
          name
        }
      }
    }
    ```

- **Update Genre**
    ```graphql
    mutation {
      updateGenre(id: 1, name: "Adventure") {
        genre {
          id
          name
        }
      }
    }
    ```

- **Delete Genre**
    ```graphql
    mutation {
      deleteGenre(id: 1) {
        genre {
          id
          name
        }
      }
    }
    ```

- **Create Movie**
    ```graphql
    mutation {
      createMovie(title: "Inception", director: "Christopher Nolan", year: 2010, genreIds: [1]) {
        movie {
          id
          title
          director
          year
          genres {
            id
            name
          }
        }
      }
    }
    ```

- **Update Movie**
    ```graphql
    mutation {
      updateMovie(id: 1, title: "Inception", director: "Christopher Nolan", year: 2010, genreIds: [1]) {
        movie {
          id
          title
          director
          year
          genres {
            id
            name
          }
        }
      }
    }
    ```

- **Delete Movie**
    ```graphql
    mutation {
      deleteMovie(id: 1) {
        movie {
          id
          title
          director
          year
          genres {
            id
            name
          }
        }
      }
    }
    ```

### Queries

- **Get All Movies**
    ```graphql
    query {
      movies {
        id
        title
        director
        year
        genres {
          id
          name
        }
      }
    }
    ```

- **Get All Genres**
    ```graphql
    query {
      genres {
        id
        name
      }
    }
    ```

- **Get Movies by Genre**
    ```graphql
    query {
      getMoviesByGenre(genreId: 1) {
        id
        title
        director
        year
        genres {
          id
          name
        }
      }
    }
    ```

- **Get Genres by Movie**
    ```graphql
    query {
      getGenresByMovie(movieId: 1) {
        id
        name
      }
    }
    ```



