from unittest.mock import MagicMock
import pytest
from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO
from setup_db import db


# Шаг 3. Создаем фикстуру с моком для DirectorServicerDAO.
@pytest.fixture()
def director_dao():
    dd = DirectorDAO(db.session)  # или None?

    sasha = Director(id=1, name="Саня Белый")
    lesha = Director(id=2, name="Лёха Черный")

    # словарь, где хранятся все режиссеры
    directors = {
        1: sasha,
        2: lesha
    }

    dd.get_one = MagicMock(return_value=sasha)
    dd.get_all = MagicMock(return_value=directors.values())  # или [sasha, lesha]
    dd.create = MagicMock(return_value=lesha)  # или Director(id=2)
    dd.update = MagicMock()
    dd.delete = MagicMock()

    return dd


# Шаг 5. Создаем фикстуру с моком для GenreDAO.
@pytest.fixture()
def genre_dao():
    dd = GenreDAO(db.session)

    nemoe = Genre(id=1, name="Немое кино")
    porno = Genre(id=2, name="Порно")

    # словарь, где хранятся все жанры
    genres = {
        1: nemoe,
        2: porno
    }

    dd.get_one = MagicMock(return_value=nemoe)
    dd.get_all = MagicMock(return_value=genres.values())  # [nemoe, porno]
    dd.create = MagicMock(return_value=porno)  # Genre(id=2)
    dd.update = MagicMock()
    dd.delete = MagicMock()

    return dd


# Шаг 7. Создаем фикстуру с моком для  MovieDAO.
@pytest.fixture()
def movie_dao():
    dd = MovieDAO(None)

    movie_1 = Movie(
        id=1,
        title="Название 1",
        description="Описание фильма 1",
        trailer="http/",
        year=2000,
        rating=4.8,
        genre_id=2,
        director_id=2
    )
    movie_2 = Movie(
        id=2,
        title="Название 2",
        description="Описание фильма 2",
        trailer="http/",
        year=2002,
        rating=8.8,
        genre_id=1,
        director_id=1
    )

    # словарь, где хранятся все фильмы
    movies = {
        1: movie_1,
        2: movie_2
    }

    dd.get_one = MagicMock(return_value=movie_1)
    dd.get_all = MagicMock(return_value=movies.values())  # [movie_1, movie_2]
    # для того чтобы можно было добавить фильм просто с названием, без других полей
    dd.create = MagicMock(return_value=Movie(id=1, title="Название 1"))
    dd.update = MagicMock()
    dd.delete = MagicMock()

    return dd
