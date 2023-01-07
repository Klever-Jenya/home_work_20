import pytest
from service.genre import GenreService


# Шаг 6. Пишем класс с тестами для GenreService.

class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):  # наш фиктивный genre_dao попадает в GenreService
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None  # везде нужно, где возврат-return значений
        assert genre.id is not None
        assert genre.name == "Немое кино"

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0
        assert genres is not None  # везде нужно, где возврат-return значений

    def test_create(self):
        genre_d = {
            "id": 3,
            "name": "Вымышленное"
        }

        genre = self.genre_service.create(genre_d)
        assert genre.id is not None

    def test_delete(self):
        # функция ничего не возвращает,
        # поэтому мы проверяем, что возвращается None, а не ошибка
        assert  self.genre_service.delete(2) is None

    def test_update(self):
        genre_d = {
            "id": 1,
            "name": "Вымышленное"
        }
        assert self.genre_service.update(genre_d) is not None
