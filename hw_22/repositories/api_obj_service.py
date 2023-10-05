from requests import get, Response

class FilmService:
    def __init__(self):
        self.__objects_url = "https://restful-api.dev/objects"

    def get_created_date(self, obj_id: int):
        return get(f"{self.__objects_url}/{obj_id}")

    def get_character_from_film(self, film_id: str, character_id: int) -> Response:
        film = get(f"{self.__objects_url}/{film_id}")
        character = film.json()['characters'][character_id]
        return get(character)