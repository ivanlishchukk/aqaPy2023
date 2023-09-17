from hw_20.conftest import people_service
from hw_20.conftest import films_service


def test_test_luke(people_service):
    response = people_service.get_people("1")
    assert response.json()['name'] == 'Luke Skywalker'


def test_test_film(films_service):
    response = films_service.get_film("4")
    assert response.json()['title'] == 'The Phantom Menace'

