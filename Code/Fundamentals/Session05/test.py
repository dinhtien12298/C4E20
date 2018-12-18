quy = ["Quy", 20, "Vinh Phuc", 2, 3, ["Anime","Porn"]]
# dictionary
# CRUD
# key : value

# create
person = {
    "name": "Quy",
    "age": 20,
    "unniversity": "hust",
    "ex": 2,
    "favs": ["Anime", "Porn"]
}

# read
# for key in person.keys():
#     print(key, end="\t")
    
# for key, value in person.items():
#     print(key, value)

# for value in person.values():
#     print(value)

# add
# person["gender"] = "male"
# print(person)

# update
person["ex"] = 20

# delete
del person["age"]
print(person) 