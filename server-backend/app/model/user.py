from flask_restplus import Model, fields

from app.model import user_ns

user = Model('User', {
    'idx': fields.Integer(required=False, example=1, description='internal id'),
    'user_id': fields.Integer(required=True, example=1, description='user specified id'),
    'topic': fields.String(required=False, example='topic_name', description='topic to which user will be broadcasted'),
    'created_timestamp': fields.String(required=False, example='2020-09-06 02:21:59', description='created time'),
    'updated_timestamp': fields.String(required=False, example='2020-09-06 02:21:59', description='last update time')
})

user_ns.add_model(name=user.name, definition=user)
