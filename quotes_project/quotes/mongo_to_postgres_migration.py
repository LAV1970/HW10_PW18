import pymongo
import psycopg2
from psycopg2 import sql

# Подключение к MongoDB
mongo_client = pymongo.MongoClient("mongodb://localhost:27017")
mongo_db = mongo_client["hw8pw18"]
mongo_collection = mongo_db["hw8pw18"]

# Подключение к PostgreSQL (замените параметры на свои)
postgres_connection = psycopg2.connect(
    database="hw10_db",
    user="lomakin",
    password="QwertY123456",
    host="localhost",
    port="5432",
)
postgres_cursor = postgres_connection.cursor()

# Создание таблицы в PostgreSQL (замените это на свою модель)
table_name = "your_postgres_table"
postgres_cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS {} (
        id SERIAL PRIMARY KEY,
        field1 VARCHAR(255),
        field2 INTEGER
        -- Добавьте другие поля, если необходимо
    )
""".format(
        sql.Identifier(table_name)
    )
)

# Получение данных из MongoDB
mongo_data = list(mongo_collection.find())

# Вставка данных в PostgreSQL
for document in mongo_data:
    postgres_cursor.execute(
        """
        INSERT INTO {} (field1, field2) VALUES (%s, %s)
    """.format(
            sql.Identifier(table_name)
        ),
        (document["mongo_field1"], document["mongo_field2"]),
    )
    # Добавьте другие поля, если необходимо

# Применение изменений
postgres_connection.commit()

# Закрытие соединений
mongo_client.close()
postgres_cursor.close()
postgres_connection.close()
