from flask import Blueprint
from flask_restplus import Api
from .controller import operation_ns, user_ns

__all__ = ['caramel_blueprint', 'caramel_api']

caramel_blueprint = Blueprint('api', __name__, url_prefix='/caramel')
caramel_api = Api(caramel_blueprint,
                  title='Project Lemur (caramel)',
                  version='1.0.0',
                  description='This is caramel api for managing IOT controller operations',
                  default_mediatype='application/json')


caramel_api.add_namespace(operation_ns)
caramel_api.add_namespace(user_ns)
