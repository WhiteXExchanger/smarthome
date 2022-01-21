""" Database Stuff
import pymongo

myClient = pymongo.MongoClient("mongodb+srv://WhiteXExchanger:Bmwkrisztian2002@cluster0.ynekb.mongodb.net")
db = myClient["test"]
houses = db["houses"]

x = houses.insert_one(mydict)
for x in houses.find({},{ "_id": 0, "name": 1 }):
  print(x)

print(myClient.list_database_names())
"""

mydict = { "name":"James", "state": True, "age": 12 }
print(mydict)

class house(object):
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

houses = []

def create(id,name):
    houses.append(house(id, name))

def delete(id):
    i=0
    while (houses[i].id != id):
        i=+1
    del houses[i]

print(houses)
create(0,"Kaka")
create(2,"Kiki")
print(houses)
delete(2)
print(houses)
