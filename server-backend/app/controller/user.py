from flask_restplus import Resource, reqparse
from app.model import user_ns
from service import user_service
import logging

user_get_parser = reqparse.RequestParser()
user_get_parser.add_argument('id', type=int, location='args', help='id of user')


@user_ns.route('/', methods=['GET', 'POST'])
class UserController(Resource):

    @user_ns.doc(parser=user_get_parser)
    @user_ns.expect(user_get_parser, validate=True)
    def get(self) -> (str, int):
        try:
            logging.info("-------------- get user controller --------------")
            args = user_get_parser.parse_args()
            code, message = user_service.get_users(user_id=args['id'])
            return message, code
        except Exception as e:
            return str(e), 500

    @user_ns.expect(user_ns.models['User'], validate=True)
    def post(self) -> (str, int):
        try:
            logging.info("--------------- post user controller --------------")
            code, message = user_service.create_user(user=user_ns.payload)
            return message, code
        except Exception as e:
            return str(e), 500
