import pytest
from hw_20.infrastructure.people_service import PeopleService
from hw_20.infrastructure.films_service import FilmService


@pytest.fixture()
def people_service():
    yield PeopleService()


@pytest.fixture()
def films_service():
    yield FilmService()
