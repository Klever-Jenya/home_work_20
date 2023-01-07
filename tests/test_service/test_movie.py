import pytest
from service.movie import MovieService


# Шаг 8. Пишем класс с тестами для MovieService.

class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):  # наш фиктивный movie_dao попадает в MovieService
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):  # тестируем получение одного фильма
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.title == "Название 1"
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert movies is not None  # везде нужно, где возврат-return значений
        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            "title": "Название 1",
            "description": "Описание фильма 1",
            "trailer": "http/",
            "year": 2000,
            "rating": 4.8,
            "genre_id": 2,
            "director_id": 2
        }

        movie = self.movie_service.create(movie_d)
        assert movie.id is not None

    def test_delete(self):
        # функция ничего не возвращает,
        # поэтому мы проверяем, что возвращается None, а не ошибка
        assert self.movie_service.delete(1) is None

    def test_update(self):
        movie_d = {
            "id": 1,
            "title": "Название 1 изменено",
            "description": "Описание фильма 1",
            "trailer": "http/",
            "year": 2000,
            "rating": 4.8,
            "genre_id": 2,
            "director_id": 2
        }

        assert self.movie_service.update(movie_d) is not None
