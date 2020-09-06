from flask import Flask
from app import caramel_blueprint


def start_server():
    app = Flask(__name__)
    app.register_blueprint(caramel_blueprint)
    app.config['ERROR_404_HELP'] = False
    app.run(host='127.0.0.1', port='3414', debug=True)


if __name__ == '__main__':
    start_server()
