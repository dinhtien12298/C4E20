import mongoengine

# mongodb://dblearn-c4e20:thinking12@ds125362.mlab.com:25362/muadongkhonglanh12-c4e20

host = "ds125362.mlab.com"
port = 25362
db_name = "muadongkhonglanh12-c4e20"
user_name = "dblearn-c4e20"
password = "thinking12"


def connect():
    mongoengine.connect(
        db_name, 
        host=host, 
        port=port, 
        username=user_name, 
        password=password
    )