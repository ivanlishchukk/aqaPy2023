from hw_22.repositories.api_sql_defs import ApiSqlDefs
import hw_22.repositories.api_sql_defs


class Adapter:
    def __init__(self):
        self.url = "https://api.restful-api.dev/objects"

    def post_get_insert_select(self, name, price, color):
        t = ApiSqlDefs()
        response, obj_id = t.post_an_object(name=name, price=price, color=color)
        get_response = t.get_an_object(obj_id)
        assert response.status_code == 200
        assert get_response.status_code == 200
        t.insert_an_object(obj_id)
        assert t.select_object_by_id(obj_id).id == obj_id

    def put_get_update_select(self, name_to_get: str, name: str, price, color: str):
        t = ApiSqlDefs()
        obj_id = t.obj_id_from_cell(name_to_get)
        t.put_an_object(obj_id, changed_dict={"name": name,
                                              "data": {"price": price, "color": color}})
        assert t.get_an_object(obj_id).json()['name'] == name
        t.update_an_object_name_from_api(obj_id)
        assert t.select_object_by_id(obj_id).name == name

    def update_select_put_get(self, name_to_get: str, name: str):
        t = ApiSqlDefs()
        obj_id = t.obj_id_from_cell(name_to_get)
        t.update_an_object_name(obj_id, name)
        assert t.select_object_by_id(obj_id).name == name
        t.put_an_object(obj_id, changed_dict={"name": t.select_object_by_id(obj_id).name})
        assert t.get_an_object(obj_id).json()['name']
