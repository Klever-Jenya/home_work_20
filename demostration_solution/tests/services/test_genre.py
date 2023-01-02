from unittest.mock import MagicMock
import pytest

from demostration_solution.dao.genre import GenreDAO
from demostration_solution.dao.model.genre import Genre
from demostration_solution.service.genre import GenreService


# Шаг 5. Создаем фикстуру с моком для GenreDAO.
@pytest.fixture()
def genre_dao():
    dd = GenreDAO(None)

    nemoe = Genre(id=1, name="Немое кино")
    porno = Genre(id=2, name="Порно")

    dd.get_one = MagicMock(return_value=nemoe)
    dd.get_all = MagicMock(return_value=[nemoe, porno])
    dd.create = MagicMock(return_value=Genre(id=2))
    dd.update = MagicMock(return_value=Genre(id=1))
    dd.delete = MagicMock()


# Шаг 6. Пишем класс с тестами для GenreService.

class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        genre_d = {
            "name": "Вымышленное"
        }

        genre = self.genre_service.create(genre_d)
        assert genre.id is not None

    def test_delete(self):
        self.genre_service.delete(2)

    def test_update(self):
        genre_d = {
            "id": 3,
            "name": "Вымышленное"
        }
        self.genre_service.update(genre_d)