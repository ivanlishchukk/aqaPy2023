import requests
import sqlite3


class ApiSqlAdapter:
    def __init__(self):
        self.api_url = 'https://restful-api.dev/'
        self.endpoint = 'objects/7'
        self.db_path = 'hw_22/test_database.db'
        self.conn = sqlite3.connect('/Users/ivanlishchuk/PycharmProjects/aqaPy2106/hw_22/test_database.db')
        self.create_tables()

    def create_tables(self):
        create_table_sql = """
            CREATE TABLE IF NOT EXISTS api_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT
            );
        """
        with self.conn:
            self.conn.execute(create_table_sql)
            self.conn.commit()

    def get_data_from_api(self):
        response = requests.get(self.api_url + self.endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch data from API. Status code: {response.status_code}")

    def insert_data_into_sql(self, data):
        with self.conn:
            self.conn.execute("INSERT INTO api_data (data) VALUES (?)", (data,))
            self.conn.commit()

    def update_data_in_sql(self, id, data):
        with self.conn:
            self.conn.execute("UPDATE api_data SET data = ? WHERE id = ?", (data, id))
            self.conn.commit()

    def select_data_from_sql(self, id):
        cursor = self.conn.execute("SELECT data FROM api_data WHERE id = ?", (id,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    def synchronize_api_to_sql(self):
        api_data = self.get_data_from_api()
        for item in api_data:
            self.insert_data_into_sql(item)

    def synchronize_sql_to_api(self, id):
        sql_data = self.select_data_from_sql(id)
        if sql_data:
            response = requests.put(self.api_url + self.endpoint, json={"data": sql_data})
            if response.status_code != 200:
                raise Exception(f"Failed to update data on API. Status code: {response.status_code}")
        else:
            raise Exception(f"Data with id {id} not found in SQL database")
