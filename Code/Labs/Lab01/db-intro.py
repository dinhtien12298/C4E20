from pymongo import MongoClient

mongo_uri = "mongodb://howtorich:thinking12@ds111562.mlab.com:11562/c4e20-tien-labs"

# 1. Connect to database
client = MongoClient(mongo_uri)

# 2. Get database
db = client.get_default_database()

# 3. Create a collection
games = db['games']

# 4. Create a document
# new_game = {
#     "title": "AOE",
#     "description": "Age Of Empires"
# }

# 5. Insert doc into collection
# games.insert_one(new_game)

# 6. Read all documents
all_game = games.find()
first_game = all_game[0]

print(first_game['title'])