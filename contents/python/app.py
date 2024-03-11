# pip install Flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# http://127.0.0.1:5000/add/2/3
# http://localhost:5000/add/2/3


# http://127.0.0.1:5000
# http://localhost:5000
