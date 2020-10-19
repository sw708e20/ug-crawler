import sys
import json
import mysql.connector  # install mysql-connector-python

argc = len(sys.argv)
connection_string = "" #Default connection string
elif argc == 2
    raise "Should be called with 'python upload.py json_data_file"

filePath = argv[1]

file = open(filePath, "r")
raw_educations = json.load(file)
file.close()

conn = mysql.connector.connect(
  host="130.225.57.130",
  user="root",
  password="",
  database = "dbName",
)

with(conn):
    for education in raw_educations:
        insert_education(conn, education)
        
    conn.commit()



def insert_education(conn, education):
    sql = '''INSERT INTO education(name, description)
            VALUES(?,?)'''

    data = (education["name"], education["description"])

    cur = conn.cursor()
    cur.execute(sql, data)

    education_fk = cur.lastrowid
    for edu_type in education["edu_type"].keys():
        insert_type(conn, edu_type, education["edu_type"][edu_type], education_fk)

def insert_type(conn, type_name, type_url, education_fk):
    sql = '''INSERT INTO education_type(education, url, name)
            VALUES(?,?,?)'''

    data = (education_fk, type_url, type_name)

    cur = conn.cursor()
    cur.execute(sql, data)
