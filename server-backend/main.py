from pymongo import MongoClient

from dao import OperationDB, UserDB, SequenceDB
from model import User, Operation, Sequence

user = User(1, "11212", "asdsad", "")
u = user.get_json_str()
print(u)
u1 = User()
u1.convert_to_obj(u)
print(u1.idx)


operation = Operation(1, 1, "test", {'test': 'value'}, 'created')
o = operation.get_json_str()
print(o)
o1 = Operation()
o1.convert_to_obj(o)
print(o1.idx)


sequence = Sequence(1, "test", 1)
s = sequence.get_json_str()
print(s)
s1 = Sequence()
s1.convert_to_obj(s)
print(s1.idx)


m = MongoClient('localhost', 27017)
o = OperationDB(connection=m)
print(o.create(obj=operation))
operation.user_id=2
print(o.update(obj=operation))
print(o.delete(idx=operation.idx))
print(o.find(**{}))
u = UserDB(connection=m)
print(u.create(obj=user))
user.uuid='2323f'
print(u.update(obj=user))
print(u.delete(idx=user.idx))
print(u.find(**{}))
s = SequenceDB(connection=m)
print(s.create(obj=sequence))
sequence.collection_name='sdsds'
print(s.update(obj=sequence))
print(s.delete(idx=sequence.idx))
print(s.find(**{}))

