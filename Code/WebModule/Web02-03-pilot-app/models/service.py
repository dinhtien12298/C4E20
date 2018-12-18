from mongoengine import *

# Design database
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = StringField()
    image = ImageField()
    description = ListField()
    measurements = ListField()