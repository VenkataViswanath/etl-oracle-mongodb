# etl-oracle-mongodb
ETL with oracle and mongo database

# Tools and Techstack
- Python - for code (Libraries: Pandas for Dataframe operations, OracleDB for Oracle connection and PyMongo for Mongo connection)
- Oracle DB - for SQL Database
- Mongo DB - for No SQL Database
- Visual Studio Code


## Connection test files:
mongoconnection.py
oracledbconnection.py

## OracleMongoJoin file:
- This code connects to Oracle DB, fetches the table information into a pandas dataframe.
- This also connects to MongoDB using pymongo driver and reads the contents of a collection into a different pandas dataframe.
- Now it performs left join and stores the result in a different Mongo collection.
