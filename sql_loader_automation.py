import mysql.connector
import pandas as pd
mydb=mysql.connector.connect(host='localhost',user='root',password='Syed@1997',database='demo')

mycursor=mydb.cursor()
# mycursor.execute("CREATE DATABASE DEMO")  to create a new database

# mycursor.execute("CREATE TABLE DATA(name VARCHAR(255),address VARCHAR(255))")

df=pd.read_csv('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Data\\demo\\data.csv')
print(df.head())

# Generate SQL Loader control file dynamically
control_file_content = """
LOAD DATA
INFILE 'data.csv'
INTO TABLE data
FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES;
"""

mycursor.execute(control_file_content)

# Commit changes and close connection
mydb.commit()
mydb.close()

print("Data loaded successfully into MySQL database.")

