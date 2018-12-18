from mongoengine import *

# class Student(Document):

# class Classromm(Document):
#     students = ListField(ReferenceField(Student))

class Order(Document):
    user_id = StringField()
    service_id = StringField()
    order_time = DateTimeField()
    is_accepted = BooleanField()
