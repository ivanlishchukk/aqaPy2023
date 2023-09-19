from requests import get, Response
from hw_20 import config


class FilmService:
    def __init__(self):
        self.__films_url = f"{config['host']}/films"

    def get_film(self, film_id: str) -> Response:
        return get(f"{self.__films_url}/{film_id}")

    def get_created_date(self, film_id: int):
        return get(f"{self.__films_url}/{film_id}")

    def get_character_from_film(self, film_id: str, character_id: int) -> Response:
        film = get(f"{self.__films_url}/{film_id}")
        character = film.json()['characters'][character_id]
        return get(character)