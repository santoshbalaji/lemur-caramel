import logging
from flask import Flask
from app import caramel_blueprint
from constants import FLASK_HOST, FLASK_PORT
from dao import disconnect_database


def start_server() -> None:
    app = Flask(__name__)
    app.register_blueprint(caramel_blueprint)
    app.config['ERROR_404_HELP'] = False
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=True, threaded=True)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    start_server()
    text = ''
    while text != 'y':
        text = input("Enter y to stop the process")
    disconnect_database()
