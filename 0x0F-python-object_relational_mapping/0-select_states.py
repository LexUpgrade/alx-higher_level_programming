#!/usr/bin/python3
"""List all 'states' from the database 'hbtn_0e_0_usa'."""
from sys import argv
import MySQLdb

usr = argv[1]
pswrd = argv[2]
db_name = argv[3]

db = MySQLdb.connect(host='localhost', port=3306,
                     user=usr, passwd=pswrd, db=db_name)
cursor = db.cursor()

cursor.execute("SELECT * FROM states;")
states = cursor.fetchall()

cursor.close()
db.close()

for state in states:
    print(state)
