class Message(object):
    OPERATION_UPDATED = 'Updated operation with id: {}'


class Error(object):
    ERROR_OPERATION_NOT_EXISTS = 'Provided operation not exists with id: {}'
    ERROR_OPERATION_UPDATE = 'Error in update operation: {}'
    ERROR_OPERATION_GET_NEXT_JOB = 'Error in fetching next operation: {}'
    ERROR_OPERATION_GET_RESULT = 'Error in results update of operation: {}'
