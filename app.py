from flask import Flask, render_template
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
cur.execute('CREATE TABLE tasks(task_id serial PRIMARY KEY,'
            'status boolean NOT NULL DEFAULT FALSE,'
            'description character varying NULL,'
            'created_at timestamp NOT NULL,'
            'completed_at timestamp NULL);'
            'INSERT INTO tasks(description, created_at) VALUES (%s, %s);', ('test', '2000-01-01'))
conn.commit()

cur.close()
conn.close()

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='postgres',
                            user='admin',
                            password='admin')
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM tasks')
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('home.html', tasks=tasks)

if __name__ == '__main__':
    app.run()
