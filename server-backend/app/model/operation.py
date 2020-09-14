from flask_restplus import Model, fields

from app.model import operation_ns

operation = Model('Operation', {
    'idx': fields.Integer(required=False, example=1, description='internal id'),
    'user_id': fields.Integer(required=True, example=1, description='user id'),
    'operation': fields.String(required=True, example='WASH', description='type of operation for controller'),
    'parameters': fields.Raw(required=True, example='{"type": "QUICK"}', description='additional parameters'),
    'status': fields.String(required=False, exampel='created', description='status of operation'),
    'created_timestamp': fields.String(required=False, example='2020-09-06 02:21:59', description='created time'),
    'updated_timestamp': fields.String(required=False, example='2020-09-06 02:21:59', description='last update time')
})

operation_ns.add_model(name=operation.name, definition=operation)
