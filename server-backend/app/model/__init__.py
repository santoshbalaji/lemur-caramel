from flask_restplus import Namespace

__all__ = ['operation_ns', 'user_ns']

operation_ns = Namespace(name='Operation', path='/operations', description='API for operation')
user_ns = Namespace(name='User', path='/users', description='API for user')


