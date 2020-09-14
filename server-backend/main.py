from flask import Flask
from app import caramel_blueprint
from constants import FLASK_HOST, FLASK_PORT


def start_server() -> None:
    app = Flask(__name__)
    app.register_blueprint(caramel_blueprint)
    app.config['ERROR_404_HELP'] = False
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=True, threaded=True)


if __name__ == '__main__':
    start_server()
