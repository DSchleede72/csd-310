from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.8do7jnn.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
docs = db.students.find({})
 
for doc in docs:
 print(doc)


result = db.students.update_one({'student_id': '1007'}, {'$set': {'last_name': 'Stevens'}})

doc = db.students.find_one(
    {"student_id": "1007"}
)
print(doc)
