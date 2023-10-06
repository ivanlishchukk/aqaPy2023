from hw_22.repositories.api_sql_adapter import Adapter

t = Adapter()


def test_post_get_insert_select():
    t.post_get_insert_select("Apple Home", 150, "white")


def test_put_get_update_select():
    t.put_get_update_select("Apple Home", "Google Assistant", 150, "white")


def test_update_select_put_get():
    t.update_select_put_get("Google Assistant", "iPhone 35")
