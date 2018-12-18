import mongoengine

# mongodb://dblearn-c4e20:thinking12@ds133601.mlab.com:33601/cms-app-c4e20

host = "ds133601.mlab.com"
port = 33601
db_name = "cms-app-c4e20"
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
