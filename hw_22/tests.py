from hw_22.repositories.api_sql_adapter import ApiSqlAdapter


def test_post_get_insert_select():
    t = ApiSqlAdapter()
    response, obj_id = t.post_an_object()
    get_response = t.get_an_object(obj_id)
    assert response.status_code == 200
    assert get_response.status_code == 200
    t.insert_an_object(obj_id)
    assert t.select_object_by_id(obj_id).id == obj_id


def test_put_get_update_select():
    t = ApiSqlAdapter()
    obj_id = t.obj_id_from_cell("Apple Home")
    t.put_an_object(obj_id, changed_dict={"name": "Google Assistant",
                                          "data": {"price": 135, "color": "white"}})
    assert t.get_an_object(obj_id).json()['name'] == "Google Assistant"
    t.update_an_object_name_from_api(obj_id)
    assert t.select_object_by_id(obj_id).name == "Google Assistant"


def test_update_select_put_get():
    t = ApiSqlAdapter()
    obj_id = t.obj_id_from_cell("Google Assistant")
    t.update_an_object_name(obj_id, "iPhone 35")
    assert t.select_object_by_id(obj_id).name == "iPhone 35"
    t.put_an_object(obj_id, changed_dict={"name":t.select_object_by_id(obj_id).name})
    assert t.get_an_object(obj_id).json()['name']

