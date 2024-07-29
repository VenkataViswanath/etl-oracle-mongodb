# Making changes under thorri pallu Summi's guidance.

import pymongo
import pandas as pd

# Connection string
connection_string = "mongodb+srv://cvviswa7:Sanp7777!@cluster0.er4h8h9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to the MongoDB database
client = pymongo.MongoClient(connection_string)

# Access the database
db = client["test"]

# Access the collection
collection = db["mongotest"]

print("Connect to an excel file, compare and transform with Mongo data, and then push it to another Mongo collection")