from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Movie(Base):
    __tablename__ = 'movies'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(db.String(255))
    director: Mapped[str] = mapped_column(db.String(255))
    year: Mapped[int] = mapped_column(db.Integer)
    genre_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('genres.id'))
    genre: Mapped['Genre'] = relationship('Genre')


class Genre(Base):
    __tablename__ = 'genres'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False, unique=True)