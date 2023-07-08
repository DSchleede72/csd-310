from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.8do7jnn.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print(db.list_collection_names())
gojo = {
    "first_name": "Satoru",
    "last_name": "Gojo",
    "student_id": "1007"
}
gojo_student_id = db.students.insert_one(gojo).inserted_id
print(gojo_student_id)
harry = {
    "first_name": "Harry",
    "last_name": "Williamson",
    "student_id": "1008"
}
harry_student_id = db.students.insert_one(harry).inserted_id
print(harry_student_id)
josh = {
    "first_name": "Josh",
    "last_name": "Beck",
    "student_id": "1009"
}
josh_student_id = db.students.insert_one(josh).inserted_id
print(josh_student_id)