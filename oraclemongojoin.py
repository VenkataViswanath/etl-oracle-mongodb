import oracledb
import pandas as pd
import pymongo

cs='''(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.us-ashburn-1.oraclecloud.com))(connect_data=(service_name=ga7eebea0e99731_mytestdb_high.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))'''

connection=oracledb.connect(
     user="admin",
     password="Sanp7777!!!!@@@@",
     dsn=cs)


# Fetch data from Oracle
oracle_query = 'SELECT * FROM Employees'
oracle_data = pd.read_sql(oracle_query, connection)

# Print the data
print(oracle_data.head())

# Connection string
connection_string = "mongodb+srv://cvviswa7:Sanp7777!@cluster0.er4h8h9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to the MongoDB database
client = pymongo.MongoClient(connection_string)

# Access the database
db = client["test"]

# Access the collection
collection = db["mongotest"]

documents = list(collection.find())

# Print the documents
for doc in documents:
    print(doc)

# Convert MongoDB data to DataFrame
mongo_df = pd.DataFrame(documents)

print(mongo_df)
print(oracle_data)
# Perform a left join on the common column, e.g., 'id'
joined_data = pd.merge(mongo_df, oracle_data, on='EMPLOYEE_ID', how='left')

# Convert the joined DataFrame to a list of dictionaries
joined_data_dict = joined_data.to_dict(orient='records')

# Insert the joined data into a new MongoDB collection
new_mongo_collection = db['joined_collection']
new_mongo_collection.insert_many(joined_data_dict)
