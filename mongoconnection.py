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

additional_documents = [
    {
        "EMPLOYEE_ID": 1,
        "project_name": "Project Alpha",
    },
    {
        "EMPLOYEE_ID": 2,
        "project_name": "Project Beta",
    },
    {
        "EMPLOYEE_ID": 3,
        "project_name": "Project Gamma",
    },
    {
        "EMPLOYEE_ID": 4,
        "project_name": "Project Delta",
    },
    {
        "EMPLOYEE_ID": 5,
        "project_name": "Project Epsilon",
    }
]

collection.insert_many(additional_documents)

print("Additional documents inserted successfully.")

documents = list(collection.find())

# Print the documents
for doc in documents:
    print(doc)