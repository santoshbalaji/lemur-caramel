from flask_restplus import Resource, reqparse
from app.model import operation_ns
from service import operation_service
import logging

operation_get_parser = reqparse.RequestParser()
operation_get_parser.add_argument('status', type=str, location='args', help='status for operation')


@operation_ns.route('/', methods=['GET', 'POST'])
class OperationController(Resource):

    @operation_ns.doc(parser=operation_get_parser)
    @operation_ns.expect(operation_get_parser, validate=True)
    def get(self) -> (str, int):
        try:
            logging.info("----------- get operation controller -------------")
            args = operation_get_parser.parse_args()
            code, message = operation_service.get_all_operations(operation_status=args['status'])
            return message, code
        except Exception as e:
            return str(e), 500

    @operation_ns.expect(operation_ns.models['Operation'], validate=True)
    def post(self) -> (str, int):
        try:
            logging.info("----------- post operation controller -------------")
            code, message = operation_service.create_operation(operation=operation_ns.payload)
            return message, code
        except Exception as e:
            return str(e), 500

