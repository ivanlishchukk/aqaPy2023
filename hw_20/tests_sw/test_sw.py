from hw_20.conftest import people_service
from hw_20.conftest import films_service


def test_test_luke(people_service):
    response = people_service.get_people("1")
    assert response.json()['name'] == 'Luke Skywalker'


def test_starships_count(people_service):
    response = people_service.get_starships_count('1')
    assert response == 2


def test_get_next_people_page(people_service):
    response = people_service.get_page("2")
    assert response.json()['previous'] == 'https://swapi.dev/api/people/?page=1'


def test_test_film_in_list(films_service):
    response = films_service.get_film("1")
    assert response.json()['title'] == 'A New Hope'


def test_get_film_by_episode_id(films_service):
    response = films_service.get_created_date("2")
    assert response.json()['created'] == '2014-12-12T11:26:24.656000Z'


def test_get_character_in_film(films_service):
    response = films_service.get_character_from_film("1", 0)
    assert response.json()['name'] == 'Luke Skywalker'