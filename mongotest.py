import pymongo
client = pymongo.MongoClient("mongodb+srv://mango:ineuron123@cluster0.ibohfnd.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "sudhanshu",
    "email": "sudhanshu@ineuron.ai",
    "surname": "kumar"
    }

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)