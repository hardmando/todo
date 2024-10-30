from flask import Flask
import psycopg2

app = Flask(__name__)


#DB connection
conn = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='admin',
    password='admin'
)

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS tasks')
cur.execute('CREATE TABLE tasks(task_id serial PRIMARY KEY, description character varying NULL, created_at timestamp NOT NULL, completed_at timestamp NULL)')
conn.commit()

cur.close()
conn.close()

@app.route('/')
def home():  # put application's code here
    return ()


if __name__ == '__main__':
    app.run()
