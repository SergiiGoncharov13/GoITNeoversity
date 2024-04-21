import psycopg2
import random
import logging
from psycopg2 import DatabaseError
from faker import Faker

logging.basicConfig(level=logging.ERROR) 

fake = Faker()

# Connect to db
try:
    conn = psycopg2.connect(host="localhost", database="hw3_CS", user="postgres", password="123321")
    cur = conn.cursor()
except psycopg2.Error as e:
    logging.error("Failed to connect to the database: %s", e)
    exit()


for _ in range(10):  
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)",
                (fake.name(), fake.email()))

status_ids = [1, 2, 3]  
cur.execute("SELECT id FROM users")
user_ids = [id[0] for id in cur.fetchall()]

for _ in range(20):  
    title = fake.sentence()
    description = fake.text()
    status_id = random.choice(status_ids)
    user_id = random.choice(user_ids)
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                (title, description, status_id, user_id))

try:
    conn.commit()
except DatabaseError as e:
    logging.error(e)
    conn.rollback()
finally:
    cur.close()
    conn.close()