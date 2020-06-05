import pymongo

client = pymongo.MongoClient("mongodb+srv://seminar:seminarseminar@cluster0-kdbww.mongodb.net/seminar?retryWrites=true&w=majority")
db = client.seminar