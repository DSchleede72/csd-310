#import pymongo from MongoClient
from pymongo import MongoClient
#assign connection string to variable url
url = "mongodb+srv://admin:admin@cluster0.8do7jnn.mongodb.net/?retryWrites=true&w=majority"
#create a variable named client
client = MongoClient(url)
#create a variable named db
db = client.pytech
print(db.list_collection_names)     