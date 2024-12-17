import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Movie as MovieModel, Genre as GenreModel, db
from sqlalchemy.orm import Session

class Movie(SQLAlchemyObjectType):
    class Meta:
        model = MovieModel

class Query(graphene.ObjectType):
    movies = graphene.List(Movie)

    def resolve_movies(self,info):
        return db.session.execute(db.select(MovieModel)).scalars()
    
class AddMovie(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        director = graphene.String(required=True)
        year = graphene.Int(required=True)
        genre_ids = graphene.List(graphene.Int)

    movie = graphene.Field(Movie)

    def mutate(self, info, title, director, year, genre_ids):
        with Session(db.engine) as session:
            movie = MovieModel(title=title, director=director, year=year)
            if genre_ids:
                genres = session.execute(db.select(GenreModel).where(GenreModel.id.in_(genre_ids))).scalars().all()
                movie.genres.extend(genres)
            session.add(movie)
            session.commit()
            session.refresh(movie)

           
            genres = movie.genres 
        return AddMovie(movie=movie)




class UpdateMovie(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String(required=True)
        director = graphene.String(required=True)
        year = graphene.Int(required=True)

    movie = graphene.Field(Movie)

    def mutate(self, info, id, title, director, year):
        with Session(db.engine) as session:
            with session.begin():
                movie = session.execute(db.select(MovieModel).where(MovieModel.id == id)).scalars().first()
                if movie:
                    movie.title = title
                    movie.director = director
                    movie.year = year
                else:
                    return None
            session.refresh(movie)
            return UpdateMovie(movie=movie)
        

class DeleteMovie(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    movie = graphene.Field(Movie)

    def mutate(self, info, id):
        with Session(db.engine) as session:
            with session.begin():
                movie = session.execute(db.select(MovieModel).where(MovieModel.id == id)).scalars().first()
                if movie:
                    session.delete(movie)
                else:
                    return None
            session.refresh(movie)
            return DeleteMovie(movie=movie)
        

class Genre(SQLAlchemyObjectType):
    class Meta:
        model = GenreModel

class CreateGenre(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    genre = graphene.Field(Genre)

    def mutate(self, info, name):
        if not name or len(name) > 255:
            raise Exception("Invalid genre name.")
        with Session(db.engine) as session:
            genre = GenreModel(name=name)
            session.add(genre)
            session.commit()
            session.refresh(genre)
        return CreateGenre(genre=genre)

class UpdateGenre(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)

    genre = graphene.Field(Genre)

    def mutate(self, info, id, name):
        if not name or len(name) > 255:
            raise Exception("Invalid genre name.")
        with Session(db.engine) as session:
            genre = session.execute(db.select(GenreModel).where(GenreModel.id == id)).scalars().first()
            if not genre:
                raise Exception("Genre not found.")
            genre.name = name
            session.commit() 
            session.refresh(genre)
        return UpdateGenre(genre=genre)

class DeleteGenre(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    genre = graphene.Field(Genre)

    def mutate(self, info, id):
        with Session(db.engine) as session:
            genre = session.execute(db.select(GenreModel).where(GenreModel.id == id)).scalars().first()
            if not genre:
                raise Exception("Genre not found.")
            session.delete(genre)
            session.commit()  
        return DeleteGenre(genre=genre)



class Query(graphene.ObjectType):
    movies = graphene.List(Movie)
    genres = graphene.List(Genre)
    get_movies_by_genre = graphene.List(Movie, genre_id=graphene.Int(required=True))
    get_genres_by_movie = graphene.List(Genre, movie_id=graphene.Int(required=True))

    def resolve_movies(self, info):
        return db.session.execute(db.select(MovieModel)).scalars()

    def resolve_genres(self, info):
        return db.session.execute(db.select(GenreModel)).scalars()

    def resolve_get_movies_by_genre(self, info, genre_id):
        with Session(db.engine) as session:
            genre = session.execute(db.select(GenreModel).where(GenreModel.id == genre_id)).scalars().first()
            if not genre:
                raise Exception("Genre not found.")
            movies = genre.movies  

            for movie in movies:
                movie.genres

          
            for movie in movies:
                session.expunge(movie)
            return movies

    def resolve_get_genres_by_movie(self, info, movie_id):
        with Session(db.engine) as session:
            movie = session.execute(db.select(MovieModel).where(MovieModel.id == movie_id)).scalars().first()
            if not movie:
                raise Exception("Movie not found.")
            genres = movie.genres  


            session.expunge(movie)
            return genres




class Mutation(graphene.ObjectType):
    create_movie = AddMovie.Field()
    update_movie = UpdateMovie.Field()
    delete_movie = DeleteMovie.Field()
    create_genre = CreateGenre.Field()
    update_genre = UpdateGenre.Field()
    delete_genre = DeleteGenre.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
