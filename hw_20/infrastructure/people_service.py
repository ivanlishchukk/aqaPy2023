from requests import get, Response
from hw_20 import config


class PeopleService:
    def __init__(self):
        self.__people_url = f"{config['host']}/people"

    def get_people(self, people_id:str) -> Response:
        return get(f"{self.__people_url}/{people_id}")

    def get_page(self, page_id:str) -> Response:
        return get(f"{self.__people_url}/?page={page_id}")

