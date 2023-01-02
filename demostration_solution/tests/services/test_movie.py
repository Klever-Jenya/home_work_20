from unittest.mock import MagicMock
import pytest
from demostration_solution.dao.model.movie import Movie
from demostration_solution.dao.movie import MovieDAO
from demostration_solution.service.movie import MovieService


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

    dd.get_one = MagicMock(return_value=movie_1)
    dd.get_all = MagicMock(return_value=[movie_1, movie_2])
    dd.create = MagicMock(return_value=Movie(id=2))
    dd.update = MagicMock(return_value=Movie(id=1))
    dd.delete = MagicMock()


# Шаг 8. Пишем класс с тестами для MovieService.

class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie.title is not None
        assert movie.id is not None
        assert movie.description is not None
        assert movie.trailer is not None
        assert movie.year is not None
        assert movie.rating is not None
        assert movie.genre_id is not None
        assert movie.director_id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            "title": "Название 3",
            "description": "Описание фильма 3",
            "trailer": "http/",
            "year": 2003,
            "rating": 3.8,
            "genre_id": 1,
            "director_id": 2
        }

        movie = self.movie_service.create(movie_d)
        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            "id": 3,
            "title": "Название 3",
            "description": "Описание фильма 3",
            "trailer": "http/",
            "year": 2002,
            "rating": 8.8,
            "genre_id": 1,
            "director_id": 1
        }
        self.movie_service.update(movie_d)
