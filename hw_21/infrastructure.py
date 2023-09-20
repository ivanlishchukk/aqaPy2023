import requests
import json

url = "https://api.restful-api.dev/objects"


def get_all_objects():
    response = requests.get(f"{url}")
    return response


def get_an_object(object_id):
    response = requests.get(f"{url}/{object_id}")
    return response


def get_list_of_objects(obj1_id, obj2_id):
    response = requests.get(f"{url}?id={obj1_id}&id={obj2_id}")
    return response


def create_an_object():
    headers = {"content-type": "application/json"}
    payload = json.dumps({"name": "Apple Home", "data": {"color": "grey", "generation": "2nd", "price": 150}})
    response = requests.post(url, data=payload, headers=headers)
    return response, response.json()['id']


def update_an_object(obj_id, changed_dict):
    headers = {"content-type": "application/json"}
    payload = json.dumps(changed_dict)
    response = requests.put(f'{url}/{obj_id}', data=payload, headers=headers)
    return response


def delete_an_object(obj_id):
    response = requests.delete(f'{url}/{obj_id}')
    return response
