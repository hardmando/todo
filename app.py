import datetime

from flask import Flask, render_template, request, url_for, flash, redirect
import psycopg2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c1f5eb607c6ee4009644da33163dca00e36b6783c0245814'


#DB connection
conn = psycopg2.connect(
    host='localhost',
    port='5433',
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
            'INSERT INTO tasks(description, created_at) VALUES (%s, %s);',
            ('test0', '2000-01-01'))
cur.execute('INSERT INTO tasks (description, created_at) VALUES (%s, %s);', ('test1', '2000-01-01'))
conn.commit()

cur.close()
conn.close()

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            port='5433',
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

@app.route('/post_task', methods=['GET', 'POST'])
def post_task():
    conn = get_db_connection()
    cur = conn.cursor()
    description = request.form['task_desc']
    cur.execute('INSERT INTO tasks (description, created_at) VALUES (%s, %s);', (description, datetime.datetime.now()))
    conn.commit()

    cur.execute('SELECT * FROM tasks')
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('home.html', tasks=tasks)

@app.route('/drop_task', methods=['GET', 'POST'])
def drop_task():
    conn = get_db_connection()
    cur = conn.cursor()
    task_id = request.form['task_id']
    cur.execute('DELETE FROM tasks WHERE task_id = %s;', (task_id,))
    conn.commit()

    cur.execute('SELECT * FROM tasks')
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('home.html', tasks=tasks)

if __name__ == '__main__':
    app.run()
