#!/usr/bin/python3
"""List all 'states' from the database 'hbtn_0e_0_usa'."""
from sys import argv as av
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=av[1], passwd=av[2], db=av[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()
    cursor.close()
    db.close()

    for state in states:
        print(state)
