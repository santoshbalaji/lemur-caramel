class Message(object):
    OPERATION_CREATED = 'Created new operation with id: {}'
    OPERATION_UPDATED = 'Updated operation with id: {}'
    USER_CREATED = 'Created new user with id: {}'


class Error(object):
    ERROR_OPERATION_USER_NOT_EXISTS = 'Wrong user id provided user id: {}'
    ERROR_OPERATION_CREATE = 'Error in create operation: {}'
    ERROR_OPERATION_NOT_EXISTS = 'Provided operation not exists with id: {}'
    ERROR_OPERATION_UPDATE = 'Error in update operation: {}'
    ERROR_OPERATION_GET = 'Error in fetching operation: {}'
    ERROR_USER_CREATE = 'Error in create user: {}'
    ERROR_USER_GET = 'Error in fetching user: {}'
