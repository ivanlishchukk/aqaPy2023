import hw_21.infrastructure as infra
import json


def test_get_all_objects():
    assert infra.get_all_objects().status_code == 200
    assert len(infra.get_all_objects().json()) == 13


def test_get_object():
    assert infra.get_an_object(3).status_code == 200
    assert infra.get_an_object(3).json()['name'] == 'Apple iPhone 12 Pro Max'


def test_get_list_of_objects():
    assert infra.get_list_of_objects(1,2).status_code == 200
    assert len(infra.get_list_of_objects(1,2).json()) == 2


def test_get_list_of_objects_2():
    assert infra.get_list_of_objects(10,11).status_code == 200
    assert infra.get_list_of_objects(10,11).json()[1]['name'] == 'Apple iPad Mini 5th Gen'
    assert infra.get_list_of_objects(10,11).json()[0]['name'] == 'Apple iPad Mini 5th Gen'


def test_create_an_object():
    response, obj_id = infra.create_an_object()
    get_response = infra.get_an_object(obj_id)
    assert response.status_code == 200
    assert get_response.status_code == 200
    assert infra.get_an_object(obj_id).json()['name'] == 'Apple Home'


def test_update_object():
    response, obj_id = infra.create_an_object()
    changed_obj = infra.update_an_object(obj_id, {"name": "Google Assistant",
                                                  "data": {"color": "white", "generation": "3rd", "price": 135}})
    assert response.status_code == 200
    assert changed_obj.status_code == 200
    assert infra.get_an_object(obj_id).json()['name'] == 'Google Assistant'


def test_delete_object():
    response, obj_id = infra.create_an_object()
    deleted_obj = infra.delete_an_object(obj_id)
    assert deleted_obj.status_code == 200
    assert deleted_obj.json()['message'] == f'Object with id = {obj_id} has been deleted.'
