from requests import get, Response
from hw_20 import config


class FilmService:
    def __init__(self):
        self.__films_url = f"{config['host']}/films"

    def get_film(self, film_id:str) -> Response:
        return get(f"{self.__films_url}/{film_id}")