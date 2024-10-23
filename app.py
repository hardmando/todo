from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return (
        '<h2>Hello World! Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello'
        'World!Hello World!Hello World!</h2>'
    )


if __name__ == '__main__':
    app.run()