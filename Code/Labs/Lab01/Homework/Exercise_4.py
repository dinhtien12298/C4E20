import matplotlib
from matplotlib import pyplot
from pymongo import MongoClient

matplotlib.use("TkAgg")

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
db = client.get_default_database()
customer = db["customers"]

customers = customer.find()

references = {
    "Events": 0,
    "Advertisement": 0,
    "Word of mouth": 0
}

for i in customers:
    if i["ref"] == "events":
        references["Events"] += 1
    elif i["ref"] == "ads":
        references["Advertisement"] += 1
    elif i["ref"] == "wom":
        references["Word of mouth"] += 1

labels = ["Event","Advertisement","Word of mouth"]
colors = ["red", "green", "blue"]
explode = [0, 0.1, 0.2]
values = []
for key, value in references.items():
    values.append(value)

pyplot.pie(
        values,
        labels=labels,
        colors=colors,
        explode=explode
        )
pyplot.axis("equal")

pyplot.show()
