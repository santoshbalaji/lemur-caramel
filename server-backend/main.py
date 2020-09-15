import logging
from flask import Flask
from app import caramel_blueprint
from constants import FLASK_HOST, FLASK_PORT
from dao import disconnect_database


def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


def start_server() -> None:
    app = Flask(__name__)
    app.after_request(after_request)
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
