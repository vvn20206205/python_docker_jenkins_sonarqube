# pip install Flask
from flask import Flask
from  modules.add_numbers import add_numbers

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return str(add_numbers(a, b))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# http://127.0.0.1:5000/add/2/3
# http://localhost:5000/add/2/3


# http://127.0.0.1:5000
# http://localhost:5000
