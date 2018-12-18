from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
db = client.get_default_database()

add_posts = {
    "title": "Quote",
    "author": "Nguyen Dinh Tien",
    "content": '''If you think you cant do that
                You are right
                If you think you can do that
                Yeah you are also right!!!'''
}

db["posts"].insert_one(add_posts)