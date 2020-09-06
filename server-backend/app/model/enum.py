from flask_restplus import fields

status = fields.String(
    title='Status for operation',
    enum=['created',
          'preparing',
          'executing',
          'completed'],
    description=('Status of operation\n\n'
                 '1. created = when operation is created\n'
                 '2. preparing = when operation is broadcasted to controller\n'
                 '3. executing = when controller started executing the task'
                 '4. completed = when controller completes the task'),
)
