import pytest
from service.director import DirectorService


# Шаг 4. Пишем класс с тестами для DirectorService.

class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):  # наш фиктивный director_dao попадает в DirectorService
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None
        assert director.name == "Саня Белый"

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert directors is not None  # везде нужно, где возврат-return значений
        assert len(directors) > 0

    def test_create(self):
        director_d = {
            "name": "Саня Белый"
        }

        director = self.director_service.create(director_d)
        assert director.id is not None

    def test_delete(self):
        # функция ничего не возвращает,
        # поэтому мы проверяем, что возвращается None, а не ошибка
        assert self.director_service.delete(1) is None

    def test_update(self):
        director_d = {
            "id": 1,
            "name": "Катя Серая"
        }
        assert self.director_service.update(director_d) is not None
