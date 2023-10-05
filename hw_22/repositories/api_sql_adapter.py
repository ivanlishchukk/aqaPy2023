import numpy as np

from hw_22.session_handler import session
from hw_22.model.endpoint_obj import Objects
from requests import get, Response
from sqlalchemy.sql.expression import Insert
from sqlalchemy import select, insert, update
import requests
import json

'''
в якості ендпойнта для апі візьміть https://restful-api.dev/

т.як ендпойнт створює айді запису самостійно, реалізуйте наступні зв'язки:

api=>sql
POST+GET=>INSERT+SELECT
PUT+GET=>UPDATE+SELECT

sql=>api
UPDATE+SELECT=>PUT+GET

Tam де вказано +GET, +SELECT треба виконати ці операції після операцій зміни/створення, 
щоб пересвідчитись, що об'єкти створились/оновились правильно. 

Hапишіть довільну кількість тестів, щоб покрити функціонал цього адаптера.

Приклад
Ви створюєте об'єкт в апі через POST, пересвідчуєтесь, що він створився через GET, 
записуєте поля об'єкта в таблицю за допомогою INSERT, перевіряєте, чи створився запис за допомогою SELECT
'''


class ApiSqlAdapter:
    def __init__(self):
        self.__session = session
        self.url = "https://api.restful-api.dev/objects"

    def select_object_by_name(self, name):
        return self.__session.query(Objects).filter_by(name=name)

    def select_object_by_id(self, id):
        return self.__session.get(Objects, {'id': id})

    def obj_id_from_cell(self, name):
        cell = self.__session.query(Objects).filter_by(name=name).first()
        obj_id = (cell.id)
        return obj_id

    def select_all(self):
        bunch_of_objects = []
        for object in self.__session.query(Objects).all():
            bunch_of_objects.append(object)
        return bunch_of_objects

    def add_one_row(self, endpoint_obj):
        self.__session.add(endpoint_obj)
        self.__session.commit()

    def update_the_row(self, endpoint_obj):
        self.__session.delete(endpoint_obj)
        self.__session.commit()

    def insert_an_object(self, obj_id):
        object_to_add = Objects(
                                id=ApiSqlAdapter().get_object_id(obj_id),
                                name=ApiSqlAdapter().get_object_name(obj_id),
                                price=ApiSqlAdapter().get_object_price(obj_id),
                                color=ApiSqlAdapter().get_object_color(obj_id)
                                )
        ApiSqlAdapter().add_one_row(object_to_add)

    def update_an_object_name(self, obj_id):
        new_name = ApiSqlAdapter().get_object_name(obj_id)
        object_to_update = session.query(Objects.__tablename__).filter(Objects.__tablename__.id == f"{obj_id}").first()
        object_to_update.name = str(new_name)
        ApiSqlAdapter().update_the_row(object_to_update)

    def get_an_object(self, object_id):
        response = requests.get(f"{self.url}/{object_id}")
        return response

    def post_an_object(self):
        headers = {"content-type": "application/json"}
        payload = json.dumps({"name": "Apple Home", "data": {"price": 150, "color": "black"}})
        response = requests.post(self.url, data=payload, headers=headers)
        return response, response.json()['id']

    def put_an_object(self, obj_id, changed_dict):
        headers = {"content-type": "application/json"}
        payload = json.dumps(changed_dict)
        response = requests.put(f'{self.url}/{obj_id}', data=payload, headers=headers)
        return response

    def get_object_id(self, obj_id) -> Response:
        object = get(f"{self.url}/{obj_id}")
        id = object.json()['id']
        return id

    def get_object_name(self, obj_id) -> Response:
        object = get(f"{self.url}/{obj_id}")
        name = object.json()['name']
        return name

    def get_object_price(self, obj_id) -> Response:
        object = get(f"{self.url}/{obj_id}")
        price = object.json()['data']['price']
        return price

    def get_object_color(self, obj_id) -> Response:
        object = get(f"{self.url}/{obj_id}")
        color = object.json()['data']['color']
        return color
