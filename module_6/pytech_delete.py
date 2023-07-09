from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.8do7jnn.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
#find and display all documents in collection
docs = db.students.find({}) 
for doc in docs:
 print(doc)

#insert one student with id 1010
Suguru = {
    "first_name": "Suguru",
    "last_name": "Geto",
    "student_id": "1010"
}
db.students.insert_one(Suguru)

#find and display student with id 1010
doc = db.students.find_one(
    {"student_id": "1010"}
)
print(doc)
#delete student with id 1010
db.students.delete_one(
    {"student_id": "1010"}
)
#find and display all documents in collection
docs = db.students.find({}) 
for doc in docs:
 print(doc)
