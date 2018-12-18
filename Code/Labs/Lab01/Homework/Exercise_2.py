# mongodb://admin:admin@ds021182.mlab.com:21182/c4e
from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

# Connect to database:
client = MongoClient(mongo_uri)

db = client.get_default_database()