import oracledb
import pandas as pd

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