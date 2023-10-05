import psycopg2

connection = psycopg2.connect(user='postgres',
                              password='05071998qaz',
                              host='localhost',
                              port='5432',
                              database='postgres')

cursor = connection.cursor()
cursor.execute('CREATE TABLE endpoint_objects (id varchar(50) primary key, name varchar(50),'
               'price int, color varchar(50));COMMIT;')
cursor.execute('SELECT * from endpoint_objects;')
connection.commit()
for row in cursor.fetchall():
    print(row)
cursor.close()
if connection:
    connection.close()